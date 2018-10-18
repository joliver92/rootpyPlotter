from collections import OrderedDict

def variableDict(variable):
      
      leptonvariables = OrderedDict([
          

      ])
      
      standardvariables = OrderedDict([
          ('nJet20'                        ,{'latex':"n^{20}_{J}"           ,'units':''   ,'nbins':6,'xmin':0,'xmax':6}),
          ('nBJet20_MV2c10_FixedCutBEff_77',{'latex':"n^{20,77}_{b}"        ,'units':''   ,'nbins':6,'xmin':0,'xmax':6}),   
          ('lepPt[0]'                        ,{'latex':"p_{T}^{l,leadlep}"  ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
          ('lepPt[1]'                        ,{'latex':"p_{T}^{l,sublead}"  ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
          ('jetPt[0]'                        ,{'latex':"p_{T}^{jet,lead}"   ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
          ('jetPt[1]'                        ,{'latex':"p_{T}^{jet,sublead}",'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
          ('mll_RJ'                          ,{'latex':"m_{ll}^{RJ}"        ,'units':'GeV','nbins':20,'xmin':0,'xmax':400}),
          #('lepPt[2]'                        ,{'latex':"p_{T}^{subsublead}"   ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
          ('mll_RJ',{'nbins':0, 'xmin':0,'xmax':6,'units':'','latex':"n^{20}_{J}"}),
          ('lepPt[0]',{'nbins':0, 'xmin':0,'xmax':6,'units':'','latex':"n^{20}_{J}"}),
          #add mechanism to automatically calculate the Events/X where X = ( xmax - xmin)/nbins 
          # N-1 cuts... not really automated. 
          #add mechanism that if units are MeV the conversion takes place. 
  )




nJet20              0     6   6   n^{20}_{J}              Entries               Plot
mll_RJ              0     400 20  m_{ll}                Entries/20GeV    Plot

lepPt[3]            0     500 25   p_{T}^{l4}     Entries/20GeV       nPlot
met_Et              0     400 20  E_{T}^{miss}[GeV]  Events/20GeV     Plot

nBJet20_MV2c10_FixedCutBEff_77  0  6  6  n^{20,77}_{b} Entries Plot
mjj 0 500 25 m_{jj} Entries/20GeV Plot
dphiVP 0 3.2 16 #Delta#phi_V^P Entries/0.2rad Plot
mTl3 0 500 25 mTl3 Entries/20GeV   Plot
H5PP 0 800 20 H_{4,1}^{PP} Entries/40GeV Plot
R_minH2P_minH3P 0 1 10 #frac{min(H_{1,1}^{P_a},H_{1,1}^{P_b})}{min(H_{2,1}^{P_a},H_{2,1}^{P_b})} Entries/0.1 Plot
H2PP 0 800 20 H_{1,1}^{PP} Entries/20GeV Plot
RPT_HT5PP 0 1 20 #frac{p_{TPP}^{lab}}{p_{TPP}^{lab}+H_{T4,1}^{PP}} Entries/0.05 Plot
H2PP/H4PP 0 1 20 #frac{H_{1,1}^{PP}}{H_{4,1}^{PP}} Entries/0.05 Plot
minDphi 0 3.2 16 min#Delta#phi(j1/j2,#vec{p}_{T}^{miss}) Entries/0.2rad Plot
