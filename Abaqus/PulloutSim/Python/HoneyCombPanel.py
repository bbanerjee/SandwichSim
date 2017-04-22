from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import boundaryUtils
import regionToolset
import geomHoney


#  Create a model
tmpModel = mdb.Model(name='tmp')
if mdb.models.has_key('Model-1'):
  del mdb.models['Model-1']
if mdb.models.has_key('Honeycomb'):
  del mdb.models['Honeycomb']

myModel = mdb.Model(name='Honeycomb')
myAssembly = myModel.rootAssembly
del mdb.models['tmp']

# Input Parameters
rc = 0.003175
rp = 0.01
ri = 0.007125
hCore = 0.0127
hFace = 0.000457
hComb = 0.00015
hIns = hCore
nx = 11
ny = 18
nx = 4
ny = 11
bQuadratic = 0
bExplicit = 1
bDisplace = 0


#  Step Parameters
uLoad = 0.001
uForce = 1334/4
uTime = 40.0
uMaxInc = 0.05
uMinInc = 1.e-7
uMaxNumInc = 2000
uInitialInc = 0.01
mScaleInc = 1.e-4


#  Derived Parameters
lx = 4 * rc / (2 + sqrt(3))
s = lx*sin(pi/3)
c = lx*cos(pi/3)
xmax = 2*nx*(lx+c)-lx
ymax = 2*ny*s
A = ri*ri * pi / 4
P = -uForce / A

xc = xmax - c - lx/2
yc = ymax - s
cx = xc - 0.0254
cy = yc - 0.0255

#  Mesh Parameters
hMesh = 0.001
scMesh = 2

#  Create Insert
skInsert = myModel.ConstrainedSketch( name='insertProfile', sheetSize = 2*ri )
skInsert.CircleByCenterPerimeter( center=(xc,yc), point1=(xc+ri,yc) )
prtInsert = myModel.Part( dimensionality=THREE_D, name='Insert', type=DEFORMABLE_BODY )
prtInsert.BaseSolidExtrude( depth=hIns, sketch=skInsert )

#  Create Honeycomb
skHoney = myModel.ConstrainedSketch( name='honeyProfile', sheetSize=2*xmax )
cnrs = geomHoney.getCorners( lx, nx, ny )
for i in range( len(cnrs) ):
  for j in range( 6 ):
    lines = geomHoney.getLines( cnrs[i], lx )
    skHoney.Line( point1=lines[j][0], point2=lines[j][1] )
prtCells = myModel.Part( dimensionality=THREE_D, name='Cells', type=DEFORMABLE_BODY )
prtCells.BaseShellExtrude( depth=hCore, sketch=skHoney )


#  Create Potting Base
skBlock = myModel.ConstrainedSketch( name='blockProfile', sheetSize=3*lx )
lines = geomHoney.getLines( (0,0), lx )
for i in range( 6 ):
  skBlock.Line( point1=lines[i][0], point2=lines[i][1] )
prtBlock = myModel.Part( dimensionality=THREE_D, name='Block', type=DEFORMABLE_BODY )
prtBlock.BaseSolidExtrude( depth=hCore, sketch=skBlock )

instBlks = []
nBlks = 0
for i in range( len(cnrs) ):
  vtxs = geomHoney.getVertices( cnrs[i], lx )
  if ( geomHoney.getMinDist( (xc,yc), vtxs ) < rp ):
    nBlk = 'Blk ' + str(nBlks)
    instBlks.append( myAssembly.Instance( name=nBlk, part=prtBlock, dependent=ON ) )
    instBlks[nBlks].translate( vector=cnrs[i] )
    nBlks = nBlks + 1

prtEpox0 = myAssembly.PartFromBooleanMerge( name='Epox0', instances=instBlks, keepIntersections=False )

for i in range( nBlks ):
  nBlk = 'Blk ' + str(i)
  del myAssembly.instances[nBlk]
del instBlks


#  Create Potting
instEpox0 = myAssembly.Instance( name='instEpox0', part=prtEpox0, dependent=ON )
instInsert = myAssembly.Instance( name='instInsert', part=prtInsert, dependent=ON )
prtPotting = myAssembly.PartFromBooleanCut( name='Potting', instanceToBeCut=instEpox0, cuttingInstances=(instInsert,) )
instPotting = myAssembly.Instance( name='instPotting', part=prtPotting, dependent=ON )
del myModel.parts['Block']


#  Create Face Sheets
skSheet = myModel.ConstrainedSketch( name='sheetProfile', sheetSize=3*nx*lx )
skSheet.rectangle( point1=(0,0), point2=(xmax,ymax) )
prtFace = myModel.Part( dimensionality=THREE_D, name='Face', type=DEFORMABLE_BODY )
prtFace.BaseShell( sketch=skSheet )
prtFace.PartitionFaceBySketch( faces=prtFace.faces, sketch=skHoney )
instFace = myAssembly.Instance( name='instFace', part=prtFace, dependent=ON )
prtFace = myAssembly.PartFromBooleanCut( name='Face', instanceToBeCut=instFace, cuttingInstances=(instPotting,instInsert,) )
del myAssembly.instances['instFace']


#  Subtract Potting From Core
instCells = myAssembly.Instance( name='instCells', part=prtCells, dependent=ON )
prtCore  = myAssembly.PartFromBooleanCut( name='Core', instanceToBeCut=instCells, cuttingInstances=(instEpox0,) )
del myAssembly.instances['instCells']
del myAssembly.instances['instEpox0']
del myModel.parts['Cells']
del myModel.parts['Epox0']


#  Create Panel
instBotFace = myAssembly.Instance( name='instBotFace', part=prtFace, dependent=ON )
instCore = myAssembly.Instance( name='instCore', part=prtCore, dependent=ON )
instPotting = myAssembly.Instance( name='instPotting', part=prtPotting, dependent=ON )
instTopFace = myAssembly.Instance( name='instTopFace', part=prtFace, dependent=ON )
instTopFace.translate( vector=(0,0,hCore) )
prtPanel0 = myAssembly.PartFromBooleanMerge( name='Panel0', instances=(instBotFace,instCore,instPotting,instInsert,instTopFace), 
                                             keepIntersections=True )
instPanel0 = myAssembly.Instance( name='instPanel0', part=prtPanel0, dependent=ON )


#  Create Symmetry Block
skSymBlock = myModel.ConstrainedSketch( name='symBlockProfile', sheetSize = xmax )
skSymBlock.Line( point1=(0,2*ymax), point2=(2*xmax,2*ymax) )
skSymBlock.Line( point1=(2*xmax,2*ymax), point2=(2*xmax,0) )
skSymBlock.Line( point1=(2*xmax,0), point2=(xc,0) )
skSymBlock.Line( point1=(xc,0), point2=(xc,yc) )
skSymBlock.Line( point1=(xc,yc), point2=(0,yc) )
skSymBlock.Line( point1=(0,yc), point2=(0,2*ymax) )
prtSymBlock = myModel.Part( dimensionality=THREE_D, name='SymBlock', type=DEFORMABLE_BODY )
prtSymBlock.BaseSolidExtrude( depth=hCore, sketch=skSymBlock )


#  Cut Parts
instSymBlock = myAssembly.Instance( name='instSymBlock', part=prtSymBlock, dependent=ON )
prtPanel = myAssembly.PartFromBooleanCut( name='Panel', instanceToBeCut=instPanel0, cuttingInstances=(instSymBlock,) )
prtSymBotFace = myAssembly.PartFromBooleanCut( name='SymBotFace', instanceToBeCut=instBotFace, cuttingInstances=(instSymBlock,) )
prtSymCore = myAssembly.PartFromBooleanCut( name='SymCore', instanceToBeCut=instCore, cuttingInstances=(instSymBlock,) )
prtSymPotting = myAssembly.PartFromBooleanCut( name='SymPotting', instanceToBeCut=instPotting, cuttingInstances=(instSymBlock,) )
prtSymInsert = myAssembly.PartFromBooleanCut( name='SymInsert', instanceToBeCut=instInsert, cuttingInstances=(instSymBlock,) )
prtSymTopFace = myAssembly.PartFromBooleanCut( name='SymTopFace', instanceToBeCut=instTopFace, cuttingInstances=(instSymBlock,) )


#  Delete Original Parts and Instances
del myAssembly.instances['instBotFace']
del myAssembly.instances['instCore']
del myAssembly.instances['instPotting']
del myAssembly.instances['instTopFace']
del myAssembly.instances['instSymBlock']
del myAssembly.instances['instInsert']
del myAssembly.instances['instPanel0']
del myModel.parts['Insert']
del myModel.parts['Panel0']
del myModel.parts['Face']
del myModel.parts['Core']
del myModel.parts['Potting']
del myModel.parts['SymBlock']


#  Recreate Half Instances
instBotFace = myAssembly.Instance( name='instBotFace', part=prtSymBotFace, dependent=ON )
instCore = myAssembly.Instance( name='instCore', part=prtSymCore, dependent=ON )
instPotting = myAssembly.Instance( name='instPotting', part=prtSymPotting, dependent=ON )
instInsert = myAssembly.Instance( name='instInsert', part=prtSymInsert, dependent=ON )
instTopFace = myAssembly.Instance( name='instTopFace', part=prtSymTopFace, dependent=ON )


#  Partition Parts
for i in range( len( myModel.parts ) ):
  tmpPart = myModel.parts[ myModel.parts.keys()[i] ]
  tmpPart.DatumPlaneByPrincipalPlane( offset=cx, principalPlane=YZPLANE )
  tmpPart.DatumPlaneByPrincipalPlane( offset=cy, principalPlane=XZPLANE )

  for j in range( len( tmpPart.datums ) ):
    datum = tmpPart.datums[ tmpPart.datums.keys()[j] ] 
    try:
      tmpPart.PartitionCellByDatumPlane( cells=tmpPart.cells, datumPlane=datum )
    except:
      x = 0
    try:
      tmpPart.PartitionFaceByDatumPlane( faces=tmpPart.faces, datumPlane=datum )
    except:
      x = 0
    del datum
  del tmpPart


#  Create Material Properties
tabLaminate = ( 17.9e9, 17.9e9, 6.e9, 0.3, 0.3, 0.3, 6.0e9, 1.0e9, 1.0e9 )
tabHoneycomb = ( 1.e9, 0.3 )
tabPotting = ( 890.e6, 0.3 )
tabSteel = ( 2.1e11, 0.3 )
matLaminate = myModel.Material( name='Laminate' )
matLaminate.Elastic( type=ENGINEERING_CONSTANTS, table=( tabLaminate, ) )
matHoneycomb = myModel.Material( name='Honeycomb' )
matHoneycomb.Elastic( type=ISOTROPIC, table=( tabHoneycomb, ) )
matPotting = myModel.Material( name='Potting' )
matPotting.Elastic( type=ISOTROPIC, table=( tabPotting, ) )
matSteel = myModel.Material( name='Steel' )
matSteel.Elastic( type=ISOTROPIC, table=( tabSteel, ) )
matHoneycomb.Density(table=((1000.0, ), ))
matLaminate.Density(table=((1652.0, ), ))
matPotting.Density(table=((1100.0, ), ))
matSteel.Density(table=((7700.0, ), ))


#  Create Section Definitions
secSteel = myModel.HomogeneousSolidSection( name='secSteel', material='Steel' )
secPotting = myModel.HomogeneousSolidSection( name='secPotting', material='Potting' )
secLaminate = myModel.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='Laminate', 
                                              name='secLaminate', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, 
                                              preIntegrate=OFF, temperature=GRADIENT, thickness=hFace, thicknessField='', 
                                              thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)
secHoneycomb = myModel.HomogeneousShellSection(idealization=NO_IDEALIZATION, integrationRule=SIMPSON, material='Honeycomb', 
                                               name='secHoneycomb', nodalThicknessField='', numIntPts=5, poissonDefinition=DEFAULT, 
                                               preIntegrate=OFF, temperature=GRADIENT, thickness=hComb, thicknessField='', 
                                               thicknessModulus=None, thicknessType=UNIFORM, useDensity=OFF)


#  Create Skins on Top and Bottom of Potting
seqPotSkinBase = boundaryUtils.getFacesFromCntnr( prtPanel, instPotting )
seqTopPotSkin = boundaryUtils.getFacesList( prtPanel, seqPotSkinBase, 2, hCore )
seqBotPotSkin = boundaryUtils.getFacesList( prtPanel, seqPotSkinBase, 2, 0 )
seqPotSkin = seqTopPotSkin + seqBotPotSkin
prtPanel.Skin( faces=seqTopPotSkin, name='PottingTop' )
prtPanel.Skin( faces=seqBotPotSkin, name='PottingBot' )


#  Get Sequences of Faces/Cells for Each Material
seqSteel = boundaryUtils.getCellsFromCntnr( prtPanel, instInsert )
seqPotting = boundaryUtils.getCellsFromCntnr( prtPanel, instPotting  )
seqTopLaminate = boundaryUtils.getFacesFromCntnr( prtPanel, instTopFace )
seqBotLaminate = boundaryUtils.getFacesFromCntnr( prtPanel, instBotFace )
seqLaminate = seqTopLaminate + seqBotLaminate
seqCore = boundaryUtils.getFacesFromCntnr( prtPanel, instCore )


#  Create Regions for Section Assignments
regLaminate = regionToolset.Region( faces=seqLaminate )
regSkin = regionToolset.Region( skinFaces=(('PottingTop', seqTopPotSkin),('PottingBot', seqBotPotSkin),) )
regSteel = regionToolset.Region( cells=seqSteel )
regPotting = regionToolset.Region( cells=seqPotting )
regCore = regionToolset.Region( faces=seqCore   )


#  Create Section Assignments
prtPanel.SectionAssignment( region=regLaminate, sectionName='secLaminate' )
prtPanel.SectionAssignment( region=regSkin, sectionName='secLaminate' ) 
prtPanel.SectionAssignment( region=regCore, sectionName='secHoneycomb' ) 
prtPanel.SectionAssignment( region=regPotting, sectionName='secPotting' ) 
prtPanel.SectionAssignment( region=regSteel,  sectionName='secSteel'   )


#  Assign Material Directions
regTopLaminate = regionToolset.Region( faces=seqTopLaminate )
regBotLaminate = regionToolset.Region( faces=seqBotLaminate )
regTopSkin = regionToolset.Region( skinFaces=(('PottingTop', seqTopPotSkin),) )
regBotSkin = regionToolset.Region( skinFaces=(('PottingBot', seqBotPotSkin),) )
prtPanel.DatumCsysByThreePoints( name='Global', coordSysType=CARTESIAN, origin=(0,0,0), point1=(1,0,0), line2=(0,1,0))
prtPanel.DatumCsysByThreePoints( name='Global', coordSysType=CARTESIAN, origin=(0,0,0), point1=(1,0,0), line2=(0,-1,0))
k = len(prtPanel.datums.keys()) - 2
panelDatum1 = prtPanel.datums[ prtPanel.datums.keys()[k] ]
panelDatum2 = prtPanel.datums[ prtPanel.datums.keys()[k+1] ]
prtPanel.MaterialOrientation( axis=AXIS_3, localCsys=panelDatum1, region=regTopLaminate, stackDirection=STACK_3 )
prtPanel.MaterialOrientation( axis=AXIS_3, localCsys=panelDatum1, region=regTopSkin, stackDirection=STACK_3 )
prtPanel.MaterialOrientation( axis=AXIS_3, localCsys=panelDatum1, region=regBotLaminate, stackDirection=STACK_3 )
prtPanel.MaterialOrientation( axis=AXIS_3, localCsys=panelDatum2, region=regBotSkin, stackDirection=STACK_3 )
del panelDatum1, panelDatum2


#  Set Element Types
if( bQuadratic == 1 ):
  prtPanel.setElementType( elemTypes=( ElemType(elemCode=S8R, elemLibrary=STANDARD), ElemType(elemCode=STRI65, elemLibrary=STANDARD)), 
                           regions=regLaminate )
  prtPanel.setElementType( elemTypes=( ElemType(elemCode=S8R, elemLibrary=STANDARD), ElemType(elemCode=STRI65, elemLibrary=STANDARD)), 
                           regions=regCore )
  prtPanel.setElementType( elemTypes=( ElemType(elemCode=S8R, elemLibrary=STANDARD), ElemType(elemCode=STRI65, elemLibrary=STANDARD)), 
                           regions=regSkin )
  prtPanel.setElementType(elemTypes=( ElemType(elemCode=C3D20R, elemLibrary=STANDARD), ElemType(elemCode=C3D15, elemLibrary=STANDARD), 
                                      ElemType(elemCode=C3D10M, elemLibrary=STANDARD)), regions=regSteel )
  prtPanel.setElementType(elemTypes=( ElemType(elemCode=C3D20R, elemLibrary=STANDARD), ElemType(elemCode=C3D15, elemLibrary=STANDARD), 
                                      ElemType(elemCode=C3D10M, elemLibrary=STANDARD)), regions=regPotting )
else:
  prtPanel.setElementType( elemTypes=( ElemType(elemCode=S4, elemLibrary=STANDARD), ElemType(elemCode=S3, elemLibrary=STANDARD)), 
                           regions=regLaminate )
  prtPanel.setElementType( elemTypes=( ElemType(elemCode=S4, elemLibrary=STANDARD), ElemType(elemCode=S3, elemLibrary=STANDARD)), 
                           regions=regCore )
  prtPanel.setElementType( elemTypes=( ElemType(elemCode=S4, elemLibrary=STANDARD), ElemType(elemCode=S3, elemLibrary=STANDARD)), 
                           regions=regSkin )
  prtPanel.setElementType(elemTypes=( ElemType(elemCode=C3D8, elemLibrary=STANDARD), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
                                      ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=regSteel )
  prtPanel.setElementType(elemTypes=( ElemType(elemCode=C3D8, elemLibrary=STANDARD), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
                                      ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=regPotting )



#  Mesh Panel and Create Part Instance
prtPanel.setMeshControls( allowMapped=True, elemShape=QUAD, regions=seqCore     )
prtPanel.setMeshControls( allowMapped=True, elemShape=QUAD, regions=seqLaminate )
prtPanel.setMeshControls( allowMapped=True, elemShape=HEX,  regions=seqSteel    )
prtPanel.setMeshControls( allowMapped=True, elemShape=HEX,  regions=seqPotting  )
prtPanel.seedPart( deviationFactor=0.1, size=hMesh )
seqCoarseEdges = boundaryUtils.getColinearEdges( prtPanel, (0,0,1) )
prtPanel.seedEdgeBySize( edges=seqCoarseEdges, size=scMesh*hMesh )
prtPanel.generateMesh()

instPanel = myAssembly.Instance( name='instPanel', part=prtPanel, dependent=ON )


#  Create Step
if( bExplicit == 1 ):
  stepPullout = myModel.ExplicitDynamicsStep( description='Explicit Pullout', name='Pullout', previous='Initial' )
  stepPullout.setValues( timePeriod = uTime )
  stepPullout.setValues( massScaling = ((SEMI_AUTOMATIC, MODEL, THROUGHOUT_STEP, 0.0, mScaleInc, BELOW_MIN, 100, 0, 0.0, 0.0, 0, None), ))
else:
  stepPullout = myModel.StaticStep( description='Pullout Load', name='Pullout', nlgeom=ON, previous='Initial' )
  stepPullout.setValues( timePeriod=uTime )
  stepPullout.setValues( maxNumInc=uMaxNumInc )
  stepPullout.setValues( initialInc=uInitialInc )
  stepPullout.setValues( minInc=uMinInc )
  stepPullout.setValues( maxInc=uMaxInc )

#  Apply Load Condition
if( bDisplace == 0 ):
  seqPress = instPanel.faces[0:0]
  for i in range( len( instPanel.faces ) ):
    x = prtPanel.faces[i].getCentroid()
    if( abs( x[0][2] - hCore ) < 1.e-5 ):
      if( boundaryUtils.dist( x[0], (xc,yc,hCore) ) < ri ):
        seqPress = seqPress + instPanel.faces.findAt( x, printWarning=False )  

  myModel.Pressure( createStepName='Pullout', distributionType=UNIFORM, field='', magnitude=P, name='Pressure',
                    region=Region( side1Faces=seqPress ) )
  myModel.EquallySpacedAmplitude(begin=0.0, data=(0.0, 0.5, 1.0, 1.0), 
    fixedInterval=uTime/4, name='EqAmp', smooth=SOLVER_DEFAULT, timeSpan=STEP)
  myModel.SmoothStepAmplitude(data=((0.0, 0.0), (uTime/2,1.0), (uTime, 1.0)), name='SmoothAmp', timeSpan=STEP)
  myModel.loads['Pressure'].setValues(amplitude='EqAmp')
else:
  seqInsertBase = boundaryUtils.getFacesFromCntnr( instPanel, instInsert )
  seqTopInsert = boundaryUtils.getFacesList( instPanel, seqInsertBase, 2, hCore )
  myModel.DisplacementBC( amplitude=UNSET, createStepName='Pullout', distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None,
                          name='Load', region=Region( faces=seqTopInsert ), u1=UNSET, u2=UNSET, u3=uLoad, ur1=UNSET, ur2=UNSET, ur3=UNSET )


#  Apply Clamp Boundary Condition
seqClamp = instPanel.faces[0:0]
for i in range( len( instPanel.faces ) ):
  x = instPanel.faces[i].getCentroid()
  if( abs( x[0][2] - hCore ) < 1.e-5 ):
    if( x[0][0] < cx ):
      seqClamp = seqClamp + instPanel.faces.findAt( x, printWarning=False )
    if( x[0][1] < cy ):
      seqClamp = seqClamp + instPanel.faces.findAt( x, printWarning=False )
myModel.DisplacementBC( amplitude=UNSET, createStepName='Initial', distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None,
                        name='Clamp', region=Region( faces=seqClamp ), u1=UNSET, u2=UNSET, u3=0, ur1=UNSET, ur2=UNSET, ur3=UNSET )


#  Apply Symmetry Boundary Condition
seqSymFaces = boundaryUtils.getFaces( instPanel, 1, yc )
seqSymEdges = boundaryUtils.getEdges( instPanel, 1, yc )
myModel.YsymmBC(createStepName='Initial', name='YSym', region=Region( faces=seqSymFaces, edges=seqSymEdges ))

seqSymFaces = boundaryUtils.getFaces( instPanel, 0, xc )
seqSymEdges = boundaryUtils.getEdges( instPanel, 0, xc )
myModel.XsymmBC(createStepName='Initial', name='XSym', region=Region( faces=seqSymFaces, edges=seqSymEdges ))


#  Create Set on Insert Top
seqInsertTop = prtPanel.faces[0:0]
for i in range( len( prtPanel.faces ) ):
  x = prtPanel.faces[i].getCentroid()
  if( abs( x[0][2] - hCore ) < 1.e-5 ):
    if( boundaryUtils.dist( x[0], (xc,yc,hCore) ) < ri ):
      seqInsertTop = seqInsertTop + prtPanel.faces.findAt( x, printWarning=False )  

prtPanel.Set( faces=seqInsertTop, name='Insert-Top' )


# Create Reaction Force History Output Request
myModel.HistoryOutputRequest( createStepName='Pullout', name='Insert-ReactionForce', rebar=EXCLUDE,
                              region=instPanel.sets['Insert-Top'], sectionPoints=DEFAULT, variables=('U3', 'RF3') )


#  Delete Extra Instances and Parts
del myAssembly.instances['instBotFace']
del myAssembly.instances['instCore']
del myAssembly.instances['instPotting']
del myAssembly.instances['instInsert']
del myAssembly.instances['instTopFace']
del myModel.parts['SymBotFace']
del myModel.parts['SymCore']
del myModel.parts['SymInsert']
del myModel.parts['SymPotting']
del myModel.parts['SymTopFace']


#  Create Job
mdb.Job( contactPrint=OFF, description='Pullout Load Applied', echoPrint=OFF, explicitPrecision=SINGLE,
         historyPrint=OFF, memory=90, memoryUnits=PERCENTAGE, model='Honeycomb', modelPrint=OFF, multiprocessingMode=DEFAULT, 
         name='Pullout-NB221-1e9-1in', nodalOutputPrecision=SINGLE, numCpus=1, numDomains=1, parallelizationMethodExplicit=DOMAIN, scratch='',
         type=ANALYSIS, userSubroutine='' )




"""
"""
