function plotAxial_d

%-----------------------------------
% Load the displacement vs time data
%-----------------------------------
load AxLessShort_Disp.dat
disptime = AxLessShort_Disp(:,2);
dispval = AxLessShort_Disp(:,3);
figure
plot(disptime, dispval, 'x-'); hold on;
%size(disptime)

%-----------------------------------
% Load the load vs time data
%-----------------------------------
load AxLessShort_load.dat
loadtime = AxLessShort_load(:,1);
loadval = AxLessShort_load(:,2);
figure
plot(loadtime, loadval, 'x-'); hold on;
%size(loadtime)
%disptime - loadtime(1:length(loadtime)-1)

%-----------------------------------
% Load the reaction vs time data
%-----------------------------------
load AxLessShort_reac.dat
reactime = AxLessShort_reac(:,1);
reacvalx = AxLessShort_reac(:,2);
reacvaly = AxLessShort_reac(:,3);
plot(reactime, reacvalx, 'rx-'); hold on;
plot(reactime, reacvaly, 'gx-'); hold on;
%size(reactime)
%reactime-loadtime

%-----------------------------------
% Load the load vs. disp data
%-----------------------------------
figure
%plot(-dispval, -loadval(1:length(loadval)-1), 'b-'); hold on;
plot(-dispval, reacvalx(1:length(reacvalx)-1), 'r-'); hold on;
plot(-dispval, reacvaly(1:length(reacvaly)-1), 'g-'); hold on;

%-----------------------------------
% Load the adhesive stress data
%-----------------------------------
load AxLessShort_Adh.dat
sigtime = AxLessShort_Adh(:,3);
sigval = AxLessShort_Adh(:,5);
numEl = AxLessShort_Adh(1,1);
numStep = length(sigval')/numEl;
color = [0.9 0.1 0.1];

%plotStress(loadtime, loadval, reactime, reacvalx, reacvaly, ...
%           sigtime, sigval, numEl, numStep, color);

%-----------------------------------
% Load the core shear stress data
%-----------------------------------
load AxLessShort_CoreS.dat
sigtimeCoreS = AxLessShort_CoreS(:,3);
sigvalCoreS = AxLessShort_CoreS(:,5);
numElCoreS = AxLessShort_CoreS(1,1);
numStepCoreS = length(sigvalCoreS')/numElCoreS;
color = [0.1 0.6 0.1];

%plotStress(loadtime, loadval, reactime, reacvalx, reacvaly, ...
%           sigtimeCoreS, sigvalCoreS, numElCoreS, numStepCoreS, color);

%-----------------------------------
% Load the core compressive stress data
%-----------------------------------
load AxLessShort_CoreC.dat
sigtimeCoreC = AxLessShort_CoreC(:,3);
sigvalCoreC = AxLessShort_CoreC(:,5);
numElCoreC = AxLessShort_CoreC(1,1);
numStepCoreC = length(sigvalCoreC')/numElCoreC;
color = [0.1 0.1 0.9];

%plotStress(loadtime, loadval, reactime, reacvalx, reacvaly, ...
%           sigtimeCoreC, sigvalCoreC, numElCoreC, numStepCoreC, color);

%-----------------------------------
% Load the face compressive stress data
%-----------------------------------
load AxLessShort_FaceC.dat
sigtimeFaceC = AxLessShort_FaceC(:,3);
sigvalFaceC = AxLessShort_FaceC(:,5);
numElFaceC = AxLessShort_FaceC(1,1);
numStepFaceC = length(sigvalFaceC')/numElFaceC;
color = [0.4 0.25 0.7];

%plotStress(loadtime, loadval, reactime, reacvalx, reacvaly, ...
%           sigtimeFaceC, sigvalFaceC, numElFaceC, numStepFaceC, color);

%====================================================
% Plot the stress vs load
%====================================================
function plotStress(loadtime, loadval, reactime, reacvalx, reacvaly, ...
                    sigtime, sigval, numEl, numStep, color)

  %----------------------------------------------------
  % Save the load val for each time in stress data file
  %----------------------------------------------------
  for ii=1:numStep-1
    row = numEl*(ii-1)+1;
    time = sigtime(row);
    for jj=1:length(loadtime)-1
      startTime = loadtime(jj); 
      endTime = loadtime(jj+1); 
      t = (time - startTime)/(endTime-startTime);
      if (t >= 0.0) && (t <= 1.0)
        timeval(ii) = time;
        forceval(ii) = (1-t)*loadval(jj) + t*loadval(jj+1);
        break;
      end
    end
  end
  %plot(timeval, forceval, 'ro-');
  
  %----------------------------------------------------
  % Save the reaction val for each time in stress data file
  %----------------------------------------------------
  for ii=1:numStep-1
    row = numEl*(ii-1)+1;
    time = sigtime(row);
    for jj=1:length(reactime)-1
      startTime = reactime(jj); 
      endTime = reactime(jj+1); 
      t = (time - startTime)/(endTime-startTime);
      if (t >= 0.0) && (t <= 1.0)
        reactimeval(ii) = time;
        reacforceval(ii) = (1-t)*reacvalx(jj) + t*reacvalx(jj+1);
        break;
      end
    end
  end
  %plot(reactimeval, reacforceval, 'mo-');
  
  %-----------------------------------------------
  % Find the right sign for the stress and the load
  %-----------------------------------------------
  maxsig = abs(max(sigval));
  minsig = abs(min(sigval));
  signsig = 1;
  if (minsig > maxsig)
    signsig = -1;
  end
  maxforce = abs(max(forceval));
  minforce = abs(min(forceval));
  signforce = 1;
  if (minforce > maxforce)
    signforce = -1;
  end
  
  %-----------------------------------------------
  % Loop through each element and save load vs sig
  %-----------------------------------------------
  for jj=1:numEl
    for ii=1:length(timeval)
      row = numEl*(ii-1)+jj;
      time = timeval(ii);
      force(jj,ii) = signforce*forceval(ii);
      stress(jj,ii) = signsig*sigval(row);
    end
    %plot(force(jj,:),stress(jj,:)); hold on;
  end
  [maxsig, maxelem] = max(stress(:,length(timeval)));
  %plot(force(maxelem,:)*1.0e-3,stress(maxelem,:)*1.0e-6); hold on;
  plot(force(maxelem,:)*1.0e-3,stress(maxelem,:)/maxsig,'--','Color',color); hold on;
  
  %-----------------------------------------------
  % Loop through each element and save reaction vs sig
  %-----------------------------------------------
  for jj=1:numEl
    for ii=1:length(reactimeval)
      row = numEl*(ii-1)+jj;
      time = reactimeval(ii);
      reac(jj,ii) = reacforceval(ii);
      sig(jj,ii) = signsig*sigval(row);
    end
    %plot(reac(jj,:),sig(jj,:),'r-');
  end
  [maxsig, maxelem] = max(sig(:,length(reactimeval)));
  %plot(reac(maxelem,:)*1.0e-3,sig(maxelem,:)*1.0e-6,'r-'); hold on;
  plot(reac(maxelem,:)*1.0e-3,sig(maxelem,:)/maxsig,'-','Color',color); hold on;
  
