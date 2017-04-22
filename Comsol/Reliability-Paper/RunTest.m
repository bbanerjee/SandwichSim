function RunTest( x, sCase, inParams, bWarning )
if( nargin < 4 ) bWarning = false; end

global g_Load;

switch sCase
  case 1
    fname_0 = 'MCTest1D';
    inDir   = 'Insert1D';
    outDir  = 'Data_MC';
    f_0     = inParams.f;
    n_0     = inParams.n;
    sCase_0 = 1;
  case 2
    fname_0 = 'MCTest2D';
    inDir   = 'Insert2D';
    outDir  = 'Data_MC';
    f_0     = inParams.f;
    n_0     = inParams.n;
    sCase_0 = 1;
  case 3
    fname_0 = 'FormTest1D';
    inDir   = 'Insert1D';
    outDir  = 'Data_FORM';
    f_0     = inParams.f;
    sCase_0 = 2;
  case 4
    fname_0 = 'FormTest2D';
    inDir   = 'Insert2D';
    outDir  = 'Data_FORM';
    f_0     = inParams.f;
    sCase_0 = 2;
  case 5
    fname_0 = 'LineTest1D';
    inDir   = 'Insert1D';
    outDir  = 'Data_LINE';
    f_0     = inParams.f;
    n_0     = inParams.n;
    sCase_0 = 3;
  case 6
    fname_0 = 'LineTest2D';
    inDir   = 'Insert2D';
    outDir  = 'Data_LINE';
    f_0     = inParams.f;
    n_0     = inParams.n;
    sCase_0 = 3;
  case 7
    fname_0 = 'SubTest1D';
    inDir   = 'Insert1D';
    outDir  = 'Data_SUB';
    f_0     = inParams.f;
    nL_0    = inParams.nLevels;
    nN_0    = inParams.nN;
    nP_0    = inParams.nP;
    pW_0    = inParams.pWin;
    sCase_0 = 4;
  case 8
    fname_0 = 'SubTest1D';
    inDir   = 'Insert2D';
    outDir  = 'Data_SUB';
    f_0     = inParams.f;
    nL_0    = inParams.nLevels;
    nN_0    = inParams.nN;
    nP_0    = inParams.nP;
    pW_0    = inParams.pWin;
    sCase_0 = 4;
end

for i = 1:length(x)
  g_Load = x(i);
  fname = strcat( fname_0, num2str(g_Load) );
  switch sCase_0
    case 1
      n = n_0( min(length(n_0),i) ); 
      [tmp] = MonteCarlo( n, 100, f_0, inDir, outDir, fname );
    case 2
      [tmp] = Form( f_0, inDir, outDir, fname );
    case 3
      n = n_0( min(length(n_0),i) );
      [tmp] = LineSamp( f_0, n, inDir, outDir, fname );
    case 4
      nL = nL_0( min(length(nL_0),i) );
      nN = nN_0( min(length(nN_0),i) );
      nP = nP_0( min(length(nP_0),i) );
      pW = pW_0( min(length(pW_0),i) );
      [tmp] = SubsetSamp( nL, nN, nP, pW, f_0, inDir, outDir, fname );
  end
  if( bWarning )
    warning( strcat('Load=', num2str(g_Load), ' complete.' ) );
  end
end
    
