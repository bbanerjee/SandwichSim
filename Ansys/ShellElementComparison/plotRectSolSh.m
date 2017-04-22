%
% Function to plot Ansys solution vs Exact solution 
%
function plotRectSolSh

  % Load Ansys data
  load rectSolShBotUSigX.dat
  load rectSolShBotUSigY.dat
  load rectSolShTopUSigX.dat
  load rectSolShTopUSigY.dat
  
  rectSolShBotUSigX = sortrows(rectSolShBotUSigX, 2);
  rectSolShBotUSigY = sortrows(rectSolShBotUSigY, 3);
  rectSolShTopUSigX = sortrows(rectSolShTopUSigX, 2);
  rectSolShTopUSigY = sortrows(rectSolShTopUSigY, 3);
  
  % Get location
  xlocBot = rectSolShBotUSigX(:,2);
  ylocBot = rectSolShBotUSigY(:,3);

  nodeBot = rectSolShBotUSigX(:,1);
  zlocBot = rectSolShBotUSigX(:,4);

  xlocTop = rectSolShTopUSigX(:,2);
  ylocTop = rectSolShTopUSigY(:,3);

  nodeTop = rectSolShTopUSigX(:,1);
  zlocTop = rectSolShTopUSigX(:,4);

  xlocBot = xlocBot + max(xlocBot);
  ylocBot = ylocBot + max(ylocBot);

  xlocTop = xlocTop + max(xlocTop);
  ylocTop = ylocTop + max(ylocTop);
  
  uzx = rectSolShBotUSigX(:,7);
  uzy = rectSolShBotUSigY(:,7);
  
  sx1x = rectSolShBotUSigX(:,8);
  sy1x = rectSolShBotUSigX(:,9);
  sz1x = rectSolShBotUSigX(:,10);
  sxy1x = rectSolShBotUSigX(:,11);
  syz1x = rectSolShBotUSigX(:,12);
  szx1x = rectSolShBotUSigX(:,13);
  
  sx1y = rectSolShBotUSigY(:,8);
  sy1y = rectSolShBotUSigY(:,9);
  sz1y = rectSolShBotUSigY(:,10);
  sxy1y = rectSolShBotUSigY(:,11);
  syz1y = rectSolShBotUSigY(:,12);
  szx1y = rectSolShBotUSigY(:,13);
  
  sx3x = rectSolShTopUSigX(:,8);
  sy3x = rectSolShTopUSigX(:,9);
  sz3x = rectSolShTopUSigX(:,10);
  sxy3x = rectSolShTopUSigX(:,11);
  syz3x = rectSolShTopUSigX(:,12);
  szx3x = rectSolShTopUSigX(:,13);
  
  sx3y = rectSolShTopUSigY(:,8);
  sy3y = rectSolShTopUSigY(:,9);
  sz3y = rectSolShTopUSigY(:,10);
  sxy3y = rectSolShTopUSigY(:,11);
  syz3y = rectSolShTopUSigY(:,12);
  szx3y = rectSolShTopUSigY(:,13);
  
  figure;
  subplot(2,2,1);
  plot(xlocBot, uzx); hold on;
  xlabel('r (m)');
  ylabel('uz (m)');
  subplot(2,2,2);
  plot(xlocBot, sx1x, 'r-'); hold on;
  plot(xlocTop, sx3x, 'b-'); hold on;
  xlabel('r (m)');
  ylabel('\sigma_x (Pa)');
  subplot(2,2,3);
  plot(xlocBot, sy1x, 'r-'); hold on;
  plot(xlocTop, sy3x, 'b-'); hold on;
  xlabel('r (m)');
  ylabel('\sigma_y (Pa)');
  subplot(2,2,4);
  plot(xlocBot, szx1x, 'r-'); hold on;
  plot(xlocTop, szx3x, 'b-'); hold on;
  xlabel('r (m)');
  ylabel('\sigma_{zx} (Pa)');

  format short e
  [nodeBot xlocBot zlocBot sx1x sxy1x]
  [nodeTop xlocTop zlocTop sx3x sxy3x]
  
  figure;
  subplot(2,2,1);
  plot(ylocBot, uzy); hold on;
  xlabel('r (m)');
  ylabel('uz (m)');
  subplot(2,2,2);
  plot(ylocBot, sx1y, 'r-'); hold on;
  plot(ylocTop, sx3y, 'b-'); hold on;
  xlabel('r (m)');
  ylabel('\sigma_x (Pa)');
  subplot(2,2,3);
  plot(ylocBot, sy1y, 'r-'); hold on;
  plot(ylocTop, sy3y, 'b-'); hold on;
  xlabel('r (m)');
  ylabel('\sigma_y (Pa)');
  subplot(2,2,4);
  plot(ylocBot, syz1y, 'r-'); hold on;
  plot(ylocTop, syz3y, 'b-'); hold on;
  xlabel('r (m)');
  ylabel('\sigma_{yz} (Pa)');

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
  xx = xlocBot;
  yy = ones(size(xx))*bb/2;
  zztop = ones(size(xx))*hh/2;
  zzbot = ones(size(xx))*(-hh/2);
  zzmid = zeros(size(xx));

  % Find disp and stresses 
  for jj=1:length(xx)
    [wwbot(jj), sxbot(jj), sybot(jj)] = exactRectPlate(aa, bb, hh, nu, DD, qq, xx(jj), yy(jj), zzbot(jj));
  end

  % Set up location
  xx = xlocTop;
  yy = ones(size(xx))*bb/2;
  zztop = ones(size(xx))*hh/2;
  zzbot = ones(size(xx))*(-hh/2);
  zzmid = zeros(size(xx));

  % Find disp and stresses 
  for jj=1:length(xx)
    [wwtop(jj), sxtop(jj), sytop(jj)] = exactRectPlate(aa, bb, hh, nu, DD, qq, xx(jj), yy(jj), zztop(jj));
  end

  % Plot solution
  figure(1);
  subplot(2,2,1);
  plot(xlocBot, wwbot, 'r--'); 
  subplot(2,2,2);
  plot(xlocBot, sxbot, 'r--'); hold on;
  plot(xlocTop, sxtop, 'b--'); hold on;
  subplot(2,2,3);
  plot(xlocBot, sybot, 'r--'); hold on;
  plot(xlocTop, sytop, 'b--'); hold on;
  
  % Plot error
  figure;
  subplot(2,2,1);
  werr = uzx'-wwbot;
  plot(xlocBot, werr, 'r--'); 
  subplot(2,2,2);
  plot(xlocBot, sx1x'-sxbot, 'r--'); hold on;
  plot(xlocTop, sx3x'-sxtop, 'b--'); hold on;
  subplot(2,2,3);
  plot(xlocBot, sy1x'-sybot, 'r--'); hold on;
  plot(xlocTop, sy3x'-sytop, 'b--'); hold on;

  % Set up location
  yy = ylocBot;
  xx = ones(size(yy))*aa/2;
  zztop = ones(size(yy))*hh/2;
  zzbot = ones(size(yy))*(-hh/2);
  zzmid = zeros(size(yy));

  % Find disp and stresses 
  for jj=1:length(yy)
    [wwbot(jj), sxbot(jj), sybot(jj)] = exactRectPlate(aa, bb, hh, nu, DD, qq, xx(jj), yy(jj), zzbot(jj));
  end

  % Set up location
  yy = ylocTop;
  xx = ones(size(yy))*aa/2;
  zztop = ones(size(yy))*hh/2;
  zzbot = ones(size(yy))*(-hh/2);
  zzmid = zeros(size(yy));

  % Find disp and stresses 
  for jj=1:length(yy)
    [wwtop(jj), sxtop(jj), sytop(jj)] = exactRectPlate(aa, bb, hh, nu, DD, qq, xx(jj), yy(jj), zztop(jj));
  end

  % Plot solution
  figure(2);
  subplot(2,2,1);
  plot(ylocBot, wwbot, 'r--'); 
  subplot(2,2,2);
  plot(ylocBot, sxbot, 'r--'); hold on;
  plot(ylocTop, sxtop, 'b--'); hold on;
  subplot(2,2,3);
  plot(ylocBot, sybot, 'r--'); hold on;
  plot(ylocTop, sytop, 'b--'); hold on;
  
  % Plot error
  figure;
  subplot(2,2,1);
  werr = uzy'-wwbot;
  plot(ylocBot, werr, 'r--', 'LineWidth', 3); 
  xlabel('y (m)', 'FontSize', 18);
  ylabel('Error in w_z (m)', 'FontSize', 18);
  set(gca, 'Linewidth', 3, 'FontName', 'times', 'FontSize', 18);
  subplot(2,2,2);
  plot(ylocBot, sx1y'-sxbot, 'r--', 'LineWidth', 3); hold on;
  plot(ylocTop, sx3y'-sxtop, 'b--', 'LineWidth', 3); hold on;
  xlabel('y (m)', 'FontSize', 18);
  ylabel('Error in \sigma_{xx} (m)', 'FontSize', 18);
  set(gca, 'Linewidth', 3, 'FontName', 'times', 'FontSize', 18);
  subplot(2,2,3);
  plot(ylocBot, sy1y'-sybot, 'r--', 'LineWidth', 3); hold on;
  plot(ylocTop, sy3y'-sytop, 'b--', 'LineWidth', 3); hold on;
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

