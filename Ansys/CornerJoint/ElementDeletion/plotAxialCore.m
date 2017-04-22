function plotAxial

  %-----------------------------------
  % The applied load from the Ansys input file
  %-----------------------------------
  max_load = 230855;
  num_steps = 100;
  load_inc = max_load/num_steps;

  %-----------------------------------
  % Load the insert stress data
  %-----------------------------------
  load AxEkillCore_Ins.dat
  sigtimeIns = AxEkillCore_Ins(:,3);
  sigvalIns = AxEkillCore_Ins(:,4);
  numElIns = AxEkillCore_Ins(1,1);
  numStepIns = length(sigvalIns')/numElIns;
  color = [0.9 0.5 0.9];
  sigfail = 300e6;

  p1 = plotStress(load_inc, sigtimeIns, sigvalIns, numElIns, numStepIns, color, sigfail);

  %-----------------------------------
  % Load the adhesive stress data
  %-----------------------------------
  load AxEkillCore_Adh.dat
  sigtimeAdh = AxEkillCore_Adh(:,3);
  sigvalAdh = AxEkillCore_Adh(:,4);
  numElAdh = AxEkillCore_Adh(1,1);
  numStepAdh = length(sigvalAdh')/numElAdh-1;
  color = [0.9 0.1 0.1];
  sigfail = 10e6;

  p2 = plotStress(load_inc, sigtimeAdh, sigvalAdh, numElAdh, numStepAdh, color, sigfail);

  %-----------------------------------
  % Load the core compressive stress data
  %-----------------------------------
  load AxEkillCore_CoreC.dat
  sigtimeCoreC = AxEkillCore_CoreC(:,3);
  sigvalCoreC = AxEkillCore_CoreC(:,4);
  numElCoreC = AxEkillCore_CoreC(1,1);
  numStepCoreC = length(sigvalCoreC')/numElCoreC;
  color = [0.1 0.1 0.9];
  sigfail = 2e6;
  
  p3 = plotStress(load_inc, sigtimeCoreC, sigvalCoreC, numElCoreC, numStepCoreC, color, sigfail);
  
  %-----------------------------------
  % Load the core shear stress data
  %-----------------------------------
  load AxEkillCore_CoreS.dat
  sigtimeCoreS = AxEkillCore_CoreS(:,3);
  sigvalCoreS = AxEkillCore_CoreS(:,4);
  numElCoreS = AxEkillCore_CoreS(1,1);
  numStepCoreS = length(sigvalCoreS')/numElCoreS;
  color = [0.1 0.6 0.1];
  sigfail = 1e6;
  
  p4 = plotStress(load_inc, sigtimeCoreS, sigvalCoreS, numElCoreS, numStepCoreS, color, sigfail);
  
  %-----------------------------------
  % Load the face compressive stress data
  %-----------------------------------
  load AxEkillCore_FaceC.dat
  sigtimeFaceC = AxEkillCore_FaceC(:,3);
  sigvalFaceC = AxEkillCore_FaceC(:,4);
  numElFaceC = AxEkillCore_FaceC(1,1);
  numStepFaceC = length(sigvalFaceC')/numElFaceC;
  color = [0.4 0.25 0.7];
  sigfail = 500e6;
  
  p5 = plotStress(load_inc, sigtimeFaceC, sigvalFaceC, numElFaceC, numStepFaceC, color, sigfail);

  set([p1 p2 p3 p4 p5], 'Linewidth', 3);
  set(gca, 'LineWidth', 3, 'FontSize', 18, 'FontName', 'times');
  xlabel('Load (kN)', 'FontSize', 18, 'FontName', 'times');
  ylabel('Normalized Stress (\sigma/\sigma_f)', 'FontSize', 18, 'FontName', 'times');
  grid on;
  legend([p1 p2 p3 p4 p5], ...
         'Insert \sigma_{eq}', ...
         'Adhesive \sigma_{xy}', ...
         'Core \sigma_{y}', ...
         'Core \sigma_{xy}', ...
         'Facesheet \sigma_{x}');
  set(gca, 'XLim', [0 230], 'YLim', [0 2]);
  axis square;
  plot([0 230],[1 1],'k--','LineWidth', 2);
  set(gcf, 'Position', [370 317 662 606]);
  
%====================================================
% Plot the stress vs load
%====================================================
function [p] = plotStress(load_inc, sigtime, sigval, numEl, numStep, color, sigfail)

  %-----------------------------------------------
  % Find the right sign for the stress and the load
  %-----------------------------------------------
  maxsig = abs(max(sigval));
  minsig = abs(min(sigval));
  signsig = 1;
  if (minsig > maxsig)
    signsig = -1;
  end
  
  %-----------------------------------------------
  % Loop through each element and save load vs sig
  %-----------------------------------------------
  for jj=1:numEl
    for ii=1:numStep
      row = numEl*(ii-1)+jj;
      time = sigtime(row);
      force(jj,ii) = time*load_inc;
      stress(jj,ii) = signsig*sigval(row);
    end
    %plot(force(jj,:)*1.0e-3,stress(jj,:)/sigfail,'Color',color); hold on;
  end
  
  %-----------------------------------------------
  % Find the element with the maximum stress
  %-----------------------------------------------
  [maxStress, maxStep] = max(max(stress));
  [maxStress, maxElem] = max(stress(:,maxStep));

  p = plot(force(maxElem,:)*1.0e-3,stress(maxElem,:)/sigfail,'-','Color',color); hold on;
  load_max = max(max(force))*1.0e-3 ;
  sig_max = max(max(stress))*1.0e-6;
  [load_max sig_max]
