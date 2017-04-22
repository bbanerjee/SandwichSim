function plotMom

  %-----------------------------------
  % The applied load from the Ansys input file
  %-----------------------------------
  totalforce = 20370 + 19555 + 20234 + 20098 + ...
               19962 + 19826 + 19691;
  momentarm = 0.2438E-01 + 0.5080E-03 + 0.5*0.5080E-03;
  max_moment = totalforce*momentarm;
  num_steps = 100;
  load_inc = max_moment/num_steps;

  %-----------------------------------
  % Load the insert stress data
  %-----------------------------------
  load MomEkill_Ins.dat
  sigtimeIns = MomEkill_Ins(:,3);
  sigvalIns = MomEkill_Ins(:,4);
  numElIns = MomEkill_Ins(1,1);
  numStepIns = length(sigvalIns')/numElIns;
  color = [0.9 0.5 0.9];
  sigfail = 300e6;

  p1 = plotStress(load_inc, sigtimeIns, sigvalIns, numElIns, numStepIns, color, sigfail, 0);

  %-----------------------------------
  % Load the adhesive stress data
  %-----------------------------------
  load MomEkill_Adh.dat
  sigtimeAdh = MomEkill_Adh(:,3);
  sigvalAdh = MomEkill_Adh(:,4);
  numElAdh = MomEkill_Adh(1,1);
  numStepAdh = length(sigvalAdh')/numElAdh;
  color = [0.9 0.1 0.1];
  sigfail = 9.65e6;

  p2 = plotStress(load_inc, sigtimeAdh, sigvalAdh, numElAdh, numStepAdh, color, sigfail, 1);

  %-----------------------------------
  % Load the core compressive stress data
  %-----------------------------------
  load MomEkill_CoreC.dat
  sigtimeCoreC = MomEkill_CoreC(:,3);
  sigvalCoreC = MomEkill_CoreC(:,4);
  numElCoreC = MomEkill_CoreC(1,1);
  numStepCoreC = length(sigvalCoreC')/numElCoreC;
  color = [0.1 0.1 0.9];
  sigfail = 2e6;
  
  p3 = plotStress(load_inc, sigtimeCoreC, sigvalCoreC, numElCoreC, numStepCoreC, color, sigfail, 0);
  
  %-----------------------------------
  % Load the core shear stress data
  %-----------------------------------
  load MomEkill_CoreS.dat
  sigtimeCoreS = MomEkill_CoreS(:,3);
  sigvalCoreS = MomEkill_CoreS(:,4);
  numElCoreS = MomEkill_CoreS(1,1);
  numStepCoreS = length(sigvalCoreS')/numElCoreS;
  color = [0.1 0.6 0.1];
  sigfail = 1e6;
  
  p4 = plotStress(load_inc, sigtimeCoreS, sigvalCoreS, numElCoreS, numStepCoreS, color, sigfail, 0);
  
  %-----------------------------------
  % Load the face compressive stress data
  %-----------------------------------
  load MomEkill_FaceC.dat
  sigtimeFaceC = MomEkill_FaceC(:,3);
  sigvalFaceC = MomEkill_FaceC(:,4);
  numElFaceC = MomEkill_FaceC(1,1);
  numStepFaceC = length(sigvalFaceC')/numElFaceC;
  color = [0.4 0.25 0.7];
  sigfail = 500e6;
  
  p5 = plotStress(load_inc, sigtimeFaceC, sigvalFaceC, numElFaceC, numStepFaceC, color, sigfail, 0);

  set([p1 p2 p3 p4 p5], 'Linewidth', 3);
  set(gca, 'LineWidth', 3, 'FontSize', 18, 'FontName', 'times');
  xlabel('Moment (kN-m)', 'FontSize', 18, 'FontName', 'times');
  ylabel('Normalized Stress (\sigma/\sigma_f)', 'FontSize', 18, 'FontName', 'times');
  grid on;
  legend([p1 p2 p3 p4 p5], ...
         'Insert \sigma_{eq}', ...
         'Adhesive \sigma_{xy}', ...
         'Core \sigma_{y}', ...
         'Core \sigma_{xy}', ...
         'Facesheet \sigma_{x}');
  set(gca, 'XLim', [0 1.5], 'YLim', [0 1.2]);
  axis square;
  plot([0 1.5],[1 1],'k--','LineWidth', 2);
  set(gcf, 'Position', [370 317 662 606]);
  
%====================================================
% Plot the stress vs load
%====================================================
function [p] = plotStress(load_inc, sigtime, sigval, numEl, numStep, color, sigfail, flag)

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
    if (flag == 2)
      plot(force(jj,:)*1.0e-3,stress(jj,:)/sigfail,'Color',color); hold on;
    end
  end
  
  %-----------------------------------------------
  % Find the element with the maximum stress
  %-----------------------------------------------
  %[maxStress, maxStep] = max(max(stress));
  %[maxStress, maxElem] = max(stress(:,maxStep));
  [maxStress, maxElem] = max(stress(:,10));

  p = plot(force(maxElem,:)*1.0e-3,stress(maxElem,:)/sigfail,'-','Color',color); hold on;
  load_max = max(max(force))*1.0e-3 ;
  sig_max = max(max(stress))*1.0e-6;
  [load_max sig_max]
