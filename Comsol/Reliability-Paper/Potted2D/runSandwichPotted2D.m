%function [fc_max, fc_all, rawOut] = runSandwichPotted2D( inParms, dr )
%==========================================================================
%  Two Dimensional Sandwich Simulation
%    inParms:  Input Parameters - Geometry, Mat. Props., Failure Criteria
%    dr:       Discretization of FE Model
%    fc_max:   Output - Maximum Failure Criteria
%    fc_all:   Output - All Failure Criteria
%    rawOut:   Output - Raw Variable Output
%==========================================================================
tic;

inParms = [1000, 7.125e-3, 10.e-3, 60.e-3, 0.508e-3, 0.508e-3, 9.e-3, 25.4e-3 ];
inParms = [inParms, 71.5e9, 0.3, 2.5e9, 0.3, 1, 1, 310.e6, 0, 0, 0, 138.e6 ];
inParms = [inParms, 414.e6, 427.e6, 2.24e6, 948.e3, 17.2e6 ];

flclear fem

%  Geometry Parameters
r_ins = inParms(2);
r_pot = inParms(3);
r_ext = inParms(4);
h_top = inParms(5);
h_bot = inParms(6);
h_ins = inParms(7); 
h_cor = inParms(8);
h_inm = h_cor - h_ins;
l  = ( h_top + h_cor + h_bot );
A  = 2 * pi * r_ins * 2*l;

%  Load Parameter
Q = inParms(1);
P = Q / pi / r_ins^2;

%  Material Properties
%  Material 1 - Insert, Faces
E_f  = inParms(9);
nu_f = inParms(10);

%  Material 2 - Potting
E_p  = inParms(11);
nu_p = inParms(12);

%  Material 3 - Core
Ex_c = inParms(13);
Ey_c = inParms(14);
Ez_c = inParms(15);
nu_c12 = inParms(16);
nu_c23 = inParms(17);
nu_c13 = inParms(18);
G_c  = inParms(19);

% Geometry
gPot1   = rect2( r_ins, h_inm, 'base', 'corner', 'pos', [0,h_bot] );
gPot2   = rect2( r_pot-r_ins, h_inm, 'base', 'corner', 'pos', [r_ins,h_bot] );
gPot3   = rect2( r_pot-r_ins, h_ins, 'base', 'corner', 'pos', [r_ins,h_bot+h_inm] );
gCore1  = rect2( r_ext-r_pot, h_ins, 'base', 'corner', 'pos', [r_pot,h_bot+h_inm] );
gCore2  = rect2( r_ext-r_pot, h_inm, 'base', 'corner', 'pos', [r_pot,h_bot] );
gIns1   = rect2( r_ins, h_ins, 'base', 'corner', 'pos', [0,h_bot+h_inm] );
gIns2   = rect2( r_ins, h_top, 'base', 'corner', 'pos', [0,h_bot+h_cor] );
gFSBot1 = rect2( r_ins, h_bot, 'base', 'corner', 'pos', [0,0] );
gFSBot2 = rect2( r_pot-r_ins, h_bot, 'base', 'corner', 'pos', [r_ins,0] );
gFSBot3 = rect2( r_ext-r_pot, h_bot, 'base', 'corner', 'pos', [r_pot,0] );
gFSTop1 = rect2( r_pot-r_ins, h_top, 'base', 'corner', 'pos', [r_ins,h_bot+h_cor] );
gFSTop2 = rect2( r_ext-r_pot, h_top, 'base', 'corner', 'pos', [r_pot,h_bot+h_cor] );

%  Analyze geometry
clear s
s.objs = { gCore1, gCore2, gPot1, gPot2, gPot3, gIns1, gIns2, gFSBot1,gFSBot2,gFSBot3, gFSTop1, gFSTop2 };
fem.draw=struct('s',s);
[g,st,ft] = geomcsg(fem);
[SubInd,s0] = find(st);  
                       
fem.geom=g;

%  Add Structural Axial Symmetry Application Mode
clear appl
appl.mode.class = 'SmeAxialSolid';
appl.mode.type = 'axi';
appl.module = 'SME';
appl.shape = { 'shlag(3,''uor'')', 'shlag(3,''w'')' };
appl.gporder = 6;
appl.cporder = 3;
appl.assignsuffix = '_smaxi';


%  Apply Boundary Conditions
clear bnd
bnd.Hz = {0,1,0};
bnd.constrcond = {'free','displacement','free'};
bnd.Fz = {0,0,P};
bnd.ind = ones(31,1);
bnd.ind([28:31]) = 2;
bnd.ind(9) = 3;
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
equ.ind(SubInd) = [3,3,2,2,2,1,1,1,1,1,1,1];


%  Set up fem
appl.equ = equ;
fem.appl{1} = appl;
fem.sdim = {'r','z'};
fem.frame = {'ref'};
fem.border = 1;
clear units;
units.basesystem = 'SI';
fem.units = units;

% Create mapped quad mesh
edg1 = 0:(1/5):1;
edg2 = 0:(1/45):1;
edg3 = 0:(1/37):1;
edg4 = 0:(1/5):1;
edg5 = 0:(1/28):1;
edg6 = 0:(1/12):1;
edg7 = 0:(1/200):1;
fem.mesh = meshmap( fem, 'edgelem',{1,edg1, 3,edg2, 5,edg3, 7,edg4, 2,edg5, 11,edg6, 20,edg7}, 'hauto',5 );

%  Multiphysics
fem=multiphysics(fem);

%  Extend Mesh and Solve
fem.xmesh = meshextend( fem );
fem.sol = femstatic( fem, 'linsolver','spooles' );

%==========================================================================
%   Failure Criteria
%==========================================================================
toc
tic
%==========================================================================
%  Top Face - Tsai Wu
s1_t = posteval( fem, 'sr_smaxi', 'Dl', SubInd(11:12) );
s2_t = posteval( fem, 'sphi_smaxi', 'Dl', SubInd(11:12) );
s1_t = s1_t.d;
s2_t = s2_t.d;

s1t = inParms(20);
s1c = inParms(21);
F1 = 1/s1t - 1/s1c
F11 = 1/s1t/s1c
aa = max(s1_t+s2_t)
bb = max(s1_t.^2+s2_t.^2)
fail_ft = max( F1 * (s1_t+s2_t) + F11 * (s1_t.^2 + s2_t.^2 ) ) - 1;
clear( 's1_t', 's2_t');

%==========================================================================
%  Bottom Face - Tsai Wu
s1_b = posteval( fem, 'sr_smaxi', 'Dl', SubInd(8:10) );
s2_b = posteval( fem, 'sphi_smaxi', 'Dl', SubInd(8:10) );
s1_b = s1_b.d;
s2_b = s2_b.d;

fail_fb = max( F1 * (s1_b+s2_b) + F11 * (s1_b.^2 + s2_b.^2 ) ) - 1;
clear( 's1_b', 's2_b');

%==========================================================================
%  Core - Collapse Envelope
sc_fail = inParms(22);
st_fail = inParms(23);

sc = posteval( fem, 'sz_smaxi', 'Dl', SubInd(1:2) );
sc = min( sc.d );
sc = min( sc, 0 );
st = posteval( fem, 'srz_smaxi', 'Dl', SubInd(1:2) );
st = max( abs( st.d) );

fail_c = (sc/sc_fail)^2 + (st/st_fail)^2 - 1;
clear( 'sc', 'st' );

%==========================================================================
%  Potting - Tresca
st = posteval( fem, 'srz_smaxi', 'Dl', SubInd(1:2) );
st = max( abs( st.d ) );

st_fail = inParms(24);

fail_p = (st/st_fail)^2 - 1;


%==========================================================================
%  Overall Failure Criteria - Max of 4 Above

fc_all = [ fail_ft, fail_fb, fail_c, fail_p ]
fc_max = max( fc_all );


