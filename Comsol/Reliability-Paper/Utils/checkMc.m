function [mcOut,mcNrm] = checkMc( mcDat )

sz = size(mcDat);
inputs = getInputParms();
mu = inputs(:,1);
sig = inputs(:,2);
dist = inputs(:,3);
outSz = sz(2) - length(mu);
inIdx = (outSz+1):sz(2);

mcDat = mcDat .* (mcDat(:,1) >= -100);
mcDat = mcDat(:,inIdx);

n = 0;
for i = 1:sz(1)
    if( mcDat(i,1) ~= 0 )
        n = n+1;
        for j = 1:length(mu)
            mcOut(n,j) = dist2Norm( mcDat(i,j), mu(j), sig(j), dist(j) );
        end
    end
end

for i = 1:n
    mcNrm(i) = norm( mcOut(i,:) );
end
