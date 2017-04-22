function [stats] = LHSTest( nBoxes, nTails, nRefine );
%  Latin Hypercube Sampling Test
%  nBoxes = number of LHS boxes
%  nTails = number of tail boxes to exclude - generally 0
%  nRefine = number of mesh refinements

%  Calculate maximum strains while varying load and adhesive layer strength
%  Load - Normally distributed about 0.4 MPa with 20% standard deviation
%  Adhesive layer strength - Lognormally distributed around 10 MPa with 50% variance

tic

Ymu  = 10.0;
YVar = 5.0;

Evar = log( YVar/Ymu^2 + 1 );  %  Lognormal parameters
Emu  = log( Ymu ) - 0.5*Evar;

Lmu = 0.4;                     %  Normal parameters
Lvar = ( 0.4*0.2 )^2;

nTrials = nBoxes - nTails;     %  Number of LHS Trial boxes (subtract off tails of distribution if necessary)

rE = rand(nTrials,1);          %  Generate a vector of random variables
rL = rand(nTrials,1);

[aa,iE] = sort(rE);            %  Randomly combine the two sets of samples - shuffle by sorting the random numbers
[bb,iL] = sort(rL);            %  and keeping track of the indices

sh = nTails - 1;

for i=1:nTrials
    uE = rand(1);
    uL = rand(1);
    pE = uE/nBoxes + ( iE(i) + sh )/nBoxes;                              %  iE and iL should be shuffled
    pL = uL/nBoxes + ( iL(i) + sh )/nBoxes; 
    Ei = exp( Emu + sqrt(2 * Evar) * erfinv( 2*pE - 1 ) );               %  Transform random parameters to
    Li = Lmu + sqrt(2 * Lvar) * erfinv( 2*pL - 1 );                      %  correct distributions
    
    [emax,emaxloc] = PanelModel( Ei, abs(Li), nRefine );
    stats(i,:) = [ emax, Ei, Li, pE, pL, emaxloc(1), emaxloc(2) ];
    if( mod(i,floor(nTrials/10)) == 0 )
        pct = 100 * i/nTrials                                            %  Progress tracker
    end
end

save Data/LHSData.dat stats -ascii;

toc
