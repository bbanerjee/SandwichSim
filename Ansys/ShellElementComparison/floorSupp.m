function floorSupp

  h1 = 1.65;
  h2 = 1.0;
  h3 = 0.04;
  h4 = 0.2554;
  h5 = 0.215;
  h6 = 0.68;
  h7 = 0.845;
  h8 = h1 - h6;
  h9 = h8 - h7;

  v1 = 0.14;
  v2 = 0.7;
  v3 = 0.53;
  v4 = 0.3;
  v5 = 0.3402;
  v6 = v5 + h9;
  v7 = v3 - v6;

  x(1) = -h2;
  x(2) = 0;
  x(3) = 0;
  x(4) = -(h6 - h4);
  x(5) = x(4);
  x(6) = -h5;
  x(7) = x(6);
  x(8) = -h6;
  x(9) = x(8);
  x(10) = -h1;
  x(11) = x(10);
  x(12) = -h3;
  x(13) = x(12);
  x(14) = x(1);

  y(1) = 0;
  y(2) = 0;
  y(3) = v2 + v3 - v4;
  y(4) = y(3);
  y(7) = v2 + v3;
  y(5) = y(4) + (y(7)-y(4))/3;
  y(6) = y(4) + (y(7)-y(4))*2/3;
  y(8) = y(7);
  y(9) = y(8) - v6;
  y(10) = y(9);
  y(11) = y(10) - v7;
  y(12) = y(11);
  y(13) = v1;
  y(14) = y(13);

  %plot(x,y);

  xx = [x(1:2) -x(1) -x(14:-1:4) x(3:14) x(1)];
  yy = [y(1:2) y(1) y(14:-1:4) y(3:14) y(1)];

  [xx, yy, A, cx, cy, Ixx, Iyy] = calcAreaMoment(xx,yy)
  plot(xx,yy); hold on;
  plot(0, 0, 'r+');

%====================================================
% Calculate area
%
function [A] = calcArea(xx,yy)

  A = 0;
  for ii=1:length(xx)-1
    A = A + xx(ii)*yy(ii+1) - xx(ii+1)*yy(ii);
  end
  A = A/2;

%====================================================
% Calculate area and centroid
%
function [A, cx, cy] = calcAreaCentroid(xx,yy)

  A = calcArea(xx, yy);
  cx = 0;
  cy = 0;
  for ii=1:length(xx)-1
    cx = cx + (xx(ii)*yy(ii+1) - xx(ii+1)*yy(ii))*(xx(ii)+xx(ii+1));
    cy = cy + (xx(ii)*yy(ii+1) - xx(ii+1)*yy(ii))*(yy(ii)+yy(ii+1));
  end
  cx = cx/(6*A);
  cy = cy/(6*A);

%====================================================
% Calculate moment of inertia
%
function [xx, yy, A, cx, cy, Ixx, Iyy] = calcAreaMoment(xx,yy)

  [A, cx, cy] = calcAreaCentroid(xx,yy);
  
  xx = xx - cx;
  yy = yy - cy;

  Ixx = 0;
  Iyy = 0;
  for ii=1:length(xx)-1
    Ixx = Ixx + (xx(ii+1) - xx(ii))*(yy(ii+1) + yy(ii))*(yy(ii+1)^2 + yy(ii)^2);
    Iyy = Iyy + (yy(ii+1) - yy(ii))*(xx(ii+1) + xx(ii))*(xx(ii+1)^2 + xx(ii)^2);
  end
  Ixx = -Ixx/(12);
  Iyy = Iyy/(12);
  
