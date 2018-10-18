from ROOT import TColor
from ROOT import kBlack,kWhite,kGray,kRed,kPink,kMagenta,kViolet,kBlue,kAzure,kCyan,kTeal,kGreen,kSpring,kYellow,kOrange
from collections import OrderedDict
#____________________________________________________________________________
def sampleConfiguration(DataPeriods):

  # Blues
  myLighterBlue=kAzure-2
  myLightBlue  =TColor.GetColor('#9ecae1')
  myMediumBlue =TColor.GetColor('#0868ac')
  myDarkBlue   =TColor.GetColor('#08306b')

  # Greens
  myLightGreen   =TColor.GetColor('#c7e9c0')
  myMediumGreen  =TColor.GetColor('#41ab5d')
  myDarkGreen    =TColor.GetColor('#006d2c')

  # Oranges
  myLighterOrange=TColor.GetColor('#ffeda0')
  myLightOrange  =TColor.GetColor('#fec49f')
  myMediumOrange =TColor.GetColor('#fe9929')

  # Greys
  myLightestGrey=TColor.GetColor('#f0f0f0')
  myLighterGrey=TColor.GetColor('#e3e3e3')
  myLightGrey  =TColor.GetColor('#969696')

  # Pinks
  myLightPink = TColor.GetColor('#fde0dd')
  myMediumPink = TColor.GetColor('#fcc5c0')
  myDarkPink = TColor.GetColor('#dd3497')


  data_suffix = '_merged_processed.root'
  bkg_suffix='_merged_processed.root'

  ttbar_suffix='_merged_processed.root'
  ttbar_dilep_suffix='_dilep_merged_processed.root'
  sig_suffix='_merged_processed.root'

  samplesDictionary1516 = OrderedDict([
    ('data1516'         ,{'type':'data', 'year':'1516',  'legend':'Data'       ,   'fillcolor':0              , 'linecolor':0,  'filename': 'data15-16'+data_suffix}),
  #  'data17'         :{'type':'data', 'year':'1516',  'legend':'Data'       ,   'fillcolor':0              , 'linecolor':0,  'filename': 'data15-16'+data_suffix},
   # 'data17'           :{'type':'data', 'year':'17'  ,  'legend':'Data'       ,   'fillcolor':0              , 'linecolor':0,  'filename': 'data17'+data_suffix},
   # 'data18'           :{'type':'data', 'year':'18'  ,  'legend':'Data'       ,   'fillcolor':0              , 'linecolor':0,  'filename': 'data18'+data_suffix},
    ('ttbar1516'        ,{'type':'bkg' , 'year':'1516',  'legend':'t#bar{t}'   ,   'fillcolor':myDarkBlue     , 'filename':'ttbar'+ttbar_dilep_suffix}),
    ('singleTop1516'    ,{'type':'bkg' , 'year':'1516',  'legend':'Single top' ,   'fillcolor':myMediumBlue   , 'filename':'singleTop'+bkg_suffix}),
    ('topOther1516'     ,{'type':'bkg' , 'year':'1516',  'legend':'Top other'  ,   'fillcolor':myLightBlue    , 'filename':'topOther'+bkg_suffix}),
    ('Zjets1516'        ,{'type':'bkg' , 'year':'1516',  'legend':'Z+jets'     ,   'fillcolor':myMediumGreen  , 'filename':'Zjets'+bkg_suffix}),
    ('Wjets1516'        ,{'type':'bkg' , 'year':'1516',  'legend':'W+jets'     ,   'fillcolor':myLightGreen   , 'filename':'Wjets'+bkg_suffix}),
    ('diboson1516'      ,{'type':'bkg' , 'year':'1516',  'legend':'Diboson'    ,   'fillcolor':myMediumOrange , 'filename':'diboson'+bkg_suffix}),
    ('triboson1516'     ,{'type':'bkg' , 'year':'1516',  'legend':'Triboson'   ,   'fillcolor':myLightOrange  , 'filename':'triboson'+bkg_suffix}),
  #  'Vgamma1516'       :{'type':'bkg' , 'year':'1516',  'legend':'V+gamma'    ,   'fillcolor':myLighterOrange, 'filename':'Vgamma'+bkg_suffix},
    ('higgs1516'        ,{'type':'bkg' , 'year':'1516',  'legend':'Higgs'      ,   'fillcolor':myDarkPink     , 'filename':'higgs'+bkg_suffix}),
    ('lowMassDY1516'    ,{'type':'bkg' , 'year':'1516',  'legend':'Low mass DY',   'fillcolor':myLightGrey    , 'filename':'lowMassDY'+bkg_suffix})]
  #  'signal1516'        :{'type':'sig' , 'year':'1516',  'legend':'Signal'     ,   'fillcolor':0  , 'linecolor': kRed+2, 'filename':'Zjets'+bkg_suffix}
  )

  samplesDictionary17 = OrderedDict([
    ('data17'         ,{'type':'data', 'year':'17',  'legend':'Data'       ,   'fillcolor':0              , 'linecolor':0,  'filename': 'data17'+data_suffix}),
    ('ttbar17'        ,{'type':'bkg' , 'year':'17',  'legend':'t#bar{t}'   ,   'fillcolor':myDarkBlue     , 'filename':'ttbar'+ttbar_dilep_suffix}),
    ('singleTop17'    ,{'type':'bkg' , 'year':'17',  'legend':'Single top' ,   'fillcolor':myMediumBlue   , 'filename':'singleTop'+bkg_suffix}),
    ('topOther17'     ,{'type':'bkg' , 'year':'17',  'legend':'Top other'  ,   'fillcolor':myLightBlue    , 'filename':'topOther'+bkg_suffix}),
    ('Zjets17'        ,{'type':'bkg' , 'year':'17',  'legend':'Z+jets'     ,   'fillcolor':myMediumGreen  , 'filename':'Zjets'+bkg_suffix}),
    ('Wjets17'        ,{'type':'bkg' , 'year':'17',  'legend':'W+jets'     ,   'fillcolor':myLightGreen   , 'filename':'Wjets'+bkg_suffix}),
    ('diboson17'      ,{'type':'bkg' , 'year':'17',  'legend':'Diboson'    ,   'fillcolor':myMediumOrange , 'filename':'diboson'+bkg_suffix}),
    ('triboson17'     ,{'type':'bkg' , 'year':'17',  'legend':'Triboson'   ,   'fillcolor':myLightOrange  , 'filename':'triboson'+bkg_suffix}),
  #  'Vgamma1516'       :{'type':'bkg' , 'year':'1516',  'legend':'V+gamma'    ,   'fillcolor':myLighterOrange, 'filename':'Vgamma'+bkg_suffix},
    ('higgs17'        ,{'type':'bkg' , 'year':'17',  'legend':'Higgs'      ,   'fillcolor':myDarkPink     , 'filename':'higgs'+bkg_suffix}),
    ('lowMassDY17'    ,{'type':'bkg' , 'year':'17',  'legend':'Low mass DY',   'fillcolor':myLightGrey    , 'filename':'lowMassDY'+bkg_suffix})]
  )

  samplesDictionary18 = OrderedDict([
    ('data18'         ,{'type':'data', 'year':'18',  'legend':'Data'       ,   'fillcolor':0              , 'linecolor':0,  'filename': 'data18'+data_suffix}),
    ('ttbar18'        ,{'type':'bkg' , 'year':'18',  'legend':'t#bar{t}'   ,   'fillcolor':myDarkBlue     , 'filename':'ttbar'+ttbar_suffix}),
    ('singleTop18'    ,{'type':'bkg' , 'year':'18',  'legend':'Single top' ,   'fillcolor':myMediumBlue   , 'filename':'singleTop'+bkg_suffix}),
    ('topOther18'     ,{'type':'bkg' , 'year':'18',  'legend':'Top other'  ,   'fillcolor':myLightBlue    , 'filename':'topOther'+bkg_suffix}),
    ('Zjets18'        ,{'type':'bkg' , 'year':'18',  'legend':'Z+jets'     ,   'fillcolor':myMediumGreen  , 'filename':'Zjets'+bkg_suffix}),
    ('Wjets18'        ,{'type':'bkg' , 'year':'18',  'legend':'W+jets'     ,   'fillcolor':myLightGreen   , 'filename':'Wjets'+bkg_suffix}),
    ('diboson18'      ,{'type':'bkg' , 'year':'18',  'legend':'Diboson'    ,   'fillcolor':myMediumOrange , 'filename':'diboson'+bkg_suffix}),
    ('triboson18'     ,{'type':'bkg' , 'year':'18',  'legend':'Triboson'   ,   'fillcolor':myLightOrange  , 'filename':'triboson'+bkg_suffix})]
  )

  samplesDictionary = OrderedDict()
  if DataPeriods == '1516':
    samplesDictionary.update(samplesDictionary1516)
  elif DataPeriods == '17':
    samplesDictionary.update(samplesDictionary17)
  elif DataPeriods == '18':
    samplesDictionary.update(samplesDictionary18)
  elif DataPeriods == '15-17':
    samplesDictionary.update(samplesDictionary1516)
    samplesDictionary.update(samplesDictionary17)
  elif DataPeriods == '15-18':
    samplesDictionary.update(samplesDictionary1516)
    samplesDictionary.update(samplesDictionary17)
    samplesDictionary.update(samplesDictionary18)
  elif DataPeriods == '17-18':
    samplesDictionary.update(samplesDictionary17)
    samplesDictionary.update(samplesDictionary18)


  return samplesDictionary


