function [stats] = MCTest(nTrials, nRefine);
%  Monte Carlo Sampling Test 
%  nTrials = number of samples
%  nRefine = number of mesh refinements

%  Calculate maximum strains while varying adhesive layer strength
%  Adhesive layer strength - Lognormally distributed around 10 MPa with 50% variance

tic

Pappl = 0.4;                                  %  Applied Pressure

Ymu  = 10.0;                                  %  Desired Youngs modulus statistics
Yvar = 5.0;

Evar = log( Yvar/Ymu^2 + 1 );                 %  Lognormal parameters
Emu  = log( Ymu ) - 0.5*Evar;

for i=1:nTrials
    pE = rand(1);                                              %  Pull pE from uniform distribution
    Ei = exp( Emu + sqrt(2 * Evar) * erfinv( 2*pE - 1 ) );     %  Logormalize uniform distribution

    [emax,emaxloc] = PanelModel( Ei, Pappl, nRefine );         %  Finite element calculation
    stats(i,:) = [ emax, Ei, pE, emaxloc(1), emaxloc(2) ];

    if( mod(i,floor(nTrials/10)) == 0 )
        pct = 100 * i/nTrials                                  %  Progress tracker
    end
end

save Data/MCData.dat stats -ascii;

toc
