function[ idxs ] =  randIndices( nParms, nSamps )
%===============================================================================
%  Generate Random Indices
%    nParms:  Number of Parameters
%    nSamps:  Number of Samples
%    idxs:    Output - Matrix of Random Indices for Latin Hyper. Sampling
%===============================================================================

for i = 1:nParms
    rndTmp = rand( nSamps, 1 );
    [tmp, idx] = sort( rndTmp );
    idxs(:,i) = idx;
end