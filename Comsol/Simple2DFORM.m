function [pf,E,P,diff,stats,seq] = Simple2DFORM( dE, dP, tol, Gfail, maxn, nRefine )
%  dE,dP   - Parameters used to construct finite difference derivative approximations
%  tol     - Convergence tolerance
%  Gfail   - Failure strain
%  maxn    - Maximum number of iterations
%  nRefine - Number of mesh refinements
%
%  Calculates the probability of failure when Gfail is the failure strain.  Assumes a
%  Lognormal distribution for the Youngs modulus with mean 10 and variance 5.  Assumes
%  a normal distribution for the applied pressure with mean 0.3 and 10% standard deviation.

tic

%  Set up input parameter distributions
Emu = 10;
Ev  = 5;
Pmu = 0.3;
Pv  = ( 0.2 * Pmu )^2;

%  Parameters for the Jacobians
Esig = sqrt( log( Ev / Emu^2 + 1 ) );
Psig = sqrt( Pv );

%  Initial Values - start at the origin
En = 0;
Pn = 0;
E = SNTransLN( En, Emu, Ev );                    %  Transfer functions for changing between standard
P = SNTransN( Pn, Pmu, Pv );                     %  normal and physical distributions
OldG = PanelModel( E, P, nRefine );              %  Maximum strain at initial condition
GMean = OldG;
Dist = 0.0;

%  Initialize loop parameters
n = 0;
diff = 1;

%  Initialize iteration sequence output parameters
sn = 1;
seq(sn,:) = [En Pn];

%  Iterate
while( ( diff > tol ) & ( n < maxn ) ) 
    %  Create center difference derivatives
    G0  = OldG;
    Gep = PanelModel( E+dE, P, nRefine );
    Gem = PanelModel( E-dE, P, nRefine );
    Gpp = PanelModel( E, P+dP, nRefine );
    Gpm = PanelModel( E, P-dP, nRefine );

    dGdEn = ( Gep - Gem ) / dE / 2.0 * ( Esig * E );     %  Transform derivatives into standard normal space
    dGdPn = ( Gpp - Gpm ) / dP / 2.0 * ( Psig );
    Grad2 = dGdEn^2 + dGdPn^2;

    dEn = -( G0 - Gfail ) * dGdEn / Grad2;               %  First step - move point towards failure surface    
    dPn = -( G0 - Gfail ) * dGdPn / Grad2;
    EnHat = En + dEn;
    PnHat = Pn + dPn;

    sn = sn+1;                                           %  Add intermediate point to sequence
    seq(sn,:) = [EnHat PnHat];

    EHat = SNTransLN( EnHat, Emu, Ev );                  %  Transform intermediate point for derivative evaluation
    PHat = SNTransN( PnHat, Pmu, Pv );
    
    G0  = PanelModel( EHat,    PHat, nRefine );
    Gep = PanelModel( EHat+dE, PHat, nRefine );
    Gem = PanelModel( EHat-dE, PHat, nRefine );
    Gpp = PanelModel( EHat,    PHat+dP, nRefine );
    Gpm = PanelModel( EHat,    PHat-dP, nRefine );

    dGdEn = ( Gep - Gem ) / dE / 2.0 * ( Esig * EHat );
    dGdPn = ( Gpp - Gpm ) / dP / 2.0 * ( Psig );
    Grad2 = dGdEn^2 + dGdPn^2;

    dEnHat = dGdPn * ( dGdEn * PnHat - dGdPn * EnHat ) / Grad2;      %  Second step - move point along failure surface towards
    dPnHat = -dGdEn * ( dGdEn * PnHat - dGdPn * EnHat ) / Grad2;     %  origin
    En = EnHat + dEnHat;
    Pn = PnHat + dPnHat;

    sn = sn+1;
    seq(sn,:) = [En Pn];

    E = SNTransLN( En, Emu, Ev );                        %  Transform result for maximum strain evaluation
    P = SNTransN( Pn, Pmu, Pv );

    G0  = PanelModel( E, P, nRefine );                   %  Evaluate maximum strain at the new point
    
    dG   = G0 - OldG;                                    %  Difference in maximum strain from last iteration to this one
    OldG = G0;                                           %  Set up next iteration

    dDist = Dist - sqrt( En^2 + Pn^2 );                  %  Distance between last point and this one
    Dist  = Dist - dDist;

    n = n+1;

    diff = sqrt( dDist*dDist + dG*dG );                  %  How far has the point moved this iteration - if its not moving
                                                         %  then method has converged
    GEPDiffn = [ G0 E P diff n];                         %  Use for output purposes if semicolon is removed

    stats(n,:) = [E P En Pn G0 Dist];                    %  Output
end


%  Determine failure probability using FORM
beta = sqrt( En^2 + Pn^2 );
pf = 1/2 * ( 1  + erf( -beta/sqrt(2) ) );

if( (GMean - Gfail) > 0 )                               %  If the origin is in the failure region, pf = 1 - pf
    pf = 1 - pf;
end

FORM = [Gfail pf n]
toc

%------------------------------------------------------------------------------------------------
function [y] = SNTransLN( z, mu0, var0 )  
%  Transform a standard normal variable into a lognormal variable with mean mu0 and variance var0

v  = log( var0/mu0^2 + 1 );
mu = log( mu0 ) - 1/2 * v;

y = exp( sqrt(v) * z + mu );

%------------------------------------------------------------------------------------------------
function [z] = LNTransSN( y, mu0, var0 )  
%  Transform a lognormal variable with mean mu0 and variance var0 into a standard normal variable

v  = log( var0/mu0^2 + 1 );
mu = log( mu0 ) - 1/2 * v;

z = ( log(y) - mu ) / sqrt(v);

%------------------------------------------------------------------------------------------------
function [y] = SNTransN( z, mu0, var0 )  
%  Transform a standard normal variable into a normal variable with mean mu0 and variance var0

y = sqrt(var0) * z + mu0;


%------------------------------------------------------------------------------------------------
function [z] = NTransSN( y, mu0, var0 )  
%  Transform a normal variable with mean mu0 and variance var0 into a standard normal variable

z = ( y - mu0 ) / sqrt(var0);


