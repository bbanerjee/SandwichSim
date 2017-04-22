load laypp1mid.dat
load laypp2mid.dat
load laypp3mid.dat
load laypp4mid.dat
laypp1mid = sortrows(laypp1mid, 2);
laypp2mid = sortrows(laypp2mid, 2);
laypp3mid = sortrows(laypp3mid, 2);
laypp4mid = sortrows(laypp4mid, 2);

load laypp1midel.dat
load laypp2midel.dat
load laypp3midel.dat
load laypp4midel.dat
laypp1midel = sortrows(laypp1midel, 2);
laypp2midel = sortrows(laypp2midel, 2);
laypp3midel = sortrows(laypp3midel, 2);
laypp4midel = sortrows(laypp4midel, 2);

xloc = laypp1mid(:,2);
uz = laypp1mid(:,6);
sx1 = laypp1mid(:,7);
sy1 = laypp1mid(:,8);
sz1 = laypp1mid(:,9);
sxy1 = laypp1mid(:,10);
syz1 = laypp1mid(:,11);
szx1 = laypp1mid(:,12);
sx2 = laypp2mid(:,7);
sy2 = laypp2mid(:,8);
sz2 = laypp2mid(:,9);
sxy2 = laypp2mid(:,10);
syz2 = laypp2mid(:,11);
szx2 = laypp2mid(:,12);
sx3 = laypp3mid(:,7);
sy3 = laypp3mid(:,8);
sz3 = laypp3mid(:,9);
sxy3 = laypp3mid(:,10);
syz3 = laypp3mid(:,11);
szx3 = laypp3mid(:,12);
sx4 = laypp4mid(:,7);
sy4 = laypp4mid(:,8);
sz4 = laypp4mid(:,9);
sxy4 = laypp4mid(:,10);
syz4 = laypp4mid(:,11);
szx4 = laypp4mid(:,12);

xlocel = laypp1midel(:,2);
sx1el = laypp1midel(:,5);
sy1el = laypp1midel(:,6);
sz1el = laypp1midel(:,7);
sxy1el = laypp1midel(:,8);
syz1el = laypp1midel(:,9);
szx1el = laypp1midel(:,10);
sx2el = laypp2midel(:,5);
sy2el = laypp2midel(:,6);
sz2el = laypp2midel(:,7);
sxy2el = laypp2midel(:,8);
syz2el = laypp2midel(:,9);
szx2el = laypp2midel(:,10);
sx3el = laypp3midel(:,5);
sy3el = laypp3midel(:,6);
sz3el = laypp3midel(:,7);
sxy3el = laypp3midel(:,8);
syz3el = laypp3midel(:,9);
szx3el = laypp3midel(:,10);
sx4el = laypp4midel(:,5);
sy4el = laypp4midel(:,6);
sz4el = laypp4midel(:,7);
sxy4el = laypp4midel(:,8);
syz4el = laypp4midel(:,9);
szx4el = laypp4midel(:,10);

figure;
subplot(2,2,1);
plot(xloc, uz);
xlabel('r (m)');
ylabel('uz (m)');
subplot(2,2,2);
plot(xloc, sx1, 'r-'); hold on;
plot(xloc, sx2, 'g-'); hold on;
plot(xloc, sx3, 'b-'); hold on;
plot(xloc, sx4, 'm-'); hold on;
plot(xlocel, sx1el, 'r--'); hold on;
plot(xlocel, sx2el, 'g--'); hold on;
plot(xlocel, sx3el, 'b--'); hold on;
plot(xlocel, sx4el, 'm--'); hold on;
xlabel('r (m)');
ylabel('\sigma_x (Pa)');
subplot(2,2,3);
plot(xloc, sz1, 'r-'); hold on;
plot(xloc, sz2, 'g-'); hold on;
plot(xloc, sz3, 'b-'); hold on;
plot(xloc, sz4, 'm-'); hold on;
plot(xlocel, sz1el, 'r--'); hold on;
plot(xlocel, sz2el, 'g--'); hold on;
plot(xlocel, sz3el, 'b--'); hold on;
plot(xlocel, sz4el, 'm--'); hold on;
xlabel('r (m)');
ylabel('\sigma_z (Pa)');
subplot(2,2,4);
plot(xloc, sxy1, 'r-'); hold on;
plot(xloc, sxy2, 'g-'); hold on;
plot(xloc, sxy3, 'b-'); hold on;
plot(xloc, sxy4, 'm-'); hold on;
plot(xlocel, sxy1el, 'r--'); hold on;
plot(xlocel, sxy2el, 'g--'); hold on;
plot(xlocel, sxy3el, 'b--'); hold on;
plot(xlocel, sxy4el, 'm--'); hold on;
xlabel('r (m)');
ylabel('\sigma_{zx} (Pa)');

