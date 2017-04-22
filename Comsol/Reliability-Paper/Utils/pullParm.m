function [parm] = pullParm( p, mu, sig, dist )
%==========================================================================
%  Pull a Parameter Value from a Distribution given a Probability
%  p:     Probability
%  mu:    Mean
%  sig:   Standard Deviation
%  dist:  Distribution Index
%  parm:  Output - Parameter Value
%==========================================================================

switch dist
case 1
    parm = mu + sqrt(2)*sig * erfinv( 2*p-1 );
case 2
    lmu = log(mu) - 0.5*log( 1 + sig^2/mu^2 );
    lsig = sqrt( log( sig^2/mu^2 + 1 ) );
    parm = exp( lmu + sqrt(2)*lsig * erfinv( 2*p-1 ) );
end