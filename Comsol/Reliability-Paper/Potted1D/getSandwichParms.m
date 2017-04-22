function [mu, sigma, dist] = getSandwichParms
%==========================================================================
%  inParms = [ Q, r_ins, r_pot, r_ext, f, c, Ef, nuf, Ep, Gp, Ec, Gc, 
%              face_sigma_1t, face_sigma_1c, face_sigma_3t, face_tau_23, 
%              core_sigma_c, core_tau_0, potting_tau_0 ]
%  mu:     Means of inParms
%  sigma:  Standard Deviations
%  dist:   Distribution Indices - 1 = Normal, 2 = Lognormal

%==========================================================================
%  Scale Standard Deviations - Percents
%==========================================================================
scale_load_std = 1.0;
scale_geom_std = 2.0;
scale_mats_std = 5.0;
scale_fail_std = 5.0;


%==========================================================================
%  Load
%==========================================================================
Q = -600.0;
Q_std = 50;
Q_dst = 1;


%==========================================================================
%  Geometry
%==========================================================================
r_ins = 7.125e-3;
r_ins_std = 7.125e-5;
r_ins_dst = 1;

r_pot = 10.0e-3;
r_pot_std = 10.e-5;
r_pot_dst = 1;

r_ext = 60.e-3;
r_ext_std = 30.e-5;
r_ext_dst = 1;

ft = 0.508e-3;
ft_std = 0.508e-5;
ft_dst = 1;

fb = 0.508e-3;
fb_std = 0.508e-5;
fb_dst = 1;

hi = 9.e-3;
hi_std = 9.e-5;
hi_dst = 1;

hc = 25.4e-3;
hc_std = 25.4e-5;
hc_dst = 1;


%==========================================================================
%  Materials
%==========================================================================
Ef = 24.8e9;
Ef_std = 24.8e7;
Ef_dst = 1;

nuf = 0.3;
nuf_std = 0.003/scale_mats_std;
nuf_dst = 1;

Ep = 4.e9;
Ep_std = 4.e7;
Ep_dst = 1;

Gp = 1.5e9;
Gp_std = 1.5e7;
Gp_dst = 1;

Ec = 138.e6;
Ec_std = 138.e4;
Ec_dst = 1;

Gc = 32.75e6;
Gc_std = 32.75e4;
Gc_dst = 1;


%==========================================================================
%  Failure Criteria
%==========================================================================
face_sigma_1t = 414.e6;
face_sigma_1t_std = 414.e4;
face_sigma_1t_dst = 1;

face_sigma_1c = 427.e6;
face_sigma_1c_std = 427.e4;
face_sigma_1c_dst = 1;

core_sigma_c = 2.24e6;
core_sigma_c_std = 2.24e4;
core_sigma_c_dst = 1;

core_tau_0 = 948.e3;
core_tau_0_std = 948.e1;
core_tau_0_dst = 1;

potting_tau_0 = 17.2e6;
potting_tau_0_std = 17.2e4;
potting_tau_0_dst = 1;


%==========================================================================
%  Parameter Averages, Standard Deviations, and Distributions
%==========================================================================
mu_load = Q;
mu_geom = [ r_ins, r_pot, r_ext, ft, fb, hi, hc ];
mu_mats = [ Ef, nuf, Ep, Gp, Ec, Gc ];
mu_fail = [ face_sigma_1t, face_sigma_1c ];
mu_fail = [ mu_fail, core_sigma_c, core_tau_0, potting_tau_0 ];

mu = [ mu_load, mu_geom, mu_mats, mu_fail ];


sigma_load = [ Q_std ];
sigma_geom = [ r_ins_std, r_pot_std, r_ext_std, ft_std, fb_std, hi_std, hc_std ];
sigma_mats = [ Ef_std, nuf_std, Ep_std, Gp_std, Ec_std, Gc_std ];
sigma_fail = [ face_sigma_1t_std, face_sigma_1c_std ];
sigma_fail = [ sigma_fail, core_sigma_c_std, core_tau_0_std, potting_tau_0_std ];

sigma = [ scale_load_std*sigma_load, scale_geom_std*sigma_geom ];
sigma = [ sigma, scale_mats_std*sigma_mats, scale_fail_std*sigma_fail ]; 


dist_load = Q_dst;
dist_geom = [ r_ins_dst, r_pot_dst, r_ext_dst, ft_dst, fb_dst, hi_dst, hc_dst ];
dist_mats = [ Ef_dst, nuf_dst, Ep_dst, Gp_dst, Ec_dst, Gc_dst ];
dist_fail = [ face_sigma_1t_dst, face_sigma_1c_dst ];
dist_fail = [ dist_fail, core_sigma_c_dst, core_tau_0_dst, potting_tau_0_dst ];

dist = [ dist_load, dist_geom, dist_mats, dist_fail ];
