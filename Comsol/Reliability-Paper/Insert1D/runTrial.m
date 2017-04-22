function [outParms] = runTrial( inParms )
%==========================================================================
%  Run a Single Trial
%    inParms:   Input Parameters
%    outParms:  Output Parameters
%==========================================================================
global NN;
NN = NN + 1;

dr = 1.e-5;

[fc_max,fc_fail] = runSandwichInsert1D( inParms, dr );  
outParms = [fc_max,fc_fail];
