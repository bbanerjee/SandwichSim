function [parms] = getTrialParms( iSamp, pInfo, inIdx )
%==========================================================================
%  Get Trial Parameters
%    iSamp:  Sample Number
%    pInfo:  Mean, Standard Deviation, and Distribution of Sample
%    inIdx:  Index of Random Latin Hypercube Boxes
%    parms:  Parameters to be Used in this Iteration
%==========================================================================

inMu = pInfo(:,1);
inSigma = pInfo(:,2);
inDistIdx = pInfo(:,3);

sz = size( inIdx );
nSamps = sz(1);
nParms = sz(2);

for i = 1:nParms
    pUniform = rand/nSamps + ( inIdx(iSamp,i) - 1 ) / nSamps;
    parms(i) = pullParm( pUniform, inMu(i), inSigma(i), inDistIdx(i) );
end
