""" slabGeom - a module of slab geometry features"""

import math
from math import *
import part
import assembly

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def getCorners( lx, nx, ny ):

  s = lx*sin(pi/3)
  c = lx*cos(pi/3)

  centers = []
  for jj in range(ny):
    for ii in range(nx):
      x0 = ii*2*(lx+c)
      y0 = jj*2*s+s
      centers.append( (x0,y0,0) )

  for jj in range(ny-1):
    for ii in range(nx-1):
      x0 = ii*2*(lx+c) + lx+c
      y0 = jj*2*s+s + s
      centers.append( (x0,y0,0) )

  return centers


def getLines( x0, lx ):
  xc = (x0[0]+lx,x0[1])
  
  x = []
  for ii in range(7):
    x.append( ( xc[0]+lx*cos(ii*pi/3), xc[1]+lx*sin(ii*pi/3) ) )

  lines = []
  for ii in range(6):
    lines.append( [ x[ii], x[ii+1] ] )

  return lines


def getVertices( x0, lx ):
  xc = ( x0[0]+lx, x0[1] )  
  x = []
  for ii in range(6):
    x.append( ( xc[0]+lx*cos(ii*pi/3), xc[1]+lx*sin(ii*pi/3) ) )
  return x


def getMinDist( pt0, vtxs ):
  dMin = 1.e6

  for i in range( len(vtxs) ):
    dist = getDist( pt0, vtxs[i] )
    if ( dist < dMin ):
      dMin = dist
  return dMin


def getDist( pt1, pt2 ):

  dx = pt1[0] - pt2[0]
  dy = pt1[1] - pt2[1]

  dist = math.sqrt( dx*dx + dy*dy )
  return dist 

