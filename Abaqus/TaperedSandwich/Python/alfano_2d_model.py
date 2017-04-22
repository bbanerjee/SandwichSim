######################################################################
# ABAQUS Benchmarks                                                  #
# Script to generate 2-dimensional model for non-symmetric multi-    #
# delamination analysis in ABAQUS/Standard.                          #
######################################################################
from abaqus import *
import testUtils
testUtils.setBackwardCompatibility()
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=261.9140625,    height=208.0078125)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
Mdb()
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#
# Change model name to Alfano
#
mdb.models.changeKey(fromName='Model-1', toName='Alfano')
session.viewports['Viewport: 1'].setValues(displayedObject=None)
#
# a. Sketch and create Plate part
# b. Create profile of two cracks and the cohesive layers
# c. Remove material from the plate part by extruding two cuts (a. - b.)
#
s = mdb.models['Alfano'].Sketch(name='__profile__', sheetSize=0.4)
g, v, d = s.geometry, s.vertices, s.dimensions
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(0.2, 0.0032065))
session.viewports['Viewport: 1'].view.fitView()
s.HorizontalDimension(vertex1=v[2], vertex2=v[6], textPoint=(    0.0984431654214859, -0.00427813269197941))
s.VerticalDimension(vertex1=v[6], vertex2=v[4], textPoint=(0.202578246593475,    0.00281412387266755))
p = mdb.models['Alfano'].Part(name='Plate', dimensionality=TWO_D_PLANAR,    type=DEFORMABLE_BODY)
p = mdb.models['Alfano'].parts['Plate']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Alfano'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Alfano'].sketches['__profile__']
s1 = mdb.models['Alfano'].Sketch(name='__profile__', sheetSize=0.4,    gridSpacing=0.01)
g, v, d = s1.geometry, s1.vertices, s1.dimensions
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Alfano'].parts['Plate']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
r, r1 = s1.referenceGeometry, s1.referenceVertices
s1.rectangle(point1=(0.0, 0.001325), point2=(0.2, 0.00133825))
s1.rectangle(point1=(0.0, 0.00160325), point2=(0.2, 0.0016165))
s1.VerticalDimension(vertex1=r1.findAt((0.0, 0.0), 1), vertex2=v[1],    textPoint=(-0.000283258472336456, 0.000579574669245631))
s1.VerticalDimension(vertex1=v[1], vertex2=v[2], textPoint=(    -0.000283258472336456, 0.00133974268101156))
s1.VerticalDimension(vertex1=v[2], vertex2=v[9], textPoint=(    -0.000282614288153127, 0.00158178864512593))
s1.VerticalDimension(vertex1=v[9], vertex2=v[10], textPoint=(    -0.000280867592664436, 0.00161846936680377))
session.viewports['Viewport: 1'].view.fitView()
s1.HorizontalDimension(vertex1=v[2], vertex2=v[6], textPoint=(    0.0364299640059471, -0.00248509692028165))
session.viewports['Viewport: 1'].view.fitView()
s1.HorizontalDimension(vertex1=v[9], vertex2=v[14], textPoint=(    0.0737828761339188, -0.0102748423814774))
s1.constraintReferences(vertex1=r1.findAt((0.0, 0.0), 1))
p = mdb.models['Alfano'].parts['Plate']
p.Cut(sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Alfano'].sketches['__profile__']
#
# Create top and bottom cohesive layers with finite thickness
#
s = mdb.models['Alfano'].Sketch(name='__profile__', sheetSize=0.4)
g, v, d = s.geometry, s.vertices, s.dimensions
s.setPrimaryObject(option=STANDALONE)
s.rectangle(point1=(0.0, 0.0), point2=(0.2, 1.325e-05))
session.viewports['Viewport: 1'].view.fitView()
s.HorizontalDimension(vertex1=v[1], vertex2=v[6], textPoint=(0.199968859553337,    -1.13981359390891e-05))
s.VerticalDimension(vertex1=v[6], vertex2=v[4], textPoint=(0.20001257956028,    6.92647154210135e-06))
p = mdb.models['Alfano'].Part(name='Bottom_cohesive',    dimensionality=TWO_D_PLANAR, type=DEFORMABLE_BODY)
p = mdb.models['Alfano'].parts['Bottom_cohesive']
p.BaseShell(sketch=s)
s.unsetPrimaryObject()
p = mdb.models['Alfano'].parts['Bottom_cohesive']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
del mdb.models['Alfano'].sketches['__profile__']
p = mdb.models['Alfano'].Part(name='Top_cohesive',    objectToCopy=mdb.models['Alfano'].parts['Bottom_cohesive'])
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s1 = mdb.models['Alfano'].Sketch(name='__profile__', sheetSize=0.4,    gridSpacing=0.01)
g, v, d = s1.geometry, s1.vertices, s1.dimensions
s1.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Alfano'].parts['Top_cohesive']
p.projectReferencesOntoSketch(sketch=s1, filter=COPLANAR_EDGES)
r, r1 = s1.referenceGeometry, s1.referenceVertices
s1.rectangle(point1=(0.0, 0.0), point2=(0.04, 1.325e-05))
session.viewports['Viewport: 1'].view.fitView()
s1.VerticalDimension(vertex1=v[4], vertex2=v[2], textPoint=(    -0.0020265206694603, 0.000235539977438748))
s1.constraintReferences(vertex1=r1.findAt((0.0, 0.0), 1))
p = mdb.models['Alfano'].parts['Top_cohesive']
p.Cut(sketch=s1)
s1.unsetPrimaryObject()
del mdb.models['Alfano'].sketches['__profile__']
p = mdb.models['Alfano'].parts['Bottom_cohesive']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
s = mdb.models['Alfano'].Sketch(name='__profile__', sheetSize=0.4,    gridSpacing=0.01)
g, v, d = s.geometry, s.vertices, s.dimensions
s.setPrimaryObject(option=SUPERIMPOSE)
p = mdb.models['Alfano'].parts['Bottom_cohesive']
p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
r, r1 = s.referenceGeometry, s.referenceVertices
s.rectangle(point1=(0.06, 0.0), point2=(0.08, 1.325e-05))
s.VerticalDimension(vertex1=v[1], vertex2=v[2], textPoint=(    -0.00223228335380554, 0.00554204545915127))
s.HorizontalDimension(vertex1=v[2], vertex2=v[6], textPoint=(    0.0799874514341354, -7.78574940341059e-06))
session.viewports['Viewport: 1'].view.fitView()
p = mdb.models['Alfano'].parts['Bottom_cohesive']
p.Cut(sketch=s)
s.unsetPrimaryObject()
del mdb.models['Alfano'].sketches['__profile__']
#
# Create material Mat1 for the plate and Coh for the cohesive layer
#
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON,    engineeringFeatures=ON)
mdb.models['Alfano'].Material(name='Coh').Elastic(type=TRACTION, table=((    850000000.0, 850000000.0, 850000000.0), ))
mdb.models['Alfano'].materials['Coh'].QuadsDamageInitiation(table=((3300000.0,    7000000.0, 0.0), ))
mdb.models['Alfano'].materials['Coh'].quadsDamageInitiation.DamageEvolution(    type=ENERGY, mixedModeBehavior=POWER_LAW, power=1.0, table=((330.0, 800.0,    0.0), ))
mdb.models['Alfano'].Material(name='Mat1')
mdb.models['Alfano'].materials['Mat1'].Density(table=((2038800.0, ), ))
mdb.models['Alfano'].materials['Mat1'].Elastic(type=ENGINEERING_CONSTANTS,    table=((115000000000.0, 8500000000.0, 8500000000.0, 0.29, 0.29, 0.3,    4500000000.0, 3300000000.0, 4500000000.0), ))
mdb.models['Alfano'].HomogeneousSolidSection(name='plate', material='Mat1',    thickness=0.02)
mdb.models['Alfano'].CohesiveSection(name='coh', material='Coh',    response=TRACTION_SEPARATION, initialThicknessType=GEOMETRY,    outOfPlaneThickness=0.02)
p = mdb.models['Alfano'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p2 = mdb.models['Alfano'].parts['Plate']
p2.DatumCsysByThreePoints(name='Global', coordSysType=CARTESIAN, origin=(0.0,    0.0, 0.0), point1=(1.0, 0.0, 0.0), line2=(0.0, 1.0, 0.0))
f = p2.faces
faces = f.findAt(((0.066667, 0.002147, 0.0),), ((0.133333, 0.000883, 0.0),), ((0.066667, 0.001427, 0.0),), )
region = regionToolset.Region(faces=faces)
p1 = mdb.models['Alfano'].parts['Plate']
datums = p1.datums[3]
p1.MaterialOrientation(region=region, localCsys=datums, axis=AXIS_3)
#: Specified material orientation has been assigned to the selected regions.
p1.SectionAssignment(region=region, sectionName='plate')
p = mdb.models['Alfano'].parts['Bottom_cohesive']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p2 = mdb.models['Alfano'].parts['Bottom_cohesive']
f = p2.faces
faces = f.findAt(((0.12, 4e-06, 0.0),), ((0.04, 9e-06, 0.0),), )
region = regionToolset.Region(faces=faces)
p1 = mdb.models['Alfano'].parts['Bottom_cohesive']
p1.SectionAssignment(region=region, sectionName='coh')
p = mdb.models['Alfano'].parts['Top_cohesive']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p2 = mdb.models['Alfano'].parts['Top_cohesive']
f = p2.faces
faces = f.findAt(((0.093333, 4e-06, 0.0),), )
region = regionToolset.Region(faces=faces)
p1 = mdb.models['Alfano'].parts['Top_cohesive']
p1.SectionAssignment(region=region, sectionName='coh')
a = mdb.models['Alfano'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Alfano'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Alfano'].parts['Bottom_cohesive']
a.Instance(name='Bottom_cohesive-1', part=p, dependent=ON)
a = mdb.models['Alfano'].rootAssembly
p = mdb.models['Alfano'].parts['Plate']
a.Instance(name='Plate-1', part=p, dependent=ON)
p3 = a.instances['Plate-1']
p3.translate(vector=(0.22, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a = mdb.models['Alfano'].rootAssembly
p = mdb.models['Alfano'].parts['Top_cohesive']
a.Instance(name='Top_cohesive-1', part=p, dependent=ON)
p3 = a.instances['Top_cohesive-1']
p3.translate(vector=(0.396, 0.0, 0.0))
session.viewports['Viewport: 1'].view.fitView()
a = mdb.models['Alfano'].rootAssembly
v11 = a.instances['Top_cohesive-1'].vertices
v12 = a.instances['Plate-1'].vertices
a.CoincidentPoint(movablePoint=v11.findAt((0.596, 0.0, 0.0)), fixedPoint=v12.findAt((0.42, 0.001603, 0.0)))
session.viewports['Viewport: 1'].view.fitView()
a = mdb.models['Alfano'].rootAssembly
v11 = a.instances['Bottom_cohesive-1'].vertices
v12 = a.instances['Plate-1'].vertices
a.CoincidentPoint(movablePoint=v11.findAt((0.2, 0.0, 0.0)), fixedPoint=v12.findAt((0.42, 0.001325, 0.0)))
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(visibleInstances=(    'Plate-1', ))
a = mdb.models['Alfano'].rootAssembly
s1 = a.instances['Plate-1'].edges
side1Edges1 = s1.findAt(((0.27, 0.001617, 0.0),), )
#
# Create surfaces for defining *TIE and *CONTACT PAIRS
#
a.Surface(side1Edges=side1Edges1, name='top')
a = mdb.models['Alfano'].rootAssembly
s1 = a.instances['Plate-1'].edges
side1Edges1 = s1.findAt(((0.37, 0.001603, 0.0),), )
a.Surface(side1Edges=side1Edges1, name='middle-top')
a = mdb.models['Alfano'].rootAssembly
s1 = a.instances['Plate-1'].edges
side1Edges1 = s1.findAt(((0.27, 0.001338, 0.0),), )
a.Surface(side1Edges=side1Edges1, name='middle-bot')
a = mdb.models['Alfano'].rootAssembly
s1 = a.instances['Plate-1'].edges
side1Edges1 = s1.findAt(((0.37, 0.001325, 0.0),), )
a.Surface(side1Edges=side1Edges1, name='bottom')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(visibleInstances=(    'Bottom_cohesive-1', ))
session.viewports['Viewport: 1'].view.fitView()
a = mdb.models['Alfano'].rootAssembly
s1 = a.instances['Bottom_cohesive-1'].edges
side1Edges1 = s1.findAt(((0.39, 0.001338, 0.0),), )+s1.findAt(((0.265, 0.001338, 0.0),), )
a.Surface(side1Edges=side1Edges1, name='botCoh-Top')
a = mdb.models['Alfano'].rootAssembly
s1 = a.instances['Bottom_cohesive-1'].edges
side1Edges1 = s1.findAt(((0.33, 0.001325, 0.0),), )+s1.findAt(((0.235, 0.001325, 0.0),), )
a.Surface(side1Edges=side1Edges1, name='botCoh-Bot')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(visibleInstances=(    'Top_cohesive-1', ))
a = mdb.models['Alfano'].rootAssembly
s1 = a.instances['Top_cohesive-1'].edges
side1Edges1 = s1.findAt(((0.38, 0.001617, 0.0),), )
a.Surface(side1Edges=side1Edges1, name='topCoh-Top')
a = mdb.models['Alfano'].rootAssembly
s1 = a.instances['Top_cohesive-1'].edges
side1Edges1 = s1.findAt(((0.3, 0.001603, 0.0),), )
a.Surface(side1Edges=side1Edges1, name='topCoh-Bot')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(visibleInstances=(    'Bottom_cohesive-1', 'Plate-1', 'Top_cohesive-1'))
session.viewports['Viewport: 1'].view.fitView()
#
# Mesh the respective parts
#
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(    meshTechnique=ON)
p = mdb.models['Alfano'].parts['Top_cohesive']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF,    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(    meshTechnique=ON)
p = mdb.models['Alfano'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p2 = mdb.models['Alfano'].parts['Plate']
f = p2.faces
pickedRegions = f.findAt(((0.066667, 0.002147, 0.0),), ((0.133333, 0.000883, 0.0),), ((0.066667, 0.001427, 0.0),), )
p2.setMeshControls(regions=pickedRegions, technique=STRUCTURED)
p2 = mdb.models['Alfano'].parts['Plate']
e = p2.edges
pickedEdges = e.findAt(((0.05, 0.001617, 0.0),), )+e.findAt(((0.15, 0.003207, 0.0),), )+e.findAt(((0.15, 0.001325, 0.0),), )+e.findAt(((0.05, 0.0, 0.0),), )+e.findAt(((0.05, 0.001338, 0.0),), )+e.findAt(((0.15, 0.001603, 0.0),), )
p2.seedEdgeByNumber(edges=pickedEdges, number=200, constraint=FIXED)
session.viewports['Viewport: 1'].view.fitView()
p2 = mdb.models['Alfano'].parts['Plate']
e = p2.edges
pickedEdges = e.findAt(((0.2, 0.002014, 0.0),), )+e.findAt(((0.0, 0.002809, 0.0),), )+e.findAt(((0.0, 0.000994, 0.0),), )+e.findAt(((0.2, 0.000331, 0.0),), )+e.findAt(((0.2, 0.001404, 0.0),), )+e.findAt(((0.0, 0.001537, 0.0),), )
p2.seedEdgeByNumber(edges=pickedEdges, number=1, constraint=FIXED)
session.viewports['Viewport: 1'].view.fitView()
elemType1 = mesh.ElemType(elemCode=CPE4I, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=CPE3, elemLibrary=STANDARD)
p3 = mdb.models['Alfano'].parts['Plate']
f = p3.faces
faces = f.findAt(((0.066667, 0.002147, 0.0),), ((0.133333, 0.000883, 0.0),), ((0.066667, 0.001427, 0.0),), )
pickedRegions =(faces, )
p3.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
p3 = mdb.models['Alfano'].parts['Plate']
p3.generateMesh()
#
# Only swept meshing technique can be used for cohesive layers
#
p = mdb.models['Alfano'].parts['Top_cohesive']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
p2 = mdb.models['Alfano'].parts['Top_cohesive']
f = p2.faces
pickedRegions = f.findAt(((0.093333, 4e-06, 0.0),), )
p2.setMeshControls(regions=pickedRegions, technique=SWEEP, elemShape=QUAD)
p3 = mdb.models['Alfano'].parts['Top_cohesive']
f, e = p3.faces, p3.edges
p3.setSweepPath(region=f.findAt((0.093333, 4e-06, 0.0)), edge=e.findAt((0.04, 1e-05, 0.0)), sense=REVERSE)
p2 = mdb.models['Alfano'].parts['Top_cohesive']
e = p2.edges
pickedEdges = e.findAt(((0.04, 1e-05, 0.0),), )
p2.seedEdgeByNumber(edges=pickedEdges, number=1, constraint=FIXED)
p2 = mdb.models['Alfano'].parts['Top_cohesive']
e = p2.edges
pickedEdges = e.findAt(((0.08, 0.0, 0.0),), )
p2.seedEdgeBySize(edges=pickedEdges, size=0.001, constraint=FIXED)
elemType1 = mesh.ElemType(elemCode=COH2D4, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=UNKNOWN_TRI, elemLibrary=STANDARD)
p3 = mdb.models['Alfano'].parts['Top_cohesive']
f = p3.faces
faces = f.findAt(((0.093333, 4e-06, 0.0),), )
pickedRegions =(faces, )
p3.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
p3 = mdb.models['Alfano'].parts['Top_cohesive']
p3.generateMesh()
session.viewports['Viewport: 1'].view.fitView()
p = mdb.models['Alfano'].parts['Bottom_cohesive']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].view.fitView()
p2 = mdb.models['Alfano'].parts['Bottom_cohesive']
f = p2.faces
pickedRegions = f.findAt(((0.12, 4e-06, 0.0),), ((0.04, 9e-06, 0.0),), )
p2.setMeshControls(regions=pickedRegions, technique=SWEEP, elemShape=QUAD)
p3 = mdb.models['Alfano'].parts['Bottom_cohesive']
f1, e1 = p3.faces, p3.edges
p3.setSweepPath(region=f1[0], edge=e1[0], sense=REVERSE)
p3 = mdb.models['Alfano'].parts['Bottom_cohesive']
f, e = p3.faces, p3.edges
p3.setSweepPath(region=f.findAt((0.04, 9e-06, 0.0)), edge=e.findAt((0.0, 1e-05, 0.0)), sense=REVERSE)
session.viewports['Viewport: 1'].view.fitView()
p2 = mdb.models['Alfano'].parts['Bottom_cohesive']
e = p2.edges
pickedEdges = e.findAt(((0.08, 1e-05, 0.0),), )+e.findAt(((0.0, 1e-05, 0.0),), )
p2.seedEdgeByNumber(edges=pickedEdges, number=1, constraint=FIXED)
session.viewports['Viewport: 1'].view.fitView()
p2 = mdb.models['Alfano'].parts['Bottom_cohesive']
e = p2.edges
pickedEdges = e.findAt(((0.11, 0.0, 0.0),), )+e.findAt(((0.015, 0.0, 0.0),), )
p2.seedEdgeBySize(edges=pickedEdges, size=0.001, constraint=FIXED)
session.viewports['Viewport: 1'].view.fitView()
elemType1 = mesh.ElemType(elemCode=COH2D4, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=UNKNOWN_TRI, elemLibrary=STANDARD)
p3 = mdb.models['Alfano'].parts['Bottom_cohesive']
f = p3.faces
faces = f.findAt(((0.12, 4e-06, 0.0),), ((0.04, 9e-06, 0.0),), )
pickedRegions =(faces, )
p3.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
p3 = mdb.models['Alfano'].parts['Bottom_cohesive']
p3.generateMesh()
a = mdb.models['Alfano'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a2 = mdb.models['Alfano'].rootAssembly
a2.regenerate()
a = mdb.models['Alfano'].rootAssembly
v1 = a.instances['Plate-1'].vertices
verts1 = v1.findAt(((0.22, 0.003207, 0.0),), )
a.Set(vertices=verts1, name='topBC')
a = mdb.models['Alfano'].rootAssembly
v1 = a.instances['Plate-1'].vertices
verts1 = v1.findAt(((0.22, 0.0, 0.0),), )
a.Set(vertices=verts1, name='botBC')
session.viewports['Viewport: 1'].view.fitView()
session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(    meshTechnique=OFF)
#
# Create *STATIC step
#
mdb.models['Alfano'].StaticStep(name='Peel', previous='Initial',    description='Pulling apart the plates', maxNumInc=5000,    stabilizationMethod=DAMPING_FACTOR, stabilizationMagnitude=700000.0,    initialInc=0.01, minInc=1e-08, nlgeom=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Peel')
mdb.models['Alfano'].fieldOutputRequests['F-Output-1'].setValues(    frequency=9999)
a = mdb.models['Alfano'].rootAssembly
v1 = a.instances['Plate-1'].vertices
verts1 = v1.findAt(((0.22, 0.003207, 0.0),), )+v1.findAt(((0.22, 0.0, 0.0),), )
a.Set(vertices=verts1, name='dispBC')
regionDef=mdb.models['Alfano'].rootAssembly.sets['dispBC']
mdb.models['Alfano'].HistoryOutputRequest(name='H-Output-2',    createStepName='Peel', variables=('U2', 'RF2'), region=regionDef,    sectionPoints=DEFAULT, rebar=EXCLUDE)
mdb.models['Alfano'].fieldOutputRequests['F-Output-1'].setValues(variables=(    'S', 'U'))
a = mdb.models['Alfano'].rootAssembly
v1 = a.instances['Plate-1'].vertices
verts1 = v1.findAt(((0.22, 0.003207, 0.0),), )
region=regionToolset.Region(vertices=verts1)
mdb.models['Alfano'].steps['Peel'].Monitor(dof=2, node=region, frequency=1)
mdb.models['Alfano'].steps['Peel'].control.setValues(allowPropagation=OFF,    resetDefaultValues=OFF, discontinuous=ON, lineSearch=(4.0, 4.0, 0.25, 0.25,    0.15), timeIncrementation=(8, 10, 9, 16, 10, 4, 12, 10, 6))
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON,    predefinedFields=ON, connectors=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Alfano'].rootAssembly
region = a.sets['dispBC']
mdb.models['Alfano'].DisplacementBC(name='fix', createStepName='Initial',    region=region, u1=SET, u2=UNSET, ur3=UNSET, amplitude=UNSET,    distributionType=UNIFORM, localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Peel')
a = mdb.models['Alfano'].rootAssembly
region = a.sets['topBC']
mdb.models['Alfano'].DisplacementBC(name='applyDisp', createStepName='Peel',    region=region, u1=UNSET, u2=0.02, ur3=UNSET, amplitude=UNSET, fixed=OFF,    distributionType=UNIFORM, localCsys=None)
mdb.models['Alfano'].boundaryConditions.changeKey(fromName='applyDisp',    toName='topDisp')
a = mdb.models['Alfano'].rootAssembly
region = a.sets['botBC']
mdb.models['Alfano'].DisplacementBC(name='botDisp', createStepName='Peel',    region=region, u1=UNSET, u2=-0.02, ur3=UNSET, amplitude=UNSET, fixed=OFF,    distributionType=UNIFORM, localCsys=None)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF,    predefinedFields=OFF, interactions=ON, constraints=ON, engineeringFeatures=ON)
a = mdb.models['Alfano'].rootAssembly
region1=a.surfaces['top']
a = mdb.models['Alfano'].rootAssembly
region2=a.surfaces['topCoh-Top']
mdb.models['Alfano'].Tie(name='cohTop-Top', master=region1, slave=region2,    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON)
a = mdb.models['Alfano'].rootAssembly
region1=a.surfaces['middle-top']
a = mdb.models['Alfano'].rootAssembly
region2=a.surfaces['topCoh-Bot']
mdb.models['Alfano'].Tie(name='cohTop-Middle', master=region1, slave=region2,    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON)
a = mdb.models['Alfano'].rootAssembly
region1=a.surfaces['middle-bot']
a = mdb.models['Alfano'].rootAssembly
region2=a.surfaces['botCoh-Top']
mdb.models['Alfano'].Tie(name='botCoh-Middle', master=region1, slave=region2,    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON)
a = mdb.models['Alfano'].rootAssembly
region1=a.surfaces['bottom']
a = mdb.models['Alfano'].rootAssembly
region2=a.surfaces['botCoh-Bot']
mdb.models['Alfano'].Tie(name='botCoh-Bottom', master=region1, slave=region2,    positionToleranceMethod=COMPUTED, adjust=ON, tieRotations=ON)
mdb.models['Alfano'].ContactProperty('int')
mdb.models['Alfano'].interactionProperties['int'].TangentialBehavior(    formulation=FRICTIONLESS)
#: The interaction property "int" has been created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
a = mdb.models['Alfano'].rootAssembly
region1=a.surfaces['middle-bot']
a = mdb.models['Alfano'].rootAssembly
region2=a.surfaces['bottom']
mdb.models['Alfano'].SurfaceToSurfaceContactStd(name='lower',    createStepName='Initial', master=region1, slave=region2, sliding=FINITE,    interactionProperty='int', adjustMethod=NONE)
#: The interaction "lower" has been created.
a = mdb.models['Alfano'].rootAssembly
region1=a.surfaces['middle-top']
a = mdb.models['Alfano'].rootAssembly
region2=a.surfaces['top']
mdb.models['Alfano'].SurfaceToSurfaceContactStd(name='upper',    createStepName='Initial', master=region1, slave=region2, sliding=FINITE,    interactionProperty='int', adjustMethod=NONE)
#: The interaction "upper" has been created.
session.viewports['Viewport: 1'].assemblyDisplay.setValues(interactions=OFF,    constraints=OFF, connectors=OFF, engineeringFeatures=OFF)
mdb.Job(name='alfano_2d_tie_std', model='Alfano', type=ANALYSIS,    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE,    description='Alfano Crisfield non-symmetric multi-delamination analysis',    parallelizationMethodExplicit=DOMAIN, multiprocessingMode=DEFAULT,    numDomains=1, userSubroutine='', numCpus=1, scratch='',    echoPrint=OFF, modelPrint=OFF, contactPrint=OFF, historyPrint=OFF)
session.viewports['Viewport: 1'].view.fitView()
mdb.jobs['alfano_2d_tie_std'].writeInput()
#: The job input file has been written to "alfano_2d_tie_std.inp".
mdb.saveAs(pathName='alfano')

