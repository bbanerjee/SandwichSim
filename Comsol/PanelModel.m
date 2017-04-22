function [maxez,maxezloc] = PanelModel( AdhEz, Pappl, nRefine )
%  Solves for the maximum strain in a composite panel
%  AdhEz = Youngs modulus of the thin adhesive layer
%  Pappl = Applied Pressure
%  nRefine = Number of mesh refinements

flclear fem                                     %  Clear the finite element structure

Pappl = Pappl * 1.0e6;                          %  Put Pappl in Pa

%  Material Properties
%  Material 1 - Insert
e1   = 210e9;
nu1  = 0.3;
grz1 = 7.52e10;

%  Material 2 - Potting
e2   = 890e6;
nu2  = 0.3;
grz2 = 1.5e8;

%  Material 3 - Core
er3     = 0.34e6;
ephi3   = 0.48e6;
ez3     = 132.0e6;
nurphi3 = 0.49;
nurz3   = 2.576e-5;
nuphiz3 = 3.636e-5;
grz3    = 24.1e6;

%  Material 4 - Face Sheets
er4     = 17.3e9;
ephi4   = 17.3e9;
ez4     = 3.24e9;
nurphi4 = 0.3;
nurz4   = 0.32;
nuphiz4 = 0.32;
grz4    = 1.2e9;

%  Material 5 - Adhesive Layer
e5   = AdhEz * 1.0e6;
nu5  = 0.3;
grz5 = 1.5e6;


%  Geometry Properties
hf = 0.508e-3;		% Face Sheet Thickness		(m)
hc = 25.4e-3;	        % Core Thickness		(m)
hi = 9.52e-3;		% Insert Height			(m)
hp = 13e-3;		% Potting Depth	        	(m)

ri = 7.125e-3;		% Insert Radius			(m)
rp = 10.0e-3;		% Effective Potting Radius	(m)
rs = 25.4e-3;		% Support Ring Radius		(m)
ro = 35.0e-3;		% Outer Panel Radius		(m)

ta = 0.5e-3;            % Adhesive Layer Thickness      (m)
flt = 0.5e-3;		% Fillet Radius			(m)


% Geometry
g1 = rect2( ro, hc, 'base', 'corner', 'pos', [0,-hc] );
g2 = rect2( rp+ta, hp+ta, 'base', 'corner', 'pos', [0,-hp-ta] );
g3 = fillet( g2, 'radii', flt, 'point', [2] );
g4 = rect2( rp, hp, 'base', 'corner', 'pos', [0,-hp] );
g5 = fillet( g4, 'radii', flt, 'point', [2] );
g6 = rect2( ri, hi+hf, 'base', 'corner', 'pos', [0,-hi] );
g7 = fillet( g6, 'radii', flt, 'point', [2] );

gCore   = geomcomp( {g1,g3}, 'ns', {'g1','g3'}, 'sf', 'g1-g3', 'edge', 'none' );
gAdv    = geomcomp( {g3,g5}, 'ns', {'g3','g5'}, 'sf', 'g3-g5', 'edge', 'none' );
gPot    = geomcomp( {g5,g7}, 'ns', {'g5','g7'}, 'sf', 'g5-g7', 'edge', 'none' );
gIns    = fillet( g6, 'radii', flt, 'point', [2] );
gFSBot  = rect2( ro, hf, 'base', 'corner', 'pos', [0,-hc-hf] );
gFSTop1 = rect2( rs-ri, hf, 'base', 'corner', 'pos', [ri,0] );
gFSTop2 = rect2( ro-rs, hf, 'base', 'corner', 'pos', [rs,0] );


%  Analyze geometry
clear s
s.objs = { gCore, gAdv, gPot, gIns, gFSBot, gFSTop1, gFSTop2 };
s.name = { 'Core', 'Adhesive', 'Potting', 'Insert', 'FSBottom', 'FSTop1', 'FSTop2' };
s.tags = { 'gCore', 'gAdv', 'gPot', 'gIns', 'gFSBot', 'gFSTop1', 'gFSTop2' };
fem.draw=struct('s',s);
fem.geom=geomcsg(fem);


%  Add Structural Axial Symmetry Application Mode
clear appl
appl.mode.class = 'SmeAxialSolid';
appl.mode.type = 'axi';
appl.module = 'SME';
appl.gporder = 4;
appl.cporder = 2;
appl.assignsuffix = '_smaxi';


%  Turn on Large Deformation Property
clear prop
prop.largedef='on';
appl.prop = prop;


%  Apply Boundary Conditions
clear bnd
bnd.Hz = {0,1,0};
bnd.constrcond = {'free','displacement','free'};
bnd.Fz = {0,0,Pappl};
bnd.ind = [1,1,1,1,1,1,1,1,1,1,3,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1];
appl.bnd = bnd;


%  Add Material Properties to fem
clear equ
equ.materialmodel = {'iso','iso','ortho','ortho','iso'};
equ.Er   = { e1, e2, er3,   er4,   e5 };
equ.Ephi = { e1, e2, ephi3, ephi4, e5 };
equ.Ez   = { e1, e2, ez3,   ez4,   e5 };
equ.nurphi = { nu1, nu2, nurphi3, nurphi4, nu5 };
equ.nuphiz = { nu1, nu2, nuphiz3, nuphiz4, nu5 };
equ.nurz   = { nu1, nu2, nurz3,   nurz4,   nu5 };
equ.Grz = { grz1, grz2, grz3, grz4, grz5 };
equ.E = { e1, e2, ephi3, er4, e5 };
equ.nu = { nu1, nu2, nurz3, nurz4, nu5 };
equ.ind = [4,3,5,2,1,4,4];


%  Set up fem
appl.equ = equ;
fem.appl{1} = appl;
fem.sdim = {'r','z'};
fem.frame = {'ref'};
fem.border = 1;
clear units;
units.basesystem = 'SI';
fem.units = units;


%  Multiphysics
fem=multiphysics(fem);

%  Initialize mesh
fem.mesh = meshinit( fem );

%  Refine Mesh
if( nRefine )
  for ref = 1:nRefine;
    fem.mesh=meshrefine( fem, 'mcase', 0, 'rmethod', 'regular' );
  end
end


%  Extend Mesh and Solve
fem.xmesh=meshextend( fem );
fem.sol = femstatic( fem );


%  Get Maximum Strain and Location
[maxez,maxezloc] = postmax( fem,'ez_smaxi' );
