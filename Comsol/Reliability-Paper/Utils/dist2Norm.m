function [x] = dist2Norm( y, mu, sig, dist )
%==========================================================================
%  Transform x Drawn from a Non-standard Distribution to the Stand. Norm.
%  Distribution
%  x:     Value from Stand. Norm. Dist.
%  mu:    Mean of Input Dist.
%  sig:   Standard Deviation of Input Dist.
%  dist:  Index of Input Distribution (1-Normal, 2-Lognormal)
%  y:     Output - Value in Input Distribution
%==========================================================================

for i = 1:length(y)
    switch dist(i)
        case 1
            x(i) = y(i)/sig(i) - mu(i)/sig(i);
        case 2
            lsig = sqrt( log( (sig(i)/mu(i))^2 + 1) );
            lmu = log( mu(i) ) - 0.5 * lsig^2;
            x(i) = ( log( y(i) ) - lmu )  / lsig;
    end
end