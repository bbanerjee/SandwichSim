# Parametric tapered sandwich with cohesive zone and XFEM with curvature
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

#----------------------------------------------------------------
# Create model
#----------------------------------------------------------------
tmpModel = mdb.Model(name='tmp')
if mdb.models.has_key('Model-1'):
  del mdb.models['Model-1']
if mdb.models.has_key('TaperModelCurveXFEM1'):
  del mdb.models['TaperModelCurveXFEM1']

taperModel = mdb.Model(name='TaperModelCurveXFEM1')
taperAssem = taperModel.rootAssembly
del mdb.models['tmp']

#----------------------------------------------------------------
# Parameters
#----------------------------------------------------------------
# Geometry parameters
face1Thick = 0.00633
face2Thick = 0.00377
faceThick = face1Thick + face2Thick
coreThick = 0.03
singleSkinLen = 0.1
taperAngle = 30*pi/180
taperLen = coreThick/tan(taperAngle)
sandwichLen = 0.7
loadLen = sandwichLen - 0.35
#cohesiveThick = 1.0e-6
cohesiveThick =0.001 
#cohesiveThick =0.0001 
#cohesiveThick =0.00001 
sandwichThick = 0.05
filletRadius = 0.03

midFace1 = 0.5*face1Thick
midFace2 = 0.5*face2Thick
midCohesive = 0.5*cohesiveThick
midPanel = 0.5*sandwichThick

# Mesh parameters
#hSize = face1Thick/4.0
hSize = face1Thick/2.0
#hSize = face1Thick

# Load parameters
tractionMag = 1000

# Material properties
coreE11 = 125.0e6
coreE22 = 125.0e6
coreE33 = 125.0e6
corenu12 = 0.3
corenu13 = 0.3
corenu23 = 0.3
coreG12 = 38.0e6
coreG13 = 38.0e6
coreG23 = 38.0e6

face1E11 = 11.871e9
face1E22 = 11.871e9
face1E33 = 11.871e9
face1nu12 = 0.3
face1nu13 = 0.3
face1nu23 = 0.3
face1G12 = 4.6e9
face1G13 = 4.6e9
face1G23 = 4.6e9

face2E11 = 10.229e9
face2E22 = 10.229e9
face2E33 = 10.229e9
face2nu12 = 0.3
face2nu13 = 0.3
face2nu23 = 0.3
face2G12 = 3.9e9
face2G13 = 3.9e9
face2G23 = 3.9e9

faceFaceSign = 60e6
faceFaceSigt1 = 50e6
faceFaceSigt2 = 50e6
faceFaceDispf = 0.001
faceFaceEKnn = 69e12
faceFaceG1Kss = 69e12
faceFaceG2Ktt = 69e12

faceCoreSign = 60e6
faceCoreSigt1 = 50e6
faceCoreSigt2 = 50e6
faceCoreDispf = 0.001
faceCoreEKnn = 69e12
faceCoreG1Kss = 69e12
faceCoreG2Ktt = 69e12

coreElastic = ((coreE11, coreE22, coreE33, corenu12, corenu13, corenu23, 
   coreG12, coreG13, coreG23), )
face1Elastic = ((face1E11, face1E22, face1E33, face1nu12, face1nu13, face1nu23, 
   face1G12, face1G13, face1G23), )
face2Elastic = ((face2E11, face2E22, face2E33, face2nu12, face2nu13, face2nu23, 
   face2G12, face2G13, face2G23), )
faceFaceDamageInit = ((faceFaceSign, faceFaceSigt1, faceFaceSigt2), )
faceCoreDamageInit = ((faceCoreSign, faceCoreSigt1, faceCoreSigt2), )
faceFaceElastic = ((faceFaceEKnn, faceFaceG1Kss, faceFaceG2Ktt), )
faceCoreElastic = ((faceCoreEKnn, faceCoreG1Kss, faceCoreG2Ktt), )

#----------------------------------------------------------------
# Set up geometry
#----------------------------------------------------------------
# Section point coordinates
x1 = 0
y1 = 0
x2 = singleSkinLen
y2 = 0
x3 = x2 + taperLen
y3 = 0
x4 = loadLen
y4 = 0
x5 = sandwichLen
y5 = 0
x6 = x5
y6 = face1Thick
x7 = x5
y7 = y6 + coreThick
x8 = x5
y8 = y7 + face2Thick
x9 = x4
y9 = y8
x10 = x3
y10 = y8
x11 = x2
y11 = faceThick
x12 = x1
y12 = faceThick
x13 = x1
y13 = face1Thick
p01 = (x1, y1)
p02 = (x2, y2)
p03 = (x3, y3)
p04 = (x4, y4)
p05 = (x5, y5)
p06 = (x6, y6)
p07 = (x7, y7)
p08 = (x8, y8)
p09 = (x9, y9)
p10 = (x10, y10)
p11 = (x11, y11)
p12 = (x12, y12)
p13 = (x13, y13)

# Create sketch
taperSketch = taperModel.ConstrainedSketch(name='__profile__', sheetSize=3.0)

taperSketch.Spot(point=p01)
taperSketch.Spot(point=p02)
taperSketch.Spot(point=p03)
taperSketch.Spot(point=p04)
taperSketch.Spot(point=p05)
taperSketch.Spot(point=p06)
taperSketch.Spot(point=p07)
taperSketch.Spot(point=p08)
taperSketch.Spot(point=p09)
taperSketch.Spot(point=p10)
taperSketch.Spot(point=p11)
taperSketch.Spot(point=p12)
taperSketch.Spot(point=p13)

taperSketch.Line(point1=p01, point2=p02)
taperSketch.Line(point1=p02, point2=p03)
taperSketch.Line(point1=p03, point2=p04)
taperSketch.Line(point1=p04, point2=p05)
taperSketch.Line(point1=p05, point2=p06)
taperSketch.Line(point1=p06, point2=p07)
taperSketch.Line(point1=p07, point2=p08)
taperSketch.Line(point1=p08, point2=p09)
taperSketch.Line(point1=p09, point2=p10)
taperSketch.Line(point1=p10, point2=p11)
taperSketch.Line(point1=p11, point2=p12)
taperSketch.Line(point1=p12, point2=p13)
taperSketch.Line(point1=p13, point2=p01)

# Create fillets
taperGeom = taperSketch.geometry
pCurve1 = (0.5*(x11+x12), y11)
curve1 = taperGeom.findAt(pCurve1)
pCurve2 = (0.5*(x11+x10), 0.5*(y11+y10))
curve2 = taperGeom.findAt(pCurve2)
taperSketch.FilletByRadius(radius=filletRadius, curve1=curve1, nearPoint1=pCurve1,
  curve2=curve2, nearPoint2=pCurve2)

taperGeom = taperSketch.geometry
pCurve1 = pCurve2
curve1 = taperGeom.findAt(pCurve1)
pCurve2 = (0.5*(x9+x10), y9)
curve2 = taperGeom.findAt(pCurve2)
taperSketch.FilletByRadius(radius=filletRadius, curve1=curve1, nearPoint1=pCurve1,
  curve2=curve2, nearPoint2=pCurve2)

# Extrude
taperPart = taperModel.Part(dimensionality=THREE_D, name='TaperPart', type=
  DEFORMABLE_BODY)
taperPart.BaseSolidExtrude(depth=sandwichThick, sketch=taperSketch)
del taperSketch
 
# Find the extra points in the filleted region
pEdgeMid = (0.5*(x11+x12), 0.5*(y11+y12), 0.0)
edgeList = taperPart.edges
edgeToPartition = edgeList.findAt(pEdgeMid)
vertexList = taperPart.vertices
vertEdge = edgeToPartition.getVertices()
pFillet11 = vertexList[vertEdge[1]].pointOn[0]

pEdgeMid = (0.5*(x11+x10), 0.5*(y10+y12), 0.0)
pFillet11a = vertexList[vertEdge[0]].pointOn[0]
edgeToPartition = edgeList.findAt(pEdgeMid)
vertexList = taperPart.vertices
vertEdge = edgeToPartition.getVertices()
pFillet11a = vertexList[vertEdge[0]].pointOn[0]
pFillet10a = vertexList[vertEdge[1]].pointOn[0]
 
pEdgeMid = (0.5*(x10+x9), 0.5*(y10+y9), 0.0)
edgeList = taperPart.edges
edgeToPartition = edgeList.findAt(pEdgeMid)
vertexList = taperPart.vertices
vertEdge = edgeToPartition.getVertices()
pFillet10 = vertexList[vertEdge[0]].pointOn[0]

# Partition the geometry to create the top facesheet and associated cohesive zone
faceList = taperPart.faces
edgeList = taperPart.edges
sketchPlane = faceList.findAt((0.0, 0.0, sandwichThick))
sketchUpEdge = edgeList.findAt((sandwichLen, midFace1, sandwichThick)) 
sketchTransform = taperPart.MakeSketchTransform(sketchPlane=sketchPlane,
  sketchUpEdge=sketchUpEdge, sketchPlaneSide=SIDE1, origin=(0.0, 0.0, sandwichThick)) 
partitionSketch = taperModel.ConstrainedSketch(name='__profile__',
  sheetSize = 3.0, transform = sketchTransform)
geomList = partitionSketch.geometry
partitionSketch.setPrimaryObject(option=SUPERIMPOSE)
taperPart.projectReferencesOntoSketch(sketch=partitionSketch, filter=COPLANAR_EDGES)

## Create the partition on the sketch
pp = (0.5*(x12+x11), y12)
geomID = geomList.findAt(pp).id
partitionEdge = (geomList[geomID],)
partitionSketch.offset(distance=face2Thick, objectList=partitionEdge, side=RIGHT,
  filletCorners=FALSE)
partitionSketch.offset(distance=face2Thick+cohesiveThick, objectList=partitionEdge, side=RIGHT,
  filletCorners=FALSE)
pp = (0.5*(x11+x10), 0.5*(y11+y10))
geomID = geomList.findAt(pp).id
partitionEdge = (geomList[geomID],)
partitionSketch.offset(distance=face2Thick, objectList=partitionEdge, side=RIGHT,
  filletCorners=FALSE)
partitionSketch.offset(distance=face2Thick+cohesiveThick, objectList=partitionEdge, side=RIGHT,
  filletCorners=FALSE)
pp = (0.5*(x10+x9), 0.5*(y10+y9))
geomID = geomList.findAt(pp).id
partitionEdge = (geomList[geomID],)
partitionSketch.offset(distance=face2Thick, objectList=partitionEdge, side=RIGHT,
  filletCorners=FALSE)
partitionSketch.offset(distance=face2Thick+cohesiveThick, objectList=partitionEdge, side=RIGHT,
  filletCorners=FALSE)
pp = (0.5*(x9+x8), 0.5*(y9+y8))
geomID = geomList.findAt(pp).id
partitionEdge = (geomList[geomID],)
partitionSketch.offset(distance=face2Thick, objectList=partitionEdge, side=RIGHT,
  filletCorners=FALSE)
partitionSketch.offset(distance=face2Thick+cohesiveThick, objectList=partitionEdge, side=RIGHT,
  filletCorners=FALSE)

xmin1 = pFillet11[0]
xmax1 = pFillet11a[0]
xmin2 = pFillet10a[0]
xmax2 = pFillet10[0]
for jj in range(len(geomList)):
  key = geomList.keys()[jj]
  pointOn = geomList[key].pointOn
  px = pointOn[0]
  #if geomList[key].curveType == ARC:
  if (px > xmin1 and px < xmax1) or (px > xmin2 and px < xmax2) :
    print geomList[key].curveType
    partitionEdge = (geomList[key],)
    partitionSketch.offset(distance=face2Thick, objectList=partitionEdge, side=RIGHT,
      filletCorners=FALSE)
    partitionSketch.offset(distance=face2Thick+cohesiveThick, objectList=partitionEdge, 
      side=RIGHT, filletCorners=FALSE)

## Select the face to partition
faceList = taperPart.faces
faceToPartition = faceList.findAt((0, 0, sandwichThick))
sketchUpEdge = edgeList.findAt((sandwichLen, midFace1, sandwichThick)) 
taperPart.PartitionFaceBySketch(sketchUpEdge=sketchUpEdge, faces=faceToPartition, 
  sketch=partitionSketch)
#partitionSketch.unsetPrimaryObject()
del partitionSketch

## Select the cell to partition and sweep path
cellList = taperPart.cells
vertList = taperPart.vertices
edgeList = taperPart.edges
edgeAlongSweep = edgeList.findAt((0, 0, midPanel)) 

## Select edges to sweep
offsetThickY = face2Thick*cos(taperAngle)
offsetThickX = face2Thick*sin(taperAngle)
offsetCohThickY = (face2Thick+cohesiveThick)*cos(taperAngle)
offsetCohThickX = (face2Thick+cohesiveThick)*sin(taperAngle)
x11 = pFillet11[0]
x11a = pFillet11a[0]
x10a = pFillet10a[0]
x10 = pFillet10[0]
y11 = pFillet11[1]
y11a = pFillet11a[1]
y10a = pFillet10a[1]
y10 = pFillet10[1]

### First edge
pp = (0.5*(x12+x11), y12-face2Thick, sandwichThick)
e1 = edgeList.findAt(pp)
### Second edge
e2 = boundaryUtils.getNextEdge(edgeList, vertList, e1)
### Third edge
e3 = boundaryUtils.getNextEdge(edgeList, vertList, e2)
### Fourth edge
e4 = boundaryUtils.getNextEdge(edgeList, vertList, e3)
### Fifth edge
e5 = boundaryUtils.getNextEdge(edgeList, vertList, e4)
### Sixth edge
e6 = boundaryUtils.getNextEdge(edgeList, vertList, e5)

partitionEdges = (e1, e2, e3, e4, e5, e6)
taperPart.PartitionCellBySweepEdge(cells=cellList, edges=partitionEdges, 
  sweepPath=edgeAlongSweep)

## Select the cell to partition and sweep path
cellList = taperPart.cells
vertList = taperPart.vertices
edgeList = taperPart.edges
edgeAlongSweep = edgeList.findAt((0, 0, midPanel)) 

### First edge
ppc = (0.5*(x12+x11), y12-face2Thick-cohesiveThick, sandwichThick)
e1c = edgeList.findAt(ppc)
### Second edge
e2c = boundaryUtils.getNextEdge(edgeList, vertList, e1c)
### Third edge
e3c = boundaryUtils.getNextEdge(edgeList, vertList, e2c)
### Fourth edge
e4c = boundaryUtils.getNextEdge(edgeList, vertList, e3c)
### Fifth edge
e5c = boundaryUtils.getNextEdge(edgeList, vertList, e4c)
### Sixth edge
e6c = boundaryUtils.getNextEdge(edgeList, vertList, e5c)

partitionEdges = (e1c, e2c, e3c, e4c, e5c, e6c)
taperPart.PartitionCellBySweepEdge(cells=cellList, edges=partitionEdges, 
  sweepPath=edgeAlongSweep)

# Partition the geometry to isolate the tapered region
pEdgeMid = (0.5*(x11+x12), 0.5*(y11+y12), 0.0)
edgeList = taperPart.edges
edgeToPartition = edgeList.findAt(pEdgeMid)
vertexList = taperPart.vertices
vertEdge = edgeToPartition.getVertices()
cellList = taperPart.cells
taperPart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=pFillet11,
  cells=cellList)
  
pEdgeMid = (0.5*(x10+x9), 0.5*(y10+y9), 0.0)
edgeList = taperPart.edges
edgeToPartition = edgeList.findAt(pEdgeMid)
vertexList = taperPart.vertices
vertEdge = edgeToPartition.getVertices()
cellList = taperPart.cells
taperPart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=pFillet10,
  cells=cellList)

# Partition the geometry to create the bottom facesheet
p6 = (x6, y6, 0.0)
pTaper = (0.5*(x2+x3), 0.0, 0.0)
edgeList = taperPart.edges
edgeToPartition = edgeList.findAt(p6)
cellList = taperPart.cells
cellToPartition = cellList.findAt((p6,),(pTaper,))
taperPart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=p6,
   cells=cellToPartition)
  
# Partition the sharp corner on in the tapered region
pFaceMid = (x10a, 0.5*(y10+y3), sandwichThick)
faceList = taperPart.faces
vertexList = faceList.findAt(pFaceMid).getVertices()
v1 = taperPart.vertices[vertexList[0]].pointOn
v2 = taperPart.vertices[vertexList[1]].pointOn
v3 = taperPart.vertices[vertexList[2]].pointOn
v4 = taperPart.vertices[vertexList[3]].pointOn
v5 = taperPart.vertices[vertexList[4]].pointOn
xVert = (v1[0][0], v2[0][0], v3[0][0], v4[0][0], v5[0][0])
yVert = (v1[0][1], v2[0][1], v3[0][1], v4[0][1], v5[0][1])
xCorner = min(xVert)
xRightAngle = max(xVert)
yCorner = min(yVert)
pCorner = (xCorner, yCorner, sandwichThick)
pRightAngle = (0.5*(xRightAngle+xCorner), yCorner, sandwichThick)
edgeList = taperPart.edges
edgeToPartition = edgeList.findAt(pRightAngle)
cellList = taperPart.cells
pCell1 = (0.5*(x2+x3), 0, 0)
pCell2 = (0.5*(x2+x3), face1Thick-0.5*cohesiveThick, 0)
cellToPartition = cellList.findAt((pCell1,), (pCell2,))
taperPart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=pCorner,
  cells=cellToPartition)

# Partition the geometry to create the bottom cohesive zone
x14 = x6
y14 = y6 - cohesiveThick
p14 = (x14, y14, 0.0)
tPartition = 1.0 - (y14 - y1)/(y6 - y1)
edgeList = taperPart.edges
edgeToPartition = edgeList.findAt(p14)
taperPart.PartitionEdgeByParam(edges=edgeToPartition, parameter=tPartition)
cellList = taperPart.cells
cellToPartition = cellList.findAt((p14,),(pTaper,))
taperPart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=p14,
  cells=cellToPartition)
 
# Partition the geometry to indicate load application point
p09 = (x9, y9, 0)
edgeList = taperPart.edges
edgeToPartition = edgeList.findAt(p09)
cellList = taperPart.cells
taperPart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=p09,
   cells=cellList)

# Partition the tapered facesheet for orientation purposes
p10a = (x10a, y10a, 0)
p11a = (x11a, y11a, 0)
pMid = (0.5*(x10a+x11a), 0.5*(y10a+y11a), 0)
#pMidCoh = (0.5*(x10a+x11a), 0.5*(y10a+y11a)-face2Thick-0.5*offsetThickY, 0)
pMidCoh = (x11+cohesiveThick, y11-face2Thick-0.5*cohesiveThick, 0)
edgeList = taperPart.edges
edgeToPartition = edgeList.findAt(pMid)
cellList = taperPart.cells
cellToPartition = cellList.findAt((pMid,),(pMidCoh,))
taperPart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=p11a,
   cells=cellToPartition)
pMidCoh = (x10-cohesiveThick, y10-face2Thick-0.5*cohesiveThick, 0)
edgeList = taperPart.edges
edgeToPartition = edgeList.findAt(pMid)
cellList = taperPart.cells
cellToPartition = cellList.findAt((pMid,),(pMidCoh,))
taperPart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=p10a,
   cells=cellToPartition)

# Create virtual topology
#taperPart.createVirtualTopology(mergeShortEdges=True, shortEdgeThreshold=0.0017,
#    mergeSmallFaces=True, smallFaceAreaThreshold=1.4e-05,
#    mergeSliverFaces=True, faceAspectRatioThreshold=10.0,
#    mergeSmallAngleFaces=True, smallFaceCornerAngleThreshold=10.0,
#    mergeThinStairFaces=True, thinStairFaceThreshold=0.00034,
#    ignoreRedundantEntities=True, cornerAngleTolerance=30.0,
#    applyBlendControls=True, blendSubtendedAngleTolerance=60.0,
#    blendRadiusTolerance=0.0085)

#----------------------------------------------------------------
# Set up material properties
#----------------------------------------------------------------
matCore = taperModel.Material(name='Core')
matCoreXFEM = taperModel.Material(name='CoreXFEM')
matFace1 = taperModel.Material(name='Face1')
matFace2 = taperModel.Material(name='Face2')
matFaceFace = taperModel.Material(name='CohesiveFaceFace')
matFaceCore = taperModel.Material(name='CohesiveFaceCore')

matCore.Elastic(type=ENGINEERING_CONSTANTS, table=coreElastic)
matCoreXFEM.Elastic(type=ENGINEERING_CONSTANTS, table=coreElastic)
matCoreXFEM.MaxpeDamageInitiation(table=((0.005, ), ))
matCoreXFEM.maxpeDamageInitiation.DamageEvolution(type=DISPLACEMENT, 
  table=((0.005, ), ))
matFace1.Elastic(type=ENGINEERING_CONSTANTS, table=face1Elastic)
matFace2.Elastic(type=ENGINEERING_CONSTANTS, table=face2Elastic)
matFaceFace.Elastic(type=TRACTION, table=faceFaceElastic)
matFaceFace.MaxsDamageInitiation(table=faceFaceDamageInit)
matFaceFace.maxsDamageInitiation.DamageEvolution(type=DISPLACEMENT, 
  table=((faceFaceDispf, ), ))
matFaceCore.Elastic(type=TRACTION, table=faceCoreElastic)
matFaceCore.MaxsDamageInitiation(table=faceCoreDamageInit)
matFaceCore.maxsDamageInitiation.DamageEvolution(type=DISPLACEMENT, 
  table=((faceCoreDispf, ), ))

#----------------------------------------------------------------
# Set up sections
#----------------------------------------------------------------
secCore = taperModel.HomogeneousSolidSection(name='Core', material='Core', thickness=None)
secCoreXFEM = taperModel.HomogeneousSolidSection(name='CoreXFEM', material='CoreXFEM', thickness=None)
secFace1 = taperModel.HomogeneousSolidSection(name='Face1', material='Face1', thickness=None)
secFace2 = taperModel.HomogeneousSolidSection(name='Face2', material='Face2', thickness=None)
secFaceFace = taperModel.CohesiveSection(name='CohesiveFaceFace', 
  material='CohesiveFaceFace', response=TRACTION_SEPARATION, 
  outOfPlaneThickness=None)
secFaceCore = taperModel.CohesiveSection(name='CohesiveFaceCore',
  material='CohesiveFaceCore', response=TRACTION_SEPARATION, 
  outOfPlaneThickness=None)

#----------------------------------------------------------------
# Assign sections
#----------------------------------------------------------------
# Lower facesheet
pCellMid1 = (0.5*(x1+x2), 0.5*(y1), midPanel)
pCellMid2 = (0.5*(x11+pCorner[0]), 0.5*(y2), midPanel)
pCellMid3 = (0.5*(pCorner[0]+x3), 0.5*(pCorner[1]), midPanel)
pCellMid4 = (0.5*(x3+x4), 0.5*(y4), midPanel)
pCellMid5 = (0.5*(x4+x5), 0.5*(y5), midPanel)
cellList = taperPart.cells
cellSequence = cellList.findAt((pCellMid1,),(pCellMid2,),
  (pCellMid3,), (pCellMid4,), (pCellMid5,))
region = regionToolset.Region(cells=cellSequence)
taperPart.SectionAssignment(region=region, sectionName='Face1')
setFace1 = taperPart.Set(name='Face1', cells=cellSequence)

# Face-Face cohesive region
pCellMid1 = (0.5*(x1+x11), 0.5*(y13+y14), midPanel)
cellSequence = cellList.findAt((pCellMid1,))
region = regionToolset.Region(cells=cellSequence)
taperPart.SectionAssignment(region=region, sectionName='CohesiveFaceFace',
  offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
  thicknessAssignment=FROM_SECTION)
setCohesiveFaceFace = taperPart.Set(name='CohesiveFaceFace', cells=cellSequence)

# Bottom Face-Core cohesive region
#pCellMid6 = (pCorner[0]-cohesiveThick, pCorner[1]-cohesiveThick, midPanel)
#cellSequence = cellList.findAt((pCellMid6,))
#setFace1ExtraBit = taperPart.Set(name='Face1ExtraBit', cells=cellSequence)

pCellMid1 = (0.5*(pCorner[0]+x3), 0.5*(y13+y14), midPanel)
pCellMid2 = (0.5*(x3+x4), 0.5*(y13+y14), midPanel)
pCellMid3 = (0.5*(x4+x5), 0.5*(y13+y14), midPanel)
cellSequence = cellList.findAt((pCellMid1,),(pCellMid2,),
  (pCellMid3,))
region = regionToolset.Region(cells=cellSequence)
taperPart.SectionAssignment(region=region, sectionName='CohesiveFaceCore',
  offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
  thicknessAssignment=FROM_SECTION)
setCohesiveFaceCoreBot = taperPart.Set(name='CohesiveFaceCoreBot', cells=cellSequence)
 
# Upper facesheet
pCellMid1 = (0.5*(x1+x11), 0.5*(y12+y13), midPanel)
pCellMid2 = (0.5*(x11a+x10a), 0.5*(y11a+y10a), midPanel)
pCellMid3 = (0.5*(x3+x4), y10, midPanel)
pCellMid4 = (0.5*(x4+x5), y10, midPanel)
cellList = taperPart.cells
cellSequence = cellList.findAt((pCellMid1,),(pCellMid2,),
  (pCellMid3,), (pCellMid4,))
region = regionToolset.Region(cells=cellSequence)
cellSequence = cellList.findAt((pCellMid1,), (pCellMid3,), (pCellMid4,))
taperPart.SectionAssignment(region=region, sectionName='Face2')
setFace2 = taperPart.Set(name='Face2', cells=cellSequence)
cellSequence = cellList.findAt((pCellMid2,))
setFace2Taper = taperPart.Set(name='Face2Taper', cells=cellSequence)

# Top Face-Core cohesive region
#pCellMid1 = (0.5*(x11+x3), 0.5*(y11a+y10a)-face2Thick-0.5*offsetThickY, midPanel)
pCellMid1 = ((x11a+offsetThickX+0.5*cohesiveThick), (y11a-offsetThickY-0.5*cohesiveThick), midPanel)
pCellMid2 = (0.5*(x3+x4), y10-face2Thick-0.5*cohesiveThick, midPanel)
pCellMid3 = (0.5*(x4+x5), y10-face2Thick-0.5*cohesiveThick, midPanel)
cellList = taperPart.cells
cellSequence = cellList.findAt((pCellMid1,),(pCellMid2,),
  (pCellMid3,))
region = regionToolset.Region(cells=cellSequence)
taperPart.SectionAssignment(region=region, sectionName='CohesiveFaceCore',
  offset=0.0, offsetType=MIDDLE_SURFACE, offsetField='',
  thicknessAssignment=FROM_SECTION)
cellSequence = cellList.findAt((pCellMid1,))
setCohesiveFaceCoreTaper = taperPart.Set(name='CohesiveFaceCoreTaper', cells=cellSequence)
cellSequence = cellList.findAt((pCellMid2,),(pCellMid3,))
setCohesiveFaceCoreTop = taperPart.Set(name='CohesiveFaceCoreTop', cells=cellSequence)
 
# Core region
pCellMid1 = (0.5*(x10a+x3), 0.5*(y3+face1Thick+y10-face2Thick-cohesiveThick), midPanel)
pCellMid2 = (0.5*(x3+x4), 0.5*(y3+y10), midPanel)
pCellMid3 = (0.5*(x4+x5), 0.5*(y3+y10), midPanel)
cellList = taperPart.cells
#cellSequence = cellList.findAt((pCellMid1,),(pCellMid2,),
#  (pCellMid3,))
#region = regionToolset.Region(cells=cellSequence)
#taperPart.SectionAssignment(region=region, sectionName='Core')
cellSequence = cellList.findAt((pCellMid1,))
setCoreTaper = taperPart.Set(name='CoreTaper', cells=cellSequence)
taperPart.SectionAssignment(region=setCoreTaper, sectionName='CoreXFEM')
cellSequence = cellList.findAt((pCellMid2,),(pCellMid3,))
setCore = taperPart.Set(name='Core', cells=cellSequence)
taperPart.SectionAssignment(region=setCore, sectionName='Core')
 
# Curved upper facesheet regions
pCellMid1 = (0.5*(x11+x11a), y11-0.5*face2Thick, midPanel)
cellList = taperPart.cells
cellSequence = cellList.findAt((pCellMid1,))
region = regionToolset.Region(cells=cellSequence)
taperPart.SectionAssignment(region=region, sectionName='Face2')
setFace2Curve1 = taperPart.Set(name='Face2Curve1', cells=cellSequence)
pCellMid1 = (0.5*(x10+x10a), y10-0.5*face2Thick, midPanel)
cellList = taperPart.cells
cellSequence = cellList.findAt((pCellMid1,))
region = regionToolset.Region(cells=cellSequence)
taperPart.SectionAssignment(region=region, sectionName='Face2')
setFace2Curve2 = taperPart.Set(name='Face2Curve2', cells=cellSequence)

# Curved upper cohesive regions
pCellMid1 = (x11+cohesiveThick, y11-face2Thick-0.5*cohesiveThick, midPanel)
cellList = taperPart.cells
cellSequence = cellList.findAt((pCellMid1,))
region = regionToolset.Region(cells=cellSequence)
taperPart.SectionAssignment(region=region, sectionName='CohesiveFaceCore')
setCohesiveFaceCoreCurve1 = taperPart.Set(name='CohesiveFaceCoreCurve1', cells=cellSequence)
pCellMid1 = (x10-cohesiveThick, y10-face2Thick-0.5*cohesiveThick, midPanel)
cellList = taperPart.cells
cellSequence = cellList.findAt((pCellMid1,))
region = regionToolset.Region(cells=cellSequence)
taperPart.SectionAssignment(region=region, sectionName='CohesiveFaceCore')
setCohesiveFaceCoreCurve2 = taperPart.Set(name='CohesiveFaceCoreCurve2', cells=cellSequence)

#----------------------------------------------------------------
# Create datum coordinate systems
#----------------------------------------------------------------
vertList = taperPart.vertices
# Lower facesheet
pOrig = (x1, y1, sandwichThick)
vertOrig = vertList.findAt(pOrig)
pXAxis = (x11, y1, sandwichThick)
vertX = vertList.findAt(pXAxis)
pYAxis = (x1, y1, 0)
vertXY = vertList.findAt(pYAxis)
taperPart.DatumCsysByThreePoints(name='Datum Csys Face1', coordSysType=CARTESIAN,
  origin=vertOrig, point1=vertX, point2=vertXY)
# Lower cohesive zone
pOrig = (x1, y1+face1Thick-cohesiveThick, sandwichThick)
vertOrig = vertList.findAt(pOrig)
pXAxis = (x10, y12-face2Thick-cohesiveThick, sandwichThick)
vertX = vertList.findAt(pXAxis)
pYAxis = (x1, y1+face1Thick-cohesiveThick, 0)
vertXY = vertList.findAt(pYAxis)
taperPart.DatumCsysByThreePoints(name='Datum Csys Cohesive1', coordSysType=CARTESIAN,
  origin=vertOrig, point1=vertX, point2=vertXY)
# Upper facesheet
pOrig = (x12, y12-face2Thick, sandwichThick)
vertOrig = vertList.findAt(pOrig)
pXAxis = (x11, y12-face2Thick, sandwichThick)
vertX = vertList.findAt(pXAxis)
pYAxis = (x12, y12-face2Thick, 0)
vertXY = vertList.findAt(pYAxis)
taperPart.DatumCsysByThreePoints(name='Datum Csys Face2', coordSysType=CARTESIAN,
  origin=vertOrig, point1=vertX, point2=vertXY)
# Upper cohesive zone
pOrig = (x10, y10-face2Thick-cohesiveThick, sandwichThick)
vertOrig = vertList.findAt(pOrig)
pXAxis = (x9, y10-face2Thick-cohesiveThick, sandwichThick)
vertX = vertList.findAt(pXAxis)
pYAxis = (x9, y10-face2Thick-cohesiveThick, 0)
vertXY = vertList.findAt(pYAxis)
taperPart.DatumCsysByThreePoints(name='Datum Csys Cohesive2', coordSysType=CARTESIAN,
  origin=vertOrig, point1=vertX, point2=vertXY)
# Core
pOrig = (x4, y4+face1Thick-cohesiveThick, sandwichThick)
vertOrig = vertList.findAt(pOrig)
pXAxis = (x5, y4+face1Thick-cohesiveThick, sandwichThick)
vertX = vertList.findAt(pXAxis)
pYAxis = (x5, y4+face1Thick-cohesiveThick, 0)
vertXY = vertList.findAt(pYAxis)
taperPart.DatumCsysByThreePoints(name='Datum Csys Core', coordSysType=CARTESIAN,
  origin=vertOrig, point1=vertX, point2=vertXY)
# Tapered top facesheet
pOrig = (x11a+offsetThickX, y11a-offsetThickY, sandwichThick)
vertOrig = vertList.findAt(pOrig)
pXAxis = (x10a+offsetThickX, y10a-offsetThickY, sandwichThick)
vertX = vertList.findAt(pXAxis)
pYAxis = (x11a+offsetThickX, y11a-offsetThickY, 0)
vertXY = vertList.findAt(pYAxis)
taperPart.DatumCsysByThreePoints(name='Datum Csys Face2 Taper', coordSysType=CARTESIAN,
  origin=vertOrig, point1=vertX, point2=vertXY)
# Tapered cohesive region
pOrig = (x11a+offsetCohThickX, y11a-offsetCohThickY, sandwichThick)
vertOrig = vertList.findAt(pOrig)
pXAxis = (x10a+offsetCohThickX, y10a-offsetCohThickY, sandwichThick)
vertX = vertList.findAt(pXAxis)
pYAxis = (x11a+offsetCohThickX, y11a-offsetCohThickY, 0)
vertXY = vertList.findAt(pYAxis)
taperPart.DatumCsysByThreePoints(name='Datum Csys Cohesive2 Taper', coordSysType=CARTESIAN,
  origin=vertOrig, point1=vertX, point2=vertXY)
# Curved top facesheet 1
pOrig = (x11, y11+filletRadius, sandwichThick)
taperPart.DatumPointByCoordinate(pOrig)
vertOrig = taperPart.datums[taperPart.datums.keys()[len(taperPart.datums)-1]]
pRaxis = (x11, y11, sandwichThick)
vertR = vertList.findAt(pRaxis)
pRThetaPlane = (x11a, y11a, sandwichThick)
vertRTheta = vertList.findAt(pRThetaPlane)
taperPart.DatumCsysByThreePoints(name='Datum Csys Face2 Curve1', coordSysType=CYLINDRICAL,
  origin=vertOrig, point1=vertR, point2=vertRTheta)
# Curved top facesheet 2
pOrig = (x10, y10-filletRadius, sandwichThick)
taperPart.DatumPointByCoordinate(pOrig)
vertOrig = taperPart.datums[taperPart.datums.keys()[len(taperPart.datums)-1]]
pRaxis = (x10, y10, sandwichThick)
vertR = vertList.findAt(pRaxis)
pRThetaPlane = (x10a, y10a, sandwichThick)
vertRTheta = vertList.findAt(pRThetaPlane)
taperPart.DatumCsysByThreePoints(name='Datum Csys Face2 Curve2', coordSysType=CYLINDRICAL,
  origin=vertOrig, point1=vertR, point2=vertRTheta)

#----------------------------------------------------------------
# Assign orientations
#----------------------------------------------------------------
datumList = taperPart.datums
# Lower facesheet
datumKey = datumList.keys()[0]
datumCsys = datumList[datumKey]
taperPart.MaterialOrientation(region=setFace1, localCsys=datumCsys, axis=AXIS_1,
  additionalRotationField='', additionalRotationType=ROTATION_NONE,
  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
# Lower cohesive zone
#datumKey = datumList.keys()[1]
#datumCsys = datumList[datumKey]
#taperPart.MaterialOrientation(region=setCohesiveFaceFace, localCsys=datumCsys, axis=AXIS_1,
#  additionalRotationField='', additionalRotationType=ROTATION_NONE,
#  angle=0.0, stackDirection=STACK_1, fieldName='', orientationType=SYSTEM)
#taperPart.MaterialOrientation(region=setCohesiveFaceCoreBot, localCsys=datumCsys, axis=AXIS_1,
#  additionalRotationField='', additionalRotationType=ROTATION_NONE,
#  angle=0.0, stackDirection=STACK_1, fieldName='', orientationType=SYSTEM)
# Upper facesheet
datumKey = datumList.keys()[2]
datumCsys = datumList[datumKey]
taperPart.MaterialOrientation(region=setFace2, localCsys=datumCsys, axis=AXIS_1,
  additionalRotationField='', additionalRotationType=ROTATION_NONE,
  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
# Upper cohesive zone
#datumKey = datumList.keys()[3]
#datumCsys = datumList[datumKey]
#taperPart.MaterialOrientation(region=setCohesiveFaceCoreTop, localCsys=datumCsys, axis=AXIS_1,
#  additionalRotationField='', additionalRotationType=ROTATION_NONE,
#  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
# Core
datumKey = datumList.keys()[4]
datumCsys = datumList[datumKey]
taperPart.MaterialOrientation(region=setCore, localCsys=datumCsys, axis=AXIS_1,
  additionalRotationField='', additionalRotationType=ROTATION_NONE,
  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
taperPart.MaterialOrientation(region=setCoreTaper, localCsys=datumCsys, axis=AXIS_1,
  additionalRotationField='', additionalRotationType=ROTATION_NONE,
  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
# Tapered top facesheet
datumKey = datumList.keys()[5]
datumCsys = datumList[datumKey]
taperPart.MaterialOrientation(region=setFace2Taper, localCsys=datumCsys, axis=AXIS_1,
  additionalRotationField='', additionalRotationType=ROTATION_NONE,
  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
# Tapered cohesive region
#datumKey = datumList.keys()[6]
#datumCsys = datumList[datumKey]
#taperPart.MaterialOrientation(region=setCohesiveFaceCoreTaper, localCsys=datumCsys, 
#  additionalRotationField='', additionalRotationType=ROTATION_NONE,
#  axis=AXIS_1, angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
# Curved top facesheet 1
datumKey = datumList.keys()[8]
datumCsys = datumList[datumKey]
taperPart.MaterialOrientation(region=setFace2Curve1, localCsys=datumCsys, axis=AXIS_1,
  additionalRotationField='', additionalRotationType=ROTATION_NONE,
  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
# Curved top facesheet 2
datumKey = datumList.keys()[10]
datumCsys = datumList[datumKey]
taperPart.MaterialOrientation(region=setFace2Curve2, localCsys=datumCsys, axis=AXIS_1,
  additionalRotationField='', additionalRotationType=ROTATION_NONE,
  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
  
#----------------------------------------------------------------
# Create instances and step
#----------------------------------------------------------------
taperInst = taperAssem.Instance(dependent=ON, name='TaperAssembly', part=taperPart)
taperAssem.regenerate()
taperStep = taperModel.StaticStep(name='Step-1', previous='Initial')
taperStep.setValues(nlgeom=ON, maxNumInc=10000,
  stabilizationMagnitude=0.0002,
  stabilizationMethod=DISSIPATED_ENERGY_FRACTION,
  continueDampingFactors=False, adaptiveDampingRatio=0.05, initialInc=1e-05,
  minInc=1.0e-8, maxInc=0.001)

#----------------------------------------------------------------
# Create regions for applying bcs
#----------------------------------------------------------------
edgeList = taperInst.edges
faceList = taperInst.faces

# Left bottom edge
pLeftBot = (x1, y1, midPanel)
edgeLeftBot = edgeList.findAt((pLeftBot,))
setEdgeLeftBot = taperAssem.Set(name='EdgeLeftBot', edges=edgeLeftBot)
regEdgeLeftBot = regionToolset.Region(edges=edgeLeftBot)

# Left symmetry face
pLeftFace1 = (x1, y1+midFace1, midPanel)
pLeftCohesive = (x1, y1+face1Thick-midCohesive, midPanel)
pLeftFace2 = (x12, y12-midFace2, midPanel)
symmLeftFace = faceList.findAt((pLeftFace1,), (pLeftCohesive,), (pLeftFace2,))
setSymmLeftFace = taperAssem.Set(name='SymmLeftFace', faces=symmLeftFace)
regSymmLeftFace = regionToolset.Region(faces=symmLeftFace)

# Loading edge
pLoad = (x9, y9, midPanel)
edgeLoad = edgeList.findAt((pLoad,))
setEdgeLoad = taperAssem.Set(name='EdgeLoad', edges=edgeLoad)
regEdgeLoad = regionToolset.Region(edges=edgeLoad)

# Right support edge
pRightBot = (x5, y5, midPanel)
edgeRightBot = edgeList.findAt((pRightBot,))
setEdgeRightBot = taperAssem.Set(name='EdgeRightBot', edges=edgeRightBot)
regEdgeRightBot = regionToolset.Region(edges=edgeRightBot)

# Thickness symmetry face
symmThickFace = faceList[0:0]
for jj in range(len(faceList)):
  curFace = faceList[jj:jj+1]
  centroid = curFace[0].getCentroid()
  zCentroid = centroid[0][2]
  print zCentroid
  if zCentroid == 0.0:
    print curFace
    symmThickFace += curFace

setSymmThickFace = taperAssem.Set(name='SymmThickFace', faces=symmThickFace)
regSymmThickFace = regionToolset.Region(faces=symmThickFace)

#----------------------------------------------------------------
# Create displacement BCs
#----------------------------------------------------------------
taperModel.DisplacementBC(name='Left support BC', createStepName='Step-1',
  region=regEdgeLeftBot, u2 = 0.0)
taperModel.DisplacementBC(name='Right support BC', createStepName='Step-1',
  region=regEdgeRightBot, u2 = 0.0)
taperModel.DisplacementBC(name='Left Symmetry BC', createStepName='Step-1',
  region=regSymmLeftFace, u1 = 0.0)
taperModel.DisplacementBC(name='Thickness Symmetry BC', createStepName='Step-1',
  region=setSymmThickFace, u3 = 0.0)
taperModel.DisplacementBC(name='Load BC', createStepName='Step-1',
  region=setEdgeLoad, u2 = -0.01)

#----------------------------------------------------------------
# Create mesh
#----------------------------------------------------------------
# Element types
elemSolid1 = ElemType(elemCode=C3D8R, elemLibrary=STANDARD,
  kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF,
  hourglassControl=DEFAULT, distortionControl=DEFAULT)
elemSolid2 = ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemCohesive1 = ElemType(elemCode=COH3D8, elemLibrary=STANDARD)
elemCohesive2 = ElemType(elemCode=COH3D6, elemLibrary=STANDARD)

# Seed the part
taperPart.seedPart(size=hSize, deviationFactor=0.1)

# Mesh controls
taperPart.setMeshControls(regions=setFace1.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
taperPart.setMeshControls(regions=setFace2.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
taperPart.setMeshControls(regions=setFace2Taper.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
#taperPart.setMeshControls(regions=setFace1ExtraBit.cells, technique=SWEEP,
#  algorithm=ADVANCING_FRONT, elemShape=WEDGE)
taperPart.setMeshControls(regions=setCore.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
taperPart.setMeshControls(regions=setCoreTaper.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
taperPart.setMeshControls(regions=setCohesiveFaceFace.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
taperPart.setMeshControls(regions=setCohesiveFaceCoreBot.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
taperPart.setMeshControls(regions=setCohesiveFaceCoreTop.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
taperPart.setMeshControls(regions=setCohesiveFaceCoreTaper.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
taperPart.setMeshControls(regions=setCohesiveFaceCoreCurve1.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
taperPart.setMeshControls(regions=setCohesiveFaceCoreCurve2.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
taperPart.setMeshControls(regions=setFace2Curve1.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
taperPart.setMeshControls(regions=setFace2Curve2.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)

# Set element type
taperPart.setElementType(regions=setFace1, elemTypes=(elemSolid1, elemSolid2))
taperPart.setElementType(regions=setFace2, elemTypes=(elemSolid1, elemSolid2))
taperPart.setElementType(regions=setFace2Taper, elemTypes=(elemSolid1, elemSolid2))
taperPart.setElementType(regions=setCore, elemTypes=(elemSolid1, elemSolid2))
taperPart.setElementType(regions=setCoreTaper, elemTypes=(elemSolid1, elemSolid2))
taperPart.setElementType(regions=setCohesiveFaceFace, 
  elemTypes=(elemCohesive1, elemCohesive2))
taperPart.setElementType(regions=setCohesiveFaceCoreBot, 
  elemTypes=(elemCohesive1, elemCohesive2))
taperPart.setElementType(regions=setCohesiveFaceCoreTop, 
  elemTypes=(elemCohesive1, elemCohesive2))
taperPart.setElementType(regions=setCohesiveFaceCoreTaper, 
  elemTypes=(elemCohesive1, elemCohesive2))
taperPart.setElementType(regions=setCohesiveFaceCoreCurve1, 
  elemTypes=(elemCohesive1, elemCohesive2))
taperPart.setElementType(regions=setCohesiveFaceCoreCurve2, 
  elemTypes=(elemCohesive1, elemCohesive2))
taperPart.setElementType(regions=setFace2Curve1, elemTypes=(elemSolid1, elemSolid2))
taperPart.setElementType(regions=setFace2Curve2, elemTypes=(elemSolid1, elemSolid2))

# Generate mesh
taperPart.generateMesh()

#----------------------------------------------------------------
# Add XFEM controls
#----------------------------------------------------------------
taperAssem = taperModel.rootAssembly
setCoreTaper = taperInst.sets['CoreTaper']
taperAssem.engineeringFeatures.XFEMCrack(name='Crack-1', crackDomain=setCoreTaper)
taperInteract = taperModel.XFEMCrackGrowth(name='Int-1', createStepName='Initial', crackName='Crack-1')
#: The interaction "Int-1" has been created.
taperInteract.setValues(allowGrowth=False)
taperInteract.setValuesInStep(stepName='Step-1', allowGrowth=True)
taperContact = taperModel.ContactProperty('IntProp-1')
taperContact.NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON, contactStiffness=DEFAULT,
    contactStiffnessScaleFactor=1.0, clearanceAtZeroContactPressure=0.0,
    stiffnessBehavior=LINEAR, constraintEnforcementMethod=PENALTY)
#: The interaction property "IntProp-1" has been created.
#taperModel.historyOutputRequests['H-Output-1'].setValues(
#    contourIntegral='Crack-1', sectionPoints=DEFAULT, rebar=EXCLUDE,
#    numberOfContours=2)
taperModel.fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U', 'RF', 'CF', 'CSTRESS', 'CDISP', 'CSDMG', 'CSMAXSCRT', 'CSMAXUCRT', 'PHILSM', 'PSILSM'))

#----------------------------------------------------------------
# Create Job
#----------------------------------------------------------------
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF,
  explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF,
  memory=90, memoryUnits=PERCENTAGE, model='TaperModelCurveXFEM1', modelPrint=OFF,
  multiprocessingMode=DEFAULT, name='TaperModelCurveXFEM1', nodalOutputPrecision=SINGLE,
  numCpus=1, numDomains=1, queue=None, scratch='', type=ANALYSIS,
  userSubroutine='', waitHours=0, waitMinutes=0)

