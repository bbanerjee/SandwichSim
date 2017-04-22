function [vFail,vAll,vCov,t] = SubsetSamp( nLevels, nN, nP, pWin, fc0, inDir, outDir, fname )
%==========================================================================
%  [vFail,vAll,vCov,t] = SubsetSamp( nLevels, nN, nP, pWin, inDir, fname )
%  Subset Sampling Simulation
%    nLevels:  Number of subsets
%    nN:       Number of samples per level
%    nP:       Inverse of the probability at each level (1/p_0)
%    pWin:     Width of MCMC window (in standard deviations)
%    inDir:    Directory Containing Performance Function
%    fname:    Data File Name
%    vFail:    Output - Failure Probabilities vs. Performance Function
%    vAll:     Output - Performance Values and Input Parameters
%    vCov:     Output - Coefficient of Variation Parameters
%    t:        Output - Time for Simulation
%=========================================================================+
if nargin < 7, fname = 'SubsetSamp'; end
if nargin < 6, outDir = 'Data'; end
if nargin < 5, inDir = pwd; end
if nargin < 4, error('Not enough input parameters'); end

global NN;
NN = 0;

addpath('./Utils');
addpath( inDir );
tic

p0 = 1/nP;                      %  Probability at each Level
Nc = floor( nN/nP );		%  Number of seeds at each level
NNc = nP;                       %  Number of samples from each seed

%  Initial Monte Carlo Run
[inputs,nParms] = getInputParms();
inpIdx = randIndices( nParms, nN );
for i=1:nN
    inParms = getTrialParms( i, inputs, inpIdx );
    outParms = runTrial( inParms );
    vTmp(i,:) = [ outParms, inParms ];
end
vLvl{1} = vTmp;
vFail = getFailLvls( 1, p0, nP-1, vLvl{1} );

%  Find Indices of Input Parameters
lnIn  = length(inParms);
lnOut = length(outParms);
inIdx = (lnOut+1):(lnOut+lnIn);

%  Subsequent Levels
for i = 1:nLevels
    vLvl{i+1} = [];
    [vSds, fc] = getSeeds( vLvl{i}, Nc );		                
    for j = 1:Nc
        tmp = vSds(j,:);	
        for k = 1:NNc
            [ inTry, bNew ] = getNewParms( tmp(inIdx), inputs, pWin ); 
            if( bNew )
                parms_tmp = [ runTrial( inTry ), inTry ];
                tmp = (parms_tmp(1)<fc)*tmp + (parms_tmp(1)>=fc)*parms_tmp;
            end
            vLvl{i+1} = [ vLvl{i+1}; tmp ];
        end
    end
    vFail = [ vFail; getFailLvls( i+1, p0, nP-1, vLvl{i+1} ) ];
end

%  Evaluate Coefficient of Variation
[vCov] = getCOV( vLvl, p0, nLevels, Nc, NNc ); 

%  Compile Results
vAll = [];
for i = 1:(nLevels+1)
    vAll = [vAll; vLvl{i}];
end

Pf = 1 - getFailProb( vFail, fc0 );

%  Save Results
t = toc;
fname = strcat( outDir, '/', fname, '.mat' );
save( fname, 'vFail', 'vAll', 'vCov', 't', 'Pf', 'NN', '-mat' );

rmpath('./Utils');
rmpath( inDir );


%==========================================================================
% Get Seeds for Next Level
%==========================================================================
function [seeds,fCrit] = getSeeds( v, nSeeds )

[vSrt,i] = sort( v(:,1) );
vSrt = v(i,:);
len = (size(vSrt))(1);
idx = (len+1-nSeeds):len;
seeds = vSrt(idx,:);
fCrit = seeds(1,1);


%==========================================================================
%  Get New Parameters - Modified MCMC Procedure
%==========================================================================
function [ outParms, bNew ] = getNewParms( x_old, inputs, pWin )

mu = inputs(:,1);
sigma = inputs(:,2);
dist = inputs(:,3);
bNew = false;

for i = 1:length(mu)
    x_tmp = UDist( x_old(i), sigma(i), pWin );
    p_tmp = pullProb( x_tmp, mu(i), sigma(i), dist(i) );
    p_old = pullProb( x_old(i), mu(i), sigma(i), dist(i) );
    pRatio = min( 1, p_tmp/p_old );  
    if( pRatio > rand )
        outParms(i) = x_tmp;
        bNew = true;
    else
        outParms(i) = x_old(i);
    end
end


%==========================================================================
%  Pull a Random Variable from a Uniform Distribution - Width: 2*dist*stdev
%==========================================================================
function [y] = UDist( x, sigma, dist )
y = x + 2*(rand(1) - 1/2) * dist * sigma;


%==========================================================================
%  Get Failure Levels at each Percentile
%==========================================================================
function [fail_lvl] = getFailLvls( lvl, p, pLvls, v )

p0 = 1-p^(lvl-1);
vSrt = sort( v(:,1) );

for i = 1:pLvls
    p_i = p0 + i*p^lvl;
    idx = min( max( floor( length(vSrt)*p*i ), 1 ), length(vSrt) );
    fail_lvl(i,:) = [ p_i, vSrt(idx) ];
end

%==========================================================================
%  Get Failure Probability
%==========================================================================
function [p] = getFailProb( vF, fc0 )

ln = (size(vF))(1) - 1;
p = 0;

for i = 1:ln
  if( (vF(i,2)-fc0) * (vF(i+1,2)-fc0) < 0 )
    p = (fc0-vF(i,2))/(vF(i+1,2)-vF(i,2)) * (vF(i+1,1)-vF(i,1)) + vF(i,1);
  end
end



%==========================================================================
%  Get Coefficient of Variation
%==========================================================================
function [vCov] = getCOV( v, p, nLvls, Nc, NNc ) 

vCov(1,:) = [ sqrt( (1-p)/(p*Nc*NNc) ), 0 ];

n = nLvls;
for i = 1:n
    [vSds, fc] = getSeeds( v{i+1}, Nc );		                
    gamma = getCorr( v{i+1}, Nc, NNc, fc, p );
    delta = sqrt( (1-p)/(p*Nc*NNc) * (1+gamma) );
    vCov(i+1,:) = [ delta, gamma ];
end


%==========================================================================
%  Get MCMC Correlation
%==========================================================================
function [gamma] =  getCorr( v, Nc, NNc, fc, p )

N = Nc*NNc;
R0 = p*(1-p);
I = makeInd( v, Nc, NNc, fc );
gamma = 0;

for k = 1:(NNc-1)
    rk = 0;
    for j = 1:Nc
        for l = 1:(NNc-k)
            rk = rk + 1/(N-k*Nc) * I(j,l) * I(j,l+k);
        end
    end
    rk = rk - p^2;
    gamma = gamma + 2/R0 * (1-k/NNc) * rk;
end


%==========================================================================
%  Get MCMC Indicator Function
%==========================================================================
function [ind] =  makeInd( v, Nc, NNc, fc )

for j = 1:Nc
    for l = 1:NNc
        ind(j,l) = v( (j-1)*NNc+1, 1) >= fc;
    end
end
