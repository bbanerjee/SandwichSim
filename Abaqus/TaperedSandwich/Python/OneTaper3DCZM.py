# Save by banerjee on Fri Sep 16 14:47:39 2011
from abaqus import *
upgradeMdb('/home2/banerjee/Abaqus/AdvComp/OneTaper3D/one taper 3D-6.8-2.cae', 
    '/home2/banerjee/Abaqus/AdvComp/OneTaper3D/one taper 3D.cae')
# Save by banerjee on Fri Sep 16 14:47:39 2011
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
del mdb.jobs['Job-1']
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='OneTaper3D', nodalOutputPrecision=SINGLE
    , numCpus=2, numDomains=2, queue=None, scratch='', type=ANALYSIS, 
    userSubroutine='', waitHours=0, waitMinutes=0)
# Save by banerjee on Fri Sep 16 14:52:21 2011
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
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#410 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].seedEdgeBySize(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0 #80000000 ]', ), ), size=0.002)
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#40 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].seedEdgeBySize(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0:2 #1 ]', ), ), size=0.002)
mdb.models['Model-1'].parts['Part-2'].seedEdgeBySize(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0:2 #300 ]', ), ), size=0.002)
mdb.models['Model-1'].parts['Part-2'].seedEdgeBySize(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0 #100 ]', ), ), size=0.002)
mdb.models['Model-1'].parts['Part-2'].seedEdgeBySize(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0 #80018 ]', ), ), size=0.002)
mdb.models['Model-1'].parts['Part-2'].generateMesh()
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#410 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].seedEdgeBySize(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0 #80000110 #200 ]', ), ), size=0.0017)
mdb.models['Model-1'].parts['Part-2'].generateMesh()
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#410 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].seedEdgeByBias(biasMethod=DOUBLE, 
    endEdges=mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0 #80000000 ]', ), ), maxSize=0.002, minSize=0.001)
mdb.models['Model-1'].parts['Part-2'].generateMesh()
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#400 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#400 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].setSweepPath(edge=
    mdb.models['Model-1'].parts['Part-2'].edges[43], region=
    mdb.models['Model-1'].parts['Part-2'].cells[10], sense=FORWARD)
mdb.models['Model-1'].parts['Part-2'].generateMesh()
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#410 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].seedEdgeBySize(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0 #10 ]', ), ), size=0.002)
mdb.models['Model-1'].parts['Part-2'].seedEdgeBySize(deviationFactor=0.1, 
    edges=mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0 #80000110 #200 ]', ), ), size=0.0015)
mdb.models['Model-1'].parts['Part-2'].generateMesh()
mdb.models['Model-1'].HistoryOutputRequest(createStepName='Step-1', frequency=1
    , name='H-Output-1', variables=('IRA1', 'IRA2', 'IRA3', 'IRAR1', 'IRAR2', 
    'IRAR3', 'IRF1', 'IRF2', 'IRF3', 'IRM1', 'IRM2', 'IRM3'))
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF)
# Save by banerjee on Fri Sep 16 15:26:11 2011
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
mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
mdb.models['Model-1'].parts['Part-2'].deleteMesh()
mdb.models['Model-1'].parts['Part-2'].seedPart(deviationFactor=0.1, size=0.01)
mdb.models['Model-1'].parts['Part-2'].seedPart(deviationFactor=0.1, size=0.005)
mdb.models['Model-1'].RemeshingRule(coarseningFactor=DEFAULT_LIMIT, 
    description='', elementCountLimit=None, errorTarget=0.0, 
    maxSolutionErrorTarget=0.0, minSolutionErrorTarget=0.0, name=
    'RemeshingRule-1', outputFrequency=LAST_INCREMENT, refinementFactor=
    DEFAULT_LIMIT, region=Region(
    cells=mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].cells.getSequenceFromMask(
    mask=('[#400 ]', ), )), sizingMethod=DEFAULT, specifyMaxSize=False, 
    specifyMinSize=False, stepName='Step-1', variables=('ENDENERI', 
    'MISESERI'))
mdb.models['Model-1'].parts['Part-2'].setMeshControls(elemShape=TET, regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#400 ]', 
    ), ), sizeGrowth=MODERATE, technique=FREE)
mdb.models['Model-1'].parts['Part-2'].generateMesh()
# Save by banerjee on Fri Sep 16 16:08:50 2011
# Save by banerjee on Fri Sep 16 16:40:01 2011
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
mdb.models['Model-1'].rootAssembly.PartFromInstanceMesh(name='Part-2-mesh-1')
mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
mdb.models['Model-1'].parts['Part-2-mesh-1'].Set(elements=
    mdb.models['Model-1'].parts['Part-2-mesh-1'].elements.getSequenceFromMask(
    mask=('[#0:143 #80000000 #0:3 #80000000 #0:3 #80000000 #0:3', 
    ' #80000000 #0:3 #80000000 #0:3 #80000000 #0:3 #80000000', 
    ' #0:3 #80000000 #ffffffff:63 #20080200 #8020080 #2008020 #802008', 
    ' #80200802 #20080200 #8020080 #2008020 #802008 #80200802 #ffffff00', 
    ' #ffffffff:10 #ffff00ff #ffffffff:10 #ff00ffff #ffffffff:10 #ffffff #ffffffff:11', 
    ' #f #f00 #f0000 #f000000 #0 #f #f00', 
    ' #f0000 #f000000 #0:18 #f0000000 #0 #f0000000 #0', 
    ' #f0000000 #0 #f0000000 #0 #f0000000 #0 #f0000000', 
    ' #0 #f0000000 #0 #f0000000 #ffffffff:21 #fdffffff #ffffffff:49', 
    ' #feffffff #ffffffff:4 #fbffffff #ffffffff:11 #fffd7ffa #ffffffff:76 #fffffeff', 
    ' #ffffffff:31 #ffffffbf #ffffffff:16 #ffffefff #ffffffff:23 #fffffff7 #ffffffff:27', 
    ' #fdffffff #feffffff #ffffffff #f7fffdff #fffffdff #ffffffff:4 #fffffdff', 
    ' #ffffffff:2 #fffffdff #ffffffff:7 #ffffff7f #feffffff #ffffffff:2 #ffffffbf', 
    ' #ffffffef #ffffffff:2 #fffeffff #3ffff ]', ), ), name='BranchElements-1')
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'IF SIGNIFICANT CLEARANCE/OVERCLOSURE EXISTS BETWEEN SURFACE PAIR (ASSEMBLY__T0_PART-2-1_S,ASSEMBLY__T0_PART-2-1_M) AND THE MASTER SURFACE DOES NOT HAVE ROTATIONAL DEGREES OF FREEDOM, ADJUSTMENT IS RECOMMENDED FOR CORRECT ENFORCEMENT OF THE TIE CONSTRAINT', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'IF SIGNIFICANT CLEARANCE/OVERCLOSURE EXISTS BETWEEN SURFACE PAIR (ASSEMBLY__T1_PART-2-1_S,ASSEMBLY__T1_PART-2-1_M) AND THE MASTER SURFACE DOES NOT HAVE ROTATIONAL DEGREES OF FREEDOM, ADJUSTMENT IS RECOMMENDED FOR CORRECT ENFORCEMENT OF THE TIE CONSTRAINT', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'IF SIGNIFICANT CLEARANCE/OVERCLOSURE EXISTS BETWEEN SURFACE PAIR (ASSEMBLY__T2_PART-2-1_S,ASSEMBLY__T2_PART-2-1_M) AND THE MASTER SURFACE DOES NOT HAVE ROTATIONAL DEGREES OF FREEDOM, ADJUSTMENT IS RECOMMENDED FOR CORRECT ENFORCEMENT OF THE TIE CONSTRAINT', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST IRA1 IS NOT AVAILABLE FOR THIS TYPE OF ANALYSIS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST IRA2 IS NOT AVAILABLE FOR THIS TYPE OF ANALYSIS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST IRA3 IS NOT AVAILABLE FOR THIS TYPE OF ANALYSIS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST IRAR1 IS NOT AVAILABLE FOR THIS TYPE OF ANALYSIS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST IRAR2 IS NOT AVAILABLE FOR THIS TYPE OF ANALYSIS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST IRAR3 IS NOT AVAILABLE FOR THIS TYPE OF ANALYSIS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST IRF1 IS NOT AVAILABLE FOR THIS TYPE OF ANALYSIS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST IRF2 IS NOT AVAILABLE FOR THIS TYPE OF ANALYSIS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST IRF3 IS NOT AVAILABLE FOR THIS TYPE OF ANALYSIS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST IRM1 IS NOT AVAILABLE FOR THIS TYPE OF ANALYSIS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST IRM2 IS NOT AVAILABLE FOR THIS TYPE OF ANALYSIS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'OUTPUT REQUEST IRM3 IS NOT AVAILABLE FOR THIS TYPE OF ANALYSIS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'THE ELSET OR TRACER SET PARAMETER IS REQUIRED ON THE *ELEMENT OUTPUT OPTION FOR THIS OUTPUT DATABASE HISTORY REQUEST', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'THE ELSET OR TRACER SET PARAMETER IS REQUIRED ON THE *ELEMENT OUTPUT OPTION FOR THIS OUTPUT DATABASE HISTORY REQUEST', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'THE ELSET OR TRACER SET PARAMETER IS REQUIRED ON THE *ELEMENT OUTPUT OPTION FOR THIS OUTPUT DATABASE HISTORY REQUEST', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'THE ELSET OR TRACER SET PARAMETER IS REQUIRED ON THE *ELEMENT OUTPUT OPTION FOR THIS OUTPUT DATABASE HISTORY REQUEST', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '540 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'OneTaper3D'})
mdb.models['Model-1'].historyOutputRequests['H-Output-1'].setValues(variables=
    PRESELECT)
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'IF SIGNIFICANT CLEARANCE/OVERCLOSURE EXISTS BETWEEN SURFACE PAIR (ASSEMBLY__T0_PART-2-1_S,ASSEMBLY__T0_PART-2-1_M) AND THE MASTER SURFACE DOES NOT HAVE ROTATIONAL DEGREES OF FREEDOM, ADJUSTMENT IS RECOMMENDED FOR CORRECT ENFORCEMENT OF THE TIE CONSTRAINT', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'IF SIGNIFICANT CLEARANCE/OVERCLOSURE EXISTS BETWEEN SURFACE PAIR (ASSEMBLY__T1_PART-2-1_S,ASSEMBLY__T1_PART-2-1_M) AND THE MASTER SURFACE DOES NOT HAVE ROTATIONAL DEGREES OF FREEDOM, ADJUSTMENT IS RECOMMENDED FOR CORRECT ENFORCEMENT OF THE TIE CONSTRAINT', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'IF SIGNIFICANT CLEARANCE/OVERCLOSURE EXISTS BETWEEN SURFACE PAIR (ASSEMBLY__T2_PART-2-1_S,ASSEMBLY__T2_PART-2-1_M) AND THE MASTER SURFACE DOES NOT HAVE ROTATIONAL DEGREES OF FREEDOM, ADJUSTMENT IS RECOMMENDED FOR CORRECT ENFORCEMENT OF THE TIE CONSTRAINT', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '540 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 287.583601951599})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 1, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1, 
    'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 1, 
    'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(END_STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_COMPLETED, {
    'time': 'Mon Sep 19 12:13:52 2011', 'jobName': 'OneTaper3D'})
del mdb.models['Model-1'].parts['Part-2-mesh-1']
mdb.models['Model-1'].parts['Part-2'].setValues(space=THREE_D, type=
    DEFORMABLE_BODY)
mdb.models['Model-1'].Part(name='Part-2-failed', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'])
mdb.models['Model-1'].parts['Part-2-failed'].Unlock(reportWarnings=False)
del mdb.models['Model-1'].parts['Part-2']
mdb.models['Model-1'].parts.changeKey(fromName='Part-2-failed', toName=
    'Part-2')
mdb.models['Model-1'].rootAssembly.regenerate()
#* FeatureError: The assembly is locked and cannot be regenerated.
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'].sketch)
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'])
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].parts['Part-2'].regenerate()
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#5fb ]', 
    ), ))
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'].features['Partition face-1'].sketch)
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-2'].features['Partition face-1'])
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'].features['Partition face-1'].sketch)
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-2'].features['Partition face-1'])
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'].features['Partition face-2'].sketch)
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-2'].features['Partition face-2'])
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].parts['Part-2'].checkGeometry()
mdb.models['Model-1'].parts['Part-2'].PartitionEdgeByParam(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0:2 #20 ]', ), ), parameter=0.940457393207523)
mdb.models['Model-1'].parts['Part-2'].PartitionCellByPlaneNormalToEdge(cells=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#80 ]', 
    ), ), edge=mdb.models['Model-1'].parts['Part-2'].edges[70], point=
    mdb.models['Model-1'].parts['Part-2'].vertices[36])
mdb.models['Model-1'].parts['Part-2'].PartitionCellByPlaneNormalToEdge(cells=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#283 ]', 
    ), ), edge=mdb.models['Model-1'].parts['Part-2'].edges[6], point=
    mdb.models['Model-1'].parts['Part-2'].vertices[1])
mdb.models['Model-1'].parts['Part-2'].PartitionEdgeByParam(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0:2 #1 ]', ), ), parameter=0.00291854953763015)
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#2040 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].PartitionCellByPlaneNormalToEdge(cells=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#a0 ]', 
    ), ), edge=mdb.models['Model-1'].parts['Part-2'].edges[65], point=
    mdb.models['Model-1'].parts['Part-2'].vertices[37])
mdb.models['Model-1'].parts['Part-2'].PartitionCellByPlaneThreePoints(cells=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#11000 ]', ), ), point1=
    mdb.models['Model-1'].parts['Part-2'].InterestingPoint(
    mdb.models['Model-1'].parts['Part-2'].edges[82], MIDDLE), point2=
    mdb.models['Model-1'].parts['Part-2'].vertices[5], point3=
    mdb.models['Model-1'].parts['Part-2'].vertices[23])
# Save by banerjee on Mon Sep 19 14:38:24 2011
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
mdb.models['Model-1'].Material(name='CohesiveMatFaceFace')
mdb.models['Model-1'].materials['CohesiveMatFaceFace'].Elastic(table=((
    10000000.0, 0.45), ))
mdb.models['Model-1'].materials['CohesiveMatFaceFace'].QuadeDamageInitiation(
    table=((0.05, 0.05, 0.05), ))
mdb.models['Model-1'].materials['CohesiveMatFaceFace'].quadeDamageInitiation.DamageStabilizationCohesive(
    cohesiveCoeff=0.0001)
mdb.models['Model-1'].CohesiveSection(material='CohesiveMatFaceFace', name=
    'CohesiveSectionFaceFace', outOfPlaneThickness=1.0, response=
    TRACTION_SEPARATION)
mdb.models['Model-1'].parts['Part-2'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#4000 ]', ), )), sectionName='CohesiveSectionFaceFace', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-2'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#20010 ]', ), )), sectionName='CohesiveSectionFaceFace', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-2'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#8 ]', ), )), sectionName='CohesiveSectionFaceFace', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-2'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#2 ]', ), )), sectionName='CohesiveSectionFaceFace', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-2'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#20 ]', ), )), sectionName='CohesiveSectionFaceFace', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-2'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#4 ]', ), )), sectionName='CohesiveSectionFaceFace', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-2'].generateMesh(meshTechniqueOverride=ON)
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#40 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#1000 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#40 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#1000 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#40 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#1000 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].seedEdgeBySize(constraint=FINER, 
    deviationFactor=0.1, edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0:2 #1 ]', ), ), size=0.01)
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#1040 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#1040 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].deleteSeeds(regions=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0:2 #41 #40200 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].seedPart(size=0.01)
mdb.models['Model-1'].parts['Part-2'].seedPart(size=0.005)
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#40 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#1000 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#1000 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#2000 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#800 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#1 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#400 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#401 ]', 
    ), ), seedConstraintOverride=ON)
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#8000 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#10000 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#100 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#80 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#200 ]', 
    ), ))
# Save by banerjee on Tue Sep 20 12:24:33 2011
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
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#4000 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#1fac0 ]', ), ), seedConstraintOverride=ON)
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#20010 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#3ffd1 ]', ), ), seedConstraintOverride=ON)
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#20001 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].seedEdgeBySize(constraint=FINER, 
    deviationFactor=0.1, edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask(('[#1 ]', 
    ), ), size=0.0015)
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#1 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#20000 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#2 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#3ffd3 ]', ), ), seedConstraintOverride=ON)
mdb.models['Model-1'].parts['Part-2'].Set(elements=
    mdb.models['Model-1'].parts['Part-2'].elements.getSequenceFromMask(mask=(
    '[#0:551 #2082 #820800 #8200000 #80000002 #820 #208200', 
    ' #82080000 #20000000 #208 #82080 #20820000 #8000000 #82', 
    ' #20820 #8208000 #82000000 #20 #8208 #2082000 #20800000', 
    ' #8 #2082 #820800 #8200000 #80000002 #820 #208200 ]', ), ), name=
    'PoorElements-1')
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#8 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#3ffdb ]', ), ), seedConstraintOverride=ON)
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#20 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#4 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].generateMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#3ffff ]', ), ), seedConstraintOverride=ON)
mdb.models['Model-1'].parts['Part-2'].setElementType(elemTypes=(ElemType(
    elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#4000 ]', ), ), ))
# Save by banerjee on Fri Sep 23 16:06:04 2011
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
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#4000 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].setMeshControls(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#4000 ]', ), ), technique=BOTTOM_UP)
mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
mdb.models['Model-1'].parts['Part-2'].generateBottomUpSweptMesh(cell=
    mdb.models['Model-1'].parts['Part-2'].cells[14], geometryConnectingSides=
    Region(
    faces=mdb.models['Model-1'].parts['Part-2'].faces.getSequenceFromMask(
    mask=('[#4000000 #2000000 ]', ), )), geometrySourceSide=Region(
    faces=mdb.models['Model-1'].parts['Part-2'].faces.getSequenceFromMask(
    mask=('[#10000000 ]', ), )))
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#10 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].setMeshControls(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#10 ]', 
    ), ), technique=BOTTOM_UP)
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#20000 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].setMeshControls(elemShape=HEX, regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#20000 ]', ), ), technique=BOTTOM_UP)
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#2 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].setMeshControls(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#2 ]', 
    ), ), technique=BOTTOM_UP)
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#8 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].setMeshControls(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#8 ]', 
    ), ), technique=BOTTOM_UP)
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#bc41 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].PartitionCellByPlanePointNormal(cells=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#10 ]', 
    ), ), normal=mdb.models['Model-1'].parts['Part-2'].edges[46], point=
    mdb.models['Model-1'].parts['Part-2'].vertices[1])
#* Feature creation failed.
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#10000 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].PartitionCellByPlaneNormalToEdge(cells=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#20000 ]', ), ), edge=mdb.models['Model-1'].parts['Part-2'].edges[0], 
    point=mdb.models['Model-1'].parts['Part-2'].vertices[1])
mdb.models['Model-1'].parts['Part-2'].PartitionCellByPlaneNormalToEdge(cells=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#20 ]', 
    ), ), edge=mdb.models['Model-1'].parts['Part-2'].edges[18], point=
    mdb.models['Model-1'].parts['Part-2'].vertices[0])
mdb.models['Model-1'].parts['Part-2'].generateBottomUpSweptMesh(cell=
    mdb.models['Model-1'].parts['Part-2'].cells[1], geometrySourceSide=Region(
    faces=mdb.models['Model-1'].parts['Part-2'].faces.getSequenceFromMask(
    mask=('[#800 ]', ), )), numberOfLayers=1, targetSide=
    mdb.models['Model-1'].parts['Part-2'].faces[8])
# Save by banerjee on Mon Oct 10 14:19:09 2011
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
mdb.models['Model-1'].parts['Part-2'].generateMesh()
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'].sketch)
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'])
del mdb.models['Model-1'].sketches['__edit__']
del mdb.models['Model-1'].parts['Part-2'].features['Partition cell-16']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'].sketch)
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'])
del mdb.models['Model-1'].sketches['__edit__']
del mdb.models['Model-1'].parts['Part-2'].features['Partition cell-15']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'].sketch)
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'])
del mdb.models['Model-1'].sketches['__edit__']
del mdb.models['Model-1'].parts['Part-2'].features['Partition cell-14']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'].sketch)
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'])
del mdb.models['Model-1'].sketches['__edit__']
del mdb.models['Model-1'].parts['Part-2'].features['Partition cell-13']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'].sketch)
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'])
del mdb.models['Model-1'].sketches['__edit__']
del mdb.models['Model-1'].parts['Part-2'].features['Partition edge-2']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'].features['Partition face-1'].sketch)
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-2'].features['Partition face-1'])
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'].features['Partition face-4'].sketch)
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-2'].features['Partition face-4'])
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].parts['Part-2'].regenerate()
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.03, name='__profile__', 
    sheetSize=1.2, transform=
    mdb.models['Model-1'].parts['Part-2'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-2'].faces[65], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-2'].edges[64], 
    sketchOrientation=RIGHT, origin=(0.31, 0.05613, 0.08)))
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].Line(point1=(-0.06, 
    -0.0103769047009956), point2=(0.03, 0.02))
mdb.models['Model-1'].parts['Part-2'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['Part-2'].faces.getSequenceFromMask((
    '[#0:2 #2 ]', ), ), sketch=mdb.models['Model-1'].sketches['__profile__'], 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-2'].edges[64])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'].features['Partition face-5'].sketch)
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-2'].features['Partition face-5'])
mdb.models['Model-1'].sketches['__edit__'].ParallelConstraint(entity1=
    mdb.models['Model-1'].sketches['__edit__'].geometry[36], entity2=
    mdb.models['Model-1'].sketches['__edit__'].geometry[58])
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[58], ))
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'].features['Partition face-5'].sketch)
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-2'].features['Partition face-5'])
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[58], ))
mdb.models['Model-1'].sketches['__edit__'].offset(distance=0.000377, 
    objectList=(mdb.models['Model-1'].sketches['__edit__'].geometry[36], ), 
    side=RIGHT)
mdb.models['Model-1'].sketches['__edit__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__edit__'].geometry[114], point1=(
    0.0301184380054471, 0.0196373606276517))
mdb.models['Model-1'].sketches['__edit__'].removeGapsAndOverlaps(geomList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[115], ), tolerance=
    0.0001)
#* At least two sketch edges must be specified.
mdb.models['Model-1'].sketches['__edit__'].move(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[115], ), vector=(
    -0.000119217867788263, -1.92510976304034e-05))
mdb.models['Model-1'].sketches['__edit__'].autoTrimCurve(curve1=
    mdb.models['Model-1'].sketches['__edit__'].geometry[115], point1=(
    0.0282243216037747, 0.0190401891422276))
# Save by banerjee on Tue Oct 18 14:59:04 2011
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
del mdb.models['Model-1'].sketches['__edit__']
del mdb.models['Model-1'].parts['Part-2'].features['Partition face-5']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.03, name='__profile__', 
    sheetSize=1.2, transform=
    mdb.models['Model-1'].parts['Part-2'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-2'].faces[65], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-2'].edges[64], 
    sketchOrientation=RIGHT, origin=(0.31, 0.05613, 0.08)))
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].offset(distance=0.000377, 
    objectList=(mdb.models['Model-1'].sketches['__profile__'].geometry[36], 
    mdb.models['Model-1'].sketches['__profile__'].geometry[50]), side=RIGHT)
mdb.models['Model-1'].sketches['__profile__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[59], ))
mdb.models['Model-1'].sketches['__profile__'].move(objectList=(
    mdb.models['Model-1'].sketches['__profile__'].geometry[58], ), vector=(
    -0.000119217867788263, -1.92510976304034e-05))
mdb.models['Model-1'].parts['Part-2'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['Part-2'].faces.getSequenceFromMask((
    '[#0:2 #2 ]', ), ), sketch=mdb.models['Model-1'].sketches['__profile__'], 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-2'].edges[64])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-2'].regenerate()
mdb.models['Model-1'].ConstrainedSketch(name='__edit__', objectToCopy=
    mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'].sketch)
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__edit__'], 
    upToFeature=
    mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'])
mdb.models['Model-1'].sketches['__edit__'].offset(distance=0.004247, 
    objectList=(mdb.models['Model-1'].sketches['__edit__'].geometry[10], ), 
    side=LEFT)
mdb.models['Model-1'].sketches['__edit__'].offset(distance=0.004247, 
    objectList=(mdb.models['Model-1'].sketches['__edit__'].geometry[9], ), 
    side=LEFT)
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[14], ))
mdb.models['Model-1'].sketches['__edit__'].delete(objectList=(
    mdb.models['Model-1'].sketches['__edit__'].geometry[13], ))
mdb.models['Model-1'].parts['Part-2'].features['Solid extrude-1'].setValues(
    sketch=mdb.models['Model-1'].sketches['__edit__'])
del mdb.models['Model-1'].sketches['__edit__']
mdb.models['Model-1'].parts['Part-2'].regenerate()
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.01, name='__profile__', 
    sheetSize=0.5, transform=
    mdb.models['Model-1'].parts['Part-2'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-2'].faces[29], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-2'].edges[51], 
    sketchOrientation=RIGHT, origin=(0.42, 0.06113, 0.08)))
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].offset(distance=0.004247, 
    objectList=(mdb.models['Model-1'].sketches['__profile__'].geometry[58], ), 
    side=RIGHT)
mdb.models['Model-1'].parts['Part-2'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['Part-2'].faces.getSequenceFromMask((
    '[#20000000 #2000000 ]', ), ), sketch=
    mdb.models['Model-1'].sketches['__profile__'], sketchUpEdge=
    mdb.models['Model-1'].parts['Part-2'].edges[51])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].ConstrainedSketch(gridSpacing=0.02, name='__profile__', 
    sheetSize=1.02, transform=
    mdb.models['Model-1'].parts['Part-2'].MakeSketchTransform(
    sketchPlane=mdb.models['Model-1'].parts['Part-2'].faces[58], 
    sketchPlaneSide=SIDE1, 
    sketchUpEdge=mdb.models['Model-1'].parts['Part-2'].edges[3], 
    sketchOrientation=RIGHT, origin=(0.675, 0.06113, 0.08)))
mdb.models['Model-1'].parts['Part-2'].projectReferencesOntoSketch(filter=
    COPLANAR_EDGES, sketch=mdb.models['Model-1'].sketches['__profile__'])
mdb.models['Model-1'].sketches['__profile__'].offset(distance=0.004247, 
    objectList=(mdb.models['Model-1'].sketches['__profile__'].geometry[25], ), 
    side=RIGHT)
mdb.models['Model-1'].parts['Part-2'].PartitionFaceBySketch(faces=
    mdb.models['Model-1'].parts['Part-2'].faces.getSequenceFromMask((
    '[#0 #4000000 ]', ), ), sketch=
    mdb.models['Model-1'].sketches['__profile__'], sketchUpEdge=
    mdb.models['Model-1'].parts['Part-2'].edges[3])
del mdb.models['Model-1'].sketches['__profile__']
mdb.models['Model-1'].parts['Part-2'].PartitionCellBySweepEdge(cells=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#4000 ]', ), ), edges=(mdb.models['Model-1'].parts['Part-2'].edges[7], ), 
    sweepPath=mdb.models['Model-1'].parts['Part-2'].edges[89])
# Save by banerjee on Tue Oct 18 15:44:37 2011
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
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#10 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#1000 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#400 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#800 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#4 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#200 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , elemShape=HEX, regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#1 ]', 
    ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , elemShape=HEX, regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#8000 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#2000 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#100 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#2 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#4000 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].PartitionCellBySweepEdge(cells=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#100 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-2'].edges[16], ), sweepPath=
    mdb.models['Model-1'].parts['Part-2'].edges[68])
mdb.models['Model-1'].parts['Part-2'].PartitionCellBySweepEdge(cells=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#80 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-2'].edges[20], ), sweepPath=
    mdb.models['Model-1'].parts['Part-2'].edges[72])
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#402 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#3a1 ]', ), ), technique=SWEEP)
# Save by banerjee on Tue Oct 18 15:54:16 2011
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
mdb.models['Model-1'].parts['Part-2'].generateMesh()
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#22010 ]', ), ))
mdb.models['Model-1'].parts['Part-2'].seedEdgeByNumber(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40000000 #80 #0 #20000 ]', ), ), number=15)
mdb.models['Model-1'].parts['Part-2'].seedEdgeBySize(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40000000 #80 #0 #20000 ]', ), ), size=0.006)
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#800 ]', 
    ), ))
mdb.models['Model-1'].parts['Part-2'].seedEdgeBySize(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#44100000 #80 #0 #60800 ]', ), ), size=0.006)
mdb.models['Model-1'].parts['Part-2'].seedEdgeBySize(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#44100000 #80 #0 #60800 ]', ), ), size=0.005)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByBias(biasMethod=DOUBLE, 
    endEdges=mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#44100000 #80 #0 #60800 ]', ), ), maxSize=0.006, minSize=0.005)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByBias(biasMethod=SINGLE, 
    end1Edges=mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#44100000 #80 #0 #40800 ]', ), ), end2Edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0:3 #20000 ]', ), ), maxSize=0.006, minSize=0.005)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByBias(biasMethod=SINGLE, 
    end1Edges=mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#44100000 #80 #0 #40800 ]', ), ), end2Edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#0:3 #20000 ]', ), ), maxSize=0.006, minSize=0.004)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByNumber(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=15)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByNumber(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=14)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByNumber(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=18)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByNumber(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=20)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByNumber(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=22)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByNumber(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=24)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByNumber(edges=
    mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=27)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByBias(biasMethod=DOUBLE, 
    endEdges=mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=27, ratio=5.0)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByBias(biasMethod=DOUBLE, 
    endEdges=mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=24, ratio=5.0)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByBias(biasMethod=DOUBLE, 
    endEdges=mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=21, ratio=5.0)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByBias(biasMethod=DOUBLE, 
    endEdges=mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=19, ratio=5.0)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByBias(biasMethod=DOUBLE, 
    endEdges=mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=17, ratio=5.0)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByBias(biasMethod=DOUBLE, 
    endEdges=mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=17, ratio=3.0)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByBias(biasMethod=DOUBLE, 
    endEdges=mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=18, ratio=3.0)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByBias(biasMethod=DOUBLE, 
    endEdges=mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=18, ratio=2.0)
mdb.models['Model-1'].parts['Part-2'].seedEdgeByBias(biasMethod=DOUBLE, 
    endEdges=mdb.models['Model-1'].parts['Part-2'].edges.getSequenceFromMask((
    '[#40100000 ]', ), ), number=18, ratio=3.0)
mdb.models['Model-1'].parts['Part-2'].generateMesh()
mdb.models['Model-1'].parts['Part-2'].deleteMesh(regions=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#3fc5a ]', ), ))
mdb.models['Model-1'].parts['Part-2'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#4 ]', 
    ), ), edges=(mdb.models['Model-1'].parts['Part-2'].edges[19], ), line=
    mdb.models['Model-1'].parts['Part-2'].edges[95], sense=REVERSE)
mdb.models['Model-1'].parts['Part-2'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#1000 ]', ), ), edges=(mdb.models['Model-1'].parts['Part-2'].edges[0], ), 
    line=mdb.models['Model-1'].parts['Part-2'].edges[101], sense=REVERSE)
mdb.models['Model-1'].parts['Part-2'].PartitionCellByExtrudeEdge(cells=
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#8040 ]', ), ), edges=(mdb.models['Model-1'].parts['Part-2'].edges[13], )
    , line=mdb.models['Model-1'].parts['Part-2'].edges[111], sense=FORWARD)
# Save by banerjee on Tue Oct 18 16:12:24 2011
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
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#2814d ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].setMeshControls(algorithm=ADVANCING_FRONT
    , regions=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#2 ]', ), ), technique=SWEEP)
mdb.models['Model-1'].parts['Part-2'].generateMesh()
# Save by banerjee on Tue Oct 18 16:19:19 2011
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
mdb.models['Model-1'].parts['Part-2'].sectionAssignments[1].setValues(region=
    Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#a0c01 ]', ), )))
mdb.models['Model-1'].parts['Part-2'].sectionAssignments[2].setValues(region=
    Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#205000 ]', ), )))
mdb.models['Model-1'].parts['Part-2'].sectionAssignments[6].setValues(region=
    Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#200 ]', ), )))
mdb.models['Model-1'].parts['Part-2'].sectionAssignments[7].setValues(region=
    Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#70 ]', ), )))
mdb.models['Model-1'].parts['Part-2'].sectionAssignments[8].setValues(region=
    Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#8 ]', ), )))
# Save by banerjee on Tue Oct 18 16:46:35 2011
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
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'in keyword *DAMAGESTABILIZATION, file "OneTaper3D.inp", line 44524: The keyword is misplaced. It can be suboption for the following keyword(s)/level(s): damageevolution', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'OneTaper3D'})
mdb.models['Model-1'].parts['Part-2'].setElementType(elemTypes=(ElemType(
    elemCode=COH3D8, elemLibrary=STANDARD), ElemType(elemCode=COH3D6, 
    elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TET, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask((
    '[#40142 ]', ), ), ))
mdb.models['Model-1'].parts['Part-2'].setElementType(elemTypes=(ElemType(
    elemCode=COH3D8, elemLibrary=STANDARD), ElemType(elemCode=COH3D6, 
    elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TET, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#a0 ]', 
    ), ), ))
mdb.models['Model-1'].parts['Part-2'].setElementType(elemTypes=(ElemType(
    elemCode=COH3D8, elemLibrary=STANDARD), ElemType(elemCode=COH3D6, 
    elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TET, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(('[#210 ]', 
    ), ), ))
del mdb.models['Model-1'].materials['CohesiveMatFaceFace'].quadeDamageInitiation
mdb.models['Model-1'].materials['CohesiveMatFaceFace'].elastic.setValues(table=
    ((6900000000000.0, 6900000000000.0, 6900000000000.0), ), type=TRACTION)
mdb.models['Model-1'].materials['CohesiveMatFaceFace'].MaxsDamageInitiation(
    table=((60000000.0, 50000000.0, 50000000.0), ))
mdb.models['Model-1'].materials['CohesiveMatFaceFace'].maxsDamageInitiation.DamageEvolution(
    table=((0.001, ), ), type=DISPLACEMENT)
mdb.meshEditOptions.setValues(enableUndo=True, maxUndoCacheElements=0.5)
# Save by banerjee on Tue Oct 18 17:03:02 2011
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
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'in keyword *ELEMENTOUTPUT, file "OneTaper3D.inp", line 44573: Unknown assembly set _PICKEDSET27', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'ERROR INDICATOR OUTPUT HAS BEEN SPECIFIED ON ELSET ASSEMBLY__PICKEDSET27 BUT THIS ELSET HAS NOT BEEN DEFINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'OneTaper3D'})
del mdb.models['Model-1'].remeshingRules['RemeshingRule-1']
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': '12 elements have missing property definitions. The elements have been identified in element set ErrElemMissingSection.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '12 elements have incorrect property definitions. The elements have been identified in element set WarnElemIncorrectProperty.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'SECTION DEFINITIONS ARE MISSING OR INCORRECT FOR THE ELEMENTS INDICATED ABOVE. FURTHER PROCESSING OF THE INPUT FILE IS NOT POSSIBLE UNTIL THIS INPUT ERROR IS FIXED.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'OneTaper3D'})
mdb.models['Model-1'].rootAssembly.unlock()
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].rootAssembly.makeIndependent(instances=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'], ))
mdb.models['Model-1'].rootAssembly.setElementType(elemTypes=(ElemType(
    elemCode=COH3D8, elemLibrary=STANDARD), ElemType(elemCode=COH3D6, 
    elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TET, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].cells.getSequenceFromMask(
    ('[#8 ]', ), ), ))
mdb.models['Model-1'].parts['Part-2'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#8 ]', ), )), sectionName='CohesiveSectionFaceFace', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '24 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'Solver problem. Numerical singularity at D.O.F. 2 at one or more of the internal nodes of 10 elements. The elements have been identified in element set WarnElemSolvProbNumSing_2_0_0_0_0.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'The executable /home/Abaqus/6.10-1/exec/standard.exe aborted with system error "Illegal floating point operation" (signal 8). Please check the .dat, .msg, and .sta files for error messages if the files exist.  If there are no error messages and you cannot resolve the problem, please run the command "abaqus job=support information=support" to report and save your system information.  Use the same command to run Abaqus that you used when the problem occurred.  Please contact your local Abaqus support office and send them the input file, the file support.log which you just created, the executable name, and the error code.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'The executable /home/Abaqus/6.10-1/exec/standard.exe aborted with system error "Illegal floating point operation" (signal 8). Please check the .dat, .msg, and .sta files for error messages if the files exist.  If there are no error messages and you cannot resolve the problem, please run the command "abaqus job=support information=support" to report and save your system information.  Use the same command to run Abaqus that you used when the problem occurred.  Please contact your local Abaqus support office and send them the input file, the file support.log which you just created, the executable name, and the error code.', 
    'jobName': 'OneTaper3D'})
# Save by banerjee on Tue Oct 18 17:16:37 2011
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
mdb.models['Model-1'].parts['Part-2'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#8 ]', ), )), sectionName='inner skin', thicknessAssignment=
    FROM_SECTION)
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'ELEMENT 145 INSTANCE PART-2-1 IS MISSING A PROPERTY DEFINITION; CHECK ELEMENT SET AND ELEMENT DEFINITIONS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'OneTaper3D'})
mdb.models['Model-1'].rootAssembly.featurelistInfo()
mdb.models['Model-1'].rootAssembly.featurelistInfo()
mdb.models['Model-1'].rootAssembly.generateMesh(regions=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'], ))
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'ELEMENT 145 INSTANCE PART-2-1 IS MISSING A PROPERTY DEFINITION; CHECK ELEMENT SET AND ELEMENT DEFINITIONS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'OneTaper3D'})
# Save by banerjee on Tue Oct 18 17:29:28 2011
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
mdb.models['Model-1'].rootAssembly.setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].cells.getSequenceFromMask(
    ('[#8 ]', ), ), ))
mdb.models['Model-1'].rootAssembly.setElementType(elemTypes=(ElemType(
    elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].cells.getSequenceFromMask(
    ('[#8000 ]', ), ), ))
mdb.models['Model-1'].rootAssembly.setElementType(elemTypes=(ElemType(
    elemCode=COH3D8, elemLibrary=STANDARD), ElemType(elemCode=COH3D6, 
    elemLibrary=STANDARD), ElemType(elemCode=UNKNOWN_TET, 
    elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].cells.getSequenceFromMask(
    ('[#40 ]', ), ), ))
mdb.models['Model-1'].rootAssembly.setElementType(elemTypes=(ElemType(
    elemCode=C3D8R, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    kinematicSplit=AVERAGE_STRAIN, hourglassControl=DEFAULT, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].cells.getSequenceFromMask(
    ('[#8 ]', ), ), ))
mdb.models['Model-1'].rootAssembly.setElementType(elemTypes=(ElemType(
    elemCode=C3D8, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    distortionControl=DEFAULT), ElemType(elemCode=C3D6, elemLibrary=STANDARD), 
    ElemType(elemCode=C3D4, elemLibrary=STANDARD)), regions=(
    mdb.models['Model-1'].rootAssembly.instances['Part-2-1'].cells.getSequenceFromMask(
    ('[#8 ]', ), ), ))
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'The user defined normal of the material orientation of 1056 elements, as defined in *ORIENTATION, is orthogonal to the GASKET, COHESIVE, SHELL or MEMBRANE normal direction. Check input data. The elements have been identified in element set ErrElemUserNormMatOrient.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 347.88281917572})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.models['Model-1'].parts['Part-2'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#40 ]', ), )), sectionName='CohesiveSectionFaceFace', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'The user defined normal of the material orientation of 1056 elements, as defined in *ORIENTATION, is orthogonal to the GASKET, COHESIVE, SHELL or MEMBRANE normal direction. Check input data. The elements have been identified in element set ErrElemUserNormMatOrient.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 347.890956878662})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.models['Model-1'].parts['Part-2'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#20 ]', ), )), sectionName='CohesiveSectionFaceFace', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].parts['Part-2'].SectionAssignment(offset=0.0, 
    offsetField='', offsetType=MIDDLE_SURFACE, region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#10 ]', ), )), sectionName='CohesiveSectionFaceFace', 
    thicknessAssignment=FROM_SECTION)
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'The user defined normal of the material orientation of 1056 elements, as defined in *ORIENTATION, is orthogonal to the GASKET, COHESIVE, SHELL or MEMBRANE normal direction. Check input data. The elements have been identified in element set ErrElemUserNormMatOrient.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 347.890956878662})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.models['Model-1'].parts['Part-2'].MaterialOrientation(
    additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
    , axis=AXIS_1, fieldName='', localCsys=None, orientationType=SYSTEM, 
    region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#10 ]', ), )), stackDirection=STACK_3)
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'The user defined normal of the material orientation of 1056 elements, as defined in *ORIENTATION, is orthogonal to the GASKET, COHESIVE, SHELL or MEMBRANE normal direction. Check input data. The elements have been identified in element set ErrElemUserNormMatOrient.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 347.890956878662})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'The user defined normal of the material orientation of 1056 elements, as defined in *ORIENTATION, is orthogonal to the GASKET, COHESIVE, SHELL or MEMBRANE normal direction. Check input data. The elements have been identified in element set ErrElemUserNormMatOrient.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 347.890956878662})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.models['Model-1'].sections['CohesiveSectionFaceFace'].setValues(
    initialThicknessType=GEOMETRY, material='CohesiveMatFaceFace', 
    outOfPlaneThickness=1.0, response=TRACTION_SEPARATION)
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'The user defined normal of the material orientation of 1056 elements, as defined in *ORIENTATION, is orthogonal to the GASKET, COHESIVE, SHELL or MEMBRANE normal direction. Check input data. The elements have been identified in element set ErrElemUserNormMatOrient.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'THE ANALYSIS HAS TERMINATED DUE TO PREVIOUS ERRORS.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.models['Model-1'].parts['Part-2'].materialOrientations[0].setValues(
    orientationType=SYSTEM, stackDirection=STACK_ORIENTATION)
mdb.models['Model-1'].parts['Part-2'].materialOrientations[1].setValues(axis=
    AXIS_3, orientationType=SYSTEM, stackDirection=STACK_ORIENTATION)
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'The user defined normal of the material orientation of 1056 elements, as defined in *ORIENTATION, is orthogonal to the GASKET, COHESIVE, SHELL or MEMBRANE normal direction. Check input data. The elements have been identified in element set ErrElemUserNormMatOrient.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 347.890956878662})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.models['Model-1'].parts['Part-2'].materialOrientations[0].suppress()
mdb.models['Model-1'].parts['Part-2'].materialOrientations[1].suppress()
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': BATCHPRE_PHASE, 
    'message': 'Anisotropic material properties without a local orientation system have been defined for 7476 elements. Anisotripic material properties must be defined in a local orientation system. The elements are identified in element set ErrElemAnisotropicMaterial.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Analysis Input File Processor exited with an error.', 
    'jobName': 'OneTaper3D'})
mdb.models['Model-1'].parts['Part-2'].materialOrientations[0].resume()
mdb.models['Model-1'].parts['Part-2'].materialOrientations[0].setValues(
    additionalRotationType=ROTATION_NONE, fieldName='', localCsys=None, 
    orientationType=GLOBAL)
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'The user defined normal of the material orientation of 1056 elements, as defined in *ORIENTATION, is orthogonal to the GASKET, COHESIVE, SHELL or MEMBRANE normal direction. Check input data. The elements have been identified in element set ErrElemUserNormMatOrient.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 347.890956878662})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.models['Model-1'].parts['Part-2'].DatumCsysByThreePoints(coordSysType=
    CARTESIAN, name='Datum csys-2', origin=
    mdb.models['Model-1'].parts['Part-2'].InterestingPoint(
    mdb.models['Model-1'].parts['Part-2'].edges[36], MIDDLE), point1=
    mdb.models['Model-1'].parts['Part-2'].vertices[23], point2=
    mdb.models['Model-1'].parts['Part-2'].InterestingPoint(
    mdb.models['Model-1'].parts['Part-2'].edges[58], MIDDLE))
mdb.models['Model-1'].parts['Part-2'].DatumCsysByThreePoints(coordSysType=
    CARTESIAN, name='Datum csys-3', origin=
    mdb.models['Model-1'].parts['Part-2'].InterestingPoint(
    mdb.models['Model-1'].parts['Part-2'].edges[52], MIDDLE), point1=
    mdb.models['Model-1'].parts['Part-2'].vertices[27], point2=
    mdb.models['Model-1'].parts['Part-2'].InterestingPoint(
    mdb.models['Model-1'].parts['Part-2'].edges[50], MIDDLE))
mdb.models['Model-1'].parts['Part-2'].MaterialOrientation(
    additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
    , axis=AXIS_1, fieldName='', localCsys=
    mdb.models['Model-1'].parts['Part-2'].datums[143], orientationType=SYSTEM, 
    region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#40 ]', ), )), stackDirection=STACK_3)
mdb.models['Model-1'].parts['Part-2'].MaterialOrientation(
    additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
    , axis=AXIS_3, fieldName='', localCsys=
    mdb.models['Model-1'].parts['Part-2'].datums[144], orientationType=SYSTEM, 
    region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#20 ]', ), )), stackDirection=STACK_3)
mdb.models['Model-1'].parts['Part-2'].MaterialOrientation(
    additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
    , axis=AXIS_3, fieldName='', localCsys=
    mdb.models['Model-1'].parts['Part-2'].datums[144], orientationType=SYSTEM, 
    region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#10 ]', ), )), stackDirection=STACK_3)
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'The user defined normal of the material orientation of 228 elements, as defined in *ORIENTATION, is orthogonal to the GASKET, COHESIVE, SHELL or MEMBRANE normal direction. Check input data. The elements have been identified in element set ErrElemUserNormMatOrient.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 347.895302772522})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.models['Model-1'].parts['Part-2'].materialOrientations[1].resume()
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'The user defined normal of the material orientation of 228 elements, as defined in *ORIENTATION, is orthogonal to the GASKET, COHESIVE, SHELL or MEMBRANE normal direction. Check input data. The elements have been identified in element set ErrElemUserNormMatOrient.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 347.895302772522})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
# Save by banerjee on Tue Oct 18 18:14:01 2011
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
mdb.models['Model-1'].parts['Part-2'].DatumCsysByThreePoints(coordSysType=
    CARTESIAN, name='Datum csys-4', origin=
    mdb.models['Model-1'].parts['Part-2'].vertices[3], point1=
    mdb.models['Model-1'].parts['Part-2'].vertices[17], point2=
    mdb.models['Model-1'].parts['Part-2'].vertices[2])
mdb.models['Model-1'].parts['Part-2'].MaterialOrientation(
    additionalRotationField='', additionalRotationType=ROTATION_NONE, angle=0.0
    , axis=AXIS_1, fieldName='', localCsys=None, orientationType=SYSTEM, 
    region=Region(
    cells=mdb.models['Model-1'].parts['Part-2'].cells.getSequenceFromMask(
    mask=('[#40 ]', ), )), stackDirection=STACK_1)
mdb.models['Model-1'].parts['Part-2'].materialOrientations[2].suppress()
# Save by banerjee on Wed Oct 19 10:33:09 2011
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
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF, datacheckJob=True)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The 3-direction at one or more points in one or more layers in 228 elements as defined in *ORIENTATION are in the opposite direction to the element normals. Either the 1 or 2 and the 3-direction defined in *ORIENTATION will be reversed. The elements have been identified in element set WarnElem3DirOppElemNormalStep1Inc1.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 347.897059440613})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_COMPLETED, {
    'time': 'Wed Oct 19 10:33:42 2011', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The 3-direction at one or more points in one or more layers in 228 elements as defined in *ORIENTATION are in the opposite direction to the element normals. Either the 1 or 2 and the 3-direction defined in *ORIENTATION will be reversed. The elements have been identified in element set WarnElem3DirOppElemNormalStep1Inc1.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1.0, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 422.442700386047})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 1, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1, 
    'timeIncrement': 1.0, 'increment': 1, 'stepTime': 1.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 2, 
    'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(END_STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_COMPLETED, {
    'time': 'Wed Oct 19 10:34:32 2011', 'jobName': 'OneTaper3D'})
mdb.models['Model-1'].steps['Step-1'].setValues(adaptiveDampingRatio=0.05, 
    continueDampingFactors=False, initialInc=1e-06, maxInc=0.01, maxNumInc=1000
    , minInc=1e-07, nlgeom=ON, stabilizationMagnitude=0.0002, 
    stabilizationMethod=DISSIPATED_ENERGY_FRACTION)
mdb.models['Model-1'].boundaryConditions['BC-2'].setValues(u2=-0.02)
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The 3-direction at one or more points in one or more layers in 228 elements as defined in *ORIENTATION are in the opposite direction to the element normals. Either the 1 or 2 and the 3-direction defined in *ORIENTATION will be reversed. The elements have been identified in element set WarnElem3DirOppElemNormalStep1Inc1.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1e-06, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 423.494834899902})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 1U', 
    'timeIncrement': 1e-06, 'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 9, 
    'phase': STANDARD_PHASE, 'equilibrium': 9})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 2U', 
    'timeIncrement': 5e-07, 'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 9, 
    'phase': STANDARD_PHASE, 'equilibrium': 9})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 3U', 
    'timeIncrement': 1.25e-07, 'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 7, 
    'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'There is zero FORCE everywhere in the model based on the default criterion. please check the value of the average FORCE during the current iteration to verify that the FORCE is small enough to be treated as zero. if not, please use the solution controls to reset the criterion for zero FORCE.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'Time increment required is less than the minimum specified', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 4U', 
    'timeIncrement': 1e-07, 'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 9, 
    'phase': STANDARD_PHASE, 'equilibrium': 9})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.models['Model-1'].steps['Step-1'].setValues(minInc=1e-09)
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The 3-direction at one or more points in one or more layers in 228 elements as defined in *ORIENTATION are in the opposite direction to the element normals. Either the 1 or 2 and the 3-direction defined in *ORIENTATION will be reversed. The elements have been identified in element set WarnElem3DirOppElemNormalStep1Inc1.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 1e-06, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 423.494834899902})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 1U', 
    'timeIncrement': 1e-06, 'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 9, 
    'phase': STANDARD_PHASE, 'equilibrium': 9})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 2U', 
    'timeIncrement': 2.5e-07, 'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 5, 
    'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'There is zero FORCE everywhere in the model based on the default criterion. please check the value of the average FORCE during the current iteration to verify that the FORCE is small enough to be treated as zero. if not, please use the solution controls to reset the criterion for zero FORCE.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': ' 3U', 
    'timeIncrement': 6.25e-08, 'increment': 1, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 9, 
    'phase': STANDARD_PHASE, 'equilibrium': 9})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'There is zero FORCE everywhere in the model based on the default criterion. please check the value of the average FORCE during the current iteration to verify that the FORCE is small enough to be treated as zero. if not, please use the solution controls to reset the criterion for zero FORCE.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 1, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 3.125e-08, 'attempts': 4, 
    'timeIncrement': 3.125e-08, 'increment': 1, 'stepTime': 3.125e-08, 
    'step': 1, 'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 4, 
    'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 3.125e-08, 
    'attempts': ' 1U', 'timeIncrement': 3.125e-08, 'increment': 2, 
    'stepTime': 3.125e-08, 'step': 1, 'jobName': 'OneTaper3D', 'severe': 0, 
    'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 3.125e-08, 
    'attempts': ' 2U', 'timeIncrement': 7.8125e-09, 'increment': 2, 
    'stepTime': 3.125e-08, 'step': 1, 'jobName': 'OneTaper3D', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 2, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 3.3203125e-08, 
    'attempts': 3, 'timeIncrement': 1.953125e-09, 'increment': 2, 
    'stepTime': 3.3203125e-08, 'step': 1, 'jobName': 'OneTaper3D', 'severe': 0, 
    'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 3.3203125e-08, 
    'attempts': ' 1U', 'timeIncrement': 2.9296875e-09, 'increment': 3, 
    'stepTime': 3.3203125e-08, 'step': 1, 'jobName': 'OneTaper3D', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ERROR, {'phase': STANDARD_PHASE, 
    'message': 'Time increment required is less than the minimum specified', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 3.3203125e-08, 
    'attempts': ' 2U', 'timeIncrement': 1e-09, 'increment': 3, 
    'stepTime': 3.3203125e-08, 'step': 1, 'jobName': 'OneTaper3D', 'severe': 0, 
    'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ABORTED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase failed due to errors', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ERROR, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_ABORTED, {
    'message': 'Abaqus/Standard Analysis exited with an error - Please see the  message file for possible error messages if the file exists.', 
    'jobName': 'OneTaper3D'})
del mdb.models['Model-1'].parts['Part-2'].sets['PoorElements-1']
del mdb.models['Model-1'].parts['Part-2'].materialOrientations[2]
mdb.models['Model-1'].rootAssembly.regenerate()
mdb.models['Model-1'].steps['Step-1'].setValues(continueDampingFactors=False, 
    initialInc=0.001, stabilizationMagnitude=0.002, stabilizationMethod=
    DISSIPATED_ENERGY_FRACTION)
mdb.jobs['OneTaper3D'].submit(consistencyChecking=OFF)
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': BATCHPRE_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 4 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': 'DEGREE OF FREEDOM 5 IS NOT ACTIVE IN THIS MODEL AND CAN NOT BE RESTRAINED', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': BATCHPRE_PHASE, 
    'message': '36 elements are distorted. Either the isoparametric angles are out of the suggested limits or the triangular or tetrahedral quality measure is bad. The elements have been identified in element set WarnElemDistorted.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FILE, {'phase': BATCHPRE_PHASE, 
    'file': '/home2/banerjee/Abaqus/AdvComp/OneTaper3DCZM/OneTaper3D.odb', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': BATCHPRE_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STARTED, {'phase': STANDARD_PHASE, 
    'clientHost': 'kirchhoff', 'handle': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STEP, {'phase': STANDARD_PHASE, 'stepId': 1, 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'The 3-direction at one or more points in one or more layers in 228 elements as defined in *ORIENTATION are in the opposite direction to the element normals. Either the 1 or 2 and the 3-direction defined in *ORIENTATION will be reversed. The elements have been identified in element set WarnElem3DirOppElemNormalStep1Inc1.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 0, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0, 'attempts': 0, 
    'timeIncrement': 0.001, 'increment': 0, 'stepTime': 0.0, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 0, 
    'phase': STANDARD_PHASE, 'equilibrium': 0})
mdb.jobs['OneTaper3D']._Message(MEMORY_ESTIMATE, {'phase': STANDARD_PHASE, 
    'jobName': 'OneTaper3D', 'memory': 423.493077278137})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 1, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.001, 'attempts': 1, 
    'timeIncrement': 0.001, 'increment': 1, 'stepTime': 0.001, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 6, 
    'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 2, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.002, 'attempts': 1, 
    'timeIncrement': 0.001, 'increment': 2, 'stepTime': 0.002, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 5, 
    'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 3, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.003, 'attempts': 1, 
    'timeIncrement': 0.001, 'increment': 3, 'stepTime': 0.003, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 5, 
    'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 4, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.004, 'attempts': 1, 
    'timeIncrement': 0.001, 'increment': 4, 'stepTime': 0.004, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 4, 
    'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 5, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.005, 'attempts': 1, 
    'timeIncrement': 0.001, 'increment': 5, 'stepTime': 0.005, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 6, 
    'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 408 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.005, 'attempts': ' 1U', 
    'timeIncrement': 0.001, 'increment': 6, 'stepTime': 0.005, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 4, 
    'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.005, 'attempts': ' 2U', 
    'timeIncrement': 0.00025, 'increment': 6, 'stepTime': 0.005, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 4, 
    'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 6, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0050625, 'attempts': 3, 
    'timeIncrement': 6.25e-05, 'increment': 6, 'stepTime': 0.0050625, 
    'step': 1, 'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 8, 
    'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 7, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.005125, 'attempts': 1, 
    'timeIncrement': 6.25e-05, 'increment': 7, 'stepTime': 0.005125, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 5, 
    'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 8, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0051875, 'attempts': 1, 
    'timeIncrement': 6.25e-05, 'increment': 8, 'stepTime': 0.0051875, 
    'step': 1, 'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 4, 
    'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 9, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.00525, 'attempts': 1, 
    'timeIncrement': 6.25e-05, 'increment': 9, 'stepTime': 0.00525, 'step': 1, 
    'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 3, 
    'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 10, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.00534375, 
    'attempts': 1, 'timeIncrement': 9.375e-05, 'increment': 10, 
    'stepTime': 0.00534375, 'step': 1, 'jobName': 'OneTaper3D', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 11, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.005484375, 
    'attempts': 1, 'timeIncrement': 0.000140625, 'increment': 11, 
    'stepTime': 0.005484375, 'step': 1, 'jobName': 'OneTaper3D', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 12, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0056953125, 
    'attempts': 1, 'timeIncrement': 0.0002109375, 'increment': 12, 
    'stepTime': 0.0056953125, 'step': 1, 'jobName': 'OneTaper3D', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 13, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.00601171875, 
    'attempts': 1, 'timeIncrement': 0.00031640625, 'increment': 13, 
    'stepTime': 0.00601171875, 'step': 1, 'jobName': 'OneTaper3D', 'severe': 0, 
    'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 14, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.006486328125, 
    'attempts': 1, 'timeIncrement': 0.000474609375, 'increment': 14, 
    'stepTime': 0.006486328125, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 15, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0071982421875, 
    'attempts': 1, 'timeIncrement': 0.0007119140625, 'increment': 15, 
    'stepTime': 0.0071982421875, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 16, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.00826611328125, 
    'attempts': 1, 'timeIncrement': 0.00106787109375, 'increment': 16, 
    'stepTime': 0.00826611328125, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 17, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.009867919921875, 
    'attempts': 1, 'timeIncrement': 0.001601806640625, 'increment': 17, 
    'stepTime': 0.009867919921875, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 18, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0122706298828125, 
    'attempts': 1, 'timeIncrement': 0.0024027099609375, 'increment': 18, 
    'stepTime': 0.0122706298828125, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 26 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0122706298828125, 
    'attempts': ' 1U', 'timeIncrement': 0.00360406494140625, 'increment': 19, 
    'stepTime': 0.0122706298828125, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 19, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0131716461181641, 
    'attempts': 2, 'timeIncrement': 0.000901016235351563, 'increment': 19, 
    'stepTime': 0.0131716461181641, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 20, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0145231704711914, 
    'attempts': 1, 'timeIncrement': 0.00135152435302734, 'increment': 20, 
    'stepTime': 0.0145231704711914, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 21, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0165504570007324, 
    'attempts': 1, 'timeIncrement': 0.00202728652954102, 'increment': 21, 
    'stepTime': 0.0165504570007324, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 22, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0195913867950439, 
    'attempts': 1, 'timeIncrement': 0.00304092979431152, 'increment': 22, 
    'stepTime': 0.0195913867950439, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 23, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0241527814865112, 
    'attempts': 1, 'timeIncrement': 0.00456139469146729, 'increment': 23, 
    'stepTime': 0.0241527814865112, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 24, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0309948735237122, 
    'attempts': 1, 'timeIncrement': 0.00684209203720093, 'increment': 24, 
    'stepTime': 0.0309948735237122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 4 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0309948735237122, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 25, 
    'stepTime': 0.0309948735237122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 25, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0334948735237122, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 25, 
    'stepTime': 0.0334948735237122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 26, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0372448735237122, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 26, 
    'stepTime': 0.0372448735237122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 27, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0428698735237122, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 27, 
    'stepTime': 0.0428698735237122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 4 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0428698735237122, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 28, 
    'stepTime': 0.0428698735237122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 28, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0449792485237122, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 28, 
    'stepTime': 0.0449792485237122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 29, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0481433110237122, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 29, 
    'stepTime': 0.0481433110237122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 30, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0528894047737122, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 30, 
    'stepTime': 0.0528894047737122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 31, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0600085453987122, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 31, 
    'stepTime': 0.0600085453987122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 702 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0600085453987122, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 32, 
    'stepTime': 0.0600085453987122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 32, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0625085453987122, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 32, 
    'stepTime': 0.0625085453987122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 33, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0662585453987122, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 33, 
    'stepTime': 0.0662585453987122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 34, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0718835453987122, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 34, 
    'stepTime': 0.0718835453987122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 5464 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0718835453987122, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 35, 
    'stepTime': 0.0718835453987122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 35, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0739929203987122, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 35, 
    'stepTime': 0.0739929203987122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 36, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0771569828987122, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 36, 
    'stepTime': 0.0771569828987122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 37, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0819030766487122, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 37, 
    'stepTime': 0.0819030766487122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 38, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0890222172737122, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 38, 
    'stepTime': 0.0890222172737122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 835 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0890222172737122, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 39, 
    'stepTime': 0.0890222172737122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 39, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0915222172737122, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 39, 
    'stepTime': 0.0915222172737122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 40, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.0952722172737122, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 40, 
    'stepTime': 0.0952722172737122, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 41, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.100897217273712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 41, 
    'stepTime': 0.100897217273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 6 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.100897217273712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 42, 
    'stepTime': 0.100897217273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 42, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.103006592273712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 42, 
    'stepTime': 0.103006592273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 43, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.106170654773712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 43, 
    'stepTime': 0.106170654773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 44, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.110916748523712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 44, 
    'stepTime': 0.110916748523712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 45, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.118035889148712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 45, 
    'stepTime': 0.118035889148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 320 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.118035889148712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 46, 
    'stepTime': 0.118035889148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 46, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.120535889148712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 46, 
    'stepTime': 0.120535889148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 47, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.124285889148712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 47, 
    'stepTime': 0.124285889148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 48, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.129910889148712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 48, 
    'stepTime': 0.129910889148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 5509 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.129910889148712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 49, 
    'stepTime': 0.129910889148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 49, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.132020264148712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 49, 
    'stepTime': 0.132020264148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 50, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.135184326648712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 50, 
    'stepTime': 0.135184326648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 51, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.139930420398712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 51, 
    'stepTime': 0.139930420398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 52, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.147049561023712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 52, 
    'stepTime': 0.147049561023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 441 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.147049561023712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 53, 
    'stepTime': 0.147049561023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 53, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.149549561023712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 53, 
    'stepTime': 0.149549561023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 54, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.153299561023712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 54, 
    'stepTime': 0.153299561023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 55, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.158924561023712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 55, 
    'stepTime': 0.158924561023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 3745 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.158924561023712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 56, 
    'stepTime': 0.158924561023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 56, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.161033936023712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 56, 
    'stepTime': 0.161033936023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 57, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.164197998523712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 57, 
    'stepTime': 0.164197998523712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 58, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.168944092273712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 58, 
    'stepTime': 0.168944092273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 59, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.176063232898712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 59, 
    'stepTime': 0.176063232898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 2426 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.176063232898712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 60, 
    'stepTime': 0.176063232898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 60, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.178563232898712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 60, 
    'stepTime': 0.178563232898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 61, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.182313232898712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 61, 
    'stepTime': 0.182313232898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 62, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.187938232898712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 62, 
    'stepTime': 0.187938232898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 660 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.187938232898712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 63, 
    'stepTime': 0.187938232898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 63, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.190047607898712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 63, 
    'stepTime': 0.190047607898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 64, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.193211670398712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 64, 
    'stepTime': 0.193211670398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 65, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.197957764148712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 65, 
    'stepTime': 0.197957764148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 66, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.205076904773712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 66, 
    'stepTime': 0.205076904773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 2145 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.205076904773712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 67, 
    'stepTime': 0.205076904773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 67, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.207576904773712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 67, 
    'stepTime': 0.207576904773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 68, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.211326904773712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 68, 
    'stepTime': 0.211326904773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 69, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.216951904773712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 69, 
    'stepTime': 0.216951904773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 1090 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.216951904773712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 70, 
    'stepTime': 0.216951904773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 70, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.219061279773712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 70, 
    'stepTime': 0.219061279773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 71, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.222225342273712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 71, 
    'stepTime': 0.222225342273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 72, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.226971436023712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 72, 
    'stepTime': 0.226971436023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 73, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.234090576648712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 73, 
    'stepTime': 0.234090576648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 94 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.234090576648712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 74, 
    'stepTime': 0.234090576648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 74, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.236590576648712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 74, 
    'stepTime': 0.236590576648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 75, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.240340576648712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 75, 
    'stepTime': 0.240340576648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 76, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.245965576648712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 76, 
    'stepTime': 0.245965576648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 4840 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.245965576648712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 77, 
    'stepTime': 0.245965576648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 77, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.248074951648712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 77, 
    'stepTime': 0.248074951648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 78, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.251239014148712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 78, 
    'stepTime': 0.251239014148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 79, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.255985107898712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 79, 
    'stepTime': 0.255985107898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 80, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.263104248523712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 80, 
    'stepTime': 0.263104248523712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 1704 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.263104248523712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 81, 
    'stepTime': 0.263104248523712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 81, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.265604248523712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 81, 
    'stepTime': 0.265604248523712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 82, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.269354248523712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 82, 
    'stepTime': 0.269354248523712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 83, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.274979248523712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 83, 
    'stepTime': 0.274979248523712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 2993 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.274979248523712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 84, 
    'stepTime': 0.274979248523712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 84, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.277088623523712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 84, 
    'stepTime': 0.277088623523712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 85, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.280252686023712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 85, 
    'stepTime': 0.280252686023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 86, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.284998779773712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 86, 
    'stepTime': 0.284998779773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 87, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.292117920398712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 87, 
    'stepTime': 0.292117920398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 1750 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.292117920398712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 88, 
    'stepTime': 0.292117920398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 88, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.294617920398712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 88, 
    'stepTime': 0.294617920398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 89, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.298367920398712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 89, 
    'stepTime': 0.298367920398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 90, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.303992920398712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 90, 
    'stepTime': 0.303992920398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 4152 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.303992920398712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 91, 
    'stepTime': 0.303992920398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 91, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.306102295398712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 91, 
    'stepTime': 0.306102295398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 92, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.309266357898712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 92, 
    'stepTime': 0.309266357898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 93, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.314012451648712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 93, 
    'stepTime': 0.314012451648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 94, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.321131592273712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 94, 
    'stepTime': 0.321131592273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 4003 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.321131592273712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 95, 
    'stepTime': 0.321131592273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 95, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.323631592273712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 95, 
    'stepTime': 0.323631592273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 96, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.327381592273712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 96, 
    'stepTime': 0.327381592273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 97, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.333006592273712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 97, 
    'stepTime': 0.333006592273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 5917 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.333006592273712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 98, 
    'stepTime': 0.333006592273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 98, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.335115967273712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 98, 
    'stepTime': 0.335115967273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 99, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.338280029773712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 99, 
    'stepTime': 0.338280029773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 100, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.343026123523712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 100, 
    'stepTime': 0.343026123523712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 101, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.350145264148712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 101, 
    'stepTime': 0.350145264148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 5209 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.350145264148712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 102, 
    'stepTime': 0.350145264148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 102, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.352645264148712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 102, 
    'stepTime': 0.352645264148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 103, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.356395264148712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 103, 
    'stepTime': 0.356395264148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 104, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.362020264148712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 104, 
    'stepTime': 0.362020264148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 693 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.362020264148712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 105, 
    'stepTime': 0.362020264148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 105, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.364129639148712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 105, 
    'stepTime': 0.364129639148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 106, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.367293701648712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 106, 
    'stepTime': 0.367293701648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 107, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.372039795398712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 107, 
    'stepTime': 0.372039795398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 108, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.379158936023712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 108, 
    'stepTime': 0.379158936023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 4616 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.379158936023712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 109, 
    'stepTime': 0.379158936023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 109, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.381658936023712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 109, 
    'stepTime': 0.381658936023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 110, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.385408936023712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 110, 
    'stepTime': 0.385408936023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 111, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.391033936023712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 111, 
    'stepTime': 0.391033936023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 3991 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.391033936023712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 112, 
    'stepTime': 0.391033936023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 112, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.393143311023712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 112, 
    'stepTime': 0.393143311023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 113, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.396307373523712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 113, 
    'stepTime': 0.396307373523712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 114, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.401053467273712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 114, 
    'stepTime': 0.401053467273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 115, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.408172607898712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 115, 
    'stepTime': 0.408172607898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 2508 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.408172607898712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 116, 
    'stepTime': 0.408172607898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 116, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.410672607898712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 116, 
    'stepTime': 0.410672607898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 117, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.414422607898712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 117, 
    'stepTime': 0.414422607898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 118, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.420047607898712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 118, 
    'stepTime': 0.420047607898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 2331 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.420047607898712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 119, 
    'stepTime': 0.420047607898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 119, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.422156982898712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 119, 
    'stepTime': 0.422156982898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 120, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.425321045398712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 120, 
    'stepTime': 0.425321045398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 121, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.430067139148712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 121, 
    'stepTime': 0.430067139148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 122, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.437186279773712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 122, 
    'stepTime': 0.437186279773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 903 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.437186279773712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 123, 
    'stepTime': 0.437186279773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 123, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.439686279773712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 123, 
    'stepTime': 0.439686279773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 124, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.443436279773712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 124, 
    'stepTime': 0.443436279773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 125, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.449061279773712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 125, 
    'stepTime': 0.449061279773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 2877 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.449061279773712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 126, 
    'stepTime': 0.449061279773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 126, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.451170654773712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 126, 
    'stepTime': 0.451170654773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 127, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.454334717273712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 127, 
    'stepTime': 0.454334717273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 128, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.459080811023712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 128, 
    'stepTime': 0.459080811023712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 129, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.466199951648712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 129, 
    'stepTime': 0.466199951648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 2359 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.466199951648712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 130, 
    'stepTime': 0.466199951648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 130, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.468699951648712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 130, 
    'stepTime': 0.468699951648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 131, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.472449951648712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 131, 
    'stepTime': 0.472449951648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 132, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.478074951648712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 132, 
    'stepTime': 0.478074951648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 6 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.478074951648712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 133, 
    'stepTime': 0.478074951648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 133, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.480184326648712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 133, 
    'stepTime': 0.480184326648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 134, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.483348389148712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 134, 
    'stepTime': 0.483348389148712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 135, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.488094482898712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 135, 
    'stepTime': 0.488094482898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 136, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.495213623523713, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 136, 
    'stepTime': 0.495213623523713, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 1984 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.495213623523713, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 137, 
    'stepTime': 0.495213623523713, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 137, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.497713623523713, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 137, 
    'stepTime': 0.497713623523713, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 138, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.501463623523713, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 138, 
    'stepTime': 0.501463623523713, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 139, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.507088623523713, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 139, 
    'stepTime': 0.507088623523713, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 1415 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.507088623523713, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 140, 
    'stepTime': 0.507088623523713, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 140, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.509197998523713, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 140, 
    'stepTime': 0.509197998523713, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 141, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.512362061023713, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 141, 
    'stepTime': 0.512362061023713, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 142, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.517108154773713, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 142, 
    'stepTime': 0.517108154773713, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 143, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.524227295398712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 143, 
    'stepTime': 0.524227295398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 1843 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.524227295398712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 144, 
    'stepTime': 0.524227295398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 144, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.526727295398712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 144, 
    'stepTime': 0.526727295398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 145, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.530477295398712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 145, 
    'stepTime': 0.530477295398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 146, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.536102295398712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 146, 
    'stepTime': 0.536102295398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 1687 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.536102295398712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 147, 
    'stepTime': 0.536102295398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 147, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.538211670398712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 147, 
    'stepTime': 0.538211670398712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 148, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.541375732898712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 148, 
    'stepTime': 0.541375732898712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 149, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.546121826648712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 149, 
    'stepTime': 0.546121826648712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 150, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.553240967273712, 
    'attempts': 1, 'timeIncrement': 0.007119140625, 'increment': 150, 
    'stepTime': 0.553240967273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 16 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.553240967273712, 
    'attempts': ' 1U', 'timeIncrement': 0.01, 'increment': 151, 
    'stepTime': 0.553240967273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 151, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.555740967273712, 
    'attempts': 2, 'timeIncrement': 0.0025, 'increment': 151, 
    'stepTime': 0.555740967273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 152, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.559490967273712, 
    'attempts': 1, 'timeIncrement': 0.00375, 'increment': 152, 
    'stepTime': 0.559490967273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 153, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.565115967273712, 
    'attempts': 1, 'timeIncrement': 0.005625, 'increment': 153, 
    'stepTime': 0.565115967273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 1202 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.565115967273712, 
    'attempts': ' 1U', 'timeIncrement': 0.0084375, 'increment': 154, 
    'stepTime': 0.565115967273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 154, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.567225342273712, 
    'attempts': 2, 'timeIncrement': 0.002109375, 'increment': 154, 
    'stepTime': 0.567225342273712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 155, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.570389404773712, 
    'attempts': 1, 'timeIncrement': 0.0031640625, 'increment': 155, 
    'stepTime': 0.570389404773712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 156, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.575135498523712, 
    'attempts': 1, 'timeIncrement': 0.00474609375, 'increment': 156, 
    'stepTime': 0.575135498523712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 1013 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.575135498523712, 
    'attempts': ' 1U', 'timeIncrement': 0.007119140625, 'increment': 157, 
    'stepTime': 0.575135498523712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 157, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.576915283679962, 
    'attempts': 2, 'timeIncrement': 0.00177978515625, 'increment': 157, 
    'stepTime': 0.576915283679962, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 158, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.579584961414337, 
    'attempts': 1, 'timeIncrement': 0.002669677734375, 'increment': 158, 
    'stepTime': 0.579584961414337, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 159, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.5835894780159, 
    'attempts': 1, 'timeIncrement': 0.0040045166015625, 'increment': 159, 
    'stepTime': 0.5835894780159, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 160, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.589596252918244, 
    'attempts': 1, 'timeIncrement': 0.00600677490234375, 'increment': 160, 
    'stepTime': 0.589596252918244, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 2243 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.589596252918244, 
    'attempts': ' 1U', 'timeIncrement': 0.00901016235351563, 'increment': 161, 
    'stepTime': 0.589596252918244, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 161, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.591848793506623, 
    'attempts': 2, 'timeIncrement': 0.00225254058837891, 'increment': 161, 
    'stepTime': 0.591848793506623, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 162, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.595227604389191, 
    'attempts': 1, 'timeIncrement': 0.00337881088256836, 'increment': 162, 
    'stepTime': 0.595227604389191, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 163, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.600295820713043, 
    'attempts': 1, 'timeIncrement': 0.00506821632385254, 'increment': 163, 
    'stepTime': 0.600295820713043, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 16 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.600295820713043, 
    'attempts': ' 1U', 'timeIncrement': 0.00760232448577881, 'increment': 164, 
    'stepTime': 0.600295820713043, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 164, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.602196401834488, 
    'attempts': 2, 'timeIncrement': 0.0019005811214447, 'increment': 164, 
    'stepTime': 0.602196401834488, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 165, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.605047273516655, 
    'attempts': 1, 'timeIncrement': 0.00285087168216705, 'increment': 165, 
    'stepTime': 0.605047273516655, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 166, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.609323581039906, 
    'attempts': 1, 'timeIncrement': 0.00427630752325058, 'increment': 166, 
    'stepTime': 0.609323581039906, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 167, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.615738042324782, 
    'attempts': 1, 'timeIncrement': 0.00641446128487587, 'increment': 167, 
    'stepTime': 0.615738042324782, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 2 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.615738042324782, 
    'attempts': ' 1U', 'timeIncrement': 0.00962169192731381, 'increment': 168, 
    'stepTime': 0.615738042324782, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 168, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.61814346530661, 
    'attempts': 2, 'timeIncrement': 0.00240542298182845, 'increment': 168, 
    'stepTime': 0.61814346530661, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 169, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.621751599779353, 
    'attempts': 1, 'timeIncrement': 0.00360813447274268, 'increment': 169, 
    'stepTime': 0.621751599779353, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 170, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.627163801488467, 
    'attempts': 1, 'timeIncrement': 0.00541220170911402, 'increment': 170, 
    'stepTime': 0.627163801488467, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 604 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.627163801488467, 
    'attempts': ' 1U', 'timeIncrement': 0.00811830256367103, 'increment': 171, 
    'stepTime': 0.627163801488467, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 171, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.629193377129385, 
    'attempts': 2, 'timeIncrement': 0.00202957564091776, 'increment': 171, 
    'stepTime': 0.629193377129385, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 172, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.632237740590761, 
    'attempts': 1, 'timeIncrement': 0.00304436346137663, 'increment': 172, 
    'stepTime': 0.632237740590761, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 173, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.636804285782826, 
    'attempts': 1, 'timeIncrement': 0.00456654519206495, 'increment': 173, 
    'stepTime': 0.636804285782826, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 12173 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.636804285782826, 
    'attempts': ' 1U', 'timeIncrement': 0.00684981778809743, 'increment': 174, 
    'stepTime': 0.636804285782826, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 174, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.63851674022985, 
    'attempts': 2, 'timeIncrement': 0.00171245444702436, 'increment': 174, 
    'stepTime': 0.63851674022985, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 175, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.641085421900387, 
    'attempts': 1, 'timeIncrement': 0.00256868167053653, 'increment': 175, 
    'stepTime': 0.641085421900387, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 176, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.644938444406192, 
    'attempts': 1, 'timeIncrement': 0.0038530225058048, 'increment': 176, 
    'stepTime': 0.644938444406192, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 177, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.650717978164899, 
    'attempts': 1, 'timeIncrement': 0.0057795337587072, 'increment': 177, 
    'stepTime': 0.650717978164899, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 282 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.650717978164899, 
    'attempts': ' 1U', 'timeIncrement': 0.00866930063806081, 'increment': 178, 
    'stepTime': 0.650717978164899, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 178, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.652885303324414, 
    'attempts': 2, 'timeIncrement': 0.0021673251595152, 'increment': 178, 
    'stepTime': 0.652885303324414, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 179, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.656136291063687, 
    'attempts': 1, 'timeIncrement': 0.0032509877392728, 'increment': 179, 
    'stepTime': 0.656136291063687, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 180, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.661012772672596, 
    'attempts': 1, 'timeIncrement': 0.0048764816089092, 'increment': 180, 
    'stepTime': 0.661012772672596, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 91 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.661012772672596, 
    'attempts': ' 1U', 'timeIncrement': 0.0073147224133638, 'increment': 181, 
    'stepTime': 0.661012772672596, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 181, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.662841453275937, 
    'attempts': 2, 'timeIncrement': 0.00182868060334095, 'increment': 181, 
    'stepTime': 0.662841453275937, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 182, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.665584474180949, 
    'attempts': 1, 'timeIncrement': 0.00274302090501143, 'increment': 182, 
    'stepTime': 0.665584474180949, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 183, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.669699005538466, 
    'attempts': 1, 'timeIncrement': 0.00411453135751714, 'increment': 183, 
    'stepTime': 0.669699005538466, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 184, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.675870802574742, 
    'attempts': 1, 'timeIncrement': 0.00617179703627571, 'increment': 184, 
    'stepTime': 0.675870802574742, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 6 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.675870802574742, 
    'attempts': ' 1U', 'timeIncrement': 0.00617179703627571, 'increment': 185, 
    'stepTime': 0.675870802574742, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 185, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.67741375183381, 
    'attempts': 2, 'timeIncrement': 0.00154294925906893, 'increment': 185, 
    'stepTime': 0.67741375183381, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 186, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.678956701092879, 
    'attempts': 1, 'timeIncrement': 0.00154294925906893, 'increment': 186, 
    'stepTime': 0.678956701092879, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 187, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.681271124981483, 
    'attempts': 1, 'timeIncrement': 0.00231442388860339, 'increment': 187, 
    'stepTime': 0.681271124981483, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 188, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.684742760814388, 
    'attempts': 1, 'timeIncrement': 0.00347163583290509, 'increment': 188, 
    'stepTime': 0.684742760814388, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 189, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.689950214563746, 
    'attempts': 1, 'timeIncrement': 0.00520745374935763, 'increment': 189, 
    'stepTime': 0.689950214563746, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 2937 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.689950214563746, 
    'attempts': ' 1U', 'timeIncrement': 0.00781118062403645, 'increment': 190, 
    'stepTime': 0.689950214563746, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 190, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.691903009719755, 
    'attempts': 2, 'timeIncrement': 0.00195279515600911, 'increment': 190, 
    'stepTime': 0.691903009719755, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 191, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.694832202453768, 
    'attempts': 1, 'timeIncrement': 0.00292919273401367, 'increment': 191, 
    'stepTime': 0.694832202453768, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 192, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.699225991554789, 
    'attempts': 1, 'timeIncrement': 0.0043937891010205, 'increment': 192, 
    'stepTime': 0.699225991554789, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 1361 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.699225991554789, 
    'attempts': ' 1U', 'timeIncrement': 0.00659068365153075, 'increment': 193, 
    'stepTime': 0.699225991554789, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 193, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.700873662467671, 
    'attempts': 2, 'timeIncrement': 0.00164767091288269, 'increment': 193, 
    'stepTime': 0.700873662467671, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 194, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.703345168836995, 
    'attempts': 1, 'timeIncrement': 0.00247150636932403, 'increment': 194, 
    'stepTime': 0.703345168836995, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 195, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.707052428390982, 
    'attempts': 1, 'timeIncrement': 0.00370725955398605, 'increment': 195, 
    'stepTime': 0.707052428390982, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.707052428390982, 
    'attempts': ' 1U', 'timeIncrement': 0.00556088933097907, 'increment': 196, 
    'stepTime': 0.707052428390982, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 196, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.708442650723726, 
    'attempts': 2, 'timeIncrement': 0.00139022233274477, 'increment': 196, 
    'stepTime': 0.708442650723726, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 197, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.710527984222843, 
    'attempts': 1, 'timeIncrement': 0.00208533349911715, 'increment': 197, 
    'stepTime': 0.710527984222843, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 198, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.713655984471519, 
    'attempts': 1, 'timeIncrement': 0.00312800024867573, 'increment': 198, 
    'stepTime': 0.713655984471519, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 199, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.718347984844533, 
    'attempts': 1, 'timeIncrement': 0.00469200037301359, 'increment': 199, 
    'stepTime': 0.718347984844533, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 100 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.718347984844533, 
    'attempts': ' 1U', 'timeIncrement': 0.00703800055952039, 'increment': 200, 
    'stepTime': 0.718347984844533, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 200, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.720107484984413, 
    'attempts': 2, 'timeIncrement': 0.0017595001398801, 'increment': 200, 
    'stepTime': 0.720107484984413, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 201, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.722746735194233, 
    'attempts': 1, 'timeIncrement': 0.00263925020982015, 'increment': 201, 
    'stepTime': 0.722746735194233, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 202, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.726705610508963, 
    'attempts': 1, 'timeIncrement': 0.00395887531473022, 'increment': 202, 
    'stepTime': 0.726705610508963, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 43 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.726705610508963, 
    'attempts': ' 1U', 'timeIncrement': 0.00593831297209533, 'increment': 203, 
    'stepTime': 0.726705610508963, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 203, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.728190188751987, 
    'attempts': 2, 'timeIncrement': 0.00148457824302383, 'increment': 203, 
    'stepTime': 0.728190188751987, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 204, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.730417056116523, 
    'attempts': 1, 'timeIncrement': 0.00222686736453575, 'increment': 204, 
    'stepTime': 0.730417056116523, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 205, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.733757357163326, 
    'attempts': 1, 'timeIncrement': 0.00334030104680362, 'increment': 205, 
    'stepTime': 0.733757357163326, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.733757357163326, 
    'attempts': ' 1U', 'timeIncrement': 0.00501045157020543, 'increment': 206, 
    'stepTime': 0.733757357163326, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 206, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.735009970055878, 
    'attempts': 2, 'timeIncrement': 0.00125261289255136, 'increment': 206, 
    'stepTime': 0.735009970055878, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 207, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.736888889394705, 
    'attempts': 1, 'timeIncrement': 0.00187891933882704, 'increment': 207, 
    'stepTime': 0.736888889394705, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 208, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.739707268402945, 
    'attempts': 1, 'timeIncrement': 0.00281837900824056, 'increment': 208, 
    'stepTime': 0.739707268402945, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 209, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.743934836915306, 
    'attempts': 1, 'timeIncrement': 0.00422756851236083, 'increment': 209, 
    'stepTime': 0.743934836915306, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.743934836915306, 
    'attempts': ' 1U', 'timeIncrement': 0.00422756851236083, 'increment': 210, 
    'stepTime': 0.743934836915306, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 210, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.744991729043397, 
    'attempts': 2, 'timeIncrement': 0.00105689212809021, 'increment': 210, 
    'stepTime': 0.744991729043397, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 211, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.746048621171487, 
    'attempts': 1, 'timeIncrement': 0.00105689212809021, 'increment': 211, 
    'stepTime': 0.746048621171487, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 212, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.747633959363622, 
    'attempts': 1, 'timeIncrement': 0.00158533819213531, 'increment': 212, 
    'stepTime': 0.747633959363622, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 213, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.750011966651825, 
    'attempts': 1, 'timeIncrement': 0.00237800728820297, 'increment': 213, 
    'stepTime': 0.750011966651825, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 214, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.75357897758413, 
    'attempts': 1, 'timeIncrement': 0.00356701093230445, 'increment': 214, 
    'stepTime': 0.75357897758413, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 215, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.758929493982586, 
    'attempts': 1, 'timeIncrement': 0.00535051639845668, 'increment': 215, 
    'stepTime': 0.758929493982586, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 120 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.758929493982586, 
    'attempts': ' 1U', 'timeIncrement': 0.00535051639845668, 'increment': 216, 
    'stepTime': 0.758929493982586, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 216, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.7602671230822, 
    'attempts': 2, 'timeIncrement': 0.00133762909961417, 'increment': 216, 
    'stepTime': 0.7602671230822, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 217, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.761604752181815, 
    'attempts': 1, 'timeIncrement': 0.00133762909961417, 'increment': 217, 
    'stepTime': 0.761604752181815, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 218, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.763611195831236, 
    'attempts': 1, 'timeIncrement': 0.00200644364942126, 'increment': 218, 
    'stepTime': 0.763611195831236, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 219, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.766620861305368, 
    'attempts': 1, 'timeIncrement': 0.00300966547413188, 'increment': 219, 
    'stepTime': 0.766620861305368, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 9 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.766620861305368, 
    'attempts': ' 1U', 'timeIncrement': 0.00451449821119782, 'increment': 220, 
    'stepTime': 0.766620861305368, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 220, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.767749485858167, 
    'attempts': 2, 'timeIncrement': 0.00112862455279946, 'increment': 220, 
    'stepTime': 0.767749485858167, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 221, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.769442422687366, 
    'attempts': 1, 'timeIncrement': 0.00169293682919918, 'increment': 221, 
    'stepTime': 0.769442422687366, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 222, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.771981827931165, 
    'attempts': 1, 'timeIncrement': 0.00253940524379878, 'increment': 222, 
    'stepTime': 0.771981827931165, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 223, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.775790935796863, 
    'attempts': 1, 'timeIncrement': 0.00380910786569816, 'increment': 223, 
    'stepTime': 0.775790935796863, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 9, 'phase': STANDARD_PHASE, 'equilibrium': 9})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 1 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.775790935796863, 
    'attempts': ' 1U', 'timeIncrement': 0.00380910786569816, 'increment': 224, 
    'stepTime': 0.775790935796863, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 224, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.776743212763288, 
    'attempts': 2, 'timeIncrement': 0.000952276966424541, 'increment': 224, 
    'stepTime': 0.776743212763288, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 225, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.777695489729712, 
    'attempts': 1, 'timeIncrement': 0.000952276966424541, 'increment': 225, 
    'stepTime': 0.777695489729712, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 226, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.779123905179349, 
    'attempts': 1, 'timeIncrement': 0.00142841544963681, 'increment': 226, 
    'stepTime': 0.779123905179349, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 227, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.781266528353804, 
    'attempts': 1, 'timeIncrement': 0.00214262317445522, 'increment': 227, 
    'stepTime': 0.781266528353804, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 228, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.784480463115487, 
    'attempts': 1, 'timeIncrement': 0.00321393476168283, 'increment': 228, 
    'stepTime': 0.784480463115487, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 229, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.789301365258012, 
    'attempts': 1, 'timeIncrement': 0.00482090214252424, 'increment': 229, 
    'stepTime': 0.789301365258012, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 10845 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.789301365258012, 
    'attempts': ' 1U', 'timeIncrement': 0.00482090214252424, 'increment': 230, 
    'stepTime': 0.789301365258012, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 230, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.790506590793643, 
    'attempts': 2, 'timeIncrement': 0.00120522553563106, 'increment': 230, 
    'stepTime': 0.790506590793643, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 231, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.791711816329274, 
    'attempts': 1, 'timeIncrement': 0.00120522553563106, 'increment': 231, 
    'stepTime': 0.791711816329274, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 232, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.79351965463272, 
    'attempts': 1, 'timeIncrement': 0.00180783830344659, 'increment': 232, 
    'stepTime': 0.79351965463272, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 233, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.79623141208789, 
    'attempts': 1, 'timeIncrement': 0.00271175745516988, 'increment': 233, 
    'stepTime': 0.79623141208789, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 353 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.79623141208789, 
    'attempts': ' 1U', 'timeIncrement': 0.00406763618275483, 'increment': 234, 
    'stepTime': 0.79623141208789, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 234, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.797248321133579, 
    'attempts': 2, 'timeIncrement': 0.00101690904568871, 'increment': 234, 
    'stepTime': 0.797248321133579, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 235, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.798773684702112, 
    'attempts': 1, 'timeIncrement': 0.00152536356853306, 'increment': 235, 
    'stepTime': 0.798773684702112, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 236, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.801061730054912, 
    'attempts': 1, 'timeIncrement': 0.00228804535279959, 'increment': 236, 
    'stepTime': 0.801061730054912, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 237, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.804493798084111, 
    'attempts': 1, 'timeIncrement': 0.00343206802919938, 'increment': 237, 
    'stepTime': 0.804493798084111, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 157 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.804493798084111, 
    'attempts': ' 1U', 'timeIncrement': 0.00343206802919938, 'increment': 238, 
    'stepTime': 0.804493798084111, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 238, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.805351815091411, 
    'attempts': 2, 'timeIncrement': 0.000858017007299846, 'increment': 238, 
    'stepTime': 0.805351815091411, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 239, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.806209832098711, 
    'attempts': 1, 'timeIncrement': 0.000858017007299846, 'increment': 239, 
    'stepTime': 0.806209832098711, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 240, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.80706784910601, 
    'attempts': 1, 'timeIncrement': 0.000858017007299846, 'increment': 240, 
    'stepTime': 0.80706784910601, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 241, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.80835487461696, 
    'attempts': 1, 'timeIncrement': 0.00128702551094977, 'increment': 241, 
    'stepTime': 0.80835487461696, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 242, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.810285412883385, 
    'attempts': 1, 'timeIncrement': 0.00193053826642465, 'increment': 242, 
    'stepTime': 0.810285412883385, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 243, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.813181220283022, 
    'attempts': 1, 'timeIncrement': 0.00289580739963698, 'increment': 243, 
    'stepTime': 0.813181220283022, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 244, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.816077027682659, 
    'attempts': 1, 'timeIncrement': 0.00289580739963698, 'increment': 244, 
    'stepTime': 0.816077027682659, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 245, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.818972835082296, 
    'attempts': 1, 'timeIncrement': 0.00289580739963698, 'increment': 245, 
    'stepTime': 0.818972835082296, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 246, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.821868642481933, 
    'attempts': 1, 'timeIncrement': 0.00289580739963698, 'increment': 246, 
    'stepTime': 0.821868642481933, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 247, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.82476444988157, 
    'attempts': 1, 'timeIncrement': 0.00289580739963698, 'increment': 247, 
    'stepTime': 0.82476444988157, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 248, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.827660257281207, 
    'attempts': 1, 'timeIncrement': 0.00289580739963698, 'increment': 248, 
    'stepTime': 0.827660257281207, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 249, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.830556064680844, 
    'attempts': 1, 'timeIncrement': 0.00289580739963698, 'increment': 249, 
    'stepTime': 0.830556064680844, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 250, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.833451872080481, 
    'attempts': 1, 'timeIncrement': 0.00289580739963698, 'increment': 250, 
    'stepTime': 0.833451872080481, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 251, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.836347679480118, 
    'attempts': 1, 'timeIncrement': 0.00289580739963698, 'increment': 251, 
    'stepTime': 0.836347679480118, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.836347679480118, 
    'attempts': ' 1U', 'timeIncrement': 0.00289580739963698, 'increment': 252, 
    'stepTime': 0.836347679480118, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 252, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.837071631330027, 
    'attempts': 2, 'timeIncrement': 0.000723951849909245, 'increment': 252, 
    'stepTime': 0.837071631330027, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 253, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.837795583179936, 
    'attempts': 1, 'timeIncrement': 0.000723951849909245, 'increment': 253, 
    'stepTime': 0.837795583179936, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 254, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.8388815109548, 
    'attempts': 1, 'timeIncrement': 0.00108592777486387, 'increment': 254, 
    'stepTime': 0.8388815109548, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 255, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.840510402617096, 
    'attempts': 1, 'timeIncrement': 0.0016288916622958, 'increment': 255, 
    'stepTime': 0.840510402617096, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 256, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.84295374011054, 
    'attempts': 1, 'timeIncrement': 0.0024433374934437, 'increment': 256, 
    'stepTime': 0.84295374011054, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 257, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.845397077603984, 
    'attempts': 1, 'timeIncrement': 0.0024433374934437, 'increment': 257, 
    'stepTime': 0.845397077603984, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 258, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.847840415097427, 
    'attempts': 1, 'timeIncrement': 0.0024433374934437, 'increment': 258, 
    'stepTime': 0.847840415097427, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 259, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.850283752590871, 
    'attempts': 1, 'timeIncrement': 0.0024433374934437, 'increment': 259, 
    'stepTime': 0.850283752590871, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 260, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.852727090084315, 
    'attempts': 1, 'timeIncrement': 0.0024433374934437, 'increment': 260, 
    'stepTime': 0.852727090084315, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.852727090084315, 
    'attempts': ' 1U', 'timeIncrement': 0.0024433374934437, 'increment': 261, 
    'stepTime': 0.852727090084315, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 261, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.853337924457676, 
    'attempts': 2, 'timeIncrement': 0.000610834373360926, 'increment': 261, 
    'stepTime': 0.853337924457676, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 262, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.853948758831037, 
    'attempts': 1, 'timeIncrement': 0.000610834373360926, 'increment': 262, 
    'stepTime': 0.853948758831037, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 263, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.854865010391078, 
    'attempts': 1, 'timeIncrement': 0.000916251560041389, 'increment': 263, 
    'stepTime': 0.854865010391078, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 264, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.85623938773114, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 264, 
    'stepTime': 0.85623938773114, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 265, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.857613765071202, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 265, 
    'stepTime': 0.857613765071202, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 266, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.858988142411264, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 266, 
    'stepTime': 0.858988142411264, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 267, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.860362519751326, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 267, 
    'stepTime': 0.860362519751326, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 268, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.861736897091388, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 268, 
    'stepTime': 0.861736897091388, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 269, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.86311127443145, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 269, 
    'stepTime': 0.86311127443145, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 270, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.864485651771512, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 270, 
    'stepTime': 0.864485651771512, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 271, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.865860029111575, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 271, 
    'stepTime': 0.865860029111575, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 272, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.867234406451637, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 272, 
    'stepTime': 0.867234406451637, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 273, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.868608783791699, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 273, 
    'stepTime': 0.868608783791699, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 274, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.869983161131761, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 274, 
    'stepTime': 0.869983161131761, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 275, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.871357538471823, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 275, 
    'stepTime': 0.871357538471823, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 276, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.872731915811885, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 276, 
    'stepTime': 0.872731915811885, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 277, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.874106293151947, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 277, 
    'stepTime': 0.874106293151947, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 278, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.875480670492009, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 278, 
    'stepTime': 0.875480670492009, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 279, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.876855047832071, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 279, 
    'stepTime': 0.876855047832071, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 280, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.878229425172133, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 280, 
    'stepTime': 0.878229425172133, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 281, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.879603802512195, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 281, 
    'stepTime': 0.879603802512195, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 282, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.880978179852257, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 282, 
    'stepTime': 0.880978179852257, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 283, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.882352557192319, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 283, 
    'stepTime': 0.882352557192319, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 284, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.883726934532381, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 284, 
    'stepTime': 0.883726934532381, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 285, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.885101311872444, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 285, 
    'stepTime': 0.885101311872444, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 286, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.886475689212506, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 286, 
    'stepTime': 0.886475689212506, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 287, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.887850066552568, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 287, 
    'stepTime': 0.887850066552568, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 288, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.88922444389263, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 288, 
    'stepTime': 0.88922444389263, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 289, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.890598821232692, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 289, 
    'stepTime': 0.890598821232692, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 290, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.891973198572754, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 290, 
    'stepTime': 0.891973198572754, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 291, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.893347575912816, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 291, 
    'stepTime': 0.893347575912816, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 292, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.894721953252878, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 292, 
    'stepTime': 0.894721953252878, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 293, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.89609633059294, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 293, 
    'stepTime': 0.89609633059294, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 294, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.897470707933002, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 294, 
    'stepTime': 0.897470707933002, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 295, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.898845085273064, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 295, 
    'stepTime': 0.898845085273064, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 296, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.900219462613126, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 296, 
    'stepTime': 0.900219462613126, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 297, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.901593839953188, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 297, 
    'stepTime': 0.901593839953188, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 298, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.90296821729325, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 298, 
    'stepTime': 0.90296821729325, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 299, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.904342594633313, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 299, 
    'stepTime': 0.904342594633313, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 300, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.905716971973375, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 300, 
    'stepTime': 0.905716971973375, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 301, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.907091349313437, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 301, 
    'stepTime': 0.907091349313437, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 302, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.908465726653499, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 302, 
    'stepTime': 0.908465726653499, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 303, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.909840103993561, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 303, 
    'stepTime': 0.909840103993561, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 304, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.911214481333623, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 304, 
    'stepTime': 0.911214481333623, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 305, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.912588858673685, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 305, 
    'stepTime': 0.912588858673685, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 306, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.913963236013747, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 306, 
    'stepTime': 0.913963236013747, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 307, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.915337613353809, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 307, 
    'stepTime': 0.915337613353809, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 308, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.916711990693871, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 308, 
    'stepTime': 0.916711990693871, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 309, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.918086368033933, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 309, 
    'stepTime': 0.918086368033933, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 310, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.919460745373995, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 310, 
    'stepTime': 0.919460745373995, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 311, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.920835122714057, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 311, 
    'stepTime': 0.920835122714057, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 312, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.92220950005412, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 312, 
    'stepTime': 0.92220950005412, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 313, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.923583877394182, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 313, 
    'stepTime': 0.923583877394182, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 314, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.924958254734244, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 314, 
    'stepTime': 0.924958254734244, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 315, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.926332632074306, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 315, 
    'stepTime': 0.926332632074306, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 316, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.927707009414368, 
    'attempts': 1, 'timeIncrement': 0.00137437734006208, 'increment': 316, 
    'stepTime': 0.927707009414368, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.927707009414368, 
    'attempts': ' 1U', 'timeIncrement': 0.00137437734006208, 'increment': 317, 
    'stepTime': 0.927707009414368, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 317, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.928050603749383, 
    'attempts': 2, 'timeIncrement': 0.000343594335015521, 'increment': 317, 
    'stepTime': 0.928050603749383, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 318, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.928394198084399, 
    'attempts': 1, 'timeIncrement': 0.000343594335015521, 'increment': 318, 
    'stepTime': 0.928394198084399, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 319, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.928909589586922, 
    'attempts': 1, 'timeIncrement': 0.000515391502523281, 'increment': 319, 
    'stepTime': 0.928909589586922, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 320, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.929682676840707, 
    'attempts': 1, 'timeIncrement': 0.000773087253784922, 'increment': 320, 
    'stepTime': 0.929682676840707, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 7725 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.929682676840707, 
    'attempts': ' 1U', 'timeIncrement': 0.00115963088067738, 'increment': 321, 
    'stepTime': 0.929682676840707, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 321, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.929972584560876, 
    'attempts': 2, 'timeIncrement': 0.000289907720169346, 'increment': 321, 
    'stepTime': 0.929972584560876, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 322, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.93040744614113, 
    'attempts': 1, 'timeIncrement': 0.000434861580254018, 'increment': 322, 
    'stepTime': 0.93040744614113, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 323, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.931059738511511, 
    'attempts': 1, 'timeIncrement': 0.000652292370381028, 'increment': 323, 
    'stepTime': 0.931059738511511, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 324, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.932038177067083, 
    'attempts': 1, 'timeIncrement': 0.000978438555571541, 'increment': 324, 
    'stepTime': 0.932038177067083, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 325, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.933016615622654, 
    'attempts': 1, 'timeIncrement': 0.000978438555571541, 'increment': 325, 
    'stepTime': 0.933016615622654, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.933016615622654, 
    'attempts': ' 1U', 'timeIncrement': 0.000978438555571541, 'increment': 326, 
    'stepTime': 0.933016615622654, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 326, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.933261225261547, 
    'attempts': 2, 'timeIncrement': 0.000244609638892885, 'increment': 326, 
    'stepTime': 0.933261225261547, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 327, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.93350583490044, 
    'attempts': 1, 'timeIncrement': 0.000244609638892885, 'increment': 327, 
    'stepTime': 0.93350583490044, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 328, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.93387274935878, 
    'attempts': 1, 'timeIncrement': 0.000366914458339328, 'increment': 328, 
    'stepTime': 0.93387274935878, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 329, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.934423121046289, 
    'attempts': 1, 'timeIncrement': 0.000550371687508992, 'increment': 329, 
    'stepTime': 0.934423121046289, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 330, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.935248678577552, 
    'attempts': 1, 'timeIncrement': 0.000825557531263488, 'increment': 330, 
    'stepTime': 0.935248678577552, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 96 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.935248678577552, 
    'attempts': ' 1U', 'timeIncrement': 0.00123833629689523, 'increment': 331, 
    'stepTime': 0.935248678577552, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 331, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.935558262651776, 
    'attempts': 2, 'timeIncrement': 0.000309584074223808, 'increment': 331, 
    'stepTime': 0.935558262651776, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 332, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.936022638763112, 
    'attempts': 1, 'timeIncrement': 0.000464376111335712, 'increment': 332, 
    'stepTime': 0.936022638763112, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 333, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.936719202930115, 
    'attempts': 1, 'timeIncrement': 0.000696564167003568, 'increment': 333, 
    'stepTime': 0.936719202930115, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 23 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.936719202930115, 
    'attempts': ' 1U', 'timeIncrement': 0.00104484625050535, 'increment': 334, 
    'stepTime': 0.936719202930115, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 334, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.936980414492741, 
    'attempts': 2, 'timeIncrement': 0.000261211562626338, 'increment': 334, 
    'stepTime': 0.936980414492741, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 335, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.937372231836681, 
    'attempts': 1, 'timeIncrement': 0.000391817343939507, 'increment': 335, 
    'stepTime': 0.937372231836681, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 336, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.93795995785259, 
    'attempts': 1, 'timeIncrement': 0.00058772601590926, 'increment': 336, 
    'stepTime': 0.93795995785259, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 337, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.938841546876454, 
    'attempts': 1, 'timeIncrement': 0.000881589023863891, 'increment': 337, 
    'stepTime': 0.938841546876454, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.938841546876454, 
    'attempts': ' 1U', 'timeIncrement': 0.00132238353579584, 'increment': 338, 
    'stepTime': 0.938841546876454, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 338, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.939172142760403, 
    'attempts': 2, 'timeIncrement': 0.000330595883948959, 'increment': 338, 
    'stepTime': 0.939172142760403, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 339, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.939668036586327, 
    'attempts': 1, 'timeIncrement': 0.000495893825923438, 'increment': 339, 
    'stepTime': 0.939668036586327, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 340, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.940411877325212, 
    'attempts': 1, 'timeIncrement': 0.000743840738885158, 'increment': 340, 
    'stepTime': 0.940411877325212, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 77 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.940411877325212, 
    'attempts': ' 1U', 'timeIncrement': 0.00111576110832774, 'increment': 341, 
    'stepTime': 0.940411877325212, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 341, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.940690817602294, 
    'attempts': 2, 'timeIncrement': 0.000278940277081934, 'increment': 341, 
    'stepTime': 0.940690817602294, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 342, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.941109228017917, 
    'attempts': 1, 'timeIncrement': 0.000418410415622901, 'increment': 342, 
    'stepTime': 0.941109228017917, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 343, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.941736843641351, 
    'attempts': 1, 'timeIncrement': 0.000627615623434352, 'increment': 343, 
    'stepTime': 0.941736843641351, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.941736843641351, 
    'attempts': ' 1U', 'timeIncrement': 0.000941423435151527, 'increment': 344, 
    'stepTime': 0.941736843641351, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 344, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.941972199500139, 
    'attempts': 2, 'timeIncrement': 0.000235355858787882, 'increment': 344, 
    'stepTime': 0.941972199500139, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 345, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.942325233288321, 
    'attempts': 1, 'timeIncrement': 0.000353033788181823, 'increment': 345, 
    'stepTime': 0.942325233288321, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 346, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.942854783970594, 
    'attempts': 1, 'timeIncrement': 0.000529550682272734, 'increment': 346, 
    'stepTime': 0.942854783970594, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 347, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.943649109994003, 
    'attempts': 1, 'timeIncrement': 0.000794326023409101, 'increment': 347, 
    'stepTime': 0.943649109994003, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 348, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.944443436017412, 
    'attempts': 1, 'timeIncrement': 0.000794326023409101, 'increment': 348, 
    'stepTime': 0.944443436017412, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 349, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.945237762040821, 
    'attempts': 1, 'timeIncrement': 0.000794326023409101, 'increment': 349, 
    'stepTime': 0.945237762040821, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.945237762040821, 
    'attempts': ' 1U', 'timeIncrement': 0.00119148903511365, 'increment': 350, 
    'stepTime': 0.945237762040821, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 350, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.945535634299599, 
    'attempts': 2, 'timeIncrement': 0.000297872258778413, 'increment': 350, 
    'stepTime': 0.945535634299599, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 351, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.945982442687767, 
    'attempts': 1, 'timeIncrement': 0.00044680838816762, 'increment': 351, 
    'stepTime': 0.945982442687767, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 352, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.946652655270018, 
    'attempts': 1, 'timeIncrement': 0.000670212582251429, 'increment': 352, 
    'stepTime': 0.946652655270018, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.946652655270018, 
    'attempts': ' 1U', 'timeIncrement': 0.00100531887337714, 'increment': 353, 
    'stepTime': 0.946652655270018, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 353, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.946903984988363, 
    'attempts': 2, 'timeIncrement': 0.000251329718344286, 'increment': 353, 
    'stepTime': 0.946903984988363, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 354, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.947280979565879, 
    'attempts': 1, 'timeIncrement': 0.000376994577516429, 'increment': 354, 
    'stepTime': 0.947280979565879, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 355, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.947846471432154, 
    'attempts': 1, 'timeIncrement': 0.000565491866274643, 'increment': 355, 
    'stepTime': 0.947846471432154, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 356, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.948694709231566, 
    'attempts': 1, 'timeIncrement': 0.000848237799411965, 'increment': 356, 
    'stepTime': 0.948694709231566, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.948694709231566, 
    'attempts': ' 1U', 'timeIncrement': 0.00127235669911795, 'increment': 357, 
    'stepTime': 0.948694709231566, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 357, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.949012798406345, 
    'attempts': 2, 'timeIncrement': 0.000318089174779487, 'increment': 357, 
    'stepTime': 0.949012798406345, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 358, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.949489932168514, 
    'attempts': 1, 'timeIncrement': 0.00047713376216923, 'increment': 358, 
    'stepTime': 0.949489932168514, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 359, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.950205632811768, 
    'attempts': 1, 'timeIncrement': 0.000715700643253846, 'increment': 359, 
    'stepTime': 0.950205632811768, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.950205632811768, 
    'attempts': ' 1U', 'timeIncrement': 0.00107355096488077, 'increment': 360, 
    'stepTime': 0.950205632811768, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 360, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.950474020552988, 
    'attempts': 2, 'timeIncrement': 0.000268387741220192, 'increment': 360, 
    'stepTime': 0.950474020552988, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 361, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.950876602164819, 
    'attempts': 1, 'timeIncrement': 0.000402581611830288, 'increment': 361, 
    'stepTime': 0.950876602164819, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 362, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.951480474582564, 
    'attempts': 1, 'timeIncrement': 0.000603872417745432, 'increment': 362, 
    'stepTime': 0.951480474582564, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.951480474582564, 
    'attempts': ' 1U', 'timeIncrement': 0.000905808626618148, 'increment': 363, 
    'stepTime': 0.951480474582564, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 363, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.951706926739219, 
    'attempts': 2, 'timeIncrement': 0.000226452156654537, 'increment': 363, 
    'stepTime': 0.951706926739219, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 364, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.9520466049742, 
    'attempts': 1, 'timeIncrement': 0.000339678234981806, 'increment': 364, 
    'stepTime': 0.9520466049742, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 365, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.952556122326673, 
    'attempts': 1, 'timeIncrement': 0.000509517352472708, 'increment': 365, 
    'stepTime': 0.952556122326673, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 366, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.953320398355382, 
    'attempts': 1, 'timeIncrement': 0.000764276028709062, 'increment': 366, 
    'stepTime': 0.953320398355382, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 272 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.953320398355382, 
    'attempts': ' 1U', 'timeIncrement': 0.00114641404306359, 'increment': 367, 
    'stepTime': 0.953320398355382, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 367, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.953607001866148, 
    'attempts': 2, 'timeIncrement': 0.000286603510765898, 'increment': 367, 
    'stepTime': 0.953607001866148, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 368, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.954036907132297, 
    'attempts': 1, 'timeIncrement': 0.000429905266148848, 'increment': 368, 
    'stepTime': 0.954036907132297, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 369, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.95468176503152, 
    'attempts': 1, 'timeIncrement': 0.000644857899223271, 'increment': 369, 
    'stepTime': 0.95468176503152, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 1 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.95468176503152, 
    'attempts': ' 1U', 'timeIncrement': 0.000967286848834907, 'increment': 370, 
    'stepTime': 0.95468176503152, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 370, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.954923586743729, 
    'attempts': 2, 'timeIncrement': 0.000241821712208727, 'increment': 370, 
    'stepTime': 0.954923586743729, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 371, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.955286319312042, 
    'attempts': 1, 'timeIncrement': 0.00036273256831309, 'increment': 371, 
    'stepTime': 0.955286319312042, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 372, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.955830418164512, 
    'attempts': 1, 'timeIncrement': 0.000544098852469635, 'increment': 372, 
    'stepTime': 0.955830418164512, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 373, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.956646566443216, 
    'attempts': 1, 'timeIncrement': 0.000816148278704453, 'increment': 373, 
    'stepTime': 0.956646566443216, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.956646566443216, 
    'attempts': ' 1U', 'timeIncrement': 0.00122422241805668, 'increment': 374, 
    'stepTime': 0.956646566443216, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 374, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.95695262204773, 
    'attempts': 2, 'timeIncrement': 0.00030605560451417, 'increment': 374, 
    'stepTime': 0.95695262204773, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 375, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.957411705454502, 
    'attempts': 1, 'timeIncrement': 0.000459083406771255, 'increment': 375, 
    'stepTime': 0.957411705454502, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 376, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.958100330564658, 
    'attempts': 1, 'timeIncrement': 0.000688625110156882, 'increment': 376, 
    'stepTime': 0.958100330564658, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.958100330564658, 
    'attempts': ' 1U', 'timeIncrement': 0.00103293766523532, 'increment': 377, 
    'stepTime': 0.958100330564658, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 377, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.958358564980967, 
    'attempts': 2, 'timeIncrement': 0.000258234416308831, 'increment': 377, 
    'stepTime': 0.958358564980967, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 378, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.958745916605431, 
    'attempts': 1, 'timeIncrement': 0.000387351624463246, 'increment': 378, 
    'stepTime': 0.958745916605431, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 379, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.959326944042125, 
    'attempts': 1, 'timeIncrement': 0.000581027436694869, 'increment': 379, 
    'stepTime': 0.959326944042125, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 380, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.960198485197168, 
    'attempts': 1, 'timeIncrement': 0.000871541155042304, 'increment': 380, 
    'stepTime': 0.960198485197168, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.960198485197168, 
    'attempts': ' 1U', 'timeIncrement': 0.00130731173256346, 'increment': 381, 
    'stepTime': 0.960198485197168, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 9, 'phase': STANDARD_PHASE, 'equilibrium': 9})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 381, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.960852141063449, 
    'attempts': 2, 'timeIncrement': 0.000653655866281728, 'increment': 381, 
    'stepTime': 0.960852141063449, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.960852141063449, 
    'attempts': ' 1U', 'timeIncrement': 0.000980483799422592, 'increment': 382, 
    'stepTime': 0.960852141063449, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 382, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.961097262013305, 
    'attempts': 2, 'timeIncrement': 0.000245120949855648, 'increment': 382, 
    'stepTime': 0.961097262013305, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 383, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.961464943438089, 
    'attempts': 1, 'timeIncrement': 0.000367681424783472, 'increment': 383, 
    'stepTime': 0.961464943438089, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 384, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.962016465575264, 
    'attempts': 1, 'timeIncrement': 0.000551522137175208, 'increment': 384, 
    'stepTime': 0.962016465575264, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 385, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.962843748781027, 
    'attempts': 1, 'timeIncrement': 0.000827283205762812, 'increment': 385, 
    'stepTime': 0.962843748781027, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.962843748781027, 
    'attempts': ' 1U', 'timeIncrement': 0.00124092480864422, 'increment': 386, 
    'stepTime': 0.962843748781027, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 386, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.963153979983188, 
    'attempts': 2, 'timeIncrement': 0.000310231202161054, 'increment': 386, 
    'stepTime': 0.963153979983188, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 387, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.963619326786429, 
    'attempts': 1, 'timeIncrement': 0.000465346803241582, 'increment': 387, 
    'stepTime': 0.963619326786429, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 388, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.964317346991292, 
    'attempts': 1, 'timeIncrement': 0.000698020204862372, 'increment': 388, 
    'stepTime': 0.964317346991292, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 89 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.964317346991292, 
    'attempts': ' 1U', 'timeIncrement': 0.00104703030729356, 'increment': 389, 
    'stepTime': 0.964317346991292, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 389, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.964579104568115, 
    'attempts': 2, 'timeIncrement': 0.00026175757682339, 'increment': 389, 
    'stepTime': 0.964579104568115, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 390, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.96497174093335, 
    'attempts': 1, 'timeIncrement': 0.000392636365235084, 'increment': 390, 
    'stepTime': 0.96497174093335, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 391, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.965560695481203, 
    'attempts': 1, 'timeIncrement': 0.000588954547852627, 'increment': 391, 
    'stepTime': 0.965560695481203, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 392, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.966444127302982, 
    'attempts': 1, 'timeIncrement': 0.00088343182177894, 'increment': 392, 
    'stepTime': 0.966444127302982, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.966444127302982, 
    'attempts': ' 1U', 'timeIncrement': 0.00132514773266841, 'increment': 393, 
    'stepTime': 0.966444127302982, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 393, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.966775414236149, 
    'attempts': 2, 'timeIncrement': 0.000331286933167103, 'increment': 393, 
    'stepTime': 0.966775414236149, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 394, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.967272344635899, 
    'attempts': 1, 'timeIncrement': 0.000496930399750654, 'increment': 394, 
    'stepTime': 0.967272344635899, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 395, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.968017740235525, 
    'attempts': 1, 'timeIncrement': 0.000745395599625981, 'increment': 395, 
    'stepTime': 0.968017740235525, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'FORCE equilibrium accepted using the alternate tolerance.', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 396, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.969135833634964, 
    'attempts': 1, 'timeIncrement': 0.00111809339943897, 'increment': 396, 
    'stepTime': 0.969135833634964, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 11, 'phase': STANDARD_PHASE, 'equilibrium': 11})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 397, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.969974403684544, 
    'attempts': 1, 'timeIncrement': 0.000838570049579228, 'increment': 397, 
    'stepTime': 0.969974403684544, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 10, 'phase': STANDARD_PHASE, 'equilibrium': 10})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 398, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.970812973734123, 
    'attempts': 1, 'timeIncrement': 0.000838570049579228, 'increment': 398, 
    'stepTime': 0.970812973734123, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 399, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.971651543783702, 
    'attempts': 1, 'timeIncrement': 0.000838570049579228, 'increment': 399, 
    'stepTime': 0.971651543783702, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 400, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.972490113833281, 
    'attempts': 1, 'timeIncrement': 0.000838570049579228, 'increment': 400, 
    'stepTime': 0.972490113833281, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 401, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.97332868388286, 
    'attempts': 1, 'timeIncrement': 0.000838570049579228, 'increment': 401, 
    'stepTime': 0.97332868388286, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 402, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.974586538957229, 
    'attempts': 1, 'timeIncrement': 0.00125785507436884, 'increment': 402, 
    'stepTime': 0.974586538957229, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 403, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.975844394031598, 
    'attempts': 1, 'timeIncrement': 0.00125785507436884, 'increment': 403, 
    'stepTime': 0.975844394031598, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 404, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.977102249105967, 
    'attempts': 1, 'timeIncrement': 0.00125785507436884, 'increment': 404, 
    'stepTime': 0.977102249105967, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 405, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.978360104180336, 
    'attempts': 1, 'timeIncrement': 0.00125785507436884, 'increment': 405, 
    'stepTime': 0.978360104180336, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 406, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.979617959254705, 
    'attempts': 1, 'timeIncrement': 0.00125785507436884, 'increment': 406, 
    'stepTime': 0.979617959254705, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 407, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.980875814329073, 
    'attempts': 1, 'timeIncrement': 0.00125785507436884, 'increment': 407, 
    'stepTime': 0.980875814329073, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 408, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.982133669403442, 
    'attempts': 1, 'timeIncrement': 0.00125785507436884, 'increment': 408, 
    'stepTime': 0.982133669403442, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.982133669403442, 
    'attempts': ' 1U', 'timeIncrement': 0.00125785507436884, 'increment': 409, 
    'stepTime': 0.982133669403442, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 409, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.982448133172034, 
    'attempts': 2, 'timeIncrement': 0.000314463768592211, 'increment': 409, 
    'stepTime': 0.982448133172034, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 410, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.982762596940627, 
    'attempts': 1, 'timeIncrement': 0.000314463768592211, 'increment': 410, 
    'stepTime': 0.982762596940627, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 411, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.983234292593515, 
    'attempts': 1, 'timeIncrement': 0.000471695652888316, 'increment': 411, 
    'stepTime': 0.983234292593515, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 412, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.983941836072847, 
    'attempts': 1, 'timeIncrement': 0.000707543479332474, 'increment': 412, 
    'stepTime': 0.983941836072847, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.983941836072847, 
    'attempts': ' 1U', 'timeIncrement': 0.00106131521899871, 'increment': 413, 
    'stepTime': 0.983941836072847, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 6, 'phase': STANDARD_PHASE, 'equilibrium': 6})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 413, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.984207164877597, 
    'attempts': 2, 'timeIncrement': 0.000265328804749678, 'increment': 413, 
    'stepTime': 0.984207164877597, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 414, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.984605158084722, 
    'attempts': 1, 'timeIncrement': 0.000397993207124517, 'increment': 414, 
    'stepTime': 0.984605158084722, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 415, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.985202147895408, 
    'attempts': 1, 'timeIncrement': 0.000596989810686775, 'increment': 415, 
    'stepTime': 0.985202147895408, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 416, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.986097632611439, 
    'attempts': 1, 'timeIncrement': 0.000895484716030162, 'increment': 416, 
    'stepTime': 0.986097632611439, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 417, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.987440859685484, 
    'attempts': 1, 'timeIncrement': 0.00134322707404524, 'increment': 417, 
    'stepTime': 0.987440859685484, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 8, 'phase': STANDARD_PHASE, 'equilibrium': 8})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 418, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.988784086759529, 
    'attempts': 1, 'timeIncrement': 0.00134322707404524, 'increment': 418, 
    'stepTime': 0.988784086759529, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.988784086759529, 
    'attempts': ' 1U', 'timeIncrement': 0.00134322707404524, 'increment': 419, 
    'stepTime': 0.988784086759529, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 419, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.98911989352804, 
    'attempts': 2, 'timeIncrement': 0.000335806768511311, 'increment': 419, 
    'stepTime': 0.98911989352804, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 420, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.989455700296552, 
    'attempts': 1, 'timeIncrement': 0.000335806768511311, 'increment': 420, 
    'stepTime': 0.989455700296552, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 1, 'phase': STANDARD_PHASE, 'equilibrium': 1})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 421, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.989959410449319, 
    'attempts': 1, 'timeIncrement': 0.000503710152766966, 'increment': 421, 
    'stepTime': 0.989959410449319, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 422, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.990714975678469, 
    'attempts': 1, 'timeIncrement': 0.00075556522915045, 'increment': 422, 
    'stepTime': 0.990714975678469, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 423, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.991470540907619, 
    'attempts': 1, 'timeIncrement': 0.00075556522915045, 'increment': 423, 
    'stepTime': 0.991470540907619, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 424, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.99222610613677, 
    'attempts': 1, 'timeIncrement': 0.00075556522915045, 'increment': 424, 
    'stepTime': 0.99222610613677, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 425, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.993359453980496, 
    'attempts': 1, 'timeIncrement': 0.00113334784372567, 'increment': 425, 
    'stepTime': 0.993359453980496, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 7, 'phase': STANDARD_PHASE, 'equilibrium': 7})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.993359453980496, 
    'attempts': ' 1U', 'timeIncrement': 0.00113334784372567, 'increment': 426, 
    'stepTime': 0.993359453980496, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 426, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.993642790941427, 
    'attempts': 2, 'timeIncrement': 0.000283336960931419, 'increment': 426, 
    'stepTime': 0.993642790941427, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 427, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.993926127902358, 
    'attempts': 1, 'timeIncrement': 0.000283336960931419, 'increment': 427, 
    'stepTime': 0.993926127902358, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 428, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.994351133343755, 
    'attempts': 1, 'timeIncrement': 0.000425005441397128, 'increment': 428, 
    'stepTime': 0.994351133343755, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 429, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.994988641505851, 
    'attempts': 1, 'timeIncrement': 0.000637508162095692, 'increment': 429, 
    'stepTime': 0.994988641505851, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 430, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.995944903748995, 
    'attempts': 1, 'timeIncrement': 0.000956262243143538, 'increment': 430, 
    'stepTime': 0.995944903748995, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 431, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.99737929711371, 
    'attempts': 1, 'timeIncrement': 0.00143439336471531, 'increment': 431, 
    'stepTime': 0.99737929711371, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 5, 'phase': STANDARD_PHASE, 'equilibrium': 5})
mdb.jobs['OneTaper3D']._Message(WARNING, {'phase': STANDARD_PHASE, 
    'message': 'EXCESSIVE DISTORTION AT A TOTAL OF 23188 INTEGRATION POINTS IN SOLID (CONTINUUM) ELEMENTS', 
    'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.99737929711371, 
    'attempts': ' 1U', 'timeIncrement': 0.00143439336471531, 'increment': 432, 
    'stepTime': 0.99737929711371, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 432, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.997737895454889, 
    'attempts': 2, 'timeIncrement': 0.000358598341178827, 'increment': 432, 
    'stepTime': 0.997737895454889, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 4, 'phase': STANDARD_PHASE, 'equilibrium': 4})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 433, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.998096493796068, 
    'attempts': 1, 'timeIncrement': 0.000358598341178827, 'increment': 433, 
    'stepTime': 0.998096493796068, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 2, 'phase': STANDARD_PHASE, 'equilibrium': 2})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 434, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.998634391307836, 
    'attempts': 1, 'timeIncrement': 0.00053789751176824, 'increment': 434, 
    'stepTime': 0.998634391307836, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 435, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 0.999441237575488, 
    'attempts': 1, 'timeIncrement': 0.00080684626765236, 'increment': 435, 
    'stepTime': 0.999441237575488, 'step': 1, 'jobName': 'OneTaper3D', 
    'severe': 0, 'iterations': 3, 'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(ODB_FRAME, {'phase': STANDARD_PHASE, 'step': 0, 
    'frame': 436, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(STATUS, {'totalTime': 1.0, 'attempts': 1, 
    'timeIncrement': 0.000558762424511805, 'increment': 436, 'stepTime': 1.0, 
    'step': 1, 'jobName': 'OneTaper3D', 'severe': 0, 'iterations': 3, 
    'phase': STANDARD_PHASE, 'equilibrium': 3})
mdb.jobs['OneTaper3D']._Message(END_STEP, {'phase': STANDARD_PHASE, 
    'stepId': 1, 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(COMPLETED, {'phase': STANDARD_PHASE, 
    'message': 'Analysis phase complete', 'jobName': 'OneTaper3D'})
mdb.jobs['OneTaper3D']._Message(JOB_COMPLETED, {
    'time': 'Wed Oct 19 21:29:26 2011', 'jobName': 'OneTaper3D'})
# Save by banerjee on Sat Oct 22 17:23:09 2011
