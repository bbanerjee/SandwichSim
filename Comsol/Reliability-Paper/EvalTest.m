function [p,t,n] = EvalTest( x, sCase )
%      x:  Loads
%  sCase:  Case to load
%      1:  1D MC
%      2:  2D MC
%      3:  1D FORM
%      4:  2D FORM
%      5:  1D Line Sampling
%      6:  2D Line Sampling
%      7:  1D Subset Sampling
%      8:  2D Subset Sampling

switch sCase
  case 1
    fname_0 = 'Data_MC/MCTest1D';
  case 2
    fname_0 = 'Data_MC/MCTest2D';
  case 3
    fname_0 = 'Data_FORM/FormTest1D';
  case 4
    fname_0 = 'Data_FORM/FormTest2D';
  case 5
    fname_0 = 'Data_LINE/LineTest1D';
  case 6
    fname_0 = 'Data_LINE/LineTest2D';
  case 7
    fname_0 = 'Data_SUB/SubTest1D';
  case 8
    fname_0 = 'Data_SUB/SubTest1D';
end

for i = 1:length(x)
  fname = strcat( fname_0, num2str(x(i)), '.mat' );
  tmp = load(fname);
  p(i) = tmp.Pf(1);
  t(i) = tmp.t;
  n(i) = tmp.NN;
end

