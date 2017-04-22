%function [ fc_max, fc_all, rawOut ] = runSandwichPotted( inParms, dr )
%==========================================================================
%  One Dimensional Sandwich Simulation with Potted Insert
%    inParms:  Input Parameters - Geometry, Mat. Props., Failure Criteria
%    dr:       Discretization of FE Model
%    fc_max:   Output - Maximum Failure Criteria
%    fc_all:   Output - All Failure Criteria
%    rawOut:   Output - Raw Variable Output
%==========================================================================

inParms = [1000, 7.125e-3, 10.e-3, 60.e-3, 0.508e-3, 0.508e-3, 9.e-3, 25.4e-3 ];
inParms = [inParms, 71.5e9, 0.3, 2.5e9, 2.5e9/2.6, 310.e6, 138.e6 ];
inParms = [inParms, 414.e6, 427.e6, 2.24e6, 948.e3, 17.2e6 ];
dr = 1.e-5;

flclear fem;

%  Geometry Parameters
r_0   = 0.e-8;
r_ins = inParms(2)/2;
r_pot = inParms(3)/2;
r_ext = inParms(4)/2;
h_top = inParms(5)/2;
h_bot = inParms(6)/2;
h_ins = inParms(7)/2;
h_cor = inParms(8)/2;
l = ( h_top + h_cor + h_bot );
A = 2 * pi  * 2*l;

%  Load Parameters
Q = inParms(1);
P = Q/A;
F = P*A;
q = Q / pi / r_ins^2;

Ef  = inParms(9);
nuf = inParms(10);
Ep  = inParms(11);
Gp  = inParms(12);
Ec  = inParms(13);
Gc  = inParms(14);

C11 = Ef/(1-nuf^2);
C12 = nuf*C11;
u_j = (h_ins-h_top)/2;
c_j = h_cor/(h_cor+h_top-h_ins);

%============================================
%  Governing Equations
% pde_T - Top Face
% pde_B - Bottom Face
% pde_C - Core
% pde_IT - Top Face - Insert
% pde_IB - Bottom Face - Insert
% pde_IC - Core - Insert
%============================================
pdeStart = '(I0*(';
pdeT1 = '+(A11*utx+A12/x*ut)*utx_test+1/x*(A12*utx+A11/x*ut)*ut_test';
pdeT2 = '+(D11*wtxx+D12/x*wtx)*wtxx_test+1/x*(D12*wtxx+D11/x*wtx)*wtx_test';
pdeQT = '-(-(C33/2/c*(wt-wb)-c*(srzx+1/x*srz)))*wt_test';
pdeMT = '-(-srz*(ut_test-ft*wtx_test))';

pdeB1 = '+(B11*ubx+B12/x*ub)*ubx_test+1/x*(B12*ubx+B11/x*ub)*ub_test';
pdeB2 = '+(E11*wbxx+E12/x*wbx)*wbxx_test+1/x*(E12*wbxx+E11/x*wbx)*wbx_test';
pdeQB = '-(+(C33/2/c*(wt-wb)+c*(srzx+1/x*srz)))*wb_test';
pdeMB = '-(+srz*(ub_test-fb*wbx_test))';

pdeC1 = '+srzx*srzx_test+(1/x^2+6*C33*S55/c^2)*srz*srz_test+1/x*(srz*srzx_test+srzx*srz_test)';
pdeC2 = '-3/2*C33/c^3*(ut-ub+(ft+c)*wtx+(fb+c)*wbx)*srz_test';
pdeI0 = '+uix*uix_test+(srzix*srzix_test)';
pdeMid = ') + I1 * (';

pdeIT1 = '+(A11*uix+A12/x*ui)*uix_test+1/x*(A12*uix+A11/x*ui)*ui_test';
pdeIT2 = '+(D11*wtxx+D12/x*wtx)*wtxx_test+1/x*(D12*wtxx+D11/x*wtx)*wtx_test';
pdeIQT = '-(-(C33/2/c*(wt-wb)-c*(srzix+1/x*srzi)))*wt_test-q*wt_test';
pdeIMT = '-(-srzi*(ui_test-ft*wtx_test))';

pdeIB1 = '+(B11*ubx+B12/x*ub)*ubx_test+1/x*(B12*ubx+B11/x*ub)*ub_test';
pdeIB2 = '+(E11*wbxx+E12/x*wbx)*wbxx_test+1/x*(E12*wbxx+E11/x*wbx)*wbx_test';
pdeIQB = '-(+(C33/2/c*(wt-wb)+c*(srzix+1/x*srzi)))*wb_test';  
pdeIMB = '-(+srzi*(ub_test-fb*wbx_test))';

pdeIC1 = '+srzix*srzix_test+(1/x^2+6*C33*S55/c^2)*srzi*srzi_test+1/x*(srzi*srzix_test+srzix*srzi_test)';
pdeIC2 = '-3/2*C33/c^3*(ui-ub+(ft+c)*wtx+(fb+c)*wbx)*srzi_test';
pdeI1 = '+utx*utx_test-(srzx*srzx_test)';
pdeEnd = '))*2*pi*x';

pdeT = strcat( pdeT1, pdeT2, pdeQT, pdeMT );
pdeB = strcat( pdeB1, pdeB2, pdeQB, pdeMB );
pdeC = strcat( pdeC1, pdeC2, pdeI0 );
pdeIT = strcat( pdeIT1, pdeIT2, pdeIQT, pdeIMT );
pdeIB = strcat( pdeIB1, pdeIB2, pdeIQB, pdeIMB );
pdeIC = strcat( pdeIC1, pdeIC2, pdeI1 );
pde  = strcat( pdeStart, pdeT, pdeB, pdeC, pdeMid, pdeIT, pdeIB, pdeIC, pdeEnd );

% Geometry
gIns  = solid1([r_0,  r_ins]);
gPot  = solid1([r_ins,r_pot]);
gCore = solid1([r_pot,r_ext]);

% Analyzed geometry
clear s
s.objs = { gIns, gPot, gCore };
s.name = { 'Insert', 'Potting', 'Core' };
s.tags = { 'gIns', 'gPot', 'gCore' };

fem.draw=struct('s',s);
[g,st] = geomcsg(fem);
[SubInd,s0] = find(st);                         
fem.geom=g;

SubAll = ones( 1, size(st,1) );                                         

% PDE Mode
clear appl
appl.mode.class = 'FlPDEW';
appl.dim = { 'ui',   'ut',   'wt',   'ub',   'wb',   'srz',   'srzi', ...
	     'ui_t', 'ut_t', 'wt_t', 'ub_t', 'wb_t', 'srz_t', 'srzi_t' };
appl.shape = { 'shlag(2,''ui'')', 'shlag(2,''ut'')', 'shherm(3,''wt'')', 'shlag(2,''ub'')', 'shherm(3,''wb'')', ...
	       'shlag(2,''srz'')', 'shlag(2,''srzi'')'};
appl.gporder = {4,6};
appl.cporder = {2,3};
appl.border = 'on';
appl.assignsuffix = '_w';

clear bnd
bnd.constr = { {'-wtx';'-wbx';'-ui';'-ub';'srzi';'0';'0'}, {'ui-uj*wtx-ut';'(srzi-cj*srz)';'0';'0';'0';'0';'0'}, ...
	       {0}, {'-wt';'-wb';'0';'0';'0';'0';'0'} };
bnd.weak = { {0}, {'-2*pi*x*((srz+x*srzx)*srzi_test+(srzi+x*srzix)*srz_test)','0','0','0','0','0','0'}, {0}, {0} };
bnd.weak = { {0}, {0}, {0}, {0} };
bnd.ind = [1,2,3,4];
appl.bnd = bnd;


clear equ
equ.weak = pde;
equ.dweak = 0;
equ.ind = SubAll;
equ.gporder = {{1;1;2;1;2;1;1}};
equ.cporder = {{1;1;2;1;2;1;1}};
appl.equ = equ;

%===================================================
%  Equation Constants
%===================================================
r_i = h_ins/h_top;
A11 = 2 * C11 * h_top;
A12 = nuf * A11;
D11 = 2/3 * C11 * h_top^3;
D12 = nuf * D11;
B11 = 2 * C11 * h_bot;
B12 = nuf * B11;
E11 = 2/3 * C11 * h_bot^3;
E12 = nuf * E11;
%====================================================

clear equ
equ.dim = { 'ui','ut','wt','ub','wb','srz','srzi' };
equ.expr = { 'ft',{h_ins,h_top,h_top}, 'fb',{h_bot,h_bot,h_bot}, 'c',{h_cor+h_top-h_ins,h_cor,h_cor}, ...
	     'C33',{Ep,Ep,Ec}, 'S55',{0.5/Gp,0.5/Gp,0.5/Gc}, ...
	     'A11',{A11*r_i,A11,A11}, 'A12',{A12*r_i,A12,A12}, 'D11',{D11*r_i^3,D11,D11}, 'D12',{D12*r_i^3,D12,D12} , ...
	     'B11',{B11,B11,B11}, 'B12',{B12,B12,B12}, 'E11',{E11,E11,E11},'E12',{E12,E12,E12} , ...
	     'q',{q,0,0}, 'I0',{0,1,1}, 'I1',{1,0,0} };
equ.ind = [1,2,3];
fem.equ = equ;

clear units;
units.basesystem = 'SI';
fem.units = units;
fem.appl{1} = appl;
fem.frame = {'ref'};
fem.border = 1;

fem.const = { 'uj', u_j, 'cj', c_j, 'l', l, 'A', A, 'P', P, 'F',F };

fem.mesh=meshinit( fem );
fem.mesh=meshrefine( fem, 'mcase',0 );
fem.mesh=meshrefine( fem, 'mcase',0 );
fem.mesh=meshrefine( fem, 'mcase',0 );
fem.mesh=meshrefine( fem, 'mcase',0 );

fem = multiphysics( fem );
fem.xmesh = meshextend( fem );

fem.sol=femstatic(fem);
fem0=fem;

%==========================================================================
%   Failure Criteria
%==========================================================================

%==========================================================================
%  Top Face - Tsai Wu
r = r_ins:dr:r_ext;
u = postinterp( fem, 'ut', r );
w = postinterp( fem, 'wt', r );
ur = postinterp( fem, 'utx', r );
wr = postinterp( fem, 'wtx', r );
wrr = postinterp( fem, 'wtxx', r );

s1t = inParms(15);
s1c = inParms(16);
F1 = 1/s1t - 1/s1c;
F11 = 1/s1t/s1c;

s1_b = C11 * ( ur + h_top*wrr ) + C12 * ( u./r + h_top*wr./r );
s1_t = C11 * ( ur - h_top*wrr ) + C12 * ( u./r - h_top*wr./r );
s2_b = C12 * ( ur + h_top*wrr ) + C11 * ( u./r + h_top*wr./r );
s2_t = C12 * ( ur - h_top*wrr ) + C11 * ( u./r - h_top*wr./r );

%max(s1_b.^2+s2_b.^2)
max(s1_b)
max(s2_b)


fail_b = max( F1 * (s1_b+s2_b) + F11 * (s1_b.^2 + s2_b.^2 ) );
fail_t = max( F1 * (s1_t+s2_t) + F11 * (s1_t.^2 + s2_t.^2 ) );

fail_ft = max( fail_t, fail_b ) - 1;


%==========================================================================
%  Bottom Face - Tsai Wu
r = r_0:dr:r_ext;
u = postinterp( fem, 'ub', r );
ur = postinterp( fem, 'ubx', r );
wr = postinterp( fem, 'wbx', r );
wrr = postinterp( fem, 'wbxx', r );

s1t = inParms(15);
s1c = inParms(16);
F1 = 1/s1t - 1/s1c
F11 = 1/s1t/s1c

s1_b = C11 * ( ur + h_bot*wrr ) + C12 * ( u./r + h_bot*wr./r );
s1_t = C11 * ( ur - h_bot*wrr ) + C12 * ( u./r - h_bot*wr./r );
s2_b = C12 * ( ur + h_bot*wrr ) + C11 * ( u./r + h_bot*wr./r );
s2_t = C12 * ( ur - h_bot*wrr ) + C11 * ( u./r - h_bot*wr./r );

fail_b = max( F1 * (s1_b+s2_b) + F11 * (s1_b.^2 + s2_b.^2 ) );
fail_t = max( F1 * (s1_t+s2_t) + F11 * (s1_t.^2 + s2_t.^2 ) );

fail_fb = max( fail_t, fail_b ) - 1;


%==========================================================================
%  Core - Collapse Envelope
r = r_pot:dr:r_ext;
wt = postinterp( fem, 'wt', r );
wb = postinterp( fem, 'wb', r );
srz = postinterp( fem, 'srz', r );
srzr = postinterp( fem, 'srzx', r );

sc_fail = inParms(17);
st_fail = inParms(18);

sc_t = 1/2/h_cor/Ec * ( wt - wb ) - h_cor * (srzr + srz./r );
sc_b = 1/2/h_cor/Ec * ( wt - wb ) + h_cor * (srzr + srz./r );

sc = min( sc_t, sc_b );
sc = min( sc, 0 );
sc = min( sc );

st = max( abs(srz) );

fail_c = (sc/sc_fail)^2 + (st/st_fail)^2 - 1;


%==========================================================================
%  Potting - Tresca
r1 = r_ins:dr:r_pot;
r2 = r_0:dr:r_ins;
srz1 = postinterp( fem, 'srz', r );
srz2 = postinterp( fem, 'srzi', r );

st_fail = inParms(19);
st1 = max(abs(srz1));
st2 = max(abs(srz2));
st = max(st1,st2);

fail_p = (st/st_fail)^2 - 1;


%==========================================================================
%  Overall Failure Criteria - Max of 4 Above

fc_all = [ fail_ft, fail_fb, fail_c, fail_p ]
fc_max = max( fc_all );


%==========================================================================
%  Output Raw Data
r = r_ins:dr:r_ext;
ut = postinterp( fem, 'ut', r );
wt = postinterp( fem, 'wt', r );
utr = postinterp( fem, 'utx', r );
wtr = postinterp( fem, 'wtx', r );
wtrr = postinterp( fem, 'wtxx', r );

ub = postinterp( fem, 'ub', r );
wb = postinterp( fem, 'wb', r );
ubr = postinterp( fem, 'ubx', r );
wbr = postinterp( fem, 'wbx', r );
wbrr = postinterp( fem, 'wbxx', r );

srz = postinterp( fem, 'srz', r );
srzr = postinterp( fem, 'srzx', r );

rawOut = [r;ut;wt;utr;wtr;wtrr;ub;wb;ubr;wbr;wbrr;srz;srzr];

