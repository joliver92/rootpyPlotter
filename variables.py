from collections import OrderedDict

def variableDictionary(Region,doBreakdown):


  R_minH2P_minH3P_name = "#frac{min(H_{1,1}^{P_a},H_{1,1}^{P_b})}{min(H_{2,1}^{P_a},H_{2,1}^{P_b})}"
  R_HT4PP_H4PP_name= "#frac{H_{T3,1}^{PP}}{H_{3,1}^{PP}}"
  R_HT5PP_H5PP_name= "#frac{H_{T4,1}^{PP}}{H_{4,1}^{PP}}"
  leptonvariables_VR = OrderedDict([
      ('lept1Pt_VR'                        ,{'latex':"p_{T}^{l,leadlep}"  ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
      ('lept2Pt_VR'                        ,{'latex':"p_{T}^{l,sublead}"  ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
      ('mll_RJ_VR'                          ,{'latex':"m_{ll}^{RJ}"        ,'units':'GeV','nbins':20,'xmin':0,'xmax':400}),
  ])

  leptonvariables = OrderedDict([
      ('lepPt[0]'                        ,{'latex':"p_{T}^{l,leadlep}"  ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
      ('lepPt[1]'                        ,{'latex':"p_{T}^{l,sublead}"  ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
      ('mll_RJ'                          ,{'latex':"m_{ll}^{RJ}"        ,'units':'GeV','nbins':20,'xmin':0,'xmax':400}),

  ])

  jetvariables = OrderedDict([
      ('nJet20'                        ,{'latex':"n^{20}_{J}"           ,'units':'1'   ,'nbins':6,'xmin':0,'xmax':6}),
      ('nBJet20_MV2c10_FixedCutBEff_77',{'latex':"n^{20,77}_{b}"        ,'units':'1'   ,'nbins':6,'xmin':0,'xmax':6}),  
      ('jetPt[0]'                        ,{'latex':"p_{T}^{jet,lead}"   ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
      ('jetPt[1]'                        ,{'latex':"p_{T}^{jet,sublead}",'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
  ])

  metvariables = OrderedDict([
    ('met_Et'     ,{'latex':"E_{T}^{miss}"  ,'units':'GeV','nbins':20,'xmin':0,'xmax':400}),

  ])


  twolepton_VR_variables = OrderedDict([
        ('mjj'                           ,{'latex':"m_{jj}"        ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
        ('dphiVP_VR'                     ,{'latex':"#Delta#phi_{V}^{P}"        ,'units':'rad','nbins':16,'xmin':0,'xmax':3.2}   ),
        ('H2PP_VR'                       ,{'latex':"H_{1,1}^{PP}"        ,'units':'GeV','nbins':40,'xmin':0,'xmax':800}),
        ('H5PP_VR'                       ,{'latex':"H_{4,1}^{PP}"        ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
        ('R_minH2P_minH3P_VR'            ,{'latex':"R_minH2P_minH3P_VR"        ,'units':'','nbins':10,'xmin':0,'xmax':1}   ),
        ('RPT_HT5PP_VR'                  ,{'latex':"RPT_HT5PP_VR"        ,'units':'','nbins':10,'xmin':0,'xmax':1}   )
  ])

  twolepton_variables = OrderedDict([

    ('mjj'                           ,{'latex':"m_{jj}"        ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
    ('H2PP'                       ,{'latex':"H_{1,1}^{PP}"        ,'units':'GeV','nbins':40,'xmin':0,'xmax':800}),
    ('H5PP'                       ,{'latex':"H_{4,1}^{PP}"        ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
    ('dphiVP'                     ,{'latex':"#Delta#phi_{V}^{P}"        ,'units':'rad','nbins':16,'xmin':0,'xmax':3.2}   ),
    ('mTl3'                       ,{'latex':"mTl3"        ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
    ('R_minH2P_minH3P'            ,{'latex':R_minH2P_minH3P_name   ,'units':'','nbins':10,'xmin':0,'xmax':1}   ),
    ('RPT_HT5PP'                  ,{'latex':"RPT_HT5PP"        ,'units':'','nbins':10,'xmin':0,'xmax':1}   ),
    ('R_HT5PP_H5PP'                  ,{'latex': R_HT5PP_H5PP_name     ,'units':'','nbins':10,'xmin':0,'xmax':1}   ),
    ('minDphi'                     ,{'latex':"minDphi"        ,'units':'rad','nbins':16,'xmin':0,'xmax':3.2}   ),
    ('H2PP/H4PP'            ,{'latex':"#frac{H_{1,1}^{PP}}{H_{4,1}^{PP}}"        ,'units':'','nbins':10,'xmin':0,'xmax':1}   )
  ])


  ISRvariables = OrderedDict([
    ('MJ'                            ,{'latex':"m_{J}"        ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
    ('MZ'                            ,{'latex':"m_{Z}"        ,'units':'GeV','nbins':20,'xmin':0,'xmax':400}),
    ('PTCM'                          ,{'latex':"P_{T}^{CM}"        ,'units':'GeV','nbins':10,'xmin':0,'xmax':400}),
    ('PTI'                           ,{'latex':"P_{T}^{I}"        ,'units':'GeV','nbins':10,'xmin':0,'xmax':400}),
    ('PTISR'                         ,{'latex':"P_{T}^{ISR}"        ,'units':'GeV','nbins':15,'xmin':0,'xmax':300}),
    ('RISR'                          ,{'latex':"R_{ISR}"        ,'units':'','nbins':10,'xmin':0,'xmax':1}   ),
    ('dphiISRI'                      ,{'latex':"#Delta#phi_{ISR,I}"        ,'units':'rad','nbins':16,'xmin':0,'xmax':3.2}   )
  ])

  ISRvariables_VR = OrderedDict([
    ('MJ_VR'                            ,{'latex':"m_{J}"        ,'units':'GeV','nbins':25,'xmin':0,'xmax':500}),
    ('MZ_VR'                            ,{'latex':"m_{Z}"        ,'units':'GeV','nbins':20,'xmin':0,'xmax':400}),
    ('PTCM_VR'                          ,{'latex':"P_{T}^{CM}"        ,'units':'GeV','nbins':10,'xmin':0,'xmax':400}),
    ('PTI_VR'                           ,{'latex':"P_{T}^{I}"        ,'units':'GeV','nbins':10,'xmin':0,'xmax':400}),
    ('PTISR_VR'                         ,{'latex':"P_{T}^{ISR}"        ,'units':'GeV','nbins':15,'xmin':0,'xmax':300}),
    ('RISR_VR'                          ,{'latex':"R_{ISR}"        ,'units':'','nbins':10,'xmin':0,'xmax':1}   ),
    ('dphiISRI_VR'                      ,{'latex':"#Delta#phi_{ISR,I}"        ,'units':'rad','nbins':16,'xmin':0,'xmax':3.2}   )
  ])


  threeleptonvariables  = OrderedDict([
    ('mTW'                       ,{'latex':"m_{T}^{W}"        ,'units':'GeV','nbins':15,'xmin':0,'xmax':300}),
    ('H4PP'                       ,{'latex':"H_{3,1}^{PP}"        ,'units':'GeV','nbins':20,'xmin':0,'xmax':800}),
    ('RPT_HT4PP'                  ,{'latex':"RPT_HT4PP"        ,'units':'','nbins':10,'xmin':0,'xmax':1}   ),
    ('R_HT4PP_H4PP'                  ,{'latex': R_HT4PP_H4PP_name     ,'units':'','nbins':10,'xmin':0,'xmax':1}   ),
    ('R_minH2P_minH3P'            ,{'latex':R_minH2P_minH3P_name   ,'units':'','nbins':10,'xmin':0,'xmax':1}   )
    ])


  cutflow = OrderedDict([
    ('nJet20'                        ,{'latex':"n^{20}_{J}"           ,'units':'1'   ,'nbins':6,'xmin':0,'xmax':6})
  ])
  
  variableDictionary = OrderedDict()
  #variableDictionary.update(jetvariables)
  #variableDictionary.update(metvariables)

  if "CR2L-VV" or "VR2L_ISR-VV" or "CR2L_ISR-VV" in Region: 
      variableDictionary.update(leptonvariables_VR)
      variableDictionary.update(jetvariables)
      variableDictionary.update(metvariables)
      if "CR2L-VV" in Region: variableDictionary.update(twolepton_VR_variables)
      if "VR2L_ISR-VV" in Region: variableDictionary.update(ISRvariables_VR)
      if "CR2L_ISR-VV" in Region: variableDictionary.update(ISRvariables_VR)

  elif "ISR" in Region:
      variableDictionary.update(leptonvariables)
      variableDictionary.update(jetvariables)
      variableDictionary.update(metvariables)
      variableDictionary.update(ISRvariables)

  elif "2L" in Region:
      variableDictionary.update(leptonvariables)
      variableDictionary.update(jetvariables)
      variableDictionary.update(metvariables)
      variableDictionary.update(twolepton_variables)
  elif "3L" in Region: 
      variableDictionary.update(leptonvariables)
      variableDictionary.update(jetvariables)
      variableDictionary.update(metvariables)
      variableDictionary.update(threeleptonvariables)
  else:   
      #Default 
      variableDictionary.update(leptonvariables)
      variableDictionary.update(jetvariables)
      variableDictionary.update(metvariables)


  if doBreakdown:
      variableDictionary = OrderedDict()
      variableDictionary.update(cutflow)
      


  return variableDictionary 
