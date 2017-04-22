function [Pf, stats, t] = LineSamp( fc0, N, inDir, outDir, fname )
%==========================================================================
%  [Pf, stats, t] = LineSamp( fc0, N, inDir, fname )
%  Line Sampling Simulation 
%    fc0:    Failure Criterion
%    N:      Number of Samples
%    inDir:  Directory Containing Performance Function
%    fname:  Data File Name
%    Pf:     Output - Probability of Failure
%    stats:  Output - Performance Values and Input Parameters
%    t:      Output - Time for Simulation
%==========================================================================
if nargin < 5, fname = 'LineSamp'; end
if nargin < 4, outDir = 'Data'; end
if nargin < 3, inDir = pwd; end
if nargin < 2, error('Not enough input parameters'); end

global NN;
NN = 0;

addpath('./Utils');
addpath( inDir );
tic 

dr = 0.01;
inputs = getInputParms();
inMu = transpose( inputs(:,1) );                       
inSigma = transpose( inputs(:,2) );
inDistIdx = transpose( inputs(:,3) );

%  Find Important Direction
x0 = zeros( size(inMu) );
f0 = runTrial( norm2Dist(x0,inMu,inSigma,inDistIdx) );
r = calcGradient( x0, dr, inMu, inSigma, inDistIdx );
r = r / norm(r);
dr = 0.001;

%  Find Distance in Important Direction
[x0,fc,n] = calcNewton( x0, r, dr, fc0, inMu, inSigma, inDistIdx );
c0 = norm(x0);
stats(1,:) = [ normCDF(c0), fc, norm2Dist(x0,inMu,inSigma,inDistIdx), n ];

%  Reduced Dimension Monte Carlo Sampling
for i = 2:N
    x_i = 2 * ( rand( size(x0) ) - 0.5 );
    x_i = x_i - ( x_i*transpose(r) ) * r;
    x_i = x_i * randn(1)/norm(x_i);
    x = x_i + c0 * r;

    [x,fc,n] = calcNewton( x, r, dr, fc0, inMu, inSigma, inDistIdx );
    c_i = norm( x-x_i );
    stats(i,:) = [ normCDF(c_i), fc, norm2Dist(x,inMu,inSigma,inDistIdx), n ];
end

%  Calculate Probability of Failure, CoV
if( f0(1) > fc0 )
  vPf = stats(:,1);
else
  vPf = 1 - stats(:,1);
end

Pf(1) = sum(vPf) / length(vPf);
Pf(2) = std(vPf) / Pf(1);



%  Save Results
t = toc;
fname = strcat( outDir, '/', fname, '.mat' );
save( fname, 'stats', 'Pf', 't', 'NN', '-mat' );

rmpath('./Utils');
rmpath( inDir );


%==========================================================================
%  Calculate the Perf. Fun. Gradient in Stand. Norm. Space
%==========================================================================
function [ r ] = calcGradient( x0, dr, mu, sig, dist )

dx = dr*diag(ones(size(x0)));
fc0 = runTrial( norm2Dist(x0,mu,sig,dist) );
for i = 1:length(x0)
    fc1 = runTrial( norm2Dist(x0+dx(i,:),mu,sig,dist) );
    r(i) = ( fc1(1) - fc0(1) ) / dr;
end


%==========================================================================
%  Perform a Newton Solve to find the Failure Surface in Direction r
%==========================================================================
function [x,fc0,n] = calcNewton( x, r, dr, fc, mu, sig, dist )

nmax = 15;
tol = 1.e-5;
n = 0;
fc0 = runTrial( norm2Dist(x,mu,sig,dist) );
dfc = abs( fc - fc0(1) );
dx = r * dr;

while( ( dfc > tol ) && ( n < nmax ) ) 
    norm2Dist(x+dx,mu,sig,dist);
    fc1 = runTrial( norm2Dist(x+dx,mu,sig,dist) );
    dfdr = ( fc1(1) - fc0(1) ) / dr;
    d_x = (fc-fc0(1)) / dfdr;
    x = x + sign(d_x) * min( abs(d_x), 1 ) * r;
    fc0 = runTrial( norm2Dist(x,mu,sig,dist) );
    dfc = abs( fc - fc0(1) );
    n = n + 1;
end


%==========================================================================
%  Get p from the Normal Cumulative Distribution Function
%==========================================================================
function [p] = normCDF( c )

p = 1/2 + 1/2 * erf( c / sqrt(2) );
