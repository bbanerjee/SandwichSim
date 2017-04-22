function [ fc_max, fc_all, rawOut ] = runSandwichInsert1D( inParms, dr )
%==========================================================================
%  One Dimensional Sandwich Simulation with Through the Thickness Insert
%    inParms:  Input Parameters - Geometry, Mat. Props., Failure Criteria
%    dr:       Discretization of FE Model
%    fc_max:   Output - Maximum Failure Criteria
%    fc_all:   Output - All Failure Criteria
%    rawOut:   Output - Raw Variable Output
%==========================================================================

global g_Load;

flclear fem;

%inParms = [7.125e-3, 2.875e-3, 25.4e-3, 0.508e-3, 25.4e-3 ];
%inParms = [inParms, 17.3e9, 890.e6, 132.e6, 33.e6, 2.24e6, 0.95e6 ];
%dr = 1.e-5;

%  Geometry Parameters
r_ins = inParms(1);
r_pot = inParms(2) + r_ins;
r_ext  = inParms(3);
f  = inParms(4)/2;
c  = inParms(5)/2;
l  = ( f + c + f );
A  = 2 * pi * r_ins * 2*l;


%  Load Parameters
Q = g_Load;
P = Q/A;
F = Q;


%  Material Properties
Ef  = inParms(6);
nuf = 0.3;
Ep  = inParms(7);
Gp  = 3.4e8;
Ec  = inParms(8);
Gc  = inParms(9);

C11 = Ef/(1-nuf^2);
C12 = nuf*C11;
A11 = 2*f*C11;
A12 = nuf*A11;
D11 = 2*f^3/3*C11;
D12 = nuf*D11;


%  Governing Equations
pdeStart = '(';
pdeT1 = '+(A11*utx+A12/x*ut)*utx_test+1/x*(A12*utx+A11/x*ut)*ut_test';
pdeT2 = '+(D11*wtxx+D12/x*wtx)*wtxx_test+1/x*(D12*wtxx+D11/x*wtx)*wtx_test';
pdeQT = '-(C33/2/c*(wt-wb)-c*(srzx+1/x*srz))*wt_test';
pdeMT = '+srz*ut_test-ft*srz*wtx_test';

pdeB1 = '+(A11*ubx+A12/x*ub)*ubx_test+1/x*(A12*ubx+A11/x*ub)*ub_test';
pdeB2 = '+(D11*wbxx+D12/x*wbx)*wbxx_test+1/x*(D12*wbxx+D11/x*wbx)*wbx_test';
pdeQB = '-(C33/2/c*(wb-wt)-c*(srzx+1/x*srz))*wb_test';  
pdeMB = '-srz*ub_test-fb*srz*wbx_test';

pdeC1 = '-srzx*srzx_test-(1/x^2-6*C33*S55/c^2)*srz*srz_test-1/x*(srz*srzx_test+srzx*srz_test)';
pdeC2 = '-3/2*C33/c^3*(ut-ub+(ft+c)*wtx+(fb+c)*wbx)*srz_test';
pdeEnd = ')*2*pi*x';

pdeT = strcat( pdeT1, pdeT2, pdeQT, pdeMT );
pdeB = strcat( pdeB1, pdeB2, pdeQB, pdeMB );
pdeC = strcat( pdeC1, pdeC2 );
pde  = strcat( pdeStart, pdeT, pdeB, pdeC, pdeEnd );


% Geometry
gPot  = solid1([r_ins,r_pot]);
gCore = solid1([r_pot,r_ext]);


% Analyzed geometry
clear s
s.objs = { gPot, gCore };
s.name = { 'Potting', 'Core' };
s.tags = { 'gPot', 'gCore' };

fem.draw=struct('s',s);
[g,st] = geomcsg(fem);
fem.geom=g;
SubAll = ones( 1, size(st,1) );


% PDE Mode
clear appl
appl.mode.class = 'FlPDEW';
appl.dim = {'ut','wt','ub','wb','srz','ut_t','wt_t','ub_t','wb_t','srz_t'};
appl.shape = {'shlag(2,''ut'')','shherm(3,''wt'')','shlag(2,''ub'')','shherm(3,''wb'')','shlag(2,''srz'')'};
appl.gporder = {4,6};
appl.cporder = {2,3};
appl.assignsuffix = '_w';


%  Boundary Conditions
clear bnd
bnd.constr = {{'srz+P';'-ut';'-ub';'0';'0'},{0},{'-wt';'-wb';'0';'0';'0'}};
bnd.weak = { {'F*ft/l*wt_test+F*fb/l*wb_test';'0';'0';'0';'0'}, {0}, {0} };
bnd.ind = [1,2,3];
appl.bnd = bnd;


%  Subdomain Equation Settings
clear equ
equ.weak = pde;
equ.dweak = 0;
equ.ind = SubAll;
equ.gporder = {{1;2;1;2;1}};
equ.cporder = {{1;2;1;2;1}};
appl.equ = equ;


%  Subdomain Variable Settings
clear equ
equ.dim = {'ut','wt','ub','wb','srz'};
equ.expr = { 'A11',{A11,A11}, 'A12',{A12,A12}, 'D11',{D11,D11}, 'D12',{D12,D12}, 'ft',{f,f}, 'fb',{f,f}, ...
    	     'c',{c,c}, 'C33',{Ep,Ec}, 'S55',{1/2/Gp,1/2/Gc} };
equ.ind = [1,2];
fem.equ = equ;


%  Constants
fem.const = {'P',P,'l',l,'F',F};


%  Setup and Solve
clear units;
units.basesystem = 'SI';
fem.units = units;
fem.appl{1} = appl;
fem.frame = {'ref'};
fem.border = 1;

fem.mesh=meshinit( fem );
fem.mesh=meshrefine( fem, 'mcase',0 );
fem.mesh=meshrefine( fem, 'mcase',0 );
fem.mesh=meshrefine( fem, 'mcase',0 );
fem.mesh=meshrefine( fem, 'mcase',0 );

fem = multiphysics( fem );
fem.xmesh = meshextend( fem );

fem.sol=femstatic(fem, ...
                  'solcomp',{'wt','wb','ut','ub','srz','wtx','wbx'}, ...
                  'outcomp',{'wt','wb','ut','ub','srz','wtx','wbx'});


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

s2t = 475.e6;
s2c = 375.e6;
s2b = 425.e6;
F2 = 1/s2t - 1/s2c;
F22 = 1/s2t/s2c;
F12 = 1/2 / s2b^2 * ( 1 - 2*s2b*F2 - 2*s2b^2*F22 );

s1_b = C11 * ( ur + f*wrr ) + C12 * ( u./r + f*wr./r );
s1_t = C11 * ( ur - f*wrr ) + C12 * ( u./r - f*wr./r );
s2_b = C12 * ( ur + f*wrr ) + C11 * ( u./r + f*wr./r );
s2_t = C12 * ( ur - f*wrr ) + C11 * ( u./r - f*wr./r );

fail_b = max( F2*(s1_b+s2_b) + F22*(s1_b.^2 + s2_b.^2 ) + 2*F12*s1_b.*s2_b );
fail_t = max( F2*(s1_t+s2_t) + F22*(s1_t.^2 + s2_t.^2 ) + 2*F12*s1_t.*s2_t );

fail_ft = max( abs(fail_t), abs(fail_b) ) - 1;


%==========================================================================
%  Bottom Face - Tsai Wu
r = r_ins:dr:r_ext;
u = postinterp( fem, 'ub', r );
ur = postinterp( fem, 'ubx', r );
wr = postinterp( fem, 'wbx', r );
wrr = postinterp( fem, 'wbxx', r );

s1_b = C11 * ( ur + f*wrr ) + C12 * ( u./r + f*wr./r );
s1_t = C11 * ( ur - f*wrr ) + C12 * ( u./r - f*wr./r );
s2_b = C12 * ( ur + f*wrr ) + C11 * ( u./r + f*wr./r );
s2_t = C12 * ( ur - f*wrr ) + C11 * ( u./r - f*wr./r );

fail_b = max( F2*(s1_b+s2_b) + F22*(s1_b.^2 + s2_b.^2 ) + 2*F12*s1_b.*s2_b );
fail_t = max( F2*(s1_t+s2_t) + F22*(s1_t.^2 + s2_t.^2 ) + 2*F12*s1_t.*s2_t );

fail_fb = max( abs(fail_t), abs(fail_b) ) - 1;


%==========================================================================
%  Core - Collapse Envelope
r = r_pot:dr:r_ext;
wt = postinterp( fem, 'wt', r );
wb = postinterp( fem, 'wb', r );
srz = postinterp( fem, 'srz', r );
srzr = postinterp( fem, 'srzx', r );

sc_fail = inParms(10);
st_fail = inParms(11);

sc_t = 1/2/c/Ec * ( wt - wb ) - c * (srzr + srz./r );
sc_b = 1/2/c/Ec * ( wt - wb ) + c * (srzr + srz./r );

fct = (sc_t./sc_fail).^2 + (srz./st_fail).^2 - 1;
fcb = (sc_b./sc_fail).^2 + (srz./st_fail).^2 - 1;

fail_c = max( max(fct), max(fcb) );


%==========================================================================
%  Potting - Von Mises
r = r_ins:dr:r_pot;
wt = postinterp( fem, 'wt', r );
wb = postinterp( fem, 'wb', r );
srz = postinterp( fem, 'srz', r );
srzr = postinterp( fem, 'srzx', r );
sc_t = 1/2/c/Ep * ( wt - wb ) - c * (srzr + srz./r );
sc_b = 1/2/c/Ep * ( wt - wb ) + c * (srzr + srz./r );

st_t = sqrt( sc_t.^2 + 3*srz.^2 );
st_b = sqrt( sc_b.^2 + 3*srz.^2 );

st = max( max(st_t), max(st_b) );
st_fail = 59.e6;

fail_p = (st/st_fail)^2 - 1;


%==========================================================================
%  Overall Failure Criteria - Max of 4 Above

fc_all = [ fail_ft, fail_fb, fail_c, fail_p ];
fc_max = max( fc_all );

global rawOut;
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

E = Ep*(r<r_pot) + Ec*(r>=r_pot);
sc_t = -1/2/c./E .* ( wt - wb ) - c * (srzr + srz./r );

rawOut = [r;ut;wt;utr;wtr;wtrr;ub;wb;ubr;wbr;wbrr;srz;srzr];
