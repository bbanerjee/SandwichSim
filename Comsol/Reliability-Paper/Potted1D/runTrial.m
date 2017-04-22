function [outParms] = runTrial( inParms )
%==========================================================================
%  Run a Single Trial
%    inParms:   Input Parameters
%    outParms:  Output Parameters
%==========================================================================

dr = 1.e-5;

[fc_max,fc_fail] = runSandwichPotted( inParms, dr );  
outParms = [fc_max,fc_fail];
