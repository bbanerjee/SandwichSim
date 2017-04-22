function [y] = norm2Dist( x, mu, sig, dist )
%==========================================================================
%  Transform x Drawn from a Standard Normal Distribution to the Correct
%  Input Distribution
%  x:     Value from Stand. Norm. Dist.
%  mu:    Mean of Input Dist.
%  sig:   Standard Deviation of Input Dist.
%  dist:  Index of Input Distribution (1-Normal, 2-Lognormal)
%  y:     Output - Value in Input Distribution
%==========================================================================

for i = 1:length(x)
    switch dist(i)
        case 1
            y(i) = sig(i) * x(i) + mu(i);
        case 2
            lsig = sqrt( log( (sig(i)/mu(i))^2 + 1) );
            lmu = log( mu(i) ) - 0.5 * lsig^2;
            y(i) = exp( lsig * x(i) + lmu );
    end
end