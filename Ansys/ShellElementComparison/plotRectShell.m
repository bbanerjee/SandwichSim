%
% Function to plot Ansys solution vs Exact solution 
%
function plotRectShell

  % Load Ansys data
  load rectBotUSigX.dat
  load rectBotUSigY.dat
  load rectMidUSigX.dat
  load rectMidUSigY.dat
  load rectTopUSigX.dat
  load rectTopUSigY.dat
  
  rectBotUSigX = sortrows(rectBotUSigX, 2);
  rectBotUSigY = sortrows(rectBotUSigY, 3);
  rectMidUSigX = sortrows(rectMidUSigX, 2);
  rectMidUSigY = sortrows(rectMidUSigY, 3);
  rectTopUSigX = sortrows(rectTopUSigX, 2);
  rectTopUSigY = sortrows(rectTopUSigY, 3);
  
  % Get location
  xloc = rectBotUSigX(:,2);
  yloc = rectBotUSigY(:,3);

  % Shift location to match exact solution assumptions
  xloc = xloc + max(xloc);
  yloc = yloc + max(yloc);
  
  uzx = rectBotUSigX(:,7);
  uzy = rectBotUSigY(:,7);
  
  sx1x = rectBotUSigX(:,8);
  sy1x = rectBotUSigX(:,9);
  sz1x = rectBotUSigX(:,10);
  sxy1x = rectBotUSigX(:,11);
  syz1x = rectBotUSigX(:,12);
  szx1x = rectBotUSigX(:,13);
  
  sx1y = rectBotUSigY(:,8);
  sy1y = rectBotUSigY(:,9);
  sz1y = rectBotUSigY(:,10);
  sxy1y = rectBotUSigY(:,11);
  syz1y = rectBotUSigY(:,12);
  szx1y = rectBotUSigY(:,13);
  
  sx2x = rectMidUSigX(:,8);
  sy2x = rectMidUSigX(:,9);
  sz2x = rectMidUSigX(:,10);
  sxy2x = rectMidUSigX(:,11);
  syz2x = rectMidUSigX(:,12);
  szx2x = rectMidUSigX(:,13);
  
  sx2y = rectMidUSigY(:,8);
  sy2y = rectMidUSigY(:,9);
  sz2y = rectMidUSigY(:,10);
  sxy2y = rectMidUSigY(:,11);
  syz2y = rectMidUSigY(:,12);
  szx2y = rectMidUSigY(:,13);
  
  sx3x = rectTopUSigX(:,8);
  sy3x = rectTopUSigX(:,9);
  sz3x = rectTopUSigX(:,10);
  sxy3x = rectTopUSigX(:,11);
  syz3x = rectTopUSigX(:,12);
  szx3x = rectTopUSigX(:,13);
  
  sx3y = rectTopUSigY(:,8);
  sy3y = rectTopUSigY(:,9);
  sz3y = rectTopUSigY(:,10);
  sxy3y = rectTopUSigY(:,11);
  syz3y = rectTopUSigY(:,12);
  szx3y = rectTopUSigY(:,13);
  
  figure;
  subplot(2,2,1);
  p1 = plot(xloc, uzx); hold on;
  xlabel('x (m)', 'FontSize', 18);
  ylabel('uz (m)', 'FontSize', 18);
  set(gca, 'Linewidth', 3, 'FontName', 'times', 'FontSize', 18);
  subplot(2,2,2);
  p2 = plot(xloc, sx1x, 'r-'); hold on;
  p3 = plot(xloc, sx2x, 'g-'); hold on;
  p4 = plot(xloc, sx3x, 'b-'); hold on;
  set(gca, 'Linewidth', 3, 'FontName', 'times', 'FontSize', 18);
  xlabel('x (m)', 'FontSize', 18);
  ylabel('\sigma_x (Pa)', 'FontSize', 18);
  subplot(2,2,3);
  p5 = plot(xloc, sy1x, 'r-'); hold on;
  p6 = plot(xloc, sy2x, 'g-'); hold on;
  p7 = plot(xloc, sy3x, 'b-'); hold on;
  set(gca, 'Linewidth', 3, 'FontName', 'times', 'FontSize', 18);
  xlabel('x (m)', 'FontSize', 18);
  ylabel('\sigma_y (Pa)', 'FontSize', 18);
  subplot(2,2,4);
  p8 = plot(xloc, szx1x, 'r-'); hold on;
  p9 = plot(xloc, szx2x, 'g-'); hold on;
  p10 = plot(xloc, szx3x, 'b-'); hold on;
  set(gca, 'Linewidth', 3, 'FontName', 'times', 'FontSize', 18);
  xlabel('x (m)', 'FontSize', 18);
  ylabel('\sigma_{zx} (Pa)', 'FontSize', 18);
  
  figure;
  subplot(2,2,1);
  p11 = plot(yloc, uzy, 'LineWidth', 3); hold on;
  xlabel('y (m)', 'FontSize', 18);
  ylabel('w_z (m)', 'FontSize', 18);
  set(gca, 'Linewidth', 3, 'FontName', 'times', 'FontSize', 18);
  subplot(2,2,2);
  p12 = plot(yloc, sx1y, 'r-', 'LineWidth', 3); hold on;
  p13 = plot(yloc, sx2y, 'g-'); hold on;
  p14 = plot(yloc, sx3y, 'b-', 'LineWidth', 3); hold on;
  xlabel('y (m)', 'FontSize', 18);
  ylabel('\sigma_{xx} (Pa)', 'FontSize', 18);
  set(gca, 'Linewidth', 3, 'FontName', 'times', 'FontSize', 18);
  subplot(2,2,3);
  p15 = plot(yloc, sy1y, 'r-', 'LineWidth', 3); hold on;
  p16 = plot(yloc, sy2y, 'g-'); hold on;
  p17 = plot(yloc, sy3y, 'b-', 'LineWidth', 3); hold on;
  xlabel('y (m)', 'FontSize', 18);
  ylabel('\sigma_{yy} (Pa)', 'FontSize', 18);
  set(gca, 'Linewidth', 3, 'FontName', 'times', 'FontSize', 18);
  subplot(2,2,4);
  p18 = plot(yloc, syz1y, 'r-', 'LineWidth', 3); hold on;
  p19 = plot(yloc, syz2y, 'g-', 'LineWidth', 3); hold on;
  p20 = plot(yloc, syz3y, 'b-', 'LineWidth', 3); hold on;
  xlabel('y (m)', 'FontSize', 18);
  ylabel('\sigma_{yz} (Pa)', 'FontSize', 18);
  set(gca, 'Linewidth', 3, 'FontName', 'times', 'FontSize', 18);

  % Calculate exact solution
  aa = 1.0e-2;
  bb = 2.0e-2;
  hh = aa/25.0;
  aa = 2.0*aa;
  bb = 2.0*bb;
  %qq = -10000.0*(aa*bb);
  qq = -10000.0;
  EE = 70.0e9;
  nu = 0.35;

  % Calculate bending stiffness
  DD = calcBendingStiffness(hh, EE, nu);

  % Set up location
  xx = xloc;
  yy = ones(size(xx))*bb/2;
  zztop = ones(size(xx))*hh/2;
  zzbot = ones(size(xx))*(-hh/2);
  zzmid = zeros(size(xx));

  % Find disp and stresses 
  for jj=1:length(xx)
    [wwtop(jj), sxtop(jj), sytop(jj)] = exactRectPlate(aa, bb, hh, nu, DD, qq, xx(jj), yy(jj), zztop(jj));
    [wwbot(jj), sxbot(jj), sybot(jj)] = exactRectPlate(aa, bb, hh, nu, DD, qq, xx(jj), yy(jj), zzbot(jj));
    [wwmid(jj), sxmid(jj), symid(jj)] = exactRectPlate(aa, bb, hh, nu, DD, qq, xx(jj), yy(jj), zzmid(jj));
  end
  [xloc wwtop' sxtop' sytop']

  % Plot solution
  figure(1);
  subplot(2,2,1);
  p21 = plot(xloc, wwtop, 'r--', 'LineWidth', 4); 
  subplot(2,2,2);
  p22 = plot(xloc, sxbot, 'r--', 'LineWidth', 4); hold on;
  p23 = plot(xloc, sxmid, 'g--'); hold on;
  p24 = plot(xloc, sxtop, 'b--', 'LineWidth', 4); hold on;
  subplot(2,2,3);
  p25 = plot(xloc, sybot, 'r--', 'LineWidth', 4); hold on;
  p26 = plot(xloc, symid, 'g--'); hold on;
  p27 = plot(xloc, sytop, 'b--', 'LineWidth', 4); hold on;
  
  % Plot error
  figure;
  subplot(2,2,1);
  %werr = (uzx'-wwtop)./wwtop*100;
  werr = uzx'-wwtop;
  p28 = plot(xloc, werr, 'r--', 'LineWidth', 4); 
  subplot(2,2,2);
  p29 = plot(xloc, sx1x'-sxbot, 'r--', 'LineWidth', 4); hold on;
  p30 = plot(xloc, sx2x'-sxmid, 'g--', 'LineWidth', 4); hold on;
  plot(xloc, sx3x'-sxtop, 'b--', 'LineWidth', 4); hold on;
  subplot(2,2,3);
  p31 = plot(xloc, sy1x'-sybot, 'r--', 'LineWidth', 4); hold on;
  p32 = plot(xloc, sy2x'-symid, 'g--', 'LineWidth', 4); hold on;
  p33 = plot(xloc, sy3x'-sytop, 'b--', 'LineWidth', 4); hold on;

  % Set up location
  yy = yloc;
  xx = ones(size(yy))*aa/2;
  zztop = ones(size(yy))*hh/2;
  zzbot = ones(size(yy))*(-hh/2);
  zzmid = zeros(size(yy));

  % Find disp and stresses 
  for jj=1:length(yy)
    [wwtop(jj), sxtop(jj), sytop(jj)] = exactRectPlate(aa, bb, hh, nu, DD, qq, xx(jj), yy(jj), zztop(jj));
    [wwbot(jj), sxbot(jj), sybot(jj)] = exactRectPlate(aa, bb, hh, nu, DD, qq, xx(jj), yy(jj), zzbot(jj));
    [wwmid(jj), sxmid(jj), symid(jj)] = exactRectPlate(aa, bb, hh, nu, DD, qq, xx(jj), yy(jj), zzmid(jj));
  end
  [yloc wwtop' sxtop' sytop']

  % Plot solution
  figure(2);
  subplot(2,2,1);
  p34 = plot(yloc, wwtop, 'r--', 'LineWidth', 4); 
  subplot(2,2,2);
  p35 = plot(yloc, sxbot, 'r--', 'LineWidth', 4); hold on;
  p36 = plot(yloc, sxmid, 'g--', 'LineWidth', 4); hold on;
  p37 = plot(yloc, sxtop, 'b--', 'LineWidth', 4); hold on;
  subplot(2,2,3);
  p38 = plot(yloc, sybot, 'r--', 'LineWidth', 4); hold on;
  p39 = plot(yloc, symid, 'g--', 'LineWidth', 4); hold on;
  p40 = plot(yloc, sytop, 'b--', 'LineWidth', 4); hold on;
  
  % Plot exact
  figure;
  pe34 = plot(yloc*1000, wwtop*1.0e3, 'r-', 'LineWidth', 3); 
  xlabel('y (mm)', 'FontSize', 18, 'FontName', 'arial');
  ylabel('w_z (mm)', 'FontSize', 18, 'FontName', 'arial');
  set(gca, 'Linewidth', 3, 'FontName', 'arial', 'FontSize', 18);
  figure;
  pe35 = plot(yloc*1000, sxbot*1.0e-6, 'r-', 'LineWidth', 3); hold on;
  pe36 = plot(yloc*1000, sxmid*1.0e-6, 'g-', 'LineWidth', 3); hold on;
  pe37 = plot(yloc*1000, sxtop*1.0e-6, 'b-', 'LineWidth', 3); hold on;
  xlabel('y (mm)', 'FontSize', 18, 'FontName', 'arial');
  ylabel('\sigma_{xx} (MPa)', 'FontSize', 18, 'FontName', 'arial');
  set(gca, 'Linewidth', 3, 'FontName', 'arial', 'FontSize', 18);
  figure;
  pe38 = plot(yloc*1000, sybot*1.0e-6, 'r-', 'LineWidth', 3); hold on;
  pe39 = plot(yloc*1000, symid*1.0e-6, 'g-', 'LineWidth', 3); hold on;
  pe40 = plot(yloc*1000, sytop*1.0e-6, 'b-', 'LineWidth', 3); hold on;
  xlabel('y (mm)', 'FontSize', 18, 'FontName', 'arial');
  ylabel('\sigma_{yy} (MPa)', 'FontSize', 18, 'FontName', 'arial');
  set(gca, 'Linewidth', 3, 'FontName', 'arial', 'FontSize', 18);

  % Plot error
  figure;
  subplot(2,2,1);
  werr = uzy'-wwtop;
  p42 = plot(yloc, werr, 'r--', 'LineWidth', 4); 
  xlabel('y (m)', 'FontSize', 18);
  ylabel('Error in w_z (m)', 'FontSize', 18);
  set(gca, 'Linewidth', 3, 'FontName', 'times', 'FontSize', 18);
  subplot(2,2,2);
  p43 = plot(yloc, sx1y'-sxbot, 'r--', 'LineWidth', 4); hold on;
  p44 = plot(yloc, sx2y'-sxmid, 'g--', 'LineWidth', 4); hold on;
  p45 = plot(yloc, sx3y'-sxtop, 'b--', 'LineWidth', 4); hold on;
  xlabel('y (m)', 'FontSize', 18);
  ylabel('Error in \sigma_{xx} (m)', 'FontSize', 18);
  set(gca, 'Linewidth', 3, 'FontName', 'times', 'FontSize', 18);
  subplot(2,2,3);
  p46 = plot(yloc, sy1y'-sybot, 'r--', 'LineWidth', 4); hold on;
  p47 = plot(yloc, sy2y'-symid, 'g--', 'LineWidth', 4); hold on;
  p48 = plot(yloc, sy3y'-sytop, 'b--', 'LineWidth', 4); hold on;
  xlabel('y (m)', 'FontSize', 18);
  ylabel('Error in \sigma_{yy} (m)', 'FontSize', 18);
  set(gca, 'Linewidth', 3, 'FontName', 'times', 'FontSize', 18);

%==========================================================================
% Calculate exact solution for rectangular plate
%==========================================================================
function [ww, sx, sy] = exactRectPlate(aa, bb, hh, nu, DD, qq, xx, yy, zz)

  % Initialize
  ww = 0;
  Mx = 0;
  My = 0;

  % Add terms
  nsum = 20;
  for nn = 1:nsum
    for mm = 1:nsum
      mterm = (2*mm-1)/aa;
      nterm = (2*nn-1)/bb;
      sin_term = sin(mterm*pi*xx)*sin(nterm*pi*yy);
      sq_term = 1/(mterm^2 + nterm^2)^2;
      nu_x_term = mterm^2 + nu*nterm^2;
      nu_y_term = nterm^2 + nu*mterm^2;
      q_fac = 16*qq/(pi^4*(2*mm-1)*(2*nn-1));
      comm_term = q_fac*sq_term*sin_term;

      ww = ww + comm_term/(pi^2*DD);
      Mx = Mx + comm_term*nu_x_term;
      My = My + comm_term*nu_y_term;
    end
  end
  sx = (12*zz/hh^3)*Mx;
  sy = (12*zz/hh^3)*My;

%==========================================================================
% Calculate bending stiffness for rectangular plate
%==========================================================================
function [DD] = calcBendingStiffness(hh, EE, nu)

  DD = hh^3*EE/(12*(1-nu^2));

