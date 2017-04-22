function [fc_max, fc_all, rawOut] = runSandwichInsert2D( inParms, dr )
%==========================================================================
%  Two Dimensional Sandwich Simulation
%    inParms:  Input Parameters - Geometry, Mat. Props., Failure Criteria
%    dr:       Discretization of FE Model
%    fc_max:   Output - Maximum Failure Criteria
%    fc_all:   Output - All Failure Criteria
%    rawOut:   Output - Raw Variable Output
%==========================================================================
global g_Load;

flclear fem

%dr = 1.e-5;
%inParms = [load, 7.125e-3, 10.e-3, 25.4e-3, 0.508e-3, 0.508e-3, 25.4e-3 ];
%inParms = [inParms, 17.3e9, 2.5e9, 408.e3, 310.e6, 138.e6 ];
%inParms = [inParms, 2.24e6, 0.95e6 ];

%  Geometry Parameters
r_ins = inParms(1);
r_pot = r_ins + inParms(2);
r_ext = inParms(3);
h_top = inParms(4);
h_bot = inParms(5);
h_cor = inParms(6);
l  = ( h_top + h_cor + h_bot );
A  = 2 * pi * r_ins * l;

%  Load Parameter
Q = g_Load;
P = Q / A;

%  Material Properties
%  Material 1 - Insert, Faces
E_f  = inParms(7);
nu_f = 0.3;

%  Material 2 - Potting
E_p  = inParms(8);
nu_p = 0.3;

%  Material 3 - Core
Ex_c = inParms(9);
Ey_c = Ex_c;
Ez_c = inParms(10);
nu_c12 = 0.49;
nu_c23 = 0;
nu_c13 = 0;
G_c  = inParms(11);


% Geometry
y_top = h_cor/2;
y_cor = -h_cor/2;
y_bot = -h_cor/2-h_bot;
gFSTop1 = rect2( r_pot-r_ins,h_top, 'base','corner', 'pos',[r_ins,y_top] );
gFSTop2 = rect2( r_ext-r_pot,h_top, 'base','corner', 'pos',[r_pot,y_top] );
gCore1  = rect2( r_pot-r_ins,h_cor, 'base','corner', 'pos',[r_ins,y_cor] );
gCore2  = rect2( r_ext-r_pot,h_cor, 'base','corner', 'pos',[r_pot,y_cor] );
gFSBot1 = rect2( r_pot-r_ins,h_bot, 'base','corner', 'pos',[r_ins,y_bot] );
gFSBot2 = rect2( r_ext-r_pot,h_bot, 'base','corner', 'pos',[r_pot,y_bot] );

clear s
s.objs={ gCore1, gCore2, gFSTop1, gFSTop2, gFSBot1, gFSBot2 };

fem.draw=struct('s',s);
[g,st,ft] = geomcsg(fem);
[SubInd,s0] = find(st);                         
fem.geom=g;

SubAll = ones( 1, size(st,1) );                                         %  Used to assign values to all 
BndAll = ones( 1, size(ft,1) );                                         %  subdomains, boundaries, and points

% Create mapped quad mesh
%edg1 = 0:(1/5):1;
%edg2 = 0:(1/125):1;
%edg3 = 0:(1/5):1;
%edg4 = 0:(1/28):1;
%edg5 = 0:(1/250):1;
edg1 = 0:(1/3):1;
edg2 = 0:(1/60):1;
edg3 = 0:(1/3):1;
edg4 = 0:(1/14):1;
edg5 = 0:(1/125):1;
fem.mesh = meshmap( fem, 'edgelem',{1,edg1, 3,edg2, 5,edg3, 2,edg4, 9,edg5}, 'hauto',5 );

%  Add Structural Axial Symmetry Application Mode
clear appl
appl.mode.class = 'SmeAxialSolid';
appl.mode.type = 'axi';
appl.module = 'SME';
appl.gporder = 4;
appl.cporder = 2;
appl.assignsuffix = '_smaxi';

%  Apply Boundary Conditions
clear bnd
bnd.constrcond = {'free','displacement','displacement'};
bnd.Hr = {0,1,0};
bnd.Fz = {0,P,0};
bnd.Hz = {0,0,1};
bnd.ind = [2,1,2,1,2,1,1,1,1,1,1,1,1,1,3,3,3];
appl.bnd = bnd;

%  Add Material Properties to fem
clear equ
equ.materialmodel = {'iso','iso','ortho'};
equ.dampingtype = 'nodamping';
equ.Er   = { 1, 1, Ex_c };
equ.Ephi = { 1, 1, Ey_c };
equ.Ez   = { 1, 1, Ez_c };
equ.nurphi = { 0, 0, nu_c12 };
equ.nuphiz = { 0, 0, nu_c23 };
equ.nurz   = { 0, 0, nu_c13 };
equ.Grz = { 0, 0, G_c };
equ.E = { E_f, E_p, 1 };
equ.nu = { nu_f, nu_p, 0 };
equ.ind(SubInd) = [2,3,1,1,1,1];
appl.equ = equ;

%  Set up FEM
fem.appl{1} = appl;
fem.sdim = {'r','z'};
fem.frame = {'ref'};
fem.border = 1;

clear units;
units.basesystem = 'SI';
fem.units = units;

%  Multiphysics, Extend Mesh, Solve
fem=multiphysics(fem);
fem.xmesh=meshextend(fem);
fem.sol=femstatic( fem, 'solcomp',{'w','uor'}, 'outcomp',{'w','uor'}, 'linsolver','spooles' );
fem0=fem;


%==========================================================================
%   Failure Criteria
%==========================================================================

%==========================================================================
%  Top Face - Tsai Wu
s1 = ( posteval( fem, 'sr_smaxi',   'Dl', SubInd(3:4) ) ).d;
s2 = ( posteval( fem, 'sphi_smaxi', 'Dl', SubInd(3:4) ) ).d;

s2t = 475.e6;
s2c = 375.e6;
s2b = 425.e6;
F2  = 1/s2t - 2/s2c;
F22 = 1/s2t/s2c;
F12 = 1/2 / s2b^2 * ( 1 - 2*s2b*F2 - 2*s2b^2*F22 );

fail_ft = max( abs( F2*(s1+s2) + F22*(s1.^2+s2.^2) + 2*F12*s1.*s2 ) ) - 1;
clear( 's1', 's2');

%==========================================================================
%  Bottom Face - Tsai Wu
s1 = ( posteval( fem, 'sr_smaxi',   'Dl', SubInd(5:6) ) ).d;
s2 = ( posteval( fem, 'sphi_smaxi', 'Dl', SubInd(5:6) ) ).d;

F2  = 1/s2t - 2/s2c;
F22 = 1/s2t/s2c;
F12 = 1/2 / s2b^2 * ( 1 - 2*s2b*F2 - 2*s2b^2*F22 );

fail_fb = max( abs( F2*(s1+s2) + F22*(s1.^2+s2.^2) + 2*F12*s1.*s2 ) ) - 1;
clear( 's1', 's2');

%==========================================================================
%  Core - Collapse Envelope
sc_fail = inParms(12);
st_fail = inParms(13);

x = (r_pot+dr):dr:r_ext;
y = (y_top/2) * ones(size(x));
pt = [x;y];
pb = [x;-y];
sct = min( 2*postinterp(fem,'sz_smaxi',pt), 0 );
scb = min( 2*postinterp(fem,'sz_smaxi',pb), 0 );
stt = postinterp(fem,'srz_smaxi',pt);
stb = postinterp(fem,'srz_smaxi',pb);

fct = (sct./sc_fail).^2 + (stt./st_fail).^2 - 1;
fcb = (scb./sc_fail).^2 + (stb./st_fail).^2 - 1;

fail_c = max( max(fct), max(fcb) );
clear( 'sc', 'st' );

%==========================================================================
%  Potting - Von Mises
st = ( posteval( fem, 'mises_smaxi', 'Dl', SubInd(1) ) ).d;
st = max( abs( st ) );

st_fail = 59.e6;
fail_p = (st/st_fail)^2 - 1;
clear( 'st' );

%==========================================================================
%  Overall Failure Criteria - Max of 4 Above

fc_all = [ fail_ft, fail_fb, fail_c, fail_p ];
fc_max = max( fc_all );


