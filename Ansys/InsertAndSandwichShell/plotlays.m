load layer1mids.dat
load layer2mids.dat
load layer3mids.dat
load layer4mids.dat
layer1mids = sortrows(layer1mids, 2);
layer2mids = sortrows(layer2mids, 2);
layer3mids = sortrows(layer3mids, 2);
layer4mids = sortrows(layer4mids, 2);

load layer1midsel.dat
load layer2midsel.dat
load layer3midsel.dat
load layer4midsel.dat
layer1midsel = sortrows(layer1midsel, 2);
layer2midsel = sortrows(layer2midsel, 2);
layer3midsel = sortrows(layer3midsel, 2);
layer4midsel = sortrows(layer4midsel, 2);

xloc = layer1mids(:,2);
uz = layer1mids(:,6);
sx1 = layer1mids(:,7);
sy1 = layer1mids(:,8);
sz1 = layer1mids(:,9);
sxy1 = layer1mids(:,10);
syz1 = layer1mids(:,11);
szx1 = layer1mids(:,12);
sx2 = layer2mids(:,7);
sy2 = layer2mids(:,8);
sz2 = layer2mids(:,9);
sxy2 = layer2mids(:,10);
syz2 = layer2mids(:,11);
szx2 = layer2mids(:,12);
sx3 = layer3mids(:,7);
sy3 = layer3mids(:,8);
sz3 = layer3mids(:,9);
sxy3 = layer3mids(:,10);
syz3 = layer3mids(:,11);
szx3 = layer3mids(:,12);
sx4 = layer4mids(:,7);
sy4 = layer4mids(:,8);
sz4 = layer4mids(:,9);
sxy4 = layer4mids(:,10);
syz4 = layer4mids(:,11);
szx4 = layer4mids(:,12);

xlocel = layer1midsel(:,2);
sx1el = layer1midsel(:,5);
sy1el = layer1midsel(:,6);
sz1el = layer1midsel(:,7);
sxy1el = layer1midsel(:,8);
syz1el = layer1midsel(:,9);
szx1el = layer1midsel(:,10);
sx2el = layer2midsel(:,5);
sy2el = layer2midsel(:,6);
sz2el = layer2midsel(:,7);
sxy2el = layer2midsel(:,8);
syz2el = layer2midsel(:,9);
szx2el = layer2midsel(:,10);
sx3el = layer3midsel(:,5);
sy3el = layer3midsel(:,6);
sz3el = layer3midsel(:,7);
sxy3el = layer3midsel(:,8);
syz3el = layer3midsel(:,9);
szx3el = layer3midsel(:,10);
sx4el = layer4midsel(:,5);
sy4el = layer4midsel(:,6);
sz4el = layer4midsel(:,7);
sxy4el = layer4midsel(:,8);
syz4el = layer4midsel(:,9);
szx4el = layer4midsel(:,10);

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

