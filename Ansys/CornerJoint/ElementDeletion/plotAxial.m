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
  load AxEkill_Ins.dat
  elemIns = AxEkill_Ins(:,2);
  sigtimeIns = AxEkill_Ins(:,3);
  sigvalIns = AxEkill_Ins(:,4);
  numElIns = AxEkill_Ins(1,1);
  numStepIns = length(sigvalIns')/numElIns;
  color = [0.9 0.5 0.9];
  sigfail = 300e6;

  p1 = plotStress(load_inc, elemIns, sigtimeIns, sigvalIns, numElIns, numStepIns, color, sigfail);

  %-----------------------------------
  % Load the adhesive stress data
  %-----------------------------------
  load AxEkill_Adh.dat
  elemAdh = AxEkill_Adh(:,2);
  sigtimeAdh = AxEkill_Adh(:,3);
  sigvalAdh = AxEkill_Adh(:,4);
  numElAdh = AxEkill_Adh(1,1);
  numStepAdh = length(sigvalAdh')/numElAdh-1;
  color = [0.9 0.1 0.1];
  sigfail = 9.65e6;

  p2 = plotStress(load_inc, elemAdh, sigtimeAdh, sigvalAdh, numElAdh, numStepAdh, color, sigfail);

  %-----------------------------------
  % Load the core compressive stress data
  %-----------------------------------
  load AxEkill_CoreC.dat
  elemCoreC = AxEkill_CoreC(:,2);
  sigtimeCoreC = AxEkill_CoreC(:,3);
  sigvalCoreC = AxEkill_CoreC(:,4);
  numElCoreC = AxEkill_CoreC(1,1);
  numStepCoreC = length(sigvalCoreC')/numElCoreC;
  color = [0.1 0.1 0.9];
  sigfail = 2e6;
  
  p3 = plotStress(load_inc, elemCoreC, sigtimeCoreC, sigvalCoreC, numElCoreC, numStepCoreC, color, sigfail);
  
  %-----------------------------------
  % Load the core shear stress data
  %-----------------------------------
  load AxEkill_CoreS.dat
  elemCoreS = AxEkill_CoreS(:,2);
  sigtimeCoreS = AxEkill_CoreS(:,3);
  sigvalCoreS = AxEkill_CoreS(:,4);
  numElCoreS = AxEkill_CoreS(1,1);
  numStepCoreS = length(sigvalCoreS')/numElCoreS;
  color = [0.1 0.6 0.1];
  sigfail = 1e6;
  
  p4 = plotStress(load_inc, elemCoreS, sigtimeCoreS, sigvalCoreS, numElCoreS, numStepCoreS, color, sigfail);
  
  %-----------------------------------
  % Load the face compressive stress data
  %-----------------------------------
  load AxEkill_FaceC.dat
  elemFaceC = AxEkill_FaceC(:,2);
  sigtimeFaceC = AxEkill_FaceC(:,3);
  sigvalFaceC = AxEkill_FaceC(:,4);
  numElFaceC = AxEkill_FaceC(1,1);
  numStepFaceC = length(sigvalFaceC')/numElFaceC;
  color = [0.4 0.25 0.7];
  sigfail = 500e6;
  
  p5 = plotStress(load_inc, elemFaceC, sigtimeFaceC, sigvalFaceC, numElFaceC, numStepFaceC, color, sigfail);

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
  set(gca, 'XLim', [0 120], 'YLim', [0 1.2]);
  axis square;
  plot([0 120],[1 1],'k--','LineWidth', 2);
  set(gcf, 'Position', [370 317 662 606]);
  
%====================================================
% Plot the stress vs load
%====================================================
function [p] = plotStress(load_inc, elem, sigtime, sigval, numEl, numStep, color, sigfail)

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
      el(jj,ii) = elem(row);
    end
    %plot(force(jj,:)*1.0e-3,stress(jj,:)/sigfail,'Color',color); hold on;
  end
  
  %-----------------------------------------------
  % Find the element with the maximum stress
  %-----------------------------------------------
  %[maxStress, maxStep] = max(max(stress));
  %[maxStress, maxElem] = max(stress(:,maxStep));
  [maxStress, maxElem] = max(stress(:,10));
  element = el(maxElem,1);

  p = plot(force(maxElem,:)*1.0e-3,stress(maxElem,:)/sigfail,'-','Color',color); hold on;
  load_max = max(max(force))*1.0e-3 ;
  sig_max = max(max(stress))*1.0e-6;
  [element load_max sig_max]
