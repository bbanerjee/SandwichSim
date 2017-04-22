function [Pf,t] = Form( fc0, inDir, outDir, fname )
%==========================================================================
%  Form Simulation 
%    fc0:    Failure Criterion
%    inDir:  Directory Containing Performance Function
%    fname:  Data File Name
%    Pf:     Output - Probability of Failure
%    stats:  Output - Performance Values and Input Parameters
%    t:      Output - Time for Simulation
%==========================================================================
if nargin < 4, fname = 'Form'; end
if nargin < 3, outDir = 'Data'; end
if nargin < 2, inDir = pwd; end
if nargin < 1, error('Not enough input parameters'); end

global NN;
NN = 0;

addpath('./Utils');
addpath( inDir );
tic 

dfc_tol = 1.e-4;
dn_tol0 = 1.e-5;
dn_tol  = dn_tol0;
nmax = 1000;
n = 0;
dfc = 1;
dn = 1;
dx = 0.001;
inputs = getInputParms();
inMu = transpose( inputs(:,1) );                       
inSigma = transpose( inputs(:,2) );
inDistIdx = transpose( inputs(:,3) );

x = zeros( size(inMu) );
f0 = runTrial( norm2Dist(x,inMu,inSigma,inDistIdx) );

%  FORM Loop
while( (dfc > dfc_tol && dn > dn_tol)  && n < nmax )
    [df,f] = calcGradient( x, dx, fc0, inMu, inSigma, inDistIdx );
    x_i = min(10,1/norm(df)) * ( df * transpose(x) - f ) / norm(df) * df;
    dfc = norm( x_i - x );
    dn = abs(normCDF(norm(x_i)) - normCDF(norm(x)) );
    x = x_i;
    n = n + 1;
    n_CDF = normCDF(norm(x));
    dn_tol = min( dn_tol0, 1/1000*min(n_CDF, 1-n_CDF) );
    if( mod(n,100) == 0 )
      warning( strcat( num2str(n), ' iterations' ) );
    end
end

%  Calculate Probability of Failure, CoV
Pf = 1 - normCDF( norm( x ) );

%  Invert if mean value is in failure zone
if( f0(1) > fc0 )
  Pf = normCDF( norm(x) );
end

%  Save Results
t = toc;
fname = strcat( outDir, '/', fname, '.mat' );
save( fname, 'Pf', 'x', 't', 'NN',  '-mat' );

rmpath('./Utils');
rmpath( inDir );


%==========================================================================
%  Calculate the Perf. Fun. Gradient in Stand. Norm. Space
%==========================================================================
function [r,fc_out] = calcGradient( x0, dr, fc, mu, sig, dist )

dx = dr*diag(ones(size(x0)));
fc0 = runTrial( norm2Dist(x0,mu,sig,dist) );
for i = 1:length(x0)
    fc1 = runTrial( norm2Dist(x0+dx(i,:),mu,sig,dist) );
    r(i) = ( fc1(1) - fc0(1) ) / dr;
end

fc_out = fc0(1) - fc;


%==========================================================================
%  Get p from the Normal Cumulative Distribution Function
%==========================================================================
function [p] = normCDF( c )

p = 1/2 + 1/2 * erf( c / sqrt(2) );
