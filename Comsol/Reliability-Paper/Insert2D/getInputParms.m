function [inputs,nParms] = getInputParms( )
%===============================================================================
%  Get Input Parameters
%    inputs:  Output - Matrix:  Column 1-mu, Column 2-sigma, Column 3-dist
%    nParms:  Output - Number of Parameters
%===============================================================================

[inMu,inSigma,inDistIdx] = getSandwichParms();
inputs = [transpose(inMu),transpose(inSigma),transpose(inDistIdx)];
nParms = length(inMu);