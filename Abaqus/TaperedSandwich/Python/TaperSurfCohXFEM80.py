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
if mdb.models.has_key('TaperSurfCohXFEM'):
  del mdb.models['TaperSurfCohXFEM']

taperModel = mdb.Model(name='TaperSurfCohXFEM')
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
#cohesiveThick = 5.0e-6
cohesiveThick =0.001 
#cohesiveThick =0.0001 
#cohesiveThick = 1.0e-5
sandwichThick = 0.05
filletRadius = 0.03

midFace1 = 0.5*face1Thick
midFace2 = 0.5*face2Thick
midCohesive = 0.5*cohesiveThick
midPanel = 0.5*sandwichThick
offsetThickX = face2Thick*sin(taperAngle)
offsetThickY = face2Thick*cos(taperAngle)
offsetThickXCurve = face2Thick*sin(0.5*taperAngle)

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

# Create sketch for entire model
taperSketch = taperModel.ConstrainedSketch(name='__profile__', sheetSize=3.0)

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
 
# Create sketch for top facesheet
topFaceSketch = taperModel.ConstrainedSketch(name='__profile__', sheetSize=3.0)

topFaceSketch.Line(point1=p07, point2=p08)
topFaceSketch.Line(point1=p08, point2=p09)
topFaceSketch.Line(point1=p09, point2=p10)
topFaceSketch.Line(point1=p10, point2=p11)
topFaceSketch.Line(point1=p11, point2=p12)
topFaceSketch.Line(point1=p12, point2=p13)

## Create the partition on the sketch
geomList = topFaceSketch.geometry
pp = (0.5*(x12+x11), y12)
geomID = geomList.findAt(pp).id
offsetEdge = (geomList[geomID],)
pp = (0.5*(x11+x10), 0.5*(y11+y10))
geomID = geomList.findAt(pp).id
offsetEdge += (geomList[geomID],)
pp = (0.5*(x10+x9), 0.5*(y10+y9))
geomID = geomList.findAt(pp).id
offsetEdge += (geomList[geomID],)
pp = (0.5*(x9+x8), 0.5*(y9+y8))
geomID = geomList.findAt(pp).id
offsetEdge += (geomList[geomID],)

topFaceSketch.offset(distance=face2Thick, objectList=offsetEdge, side=LEFT,
  filletCorners=FALSE)

## Create fillets
taperGeom = topFaceSketch.geometry
pCurve1 = (0.5*(x11+x12), y11)
curve1 = taperGeom.findAt(pCurve1)
pCurve2 = (0.5*(x11+x10), 0.5*(y11+y10))
curve2 = taperGeom.findAt(pCurve2)
topFaceSketch.FilletByRadius(radius=filletRadius, curve1=curve1, nearPoint1=pCurve1,
  curve2=curve2, nearPoint2=pCurve2)

taperGeom = topFaceSketch.geometry
pCurve1 = pCurve2
curve1 = taperGeom.findAt(pCurve1)
pCurve2 = (0.5*(x9+x10), y9)
curve2 = taperGeom.findAt(pCurve2)
topFaceSketch.FilletByRadius(radius=filletRadius, curve1=curve1, nearPoint1=pCurve1,
  curve2=curve2, nearPoint2=pCurve2)

taperGeom = topFaceSketch.geometry
pCurve1 = (0.5*(x9+x10), y9-face2Thick)
curve1 = taperGeom.findAt(pCurve1)
pCurve2 = (0.5*(x11+x10)+offsetThickXCurve, 0.5*(y11+y10)-face2Thick)
curve2 = taperGeom.findAt(pCurve2)
topFaceSketch.FilletByRadius(radius=filletRadius, curve1=curve1, nearPoint1=pCurve1,
  curve2=curve2, nearPoint2=pCurve2)

## Extrude
topFacePart = taperModel.Part(dimensionality=THREE_D, name='TopFacePart', type=
  DEFORMABLE_BODY)
topFacePart.BaseSolidExtrude(depth=sandwichThick, sketch=topFaceSketch)
del topFaceSketch
 
# Find the new points in the filleted region
pEdgeMid = (0.5*(x11+x12), 0.5*(y11+y12), 0.0)
edgeList = taperPart.edges
edge = edgeList.findAt(pEdgeMid)
vertexList = taperPart.vertices
vertEdge = edge.getVertices()
pFillet11 = vertexList[vertEdge[1]].pointOn[0]
 
pEdgeMid = (0.5*(x11+x10), 0.5*(y10+y12), 0.0)
pFillet11a = vertexList[vertEdge[0]].pointOn[0]
edge = edgeList.findAt(pEdgeMid)
vertexList = taperPart.vertices
vertEdge = edge.getVertices()
pFillet11a = vertexList[vertEdge[0]].pointOn[0]
pFillet10a = vertexList[vertEdge[1]].pointOn[0]
 
pEdgeMid = (0.5*(x10+x9), 0.5*(y10+y9), 0.0)
edgeList = taperPart.edges
edge = edgeList.findAt(pEdgeMid)
vertexList = taperPart.vertices
vertEdge = edge.getVertices()
pFillet10 = vertexList[vertEdge[0]].pointOn[0]

x10, y10 = pFillet10[0], pFillet10[1]
x10a, y10a = pFillet10a[0], pFillet10a[1]
x11, y11 = pFillet11[0], pFillet11[1]
x11a, y11a = pFillet11a[0], pFillet11a[1]

# Find the new points in the unfilleted region
edgeList = topFacePart.edges
vertexList = topFacePart.vertices
pEdgeMid = (0.5*(x12+x11), y12-face2Thick, 0)
edge = edgeList.findAt(pEdgeMid)
vertEdge = edge.getVertices()
p14 = vertexList[vertEdge[0]].pointOn[0]

# Create sketch for bottom facesheet
botFaceSketch = taperModel.ConstrainedSketch(name='__profile__', sheetSize=3.0)

botFaceSketch.Line(point1=p01, point2=p02)
botFaceSketch.Line(point1=p02, point2=p03)
botFaceSketch.Line(point1=p03, point2=p04)
botFaceSketch.Line(point1=p04, point2=p05)
botFaceSketch.Line(point1=p05, point2=p06)
botFaceSketch.Line(point1=p06, point2=p13)
botFaceSketch.Line(point1=p13, point2=p01)

## Extrude
botFacePart = taperModel.Part(dimensionality=THREE_D, name='BotFacePart', type=
  DEFORMABLE_BODY)
botFacePart.BaseSolidExtrude(depth=sandwichThick, sketch=botFaceSketch)
del botFaceSketch

#----------------------------------------------------------------
# Create paritions on the parts
#----------------------------------------------------------------
# Partition the top face to isolate the tapered region and load location
edgeList = topFacePart.edges
cellList = topFacePart.cells
pEdgeMid = (0.5*(x11+x12), 0.5*(y11+y12), 0.0)
edgeToPartition = edgeList.findAt(pEdgeMid)
topFacePart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=pFillet11,
  cells=cellList)

edgeList = topFacePart.edges
cellList = topFacePart.cells
pEdgeMid = (0.5*(x10+x9), 0.5*(y10+y9), 0.0)
edgeToPartition = edgeList.findAt(pEdgeMid)
topFacePart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=pFillet10,
  cells=cellList)

edgeList = topFacePart.edges
cellList = topFacePart.cells
pEdgeMid = (0.5*(x10+x9), 0.5*(y10+y9), 0.0)
p09 = (x9, y9, 0)
edgeToPartition = edgeList.findAt(pEdgeMid)
topFacePart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=p09,
  cells=cellList)

# Partition the top face to isolate the curved regions
edgeList = topFacePart.edges
vertexList = topFacePart.vertices
cellList = topFacePart.cells
pEdgeMid = (0.5*(x10a+x11a), 0.5*(y10a+y11a), 0.0)
edgeToPartition = edgeList.findAt(pEdgeMid)
vertEdge = edgeToPartition.getVertices()
pt1 = vertexList[vertEdge[0]].pointOn
pt2 = vertexList[vertEdge[1]].pointOn
topFacePart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=pt1[0],
  cells=cellList)

edgeList = topFacePart.edges
cellList = topFacePart.cells
pEdgeMid = (0.5*(x10a+x11a), 0.5*(y10a+y11a), 0.0)
edgeToPartition = edgeList.findAt(pEdgeMid)
topFacePart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=pt2[0],
  cells=cellList)

# Partition the bottom face to isolate the tapered region and load
#edgeList = botFacePart.edges
#cellList = botFacePart.cells
#pEdgeMid = (0.5*(x1+x2), 0.5*(y1+y2), 0.0)
#p02 = (x2, y2, 0.0)
#edgeToPartition = edgeList.findAt(pEdgeMid)
#botFacePart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=p02,
#  cells=cellList)

x14 = p14[0]
y14 = p14[1]
edgeList = botFacePart.edges
tPartition = (x3 - x14)/(x3 - x2)
pLoc = (x14, 0, 0)
edgeToPartition = edgeList.findAt(pLoc)
botFacePart.PartitionEdgeByParam(edges=edgeToPartition, parameter=tPartition)
cellList = botFacePart.cells
botFacePart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=pLoc,
  cells=cellList)

#edgeList = botFacePart.edges
#cellList = botFacePart.cells
#pEdgeMid = (0.5*(x2+x3), 0.5*(y2+y3), 0.0)
#p03 = (x3, y3, 0.0)
#edgeToPartition = edgeList.findAt(pEdgeMid)
#botFacePart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=p03,
#  cells=cellList)

edgeList = botFacePart.edges
tPartition = (x4 - x10)/(x4 - x3)
pLoc = (x10, 0, 0)
edgeToPartition = edgeList.findAt(pLoc)
botFacePart.PartitionEdgeByParam(edges=edgeToPartition, parameter=tPartition)
cellList = botFacePart.cells
botFacePart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=pLoc,
  cells=cellList)

edgeList = botFacePart.edges
cellList = botFacePart.cells
pEdgeMid = (x4-cohesiveThick, 0, 0)
p04 = (x4, y4, 0.0)
edgeToPartition = edgeList.findAt(pEdgeMid)
botFacePart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=p04,
  cells=cellList)

edgeList = botFacePart.edges
tPartition = (x2 - x11)/(x2 - x1)
pLoc = (x11, 0, 0)
edgeToPartition = edgeList.findAt(pLoc)
botFacePart.PartitionEdgeByParam(edges=edgeToPartition, parameter=tPartition)
cellList = botFacePart.cells
botFacePart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=pLoc,
  cells=cellList)


# Partition the full part to isolate the tapered region and load
edgeList = taperPart.edges
vertexList = taperPart.vertices
cellList = taperPart.cells
pEdgeMid = (0.5*(x10+x9), 0.5*(y10+y9), 0.0)
edgeToPartition = edgeList.findAt(pEdgeMid)
vertEdge = edgeToPartition.getVertices()
taperPart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=pFillet10,
  cells=cellList)

edgeList = taperPart.edges
cellList = taperPart.cells
pEdgeMid = (0.5*(x10+x9), 0.5*(y10+y9), 0.0)
p09 = (x9, y9, 0)
edgeToPartition = edgeList.findAt(pEdgeMid)
taperPart.PartitionCellByPlaneNormalToEdge(edge=edgeToPartition, point=p09,
  cells=cellList)

#----------------------------------------------------------------
# Set up material properties
#----------------------------------------------------------------
matCore = taperModel.Material(name='Core')
matCoreXFEM = taperModel.Material(name='CoreXFEM')
matFace1 = taperModel.Material(name='Face1')
matFace2 = taperModel.Material(name='Face2')

matCore.Elastic(type=ENGINEERING_CONSTANTS, table=coreElastic)
matCoreXFEM.Elastic(type=ENGINEERING_CONSTANTS, table=coreElastic)
matCoreXFEM.MaxpeDamageInitiation(table=((0.005, ), ))
matCoreXFEM.maxpeDamageInitiation.DamageEvolution(type=DISPLACEMENT, 
  table=((0.005, ), ))
matFace1.Elastic(type=ENGINEERING_CONSTANTS, table=face1Elastic)
matFace2.Elastic(type=ENGINEERING_CONSTANTS, table=face2Elastic)

#----------------------------------------------------------------
# Set up sections
#----------------------------------------------------------------
secCore = taperModel.HomogeneousSolidSection(name='Core', material='Core', thickness=None)
secCoreXFEM = taperModel.HomogeneousSolidSection(name='CoreXFEM', material='CoreXFEM', thickness=None)
secFace1 = taperModel.HomogeneousSolidSection(name='Face1', material='Face1', thickness=None)
secFace2 = taperModel.HomogeneousSolidSection(name='Face2', material='Face2', thickness=None)

#----------------------------------------------------------------
# Assign sections
#----------------------------------------------------------------
# Bottom facesheet
cellList = botFacePart.cells
region = regionToolset.Region(cells=cellList)
botFacePart.SectionAssignment(region=region, sectionName='Face1')
setFace1 = botFacePart.Set(name='Face1', cells=cellList)
# Top facesheet (flat)
cellList = topFacePart.cells
pCellMid1 = (0.5*(x12+x11), y12, midPanel)
pCellMid2 = (0.5*(x10+x9), y10, midPanel)
pCellMid3 = (0.5*(x9+x8), y9, midPanel)
cellSequence = cellList.findAt((pCellMid1,),(pCellMid2,),(pCellMid3,))
region = regionToolset.Region(cells=cellSequence)
topFacePart.SectionAssignment(region=region, sectionName='Face2')
setFace2 = topFacePart.Set(name='Face2', cells=cellSequence)
# Top facesheet (tapered)
pCellMid1 = (0.5*(x11a+x10a), 0.5*(y11a+y10a), midPanel)
cellSequence = cellList.findAt((pCellMid1,))
region = regionToolset.Region(cells=cellSequence)
topFacePart.SectionAssignment(region=region, sectionName='Face2')
setFace2Taper = topFacePart.Set(name='Face2Taper', cells=cellSequence)
# Top facesheet (lower curve)
pCellMid1 = (x11+cohesiveThick, y11-cohesiveThick, midPanel)
cellSequence = cellList.findAt((pCellMid1,))
region = regionToolset.Region(cells=cellSequence)
topFacePart.SectionAssignment(region=region, sectionName='Face2')
setFace2Curve1 = topFacePart.Set(name='Face2Curve1', cells=cellSequence)
# Top facesheet (upper curve)
pCellMid1 = (x10-cohesiveThick, y10-cohesiveThick, midPanel)
cellSequence = cellList.findAt((pCellMid1,))
region = regionToolset.Region(cells=cellSequence)
topFacePart.SectionAssignment(region=region, sectionName='Face2')
setFace2Curve2 = topFacePart.Set(name='Face2Curve2', cells=cellSequence)

#----------------------------------------------------------------
# Create instances and assembly
#----------------------------------------------------------------
taperInst = taperAssem.Instance(dependent=ON, name='Taper-1', part=taperPart)
botFaceInst = taperAssem.Instance(dependent=ON, name='BotFace-1', part=botFacePart)
topFaceInst = taperAssem.Instance(dependent=ON, name='TopFace-1', part=topFacePart)
taperAssem.regenerate()

#----------------------------------------------------------------
# Create the core region
#----------------------------------------------------------------
taperAssem.InstanceFromBooleanCut(name='Core',
  instanceToBeCut=taperInst, cuttingInstances=(botFaceInst, topFaceInst, ), 
  originalInstances=SUPPRESS)
taperAssem.features['BotFace-1'].resume()
taperAssem.features['TopFace-1'].resume()
del taperAssem.features['Taper-1']
#del taperPart
coreInst = taperAssem.instances['Core-1']
corePart = taperModel.parts['Core']

# Core 
cellList = corePart.cells
pCellMid1 = (x10+cohesiveThick, 0.5*y10, midPanel)
pCellMid2 = (x9+cohesiveThick, 0.5*y9, midPanel)
cellSequence = cellList.findAt((pCellMid1,), (pCellMid2,))
region = regionToolset.Region(cells=cellSequence)
corePart.SectionAssignment(region=region, sectionName='Core')
setCore = corePart.Set(name='Core', cells=cellSequence)
# Core XFEM
cellList = corePart.cells
pCellMid1 = (x10-cohesiveThick, 0.5*y10, midPanel)
cellSequence = cellList.findAt((pCellMid1,))
region = regionToolset.Region(cells=cellSequence)
corePart.SectionAssignment(region=region, sectionName='CoreXFEM')
setCoreXFEM = corePart.Set(name='CoreXFEM', cells=cellSequence)

#----------------------------------------------------------------
# Create virtual topology
#----------------------------------------------------------------
corePart.createVirtualTopology(mergeShortEdges=True, shortEdgeThreshold=0.0017,
    mergeSmallFaces=True, smallFaceAreaThreshold=1.4e-05,
    mergeSliverFaces=True, faceAspectRatioThreshold=10.0,
    mergeSmallAngleFaces=True, smallFaceCornerAngleThreshold=10.0,
    mergeThinStairFaces=True, thinStairFaceThreshold=0.00034,
    ignoreRedundantEntities=True, cornerAngleTolerance=30.0,
    applyBlendControls=True, blendSubtendedAngleTolerance=60.0,
    blendRadiusTolerance=0.0085)
botFacePart.createVirtualTopology(mergeShortEdges=True, shortEdgeThreshold=0.0017,
    mergeSmallFaces=True, smallFaceAreaThreshold=1.4e-05,
    mergeSliverFaces=True, faceAspectRatioThreshold=10.0,
    mergeSmallAngleFaces=True, smallFaceCornerAngleThreshold=10.0,
    mergeThinStairFaces=True, thinStairFaceThreshold=0.00034,
    ignoreRedundantEntities=True, cornerAngleTolerance=30.0,
    applyBlendControls=True, blendSubtendedAngleTolerance=60.0,
    blendRadiusTolerance=0.0085)
topFacePart.createVirtualTopology(mergeShortEdges=True, shortEdgeThreshold=0.0017,
    mergeSmallFaces=True, smallFaceAreaThreshold=1.4e-05,
    mergeSliverFaces=True, faceAspectRatioThreshold=10.0,
    mergeSmallAngleFaces=True, smallFaceCornerAngleThreshold=10.0,
    mergeThinStairFaces=True, thinStairFaceThreshold=0.00034,
    ignoreRedundantEntities=True, cornerAngleTolerance=30.0,
    applyBlendControls=True, blendSubtendedAngleTolerance=60.0,
    blendRadiusTolerance=0.0085)

#----------------------------------------------------------------
# Create datum coordinate systems
#----------------------------------------------------------------
# Lower facesheet
vertList = botFacePart.vertices
pOrig = (x1, y1, sandwichThick)
vertOrig = vertList.findAt(pOrig)
pXAxis = (x11, y1, sandwichThick)
vertX = vertList.findAt(pXAxis)
pYAxis = (x1, y1, 0)
vertXY = vertList.findAt(pYAxis)
botFacePart.DatumCsysByThreePoints(name='Datum Csys Face1', coordSysType=CARTESIAN,
  origin=vertOrig, point1=vertX, point2=vertXY)

# Core
vertList = corePart.vertices
pOrig = (x4, y4+face1Thick, sandwichThick)
vertOrig = vertList.findAt(pOrig)
pXAxis = (x5, y4+face1Thick, sandwichThick)
vertX = vertList.findAt(pXAxis)
pYAxis = (x5, y4+face1Thick, 0)
vertXY = vertList.findAt(pYAxis)
corePart.DatumCsysByThreePoints(name='Datum Csys Core', coordSysType=CARTESIAN,
  origin=vertOrig, point1=vertX, point2=vertXY)

# Top facesheet (flat)
vertList = topFacePart.vertices
pOrig = (x12, y12-face2Thick, sandwichThick)
vertOrig = vertList.findAt(pOrig)
pXAxis = (x11, y12-face2Thick, sandwichThick)
vertX = vertList.findAt(pXAxis)
pYAxis = (x12, y12-face2Thick, 0)
vertXY = vertList.findAt(pYAxis)
topFacePart.DatumCsysByThreePoints(name='Datum Csys Face2', coordSysType=CARTESIAN,
  origin=vertOrig, point1=vertX, point2=vertXY)

# Top facesheet (taper)
pOrig = (x11a, y11a, sandwichThick)
vertOrig = vertList.findAt(pOrig)
pXAxis = (x10a, y10a, sandwichThick)
vertX = vertList.findAt(pXAxis)
pYAxis = (x11a, y11a, 0)
vertXY = vertList.findAt(pYAxis)
topFacePart.DatumCsysByThreePoints(name='Datum Csys Face2 Taper', coordSysType=CARTESIAN,
  origin=vertOrig, point1=vertX, point2=vertXY)

# Top facesheet (lower curve : 1)
pOrig = (x11, y11+filletRadius, sandwichThick)
topFacePart.DatumPointByCoordinate(pOrig)
vertOrig = topFacePart.datums[topFacePart.datums.keys()[len(topFacePart.datums)-1]]
pRaxis = (x11, y11, sandwichThick)
vertR = vertList.findAt(pRaxis)
pRThetaPlane = (x11a, y11a, sandwichThick)
vertRTheta = vertList.findAt(pRThetaPlane)
topFacePart.DatumCsysByThreePoints(name='Datum Csys Face2 Curve1', coordSysType=CYLINDRICAL,
  origin=vertOrig, point1=vertR, point2=vertRTheta)

# Top facesheet (upper curve : 2)
pOrig = (x10, y10-filletRadius, sandwichThick)
topFacePart.DatumPointByCoordinate(pOrig)
vertOrig = topFacePart.datums[topFacePart.datums.keys()[len(topFacePart.datums)-1]]
pRaxis = (x10, y10, sandwichThick)
vertR = vertList.findAt(pRaxis)
pRThetaPlane = (x10a, y10a, sandwichThick)
vertRTheta = vertList.findAt(pRThetaPlane)
topFacePart.DatumCsysByThreePoints(name='Datum Csys Face2 Curve2', coordSysType=CYLINDRICAL,
  origin=vertOrig, point1=vertR, point2=vertRTheta)

#----------------------------------------------------------------
# Assign orientations
#----------------------------------------------------------------
# Lower facesheet
datumList = botFacePart.datums
datumKey = datumList.keys()[0]
datumCsys = datumList[datumKey]
botFacePart.MaterialOrientation(region=setFace1, localCsys=datumCsys, axis=AXIS_1,
  additionalRotationField='', additionalRotationType=ROTATION_NONE,
  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
# Core
datumList = corePart.datums
datumKey = datumList.keys()[0]
datumCsys = datumList[datumKey]
corePart.MaterialOrientation(region=setCore, localCsys=datumCsys, axis=AXIS_1,
  additionalRotationField='', additionalRotationType=ROTATION_NONE,
  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
corePart.MaterialOrientation(region=setCoreXFEM, localCsys=datumCsys, axis=AXIS_1,
  additionalRotationField='', additionalRotationType=ROTATION_NONE,
  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
# Top facesheet (flat)
datumList = topFacePart.datums
datumKey = datumList.keys()[0]
datumCsys = datumList[datumKey]
topFacePart.MaterialOrientation(region=setFace2, localCsys=datumCsys, axis=AXIS_1,
  additionalRotationField='', additionalRotationType=ROTATION_NONE,
  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
# Top facesheet (taper)
datumKey = datumList.keys()[1]
datumCsys = datumList[datumKey]
topFacePart.MaterialOrientation(region=setFace2Taper, localCsys=datumCsys, axis=AXIS_1,
  additionalRotationField='', additionalRotationType=ROTATION_NONE,
  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
# Top facesheet (curve 1)
datumKey = datumList.keys()[3]
datumCsys = datumList[datumKey]
topFacePart.MaterialOrientation(region=setFace2Curve1, localCsys=datumCsys, axis=AXIS_1,
  additionalRotationField='', additionalRotationType=ROTATION_NONE,
  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)
# Top facesheet (curve 2)
datumKey = datumList.keys()[5]
datumCsys = datumList[datumKey]
topFacePart.MaterialOrientation(region=setFace2Curve2, localCsys=datumCsys, axis=AXIS_1,
  additionalRotationField='', additionalRotationType=ROTATION_NONE,
  angle=0.0, stackDirection=STACK_3, fieldName='', orientationType=SYSTEM)

#----------------------------------------------------------------
# Create the step
#----------------------------------------------------------------
taperStep = taperModel.StaticStep(name='Step-1', previous='Initial')
taperStep.setValues(nlgeom=ON, maxNumInc=10000,
  stabilizationMagnitude=0.0002,
  stabilizationMethod=DISSIPATED_ENERGY_FRACTION,
  continueDampingFactors=False, adaptiveDampingRatio=0.05, initialInc=1e-05,
  minInc=1.0e-8, maxInc=0.01)

#----------------------------------------------------------------
# Create regions for applying bcs
#----------------------------------------------------------------
# Left bottom edge
edgeList = botFaceInst.edges
pLeftBot = (x1, y1, midPanel)
edgeLeftBot = edgeList.findAt((pLeftBot,))
setEdgeLeftBot = taperAssem.Set(name='EdgeLeftBot', edges=edgeLeftBot)
regEdgeLeftBot = regionToolset.Region(edges=edgeLeftBot)

# Left symmetry face
faceList = botFaceInst.faces
pLeftFace1 = (x1, y1+midFace1, midPanel)
symmLeftFace = faceList.findAt((pLeftFace1,))
faceList = topFaceInst.faces
pLeftFace2 = (x12, y12-midFace2, midPanel)
symmLeftFace += faceList.findAt((pLeftFace2,))
setSymmLeftFace = taperAssem.Set(name='SymmLeftFace', faces=symmLeftFace)
regSymmLeftFace = regionToolset.Region(faces=symmLeftFace)

# Loading edge
edgeList = topFaceInst.edges
pLoad = (x9, y9, midPanel)
edgeLoad = edgeList.findAt((pLoad,))
setEdgeLoad = taperAssem.Set(name='EdgeLoad', edges=edgeLoad)
regEdgeLoad = regionToolset.Region(edges=edgeLoad)

# Right support edge
edgeList = botFaceInst.edges
pRightBot = (x5, y5, midPanel)
edgeRightBot = edgeList.findAt((pRightBot,))
setEdgeRightBot = taperAssem.Set(name='EdgeRightBot', edges=edgeRightBot)
regEdgeRightBot = regionToolset.Region(edges=edgeRightBot)

# Thickness symmetry face
symmThickFace = faceList[0:0]
for ii in range(len(taperAssem.instances)):
  key = taperAssem.instances.keys()[ii]
  faceList = taperAssem.instances[key].faces
  for jj in range(len(faceList)):
    curFace = faceList[jj:jj+1]
    centroid = curFace[0].getCentroid()
    zCentroid = centroid[0][2]
    #print zCentroid
    if zCentroid == 0.0:
      #print curFace
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
taperAssem.regenerate()

#----------------------------------------------------------------
# Create mesh
#----------------------------------------------------------------
# Element types
elemSolid1 = ElemType(elemCode=C3D8R, elemLibrary=STANDARD,
  kinematicSplit=AVERAGE_STRAIN, secondOrderAccuracy=OFF,
  hourglassControl=DEFAULT, distortionControl=DEFAULT)
elemSolid2 = ElemType(elemCode=C3D6, elemLibrary=STANDARD)

# Seed the part
topFacePart.seedPart(size=hSize, deviationFactor=0.1)
botFacePart.seedPart(size=hSize, deviationFactor=0.1)
corePart.seedPart(size=hSize, deviationFactor=0.1)

# Mesh controls
taperAssem.regenerate()
botFacePart.setMeshControls(regions=setFace1.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
topFacePart.setMeshControls(regions=setFace2.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
topFacePart.setMeshControls(regions=setFace2Taper.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
topFacePart.setMeshControls(regions=setFace2Curve1.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
topFacePart.setMeshControls(regions=setFace2Curve2.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
corePart.setMeshControls(regions=setCore.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)
corePart.setMeshControls(regions=setCoreXFEM.cells, technique=SWEEP,
  algorithm=ADVANCING_FRONT, elemShape=HEX)

# Set element type
taperAssem.regenerate()
botFacePart.setElementType(regions=setFace1, elemTypes=(elemSolid1, elemSolid2))
topFacePart.setElementType(regions=setFace2, elemTypes=(elemSolid1, elemSolid2))
topFacePart.setElementType(regions=setFace2Taper, elemTypes=(elemSolid1, elemSolid2))
topFacePart.setElementType(regions=setFace2Curve1, elemTypes=(elemSolid1, elemSolid2))
topFacePart.setElementType(regions=setFace2Curve2, elemTypes=(elemSolid1, elemSolid2))
corePart.setElementType(regions=setCore, elemTypes=(elemSolid1, elemSolid2))
corePart.setElementType(regions=setCoreXFEM, elemTypes=(elemSolid1, elemSolid2))

# Generate mesh
taperAssem.regenerate()
botFacePart.generateMesh()
topFacePart.generateMesh()
corePart.generateMesh()

#----------------------------------------------------------------
# Add XFEM controls
#----------------------------------------------------------------
taperAssem = taperModel.rootAssembly
setCoreTaper = coreInst.sets['CoreXFEM']
taperAssem.engineeringFeatures.XFEMCrack(name='Crack-1', crackDomain=setCoreTaper)
taperInteract = taperModel.XFEMCrackGrowth(name='Int-1', createStepName='Initial', 
  crackName='Crack-1')
taperInteract.setValues(allowGrowth=False)
taperInteract.setValuesInStep(stepName='Step-1', allowGrowth=True)
taperContact = taperModel.ContactProperty('IntProp-1')
taperContact.NormalBehavior(
    pressureOverclosure=HARD, allowSeparation=ON, contactStiffness=DEFAULT,
    contactStiffnessScaleFactor=1.0, clearanceAtZeroContactPressure=0.0,
    stiffnessBehavior=LINEAR, constraintEnforcementMethod=PENALTY)
taperModel.fieldOutputRequests['F-Output-1'].setValues(
    variables=('S', 'PE', 'PEEQ', 'PEMAG', 'LE', 'U', 'RF', 'CF', 'CSTRESS',
    'CDISP', 'CSDMG', 'CSMAXSCRT', 'CSMAXUCRT', 'PHILSM', 'PSILSM'))

#----------------------------------------------------------------
# Add surface to surface cohesive interactions
#----------------------------------------------------------------
## Contact properties
taperCohContact = taperModel.ContactProperty('IntProp-2')
taperCohContact.CohesiveBehavior(repeatedContacts=ON, defaultPenalties=OFF, 
  table=((faceFaceEKnn, faceFaceG1Kss, faceFaceG2Ktt), ))

## Tie the two faces
taperAssem.regenerate()
topFaceList = topFaceInst.faces
topEdgeList = topFaceInst.edges
topVertList = topFaceInst.vertices
topCellList = topFaceInst.cells
botFaceList = botFaceInst.faces
botEdgeList = botFaceInst.edges
botVertList = botFaceInst.vertices
botCellList = botFaceInst.cells
coreFaceList = coreInst.faces
coreEdgeList = coreInst.edges
coreVertList = coreInst.vertices
coreCellList = coreInst.cells

topFaceSeq = topFaceList[0:0]
botFaceSeq = botFaceList[0:0]

### First edge
#### Top face
pp = (0.5*(x12+x11), y12-face2Thick, sandwichThick)
e1 = topEdgeList.findAt(pp)
faces = e1.getFaces()
topFace = topFaceList[0:0]
for jj in range(len(faces)):
  curFace = topFaceList[faces[jj]]
  center = curFace.getCentroid()
  topFace = topFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

#### Bottom face
ppc = (0.5*(x12+x11), y12-face2Thick, sandwichThick)
e1c = botEdgeList.findAt(ppc)
faces = e1c.getFaces()
botFace = topFaceList[0:0]
for jj in range(len(faces)):
  curFace = botFaceList[faces[jj]]
  center = curFace.getCentroid()
  botFace = botFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

#### Tie
topFaceSeq += topFace
botFaceSeq += botFace

region1 = regionToolset.Region(side1Faces=topFaceSeq)
region2 = regionToolset.Region(side2Faces=botFaceSeq)
intFaceFace = taperModel.SurfaceToSurfaceContactStd(name='Int-2',
  createStepName='Initial', master=region1, slave=region2, sliding=FINITE,
  thickness=ON, interactionProperty='IntProp-2', adjustMethod=NONE,
  initialClearance=OMIT, datumAxis=None, clearanceRegion=None)

## Tie the top surfaces

### Top face
topFaceSeq = topFaceList[0:0]
#### edge 1
e2 = boundaryUtils.getNextEdge3D(topEdgeList, topVertList, e1)
e2 = boundaryUtils.getNextEdge3D(topEdgeList, topVertList, e2)
faces = e2.getFaces()
topFace = topFaceList[0:0]
for jj in range(len(faces)):
  curFace = topFaceList[faces[jj]]
  center = curFace.pointOn
  topFace = topFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

topFaceSeq += topFace

#### edge 2
e2 = boundaryUtils.getNextEdge3D(topEdgeList, topVertList, e2)
faces = e2.getFaces()
topFace = topFaceList[0:0]
for jj in range(len(faces)):
  curFace = topFaceList[faces[jj]]
  center = curFace.pointOn
  topFace = topFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

topFaceSeq += topFace

#### edge 3
e2 = boundaryUtils.getNextEdge3D(topEdgeList, topVertList, e2)
faces = e2.getFaces()
topFace = topFaceList[0:0]
for jj in range(len(faces)):
  curFace = topFaceList[faces[jj]]
  center = curFace.pointOn
  topFace = topFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

topFaceSeq += topFace

#### edge 4
e2 = boundaryUtils.getNextEdge3D(topEdgeList, topVertList, e2)
faces = e2.getFaces()
topFace = topFaceList[0:0]
for jj in range(len(faces)):
  curFace = topFaceList[faces[jj]]
  center = curFace.pointOn
  topFace = topFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

topFaceSeq += topFace

### Bottom face
botFaceSeq = botFaceList[0:0]

#### Edge 1
x15 = x10a + offsetThickX
y15 = y10a - offsetThickY
pp = (0.5*(x14+x15), 0.5*(y14+y15), sandwichThick)
e2c = coreEdgeList.findAt(pp)
faces = e2c.getFaces()
botFace = coreFaceList[0:0]
for jj in range(len(faces)):
  curFace = coreFaceList[faces[jj]]
  center = curFace.pointOn
  botFace = coreFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

botFaceSeq += botFace

#### Edge 2
e2c = boundaryUtils.getNextEdge3D(coreEdgeList, coreVertList, e2c)
faces = e2c.getFaces()
botFace = coreFaceList[0:0]
for jj in range(len(faces)):
  curFace = coreFaceList[faces[jj]]
  center = curFace.pointOn
  botFace = coreFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

botFaceSeq += botFace

#### Edge 3
e2c = boundaryUtils.getNextEdge3D(coreEdgeList, coreVertList, e2c)
faces = e2c.getFaces()
botFace = coreFaceList[0:0]
for jj in range(len(faces)):
  curFace = coreFaceList[faces[jj]]
  center = curFace.pointOn
  botFace = coreFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

botFaceSeq += botFace

#### Edge 4
e2c = boundaryUtils.getNextEdge3D(coreEdgeList, coreVertList, e2c)
faces = e2c.getFaces()
botFace = coreFaceList[0:0]
for jj in range(len(faces)):
  curFace = coreFaceList[faces[jj]]
  center = curFace.pointOn
  botFace = coreFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

botFaceSeq += botFace

#### Tie
region1 = regionToolset.Region(side1Faces=topFaceSeq)
region2 = regionToolset.Region(side2Faces=botFaceSeq)
intCoreTop = taperModel.SurfaceToSurfaceContactStd(name='Int-3',
  createStepName='Initial', master=region1, slave=region2, sliding=FINITE,
  thickness=ON, interactionProperty='IntProp-2', adjustMethod=NONE,
  initialClearance=OMIT, datumAxis=None, clearanceRegion=None)

## Tie the bottom surfaces

### Top face
topFaceSeq = coreFaceList[0:0]

#### Edge 1
pp = (0.5*(x14+x10), face1Thick, sandwichThick)
e2c = coreEdgeList.findAt(pp)
faces = e2c.getFaces()
topFace = coreFaceList[0:0]
for jj in range(len(faces)):
  curFace = coreFaceList[faces[jj]]
  center = curFace.pointOn
  topFace = coreFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

topFaceSeq += topFace

#### Edge 2
e2c = boundaryUtils.getNextEdge3D(coreEdgeList, coreVertList, e2c)
faces = e2c.getFaces()
topFace = coreFaceList[0:0]
for jj in range(len(faces)):
  curFace = coreFaceList[faces[jj]]
  center = curFace.pointOn
  topFace = coreFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

topFaceSeq += topFace

#### Edge 3
e2c = boundaryUtils.getNextEdge3D(coreEdgeList, coreVertList, e2c)
faces = e2c.getFaces()
topFace = coreFaceList[0:0]
for jj in range(len(faces)):
  curFace = coreFaceList[faces[jj]]
  center = curFace.pointOn
  topFace = coreFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

topFaceSeq += topFace

### Bottom face
botFaceSeq = botFaceList[0:0]

#### Edge 1
pp = (0.5*(x14+x10), face1Thick, sandwichThick)
e2c = botEdgeList.findAt(pp)
faces = e2c.getFaces()
botFace = botFaceList[0:0]
for jj in range(len(faces)):
  curFace = botFaceList[faces[jj]]
  center = curFace.pointOn
  botFace = botFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

botFaceSeq += botFace

#### Edge 2
e2c = boundaryUtils.getNextEdge3D(botEdgeList, botVertList, e2c)
faces = e2c.getFaces()
botFace = botFaceList[0:0]
for jj in range(len(faces)):
  curFace = botFaceList[faces[jj]]
  center = curFace.pointOn
  botFace = botFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

botFaceSeq += botFace

#### Edge 3
e2c = boundaryUtils.getNextEdge3D(botEdgeList, botVertList, e2c)
faces = e2c.getFaces()
botFace = botFaceList[0:0]
for jj in range(len(faces)):
  curFace = botFaceList[faces[jj]]
  center = curFace.pointOn
  botFace = botFaceList.findAt(center)
  zCenter = center[0][2]
  if (zCenter < sandwichThick):
    break

botFaceSeq += botFace

region1 = regionToolset.Region(side1Faces=topFaceSeq)
region2 = regionToolset.Region(side2Faces=botFaceSeq)
intCoreBot = taperModel.SurfaceToSurfaceContactStd(name='Int-4',
  createStepName='Initial', master=region1, slave=region2, sliding=FINITE,
  thickness=ON, interactionProperty='IntProp-2', adjustMethod=NONE,
  initialClearance=OMIT, datumAxis=None, clearanceRegion=None)

# Change to node to surface contact
intFaceFace.setValues(initialClearance=OMIT, surfaceSmoothing=NONE, adjustMethod=NONE,
  sliding=FINITE, enforcement=NODE_TO_SURFACE, thickness=OFF,
  supplementaryContact=SELECTIVE, smooth=0.2, bondingSet=None)
intCoreTop.setValues(initialClearance=OMIT, surfaceSmoothing=NONE, adjustMethod=NONE,
  sliding=FINITE, enforcement=NODE_TO_SURFACE, thickness=OFF,
  supplementaryContact=SELECTIVE, smooth=0.2, bondingSet=None)
intCoreBot.setValues(initialClearance=OMIT, surfaceSmoothing=NONE, adjustMethod=NONE,
  sliding=FINITE, enforcement=NODE_TO_SURFACE, thickness=OFF,
  supplementaryContact=SELECTIVE, smooth=0.2, bondingSet=None)

#----------------------------------------------------------------
# Create Job
#----------------------------------------------------------------
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF,
  explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF,
  memory=90, memoryUnits=PERCENTAGE, model='TaperSurfCohXFEM', modelPrint=OFF,
  multiprocessingMode=DEFAULT, name='TaperSurfCohXFEM', nodalOutputPrecision=SINGLE,
  numCpus=1, numDomains=1, queue=None, scratch='', type=ANALYSIS,
  userSubroutine='', waitHours=0, waitMinutes=0)

