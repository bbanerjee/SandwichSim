function [stats,t] = MonteCarlo( nSamps, freq, fc0, inDir, outDir, fname )
%==========================================================================
%  [stats,t] = MonteCarlo( nSamps, freq, inDir, fname )
%  Monte Carlo Simulation
%    nSamps:  Number of Samples
%    freq:    Frequency of progress tracker output
%    inDir:   Directory Containing Performance Function
%    fname:   Data File Name
%    stats:   Output - Performance Values and Input Parameters
%    t:       Output - Time for Simulation
%==========================================================================
if nargin < 6, fname = 'MonteCarlo'; end
if nargin < 5, outDir = 'Data'; end
if nargin < 4, inDir = pwd; end
if nargin < 3, fc0 = 0; end
if nargin < 2, freq = 100; end
if nargin < 1, error('Must input number of samples'); end

global NN;
NN = 0;

addpath('Utils');
addpath( inDir );
tic
fname = strcat( outDir, '/', fname, '.mat' );

%  Input Parameters - Averages and Standard Deviations
[inputs,nParms] = getInputParms();

%  Randomize the LHS Parameters
inIdx = randIndices( nParms, nSamps );

%  Run Through the Samples
for i=1:nSamps
    inParms = getTrialParms( i, inputs, inIdx );
    outParms = runTrial( inParms );
    stats(i,:) = [ outParms, inParms ];
    trackProgress( i, nSamps, freq );
    save( fname, 'stats', '-mat' );
end

fail = stats(:,1) > fc0;
Pf = sum(fail) / length(fail);

%  Save Results
t = toc;
save( fname, 'stats', 'Pf', 't', 'NN', '-mat' );

rmpath('./Utils');
rmpath( inDir );
