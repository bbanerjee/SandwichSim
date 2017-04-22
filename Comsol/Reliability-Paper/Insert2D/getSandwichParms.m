function [mu, sigma, dist] = getSandwichParms
%==========================================================================
%  inParms = [ Q, 
%              r_ins, r_pot, r_ext, f_top, f_bot, c, 
%              Ef, Ep, Ecr, Ec, Gc, 
%              core_sigma_c, core_tau_0 ]
%  mu:     Means of inParms
%  sigma:  Standard Deviations
%  dist:   Distribution Indices - 1 = Normal, 2 = Lognormal

%==========================================================================
%  Scale Standard Deviations - Percents
%==========================================================================
scale_geom_std = 1.0;
scale_mats_std = 10.0;
scale_fail_std = 10.0;


%==========================================================================
%  Geometry #1-6
%==========================================================================
r_ins = 7.125e-3;
r_ins_std = 0.02 * r_ins;
r_ins_dst = 1;

r_pot = 2.875e-3;
r_pot_std = 0.15 * r_pot;
r_pot_dst = 1;

r_ext = 25.4e-3;
r_ext_std = 0.05 * r_ext;
r_ext_dst = 1;

f_top = 0.508e-3;
f_top_std = 0.02 * f_top;
f_top_dst = 1;

f_bot = 0.508e-3;
f_bot_std = 0.02 * f_bot;
f_bot_dst = 1;

c = 25.4e-3;
c_std = 0.02 * c_std;
c_dst = 1;


%==========================================================================
%  Materials #7-11
%==========================================================================
Ef = 24.8e9;
Ef_std = 24.8e7;
Ef_dst = 1;

Ep = 890.e6;
Ep_std = 890.e4;
Ep_dst = 1;

Ecr = 408.e3;
Ecr_std = 408.e1;
Ecr_dst = 1;

Ec = 132.e6;
Ec_std = 132.e4;
Ec_dst = 1;

Gc = 32.75e6;
Gc_std = 32.75e4;
Gc_dst = 1;


%==========================================================================
%  Failure Criteria #12-13
%==========================================================================
core_sigma_c = 2.24e6;
core_sigma_c_std = 2.24e4;
core_sigma_c_dst = 1;

core_tau_0 = 0.95e6;
core_tau_0_std = 0.95e4;
core_tau_0_dst = 1;


%==========================================================================
%  Parameter Averages, Standard Deviations, and Distributions
%==========================================================================
mu_geom = [ r_ins, r_pot, r_ext, f_top, f_bot, c ];
mu_mats = [ Ef, Ep, Ecr, Ec, Gc ];
mu_fail = [ core_sigma_c, core_tau_0 ];
mu      = [ mu_geom, mu_mats, mu_fail ];

sigma_geom = [ r_ins_std, r_pot_std, r_ext_std, f_top_std, f_bot_std, c_std ];
sigma_mats = [ Ef_std, Ep_std, Ecr_std, Ec_std, Gc_std ];
sigma_fail = [ core_sigma_c_std, core_tau_0_std ];
sigma      = [ scale_geom_std*sigma_geom ];
sigma      = [ sigma, scale_mats_std*sigma_mats, scale_fail_std*sigma_fail ]; 

dist_geom = [ r_ins_dst, r_pot_dst, r_ext_dst, f_top_dst, f_bot_dst, c_dst ];
dist_mats = [ Ef_dst, Ep_dst, Ecr_dst, Ec_dst, Gc_dst ];
dist_fail = [ core_sigma_c_dst, core_tau_0_dst ];
dist      = [ dist_geom, dist_mats, dist_fail ];
