load layer1mid.dat
load layer2mid.dat
load layer3mid.dat
load layer4mid.dat
layer1mid = sortrows(layer1mid, 2);
layer2mid = sortrows(layer2mid, 2);
layer3mid = sortrows(layer3mid, 2);
layer4mid = sortrows(layer4mid, 2);

load layer1midel.dat
load layer2midel.dat
load layer3midel.dat
load layer4midel.dat
layer1midel = sortrows(layer1midel, 2);
layer2midel = sortrows(layer2midel, 2);
layer3midel = sortrows(layer3midel, 2);
layer4midel = sortrows(layer4midel, 2);

xloc = layer1mid(:,2);
uz = layer1mid(:,6);
sx1 = layer1mid(:,7);
sy1 = layer1mid(:,8);
sz1 = layer1mid(:,9);
sxy1 = layer1mid(:,10);
syz1 = layer1mid(:,11);
szx1 = layer1mid(:,12);
sx2 = layer2mid(:,7);
sy2 = layer2mid(:,8);
sz2 = layer2mid(:,9);
sxy2 = layer2mid(:,10);
syz2 = layer2mid(:,11);
szx2 = layer2mid(:,12);
sx3 = layer3mid(:,7);
sy3 = layer3mid(:,8);
sz3 = layer3mid(:,9);
sxy3 = layer3mid(:,10);
syz3 = layer3mid(:,11);
szx3 = layer3mid(:,12);
sx4 = layer4mid(:,7);
sy4 = layer4mid(:,8);
sz4 = layer4mid(:,9);
sxy4 = layer4mid(:,10);
syz4 = layer4mid(:,11);
szx4 = layer4mid(:,12);

xlocel = layer1midel(:,2);
sx1el = layer1midel(:,5);
sy1el = layer1midel(:,6);
sz1el = layer1midel(:,7);
sxy1el = layer1midel(:,8);
syz1el = layer1midel(:,9);
szx1el = layer1midel(:,10);
sx2el = layer2midel(:,5);
sy2el = layer2midel(:,6);
sz2el = layer2midel(:,7);
sxy2el = layer2midel(:,8);
syz2el = layer2midel(:,9);
szx2el = layer2midel(:,10);
sx3el = layer3midel(:,5);
sy3el = layer3midel(:,6);
sz3el = layer3midel(:,7);
sxy3el = layer3midel(:,8);
syz3el = layer3midel(:,9);
szx3el = layer3midel(:,10);
sx4el = layer4midel(:,5);
sy4el = layer4midel(:,6);
sz4el = layer4midel(:,7);
sxy4el = layer4midel(:,8);
syz4el = layer4midel(:,9);
szx4el = layer4midel(:,10);

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

