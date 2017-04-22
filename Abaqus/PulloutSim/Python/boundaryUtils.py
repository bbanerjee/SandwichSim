""" boundaryUtils - a module of mathematical functions"""

import math
import part
import assembly

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def dist( pt1, pt2 ):

  dx = pt1[0] - pt2[0]
  dy = pt1[1] - pt2[1]
  dz = pt1[2] - pt2[2]

  dist = math.sqrt( dx*dx + dy*dy + dz*dz )
  return dist


#----------------------------------------

def checkEdge( cntnr, idx, xyz, r ):

  result = 1
  vtxs = cntnr.edges[idx].getVertices()
  for i in range( len( vtxs ) ):
    if ( abs( cntnr.vertices[vtxs[i]].pointOn[0][xyz] - r) > 1.e-6 ):
      result = 0

  return result


#----------------------------------------

def checkLineEdge( cntnr, idx, xyz1, r1, xyz2, r2 ):

  result = 1
  vtxs = cntnr.edges[idx].getVertices()
  for i in range( len( vtxs ) ):
    if ( abs( cntnr.vertices[vtxs[i]].pointOn[0][xyz1] - r1) > 1.e-6 ):
      result = 0
    if ( abs( cntnr.vertices[vtxs[i]].pointOn[0][xyz2] - r2) > 1.e-6 ):
      result = 0
    
  return result


#----------------------------------------

def checkColinearEdge( cntnr, idx, vctr ):

  result = 1
  vtxs = cntnr.edges[idx].getVertices()
  pt0 = cntnr.vertices[vtxs[0]].pointOn[0]
  for i in range( 1,len( vtxs ) ):
    pt1 = cntnr.vertices[vtxs[i]].pointOn[0]
    dot = abs ( (pt0[0]-pt1[0])*vctr[0] + (pt0[1]-pt1[1])*vctr[1] + (pt0[2]-pt1[2])*vctr[2] )
    mag = dist( pt1, pt0 ) * dist( (0,0,0), vctr )
    if ( abs( dot - mag ) > 1.e-6 ):
      result = 0

  return result


#----------------------------------------

def checkEdgeOnCircle( edge, x0, r ):

  pt = edge.pointOn[0]
  dist = math.sqrt( (pt[0]-x0[0])*(pt[0]-x0[0]) + (pt[1]-x0[1])*(pt[1]-x0[1]) )
  if ( abs( dist - r ) < 1.e-6 ):
    return 1
  else: 
    return 0


#----------------------------------------

def checkFace( cntnr, idx, xyz, r ):

  result = 1
  edges = cntnr.faces[idx].getEdges()
  for i in range( len( edges ) ):
    if ( checkEdge(cntnr,edges[i],xyz,r) == 0 ):
      result = 0

  return result


#----------------------------------------

def checkFaceOnSphere( face, x0, r ):

  pt = face.pointOn[0]
  dist = math.sqrt( (pt[0]-x0[0])*(pt[0]-x0[0]) + (pt[1]-x0[1])*(pt[1]-x0[1]) + (pt[2]-x0[2])*(pt[2]-x0[2]) )
  if ( abs( dist - r ) < 1.e-6 ):
    return 1
  else: 
    return 0

#----------------------------------------

def checkFaceOnCircle( face, x0, r ):

  pt = face.pointOn[0]
  dist = math.sqrt( (pt[0]-x0[0])*(pt[0]-x0[0]) + (pt[1]-x0[1])*(pt[1]-x0[1]) )
  if ( abs( dist - r ) < 1.e-6 ):
    return 1
  else: 
    return 0

#----------------------------------------

def getEdges( cntnr, xyz, r ):

  bndEdges = cntnr.edges[0:0]
  for i in range( len( cntnr.edges ) ):
    if ( checkEdge(cntnr,i,xyz,r) == 1 ):
      bndEdges = bndEdges + cntnr.edges.findAt( cntnr.edges[i].pointOn, printWarning=False )

  return( bndEdges )

#----------------------------------------

def getLineEdges( cntnr, xyz1, r1, xyz2, r2 ):

  bndEdges = cntnr.edges[0:0]
  for i in range( len( cntnr.edges ) ):
    if ( checkLineEdge(cntnr,i,xyz1,r1,xyz2,r2) == 1 ):
      bndEdges = bndEdges + cntnr.edges.findAt( cntnr.edges[i].pointOn, printWarning=False )

  return( bndEdges )

#----------------------------------------

def getColinearEdges( cntnr, vctr ):

  bndEdges = cntnr.edges[0:0]
  for i in range( len( cntnr.edges ) ):
    if ( checkColinearEdge(cntnr,i,vctr) == 1 ):
      bndEdges = bndEdges + cntnr.edges.findAt( cntnr.edges[i].pointOn, printWarning=False )

  return( bndEdges )

#----------------------------------------

def getEdgesOnCircle( cntnr, x0, r ):

  bndEdges = cntnr.edges[0:0]
  for i in range( len( cntnr.edges ) ):
    if ( checkEdgeOnCircle(cntnr.edges[i],x0,r) == 1 ):
      bndEdges = bndEdges + cntnr.edges.findAt( cntnr.edges[i].pointOn, printWarning=False )

  return( bndEdges )


#----------------------------------------

def getFaces( cntnr, xyz, r ):

  bndFaces = cntnr.faces[0:0]
  for i in range( len( cntnr.faces ) ):
    if ( checkFace(cntnr,i,xyz,r) == 1 ):
      bndFaces = bndFaces + cntnr.faces.findAt( cntnr.faces[i].pointOn, printWarning=False )

  return( bndFaces )

#----------------------------------------

def getFacesOnSphere( cntnr, x0, r ):

  bndFaces = cntnr.faces[0:0]
  for i in range( len( cntnr.faces ) ):
    if ( checkFaceOnSphere(cntnr.faces[i],x0,r) == 1 ):
      bndFaces = bndFaces + cntnr.faces.findAt( cntnr.faces[i].pointOn, printWarning=False )

  return( bndFaces )

#----------------------------------------

def getFacesOnCircle( cntnr, x0, r ):

  bndFaces = cntnr.faces[0:0]
  for i in range( len( cntnr.faces ) ):
    if ( checkFaceOnCircle(cntnr.faces[i],x0,r) == 1 ):
      bndFaces = bndFaces + cntnr.faces.findAt( cntnr.faces[i].pointOn, printWarning=False )

  return( bndFaces )


#----------------------------------------

def getSequence( array ):

  seq = array[0:0]
  for i in range( len( array ) ):
    seq = seq + array.findAt( array[i].pointOn, printWarning=False )

  return( seq )


#----------------------------------------

def getCellsFromCntnr( cntnr1, cntnr2 ):
  cells = cntnr1.cells[0:0]
  for i in range( len( cntnr2.cells ) ):
    x = y = z = 0
    face = cntnr2.cells[i].getFaces()
    for j in range( len( face ) ):
      x = x + cntnr2.faces[ face[j] ].getCentroid()[0][0] / len(face)
      y = y + cntnr2.faces[ face[j] ].getCentroid()[0][1] / len(face)
      z = z + cntnr2.faces[ face[j] ].getCentroid()[0][2] / len(face)

    try:
      cell = cntnr1.cells.findAt( ((x,y,z),), printWarning=False )
    except:
      cell = cntnr1.cells[0:0]

    cells = cells + cell
  
  return( cells )


#----------------------------------------

def getFacesFromCntnr( cntnr1, cntnr2 ):
  faces = cntnr1.faces[0:0]
  for i in range( len( cntnr2.faces ) ):
    try:
      x = cntnr2.faces[i].getCentroid()
      face = cntnr1.faces.findAt( x, printWarning=False )
    except:
      face = cntnr1.faces[0:0]

    faces = faces + face
  
  return( faces )


#----------------------------------------

def checkFaceList( cntnr, chkFaces, idx, xyz, r ):

  result = 1
  edges = chkFaces[idx].getEdges()
  for i in range( len( edges ) ):
    if ( checkEdge(cntnr,edges[i],xyz,r) == 0 ):
      result = 0

  return result


#----------------------------------------

def getFacesList( cntnr, chkFaces, xyz, r ):

  bndFaces = cntnr.faces[0:0]
  for i in range( len( chkFaces ) ):
    if ( checkFaceList(cntnr,chkFaces,i,xyz,r) == 1 ):
      bndFaces = bndFaces + cntnr.faces.findAt( chkFaces[i].getCentroid(), printWarning=False )

  return( bndFaces )
