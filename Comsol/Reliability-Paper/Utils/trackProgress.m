function trackProgress( i, nMax, freq )
%==========================================================================
%  Progress Tracking
%    i:     Current Step
%    nMax:  Number of Steps
%    freq:  Frequency of Output (0.1 = 10%)
%==========================================================================

if( mod(i,floor(nMax*freq)) == 0 )
    msg = strcat( num2str( 100 * i/nMax ), '% Completed' );
    warning( msg );
end