clc
clear
close all

% Define material properties
%E = 200e9;
%v = 0.27;
E = 70.0e9;
v = 0.35;

% Define load
%q = -100000;
q = -10000.0;

% Define length, width and thickness
%a = 1;
%b = 1;
a = 2.0e-2;
b = 4.0e-2;
t = a/25;

% Define points throughout plate
%x = 0:0.01:a;
%y = 0:0.01:b;
x = 0:0.01*a:a;
y = 0:0.01*b:b;

% Define number of terms to be used (odd numbers only)
m = 7;
n = m;

% Calculate flexural rigidity
D = E*t^3/(12*(1-v^2));

% Initialise displacement matrix
w = zeros(length(x),length(y));
mx = w;
my = w;
sx = w;
sy = w;

% Calculate vertical displacement at all plate locations
for i = 1:length(x)
    for j = 1:length(y)
        k = 1;
        while k <= m
            l = 1;
            while l <= n
                w_temp = (sin(k*pi*x(i)/a)*sin(l*pi*y(j)/b))/...
                    (k*l*(k^2/a^2+l^2/b^2)^2);
                d2wdx2_temp = ((-k^2*pi^2/a^2)*sin(k*pi*x(i)/a)*sin(l*pi*y(j)/b))/...
                    (k*l*(k^2/a^2+l^2/b^2)^2);
                d2wdy2_temp = ((-l^2*pi^2/b^2)*sin(k*pi*x(i)/a)*sin(l*pi*y(j)/b))/...
                    (k*l*(k^2/a^2+l^2/b^2)^2);
                mx_temp = -D*(d2wdx2_temp+v*d2wdy2_temp);
                my_temp = -D*(d2wdy2_temp+v*d2wdx2_temp);
                w(i,j) = w(i,j) + w_temp;
                mx(i,j) = mx(i,j) + mx_temp;
                my(i,j) = my(i,j) + my_temp;
                l = l + 2;
            end
            k = k + 2;
        end
        w(i,j) = w(i,j)*(16*q/(pi^6*D));
        mx(i,j) = mx(i,j)*(16*q/(pi^6*D));
        my(i,j) = my(i,j)*(16*q/(pi^6*D));
        sx(i,j) = 6*mx(i,j)/t^2;
        sy(i,j) = 6*my(i,j)/t^2;
    end
end

% Plot results
subplot(2,1,1)
plot(w);
subplot(2,1,2)
plot(sx);

% Collate results and export to Excel file
%x=x';
%result_disp(1,2:length(y)+1) = y;
%result_disp(2:length(x)+1,1) = x;
%result_disp(2:length(x)+1,2:length(y)+1) = w;
%result_sx(1,2:length(y)+1) = y;
%result_sx(2:length(x)+1,1) = x;
%result_sx(2:length(x)+1,2:length(y)+1) = sx;
%result_sy(1,2:length(y)+1) = y;
%result_sy(2:length(x)+1,1) = x;
%result_sy(2:length(x)+1,2:length(y)+1) = sy;
%xlswrite('result_analytical.xls',result_disp,'w')
%xlswrite('result_analytical.xls',result_sx,'sx')
%xlswrite('result_analytical.xls',result_sy,'sy')
