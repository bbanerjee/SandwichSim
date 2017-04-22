function [p] = pullProb( x, mu, sig, dist )
%==========================================================================
%  Pull Probability from Distribution given a Parameter Value
%    x:     Parameter Value
%    mu:    Mean
%    sig:   Standard Deviation
%    dist:  Distribution Index
%    p:     Output - Probability of Parameter Value
%==========================================================================

switch dist
case 1
    p = 1/(sqrt(2*pi)*sig) * exp( -(x-mu)^2/(2*sig^2) );
case 2
    lmu = log(mu) - 0.5*log( 1 + sig^2/mu^2 );
    lsig = sqrt( log( sig^2/mu^2 + 1 ) );
    x = (x>0) * x + (x<=0) * 1.e-100;
    p = 1/(x*sqrt(2*pi*lsig)) * exp( -(log(x) - lmu)^2 / (2*lsig) );
end