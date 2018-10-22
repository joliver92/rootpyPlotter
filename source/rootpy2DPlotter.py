###############################################################################
###############################################################################
###############################################################################

# WHAT I WANT
# SCALABLE PLOTS 
# RATIO PLOT ON OR OFF. I.E AUTO RESCALING
# COLOR SCHEME AUTOMATIC.
# EASY LOOP THROUGH VARIABLES
# EASY LIST BACKGROUNDS 
# SCALE EACH RUN OF BACKGROUNDS SEPERATELY.
# EASY LIST DATA SAMPLES
# EASY LIST SIGNAL SAMPLES 
# PLOT OPTIONS
#    COMPARISONS
#    STACK 
#    DATA/MC vs DATA-MC 

#from plotfunctions import *

#import ROOT
import os.path
import sys
import math
import argparse
from rootpy import ROOT 
from rootpy.io import root_open 
from rootpy.plotting import F1, Hist, HistStack, Canvas, Legend, Pad,Hist2D
from rootpy.plotting.shapes import Line,Arrow
from rootpy.plotting.utils  import draw
from rootpy.plotting.views import StackView
from rootpy.plotting.style  import get_style, set_style
from rootpy import asrootpy
from rootpy.tree import Cut
from rootpy.tree import Tree


from regiondefinitions import retreiveRegionInformation
from samples import sampleConfiguration
from itertools import izip
from decimal import Decimal
import time 

t0 = time.time()


ROOT.gROOT.SetBatch(True)
Hist.SetDefaultSumw2(True)


# Instantiate the parser
parser = argparse.ArgumentParser(description='Optional app description')

parser.add_argument('--output'         , '-o' , type=str, default="rootpyoutput", help='Provide a location for output of Plots')
parser.add_argument('--systematics'    , '-s' , default="Nominal", help='Which Systematic Tree to run over? [Nominal] ')
parser.add_argument('--region'         , '-r' , type=str, default ="RJ2LA", help='Specify which Region you wish to run over [See regiondefinitions.py]'  )

parser.add_argument('--ratioplot'      , '-rp', type=bool, default=True, help='produce Ratio subplot [None, Ratio, Residual]')
parser.add_argument('--nminus1'        , '-n' , type=bool, default=False, help='Produce N-1 plots for each variable parsed [True, False]')
parser.add_argument('--regionbreakdown', '-c' , type=bool, default=False, help='Produce a breakdown of the Region [True, False]')
parser.add_argument('--dataperiods'    , '-p' , type=str , default='1516', help='Specify which data periods to include. Options: [1516, 17, 18, 15-17, 15-18]')


args = parser.parse_args()

#print args
print "outputfolder: " + args.output
print "systematics:  " + args.systematics
print "region      : " + args.region
print "regionplot  : " + str(int(args.ratioplot))
print "Nminus1     : " + str(args.nminus1 )
print "regionbreakdown: " + str(args.regionbreakdown)
print "region dataperiod: " + args.dataperiods 


DataPeriods = args.dataperiods 
Region = args.region 
doregionbreakdown = args.regionbreakdown
outputfolder = args.output
systematics  = args.systematics 
doRatio      = int(args.ratioplot )
donminus1    = args.nminus1 






atlasStatus="Internal"

canvaswidth = 1500
canvasheight= 1600

###############################################################################
############################################################################### Variable Treatment 
###############################################################################

MeVlist = ['IaPP/(IaPP+IbPP)','IbPP/(IaPP+IbPP)','IaPa/(IaPa+IbPb)','IbPb/(IaPa+IbPb)','IaLAB/(IaLAB+IbLAB)','IbLAB/(IaLAB+IbLAB)','dphilep1MET','dphilep2MET','dphilep3MET','R_HT4PP_H4PP','dphiVP_VR','RPT_HT5PP_VR','R_minH2P_minH3P_VR','nJet30','mu','RPT_HT4PP','RISR','dphiISRI','R_HT5PP_H5PP','RPT_HT5PP','R_H3Pa_H3Pb','dangle','R_minH2P_minH3P','dphiPPV','cosPP','minDphi','dphiVP',"met_phi","jet1Eta",'lept1Eta',"jet1Phi","lept1Phi","jet2Eta",'lept2Eta',"jet2Phi","lept2Phi","jet3Eta",'lept3Eta',"jet3Phi","lept3Phi","jet4Eta","jet4Phi","EventNumber","NjS","NjISR","nBJet20_MV2c10_FixedCutBEff_77","mu","is2Lep2Jet","is2L2JInt","dRll"
        ]
###############################################################################
############################################################################### Style 
###############################################################################
style = get_style('ATLAS')
titlesize=25
labelscale = 0.025
titlesize=canvasheight*labelscale*1.4
style.SetTitleSize(titlesize, "x")
style.SetTitleSize(titlesize,"y")
style.SetTitleYOffset(1)
style.SetTitleXOffset(1)
set_style(style)
ROOT.gStyle.SetPadBottomMargin(0.2)
ROOT.gStyle.SetPadRightMargin(0.2)
ROOT.gStyle.SetLineWidth(4)
ROOT.gStyle.SetPalette(1);
#ROOT.gStyle.SetPalette("kBird")

#ROOT.gPad.SetBorderWidth(5)  

labelmargin=0.20 #Labeling

#==================== EDIT THESE ========================#
sqrts  = 13
# Region = str(sys.argv[3])
# Region = Region


linestylelist      = ['solid','longdash','dotted','dashed','dashdot','verylongdashdot','longdashdotdotdot']
linestylelistReset = ['solid','longdash','dotted','dashed','dashdot','verylongdashdot','longdashdotdotdot']
#colorlist = ['#ffe259','#fee8a3','green']
#colorlist      = ["#FFF59D","#3F5aB5","#64B5F6","#FFB74D","#FF8A65","#B0BEC5","#66BB6A","#78909C"]
colorlist      = ["#FFF59D","#4DB6AC","#3F5aB5","#64B5F6","#FFB74D","#FF8A65","#B0BEC5","#66BB6A","#78909C"]
#colorlistReset = ["#FFF59D","#3F5aB5","#64B5F6","#FFB74D","#FF8A65","#B0BEC5","#66BB6A","#78909C"]
colorlistReset = ["#FFF59D","#4DB6AC","#3F5aB5","#64B5F6","#FFB74D","#FF8A65","#B0BEC5","#66BB6A","#78909C"]


sig_color      = ('chocolate','lawngreen','red')

#==================== Input Files =======================# 

#backgroundMC_location= str(sys.argv[1])

#signalMC_location =str(sys.argv[1])
#data_location=str(sys.argv[1])
#outputfolder = str(sys.argv[2])
#sampleLocation = str(sys.argv[1])


#DataPeriods = '1516'
#doNminus1 = 0

sampleLocationDictionary = {}

sampleLocationDictionary['1516'] = "samplesnew"
sampleLocationDictionary['17'] = "samples2017"
sampleLocationDictionary['18'] = "samples2018"


LuminosityDictionary = { 'data':{'1516':"1",'17':"1",'18':"1"},'bkg':{'1516':"36.2e3",'17':"43.9e3",'18':"36.2e3"},'sig':{'1516':"36.2e3",'17':"43.9e3",'18':"36.2e3"}  }
WeightDictionary    = {'data':"1", 'bkg': "trigMatch_1L2LTrigOR*pileupWeight*leptonWeight*bTagWeight*genWeight*eventWeight*jvtWeight",'sig': "trigMatch_1L2LTrigOR*pileupWeight*leptonWeight*bTagWeight*genWeight*eventWeight*jvtWeight"}

#showRelativeYields = True

#LegendExtraInformation = "None"
LegendExtraInformation = "Relative"

#LegednExtraInformation = "Absolute"


#samplesExist = os.path.isfile(samplelist)
#samplesFile = samplelist

MC = ("MC","BKG","Mc","mc","MonteCarlo","MC2017","MC2018")
DD = ("DD","ZJETS","Zjets","zjets")
DATA =("DATA","data","Data","DaTa","DaTA","dAtA","dATA","DATA2017","DATA2018")
SIGNAL  =("SIG","sig","Sig","SIg","sIg","sIG","siG","SiG","SIGNAL")
PLOT =("plot","Plot","PLot","PLOt","PLOT","PlOt","PlOT","PloT","PLoT")

VVCRlist =("CR2L-VV","CR2L_ISR-VV","CR3L-VV","CR3L_ISR-VV")
TOPCRlist = ("CR2L-TOP","CR2L_ISR-TOP")
CRlist = VVCRlist + TOPCRlist
ABCDlist = ("A","B","D","VRC","VRD")
SRlist = ("SR2L_LOW", "SR2L_INT", "SR2L_HIGH","SR2L_ISR","SR3L_LOW","SR3L_INT","SR3L_HIGH","SR3L_ISR")
BLINDEDLIST = ("SR2L_LOW", "SR2L_INT", "SR2L_HIGH","SR2L_ISR","SR3L_LOW","SR3L_INT","SR3L_HIGH","SR3L_ISR")
if "2L" in Region:
    if "CR2L-VV" in Region:
        variable_list_file = "variablelist_2LVR.txt"
    elif "CR2L_ISR-VV" in Region:
        variable_list_file = "variablelist_ISRVR.txt"
    elif "VR2L_ISR-VV" in Region:
        variable_list_file = "variablelist_ISRVR.txt"
    else:    
        variable_list_file = "variablelist_2L.txt"
elif "ISR" in Region:
    variable_list_file = "variablelist_ISR.txt"
elif "3L" in Region:
    variable_list_file = "variablelist_3L.txt"

else:
    variable_list_file = "variable21.txt"

if Region in ABCDlist:
    variable_list_file = "variable_cutflow.txt"


if doregionbreakdown:
    variable_list_file = "variable_cutflow.txt"

variable_list_file = "variablelist_2D.txt"
#variable_list_file = "variable21.txt"
if "SR2L" in Region:
    plotData = 0
    doRatio = 0
elif "SR3L" in Region:
    plotData = 0
    doRatio = 0
else:
    plotData = 1
    doRatio = 1



sampletest = ['data1516','ttbar1516','singleTop1516','topOther1516','Zjets1516','Wjets1516','diboson1516','triboson1516','higgs1516','lowMassDY1516']
sampleDictionary = sampleConfiguration(DataPeriods)


#==================== LOAD FILES ============================#

with open(variable_list_file) as f:
    input                 = zip(*[line.split() for line in f])
    variable_list         = input[0]
    xmin_list             = input[1]
    xmax_list             = input[2]
    nbins_list            = input[3]
    xtitle_list           = input[4]
    ytitle_list           = input[5]
    variable_bool_list    = input[6]

# if samplesExist:
#     with open(samplelist) as f:
#         input = zip(*[line.split() for line in f])
#         sampleList  = input[0]
#         sampleNames = input[1]
#         sampleTypes = input[2]
#         sampleBools = input[3]


samplestyleDictionary = {
    'bkg' : {'plottype':'hist','filltype':'solid','linecolor':'black','linewidth':0},
    'sig' : {'plottype':'hist','filltype':'0'    ,'linecolor':'red'  ,'linewidth':5},
    'data': {'plottype':'EP'  ,'filltype':'0'    ,'linecolor':'black','linewidth':5}
}


def RegionYrange(Region):
    if "CR" in Region:
        if "CRWZ" in Region:
            yminimum = 1e-1
            ymaximum = 1e8
        elif "CRZZ" in Region:
            yminimum = 1e-1
            ymaximum = 1e8
        elif "CRTOP" in Region:
            yminimum = 1e-1
            ymaximum = 1e8
        elif "CRZ" in Region:
            yminimum = 1e-1
            ymaximum = 1e8
        else:
            yminimum = 1e-1
            ymaximum = 1e4
    elif "VR" in Region:
        yminimum = 1e-1
        ymaximum = 1e6
    elif "SR" in Region:
        yminimum = 1e-1
        ymaximum = 1e2
    else:
        yminimum = 1e-1
        ymaximum = 1e8
    
    return yminimum,ymaximum 


def atlaslabel( input):
    plottitle = ROOT.TLatex(labelmargin,0.87,input)
    plottitle.SetTextFont(43)
    plottitle.SetTextSize(canvasheight*labelscale*1.2)
    plottitle.SetNDC()
    plottitle.Draw()

def energylabel(input):
    plottitle = ROOT.TLatex(labelmargin,0.805,input)
    plottitle.SetTextFont(43)
    plottitle.SetTextSize(canvasheight*labelscale*1.2)
    plottitle.SetNDC()
    plottitle.Draw()

def SRlabel(input):
    plottitle = ROOT.TLatex(labelmargin,0.745,input)
    plottitle.SetTextFont(43)
    plottitle.SetTextSize(canvasheight*labelscale*1.0)
    plottitle.SetNDC()
    plottitle.Draw()

def topleftplotlabel(input):
    plottitle = ROOT.TLatex(labelmargin,0.974,input)
    plottitle.SetTextFont(43)
    plottitle.SetTextSize(canvasheight*labelscale)
    plottitle.SetNDC()
    plottitle.Draw()

def toprightplotlabel(input):
    plottitle = ROOT.TLatex(0.74,0.971,input)
    plottitle.SetTextFont(43)
    plottitle.SetTextSize(canvasheight*labelscale)
    plottitle.SetNDC()
    plottitle.Draw()

def plotstackobjects(stack):

    stack.Draw()
    stack.sum.SetFillStyle(0)
    stack.sum.SetLineColor("black")
    stack.sum.SetLineWidth(4)
    stack.sum.Draw("Hist SAME")

    errorband = stack.sum.Clone()
    errorband.SetLineWidth(10)
    errorband.SetFillStyle(3244)
    errorband.SetFillColor(922)

    errorband.Draw("SAME E2P")

def plotbackgrounds(stack):
    temphist = stack.sum.Clone()
    stack.Draw()
    stack.sum.SetFillStyle(0)
    stack.sum.SetLineColor("black")
    stack.sum.SetLineWidth(4)
    stack.sum.Draw("Hist SAME")

    errorband = stack.sum.Clone()
    errorband.SetLineWidth(10)
    errorband.SetFillStyle(3244)
    errorband.SetFillColor(922)

    errorband.Draw("SAME E2P")


def plotzjets(hist):
    hist.Draw("colz")


def plotsignalobjects(backgroundstacks):

    for LegendEntry in backgroundstacks:
        if 'Signal' in LegendEntry:
            backgroundstacks[LegendEntry].sum.Draw("Hist SAME X0")
    #for signal in signals:
    #   signal.Draw("Hist SAME X0")

def plotdataobjects(data):
    datastack.sum.SetMarkerStyle('circle')
    datastack.sum.SetMarkerSize(3) 
    datastack.sum.SetLineWidth(4)
    datastack.sum.Draw("SAME EP")


def plotdata(datastack):
    datastack.sum.SetMarkerStyle('circle')
    datastack.sum.SetMarkerSize(3) 
    datastack.sum.SetLineWidth(4)
    datastack.sum.Draw("SAME EP")

def calculateNFs(backgroundstacks,datastack):
    datavalue = 0.0
    DataEstimate = 0.0
    DataEstimateError = 0.0

    datavalue,dataerror = datastack.sum.integral(error=True, overflow=True)

    DataEstimate = datavalue 
    DataEstimateError = dataerror**2 

    MCyield = 0.0
    MCerror = 0.0
    if Region in VVCRlist:
        primarybackground = ("Diboson", "VV")
    elif Region in TOPCRlist:
        primarybackground = ("t#bar{t}","Top other","Single top")
    elif Region in ABCDlist:
        primarybackground = "Z+jets"

    for LegendGroup in backgroundstacks:
        if LegendGroup == 'Data': continue
        backgroundyield,backgrounderror = backgroundstacks[LegendGroup].sum.integral(error=True,overflow=True)
        if LegendGroup not in primarybackground:
            DataEstimate      -= backgroundyield 
            DataEstimateError += backgrounderror**2 
        elif LegendGroup in primarybackground:
            MCyield += backgroundyield 
            MCerror += backgrounderror**2 
    
    DataEstimateError = math.sqrt(DataEstimateError)
    MCerror           = math.sqrt(MCerror)
    if MCyield != 0.0:
        NF = DataEstimate/MCyield
        A  = DataEstimate
        B  = MCyield 
        dA = DataEstimateError
        dB = MCerror 
        NFerror = math.sqrt((1/B/B)*dA*dA + (A*A/B/B/B/B)*dB*dB)
    else:   
        NF = 0.0
        NFerror = 0.0

    if Region in ABCDlist:
        return DataEstimate, DataEstimateError
    
    return NF, NFerror
        

def plotratio(datastack,stack):
    histRatio = datastack.sum.Clone()
    #histRatio.merge_bins([(0, 1), (-2, -1)])
    ratioMinimum=0
    ratioMaximum=2
    histRatio.SetMinimum(ratioMinimum)
    histRatio.SetMaximum(ratioMaximum)

    histRatio.xaxis.SetTitle(xtitle)
    histRatio.yaxis.SetTitle("Data/SM")
    histRatio.yaxis.CenterTitle()
    histRatio.yaxis.divisions = 5
    histRatio.Divide(stack.sum)
    histRatio.xaxis.SetTitleOffset(3.4)
    histRatio.yaxis.SetTitleOffset(2)
    histRatio.xaxis.set_label_size(int(canvasheight*labelscale*1.5))
    histRatio.yaxis.set_label_size(int(canvasheight*labelscale*1.5))

    if plotData :
        histRatio.Draw("PE")
    
    line = Line(float(xmin)+1e-2*float(xmax),1.,float(xmax)-1e-2*float(xmax),1.);
    line.SetLineWidth(4);
    line.SetLineColor("red");

    if plotData:
        line.Draw("Same");
    else:
        line.Draw();

    if plotData:
        histRatio.Draw("SAME EP")

    MCerrorband = stack.sum.Clone()
    MCerrorband.SetLineWidth(10)
    MCerrorband.SetFillStyle(3244)
    MCerrorband.SetFillColor(922)


    for i in range(1,int(nbins)+1):
        if stack.sum.GetBinContent(i) != 0:
            if datastack.sum.GetBinContent(i)/stack.sum.GetBinContent(i) >= 2:
                xcoord = stack.sum.GetBinCenter(i)
                arrow = Arrow(xcoord,1.67,xcoord,1.87,0.015,"|>")
                arrow.SetAngle(50)
                arrow.SetLineWidth(6)
                arrow.SetLineColor(2)
                arrow.SetFillColor(2)
                arrow.Draw()
            if datastack.sum.GetBinContent(i)/stack.sum.GetBinContent(i) <= -2:
                xcoord = stack.sum.GetBinCenter(i)
                arrow = Arrow(xcoord,0.33,xcoord,0.13,0.015,"|>")
                arrow.SetAngle(50)
                arrow.SetLineWidth(6)
                arrow.SetLineColor(2)
                arrow.SetFillColor(2)
                arrow.Draw();
        
        mcerror = 0.0
        content = stack.sum.GetBinContent(i)
        error = stack.sum.GetBinError(i)
        if content != 0 :
            mcerror = (content+error)/content - 1.0 
        MCerrorband.SetBinContent(i,1)
        MCerrorband.SetBinError(i,mcerror)
        
    MCerrorband.Draw("E2PSAME")





def generatedatalegend(inputdatastack,inputstack):
        datalegend_entries=2 #figure out how to remove this magic number                                                                                                                                                       
        datamargin      = 0.10
        datarightmargin = 0.00
        datatopmargin   = 0.05
        dataentryheight = 0.045
        dataentrysep    = 0.06
        datalegend = Legend(datalegend_entries, leftmargin  = 0.26,
                                      topmargin   = datatopmargin           ,
                                      rightmargin = datarightmargin         ,
                                      entryheight = dataentryheight       ,
                                      entrysep    = dataentrysep            ,
                                      margin      = datamargin              ,
                                      textfont    = 43                  ,
                                      textsize    = canvasheight*labelscale,
                                      header      = None)
        datalegend.SetLineColor(0)


        if plotData:
            datalegend.AddEntry(inputdatastack.sum,label = "Data (" + str(round(inputdatastack.sum.integral(overflow=True),1)) +")",style ="EP")

        errorband = inputstack.sum.Clone()
        errorband.SetLineWidth(10)
        errorband.SetFillStyle(3244)
        errorband.SetFillColor(922)

        if Region == "A" or Region == "B" or  Region== "D" or Region== "VRC" or Region =="VRD":
            datalegend.AddEntry(inputstack.sum, label = "SM (" + str(round(float(inputstack.sum.integral(overflow=True)),1)) + "\pm" + str(round(float(inputstack.sum.integral(error= True, overflow=True)[1]),1)   ) + ")",style = "L")
        else:
            datalegend.AddEntry(inputstack.sum, label = "SM (" + str(round(float(inputstack.sum.integral(overflow=True)),1)) + ")",style = "L")
        datalegend.Draw("SAME")


def generatebackgroundlegend(backgroundstacks):
    legend_entries=4 #figure out how to remove this magic number

    margin      = 0.30
    rightmargin = 0.07
    topmargin   = 0.05
    entryheight = 0.045
    entrysep    = 0.06

    legend = Legend(legend_entries, leftmargin  = 0.52,
                                      topmargin   = topmargin           ,
                                      rightmargin = rightmargin         ,
                                      entryheight = entryheight       ,
                                      entrysep    = entrysep            ,
                                      margin      = margin              ,
                                      textfont    = 43                  ,
                                      textsize    = canvasheight*labelscale,
                                      header      = None                )

    legend.SetLineColor(0)

    totalyield,totalerror = stack.sum.integral(error=True, overflow=True)

    for LegendGroup in backgroundstacks:
        if LegendGroup is 'Data': continue

        backgroundyield,backgrounderror = backgroundstacks[LegendGroup].sum.integral(error=True,overflow=True)
        if LegendExtraInformation == "Relative" and totalyield!=0:
            relativeyield = str(round(100*backgroundyield/totalyield,1))
            legend.AddEntry(backgroundstacks[LegendGroup].sum,label=LegendGroup + " (" + relativeyield + "%)",style="F" )
        elif LegendExtraInformation == "Absolute":
            legend.AddEntry(background,label =backgroundname + " (" + str(round(backgroundyield,1)) +")",style="F")
        else:
            legend.AddEntry(background,label =backgroundname ,style="F")

    legend.Draw("SAME");


def colorAllocator(rootfile,colorpalette):
    myLighterBlue='powderblue'
    myLightBlue  ='#9ecae1'
    myMediumBlue ='#0868ac'
    myDarkBlue   ='#08306b'

    # Greens
    myLightGreen   ='#c7e9c0'
    myMediumGreen  ='#41ab5d'
    myDarkGreen    ='#006d2c'

    # Oranges
    myLighterOrange='#ffeda0'
    myLightOrange  ='#fec49f'
    myMediumOrange ='#fe9929'

    # Greys
    myLightestGrey='#f0f0f0'
    myLighterGrey='#e3e3e3'
    myLightGrey  ='#969696'

    # Pinks
    myLightPink = '#fde0dd'
    myMediumPink = '#fcc5c0'
    myDarkPink = '#dd3497'
    sampleFillcolor ='black'

    rjhiggs ="391"
    rjwjets ="922"
    rjvgamma ='627'
    rjttbar  = '797'
    rjvvv = '598'
    rjvv  = '851'
    rjzjets = '410'
    rjDY = '845'
    rjtopother = '895'
    rjsingletop= '806'

    if colorpalette == "HIGGSINO":
        if("higgs" in rootfile):
            sampleFillcolor = myLightGrey
        elif("singleTop" in rootfile):
            sampleFillcolor =  myLighterBlue
        elif("topOther" in rootfile):
            sampleFillcolor =  myLightBlue
        elif("triboson" in rootfile):
            sampleFillcolor = myLightOrange
        elif("Vgamma" in rootfile):
            sampleFillcolor = myLighterOrange
        elif("Wjets" in rootfile):
            sampleFillcolor = myLightGreen
        elif("Zjets" in rootfile):
            sampleFillcolor = myMediumGreen
        elif("DY" in rootfile):
            sampleFillcolor = myLighterGrey
        elif("diboson" in rootfile):
            sampleFillcolor = myMediumOrange
        elif("ttbar_dilep" in rootfile):
            sampleFillcolor = myMediumBlue
 
    elif colorpalette == "RJ":
        if("higgs" in rootfile):
            sampleFillcolor = rjhiggs
        elif("singleTop" in rootfile):
            sampleFillcolor =  rjsingletop
        elif("topOther" in rootfile):
            sampleFillcolor = rjtopother
        elif("triboson" in rootfile):
            sampleFillcolor = rjvvv
        elif("Vgamma" in rootfile):
            sampleFillcolor = rjvgamma
        elif("Wjets" in rootfile):
            sampleFillcolor = rjwjets
        elif("Zjets" in rootfile):
            sampleFillcolor = rjzjets
        elif("DY" in rootfile):
            sampleFillcolor = rjDY
        elif("diboson" in rootfile):
            sampleFillcolor = rjvv
        elif("ttbar_dilep" in rootfile):
            sampleFillcolor = rjttbar

    return sampleFillcolor


def retreiveTree(sample):
    Filename = sampleDictionary[sample]['filename']
    rootfile  = rootfileDictionary[sample]

    
    if("data15" in Filename):
        print "[TREES][LOADING]: DATA15"
        tree = rootfile.data1516
    elif("data17" in Filename):
        print "[TREES][LOADING]: DATA17"
        tree = rootfile.data17
    elif("data18" in Filename):
        print "[TREES][LOADING]: DATA18"
        tree = rootfile.data
    elif("higgs" in Filename):
        print "[TREES][LOADING]: HIGGS"
        tree = rootfile.higgs_NoSys
    elif("singleTop" in Filename):
        print "[TREES][LOADING]: SINGLETOP"
        tree = rootfile.singleTop_NoSys
    elif("topOther" in Filename):
        print "[TREES][LOADING]: TOPOTHER"
        tree = rootfile.topOther_NoSys
    elif("triboson" in Filename):
        print "[TREES][LOADING]: TRIBOSON"
        tree = rootfile.triboson_NoSys
    elif("Vgamma" in Filename):
        print "[TREES][LOADING]: VGAMMA"
        tree = rootfile.Vgamma_NoSys
    elif("Wjets" in Filename):
        print "[TREES][LOADING]: WJETS"
        tree = rootfile.Wjets_NoSys
    elif("Zjets" in Filename):
        print "[TREES][LOADING]: ZJETS"
        tree = rootfile.Zjets_NoSys
    elif("DY" in Filename):
        print "[TREES][LOADING]: LOWMASSDY"
        tree = rootfile.lowMassDY_NoSys
    elif("diboson" in Filename):
        print "[TREES][LOADING]: DIBOSON"
        tree = rootfile.diboson_NoSys
    elif("ttbar_dilep" in Filename):
        print "[TREES][LOADING]: TTBAR_DILEP"
        tree = rootfile.ttbar_dilep_NoSys
    elif("ttbar" in Filename):
        print "[TREES][LOADING]: TTBAR"
        tree = rootfile.ttbar_NoSys

    return tree


def drawPlotInformation(DataPeriods,atlasStatus,RegionLabel):
        atlaslabel('#it{#bf{ATLAS}} ' + atlasStatus)
        if(DataPeriods == '1516'):
            energylabel("13TeV, 36.2 fb^{-1}")
            toprightplotlabel('#lower[0.4]{Rel21:Data1516}')
        elif(DataPeriods== '17'):
            energylabel("13TeV, 43.9 fb^{-1}")
            toprightplotlabel('#lower[0.4]{Rel21:Data17}') 
        elif(DataPeriods== '18'):
            energylabel("13TeV, 36.2 fb^{-1}")
            toprightplotlabel('#lower[0.4]{Rel21:Data18}') 
        elif(DataPeriods=='15-17'):
            energylabel("13TeV, 80.1 fb^{-1}")
            toprightplotlabel('#lower[0.4]{Rel21:Data15-17}') 
        elif(DataPeriods=='15-18'):
            energylabel("13TeV, 116.3 fb^{-1}")
            toprightplotlabel('#lower[0.4]{Rel21:Data15-18}') 
        elif(DataPeriods=='17-18'):
            energylabel("13TeV, 80.1 fb^{-1}")
            toprightplotlabel('#lower[0.4]{Rel21:Data17-18}') 
        if donminus1:
            SRlabel( RegionLabel + " N-1")
        else:
            SRlabel( RegionLabel )


# def inputSampleType(isType):
#     if isType==0:
#         isBKG=True
#     elif isType ==1:
#         isSIGNAL=True
#     elif isType ==2:
#         isDATA=True
#     return isBKG,isSIGNAL,isDATA

def sampleStyleFunc(temphist,Type):
    fillcolor = sampleDictionary[sample]['fillcolor']
    temphist.drawstyle = samplestyleDictionary[Type]['plottype']
    temphist.fillcolor = sampleDictionary[sample]['fillcolor'] 
    temphist.fillstyle = samplestyleDictionary[Type]['filltype']
    temphist.linecolor = samplestyleDictionary[Type]['linecolor']
    temphist.linewidth = samplestyleDictionary[Type]['linewidth']
    temphist.linestyle = 'solid'



def produceRegionBreakdown(backgroundstacks,stack,datastack,Region):
    cutflowstring = "Samples:"
    yieldstring = Region
    primaryyield=0.0

    for LegendEntry in backgroundstacks:
        if LegendEntry == 'Data': continue
        cutflowstring += "& $" + LegendEntry + "$"

    cutflowstring += "\\\ \\hline"

    for LegendEntry in backgroundstacks:
        backgroundyield,backgrounderror = backgroundstacks[LegendEntry].sum.integral(error=True,overflow=True)
        if Region in VVCRlist:
            primarybackground =("Diboson","VV")
        elif Region in TOPCRlist:
            primarybackground = ("Top","topOther","singleTop")
        if LegendEntry == 'Data': continue 
        if LegendEntry in primarybackground:
            primaryyield += backgroundyield 
        yieldstring += "&$" + str(round(backgroundyield,2)) + "\pm" + str(round(backgrounderror,2)) + "$"
    
    cutflowstring  += "&Total&CR Purity& CR NF& Data& Data/MC \\\ \\hline "
    totalyield, totalerror = stack.sum.integral(error=True,overflow=True)
    datayield, dataerror   =datastack.sum.integral(error=True,overflow=True)
    yieldstring += "&$" + str(round(totalyield,2)) +"\pm" + str(round(totalerror)) + "$"
    if Region in CRlist:
        yieldstring += "&$" + str(round(primaryyield/totalyield,2)) 
        yieldstring += "&$" + str(round(NormalisationFactor,3)) +"\pm" + str(round(NFerror,3)) + "$"
    else:
        yieldstring += "& - & - "

    if Region in SRlist:
        yieldstring += "& - & - \\\ \\hline "
    else:
        yieldstring += "&$" + str(round(datayield,0)) + "&" + str(round(datayield/totalyield,2)) + "$  \\\ \\hline"

    return cutflowstring,yieldstring







t1 = time.time()

print "[PREROOTFILE]" + str(round(t1 - t0,2)) + "seconds"

sampleDict = {}
treeDict = {}
treeDict2 = {}
rootfileDictionary = {}
for sample in sampleDictionary:
    #print "sample: " + sample
    if sample != 'Zjets1516':continue 
    Year        = sampleDictionary[sample]['year']
    Filename    = sampleDictionary[sample]['filename']
    Location    = sampleLocationDictionary[Year]
    rootfileDictionary[sample] = root_open(os.path.join(Location,Filename))
    t2 = time.time()

    print "[ROOTFILE LOADING][" + sample + "]" + str(round(t2 - t0,2)) + "seconds"

    treeDict[sample] = retreiveTree(sample)
    treeDict2[sample] = retreiveTree(sample)





RegionLabel= retreiveRegionInformation(Region)[0]
Cutlist    = retreiveRegionInformation(Region)[1]
Cutnames   = retreiveRegionInformation(Region)[2]

skimmed = 0
for (variable,xmin,xmax,nbins,xtitle,ytitle,variable_bool) in zip(variable_list,xmin_list,xmax_list,nbins_list,xtitle_list,ytitle_list,variable_bool_list):
    if variable_bool == 'Plot':    
        #print "[VARIABLE][" + variable + "]"
        tn = time.time()
        print "[VARIABLE][" + variable  + "]" + str(round(tn - t0,0)) + "seconds"
        doRatio = 0 



        samples = []
        backgrounds = []
        signals = []
        data    = []
        stackyield = 0
        errorsum   = 0 
        
        backgroundstacks = {}
       # print "pre sampleDictionary"
        for sample in sampleDictionary:
            if sample != 'Zjets1516':continue 
            if Region in BLINDEDLIST and sample is 'Data': continue 
            LegendEntry = sampleDictionary[sample]['legend']
            Type = sampleDictionary[sample]['type']
            backgroundstacks[LegendEntry] = HistStack()
        #    print "post initialisation of backgroundstakcs"

        #"pre second sample dictionary"

        for (variable2,xmin2,xmax2,nbins2,xtitle2,ytitle2,variable_bool2) in zip(variable_list,xmin_list,xmax_list,nbins_list,xtitle_list,ytitle_list,variable_bool_list):
            if variable_bool != 'Plot': continue 



            canvas = Canvas(width=canvaswidth,height=int((1-(1-doRatio)*0.2)*canvasheight))
            #canvas.SetFrameBorderMode(0)

            topmargins    = (1.0 , 1.0 )
            bottommargins = (0.1  , 0.4  )
            leftmargins   = (0.0  , 0.0  )
            rightmargins  = (0.1  , 0.0  )
            
            top    = topmargins[doRatio]
            bottom = bottommargins[doRatio]
            left   = leftmargins[doRatio]
            right  = 1 - rightmargins[doRatio]
    
            canvas.cd()

            #histpad = Pad(left,0.3,right, top,color="white",bordersize =5)
            
            #histpad.SetBottomMargin(0.3)

            #histpad.SetFrameBorderMode(0)

            #histpad.Draw()
            #histpad.SetLogy()
            #histpad.cd()
            #histpad.SetFrameBorderSize(2)
            #histpad.SetFrameLineWidth(2);

            for sample in sampleDictionary:
            #    print "pre blinded check"
                if sample != "Zjets1516": continue 
                if Region in BLINDEDLIST and sample is 'data1516': continue 
                #print "[BACKGROUND][" + sample + "]" 
                tn = time.time()
                print "[DRAWING][" + sample  + "]" + str(round(tn - t0,0)) + "seconds"
    
                Name        = sample 
                Type        = sampleDictionary[sample]['type']
                Year        = sampleDictionary[sample]['year']
                LegendEntry = sampleDictionary[sample]['legend']
                FillColor   = sampleDictionary[sample]['fillcolor']
                #LineColor   = sampleDictionary[sample]['linecolor']
                rootfile     = sampleDictionary[sample]['filename']

                Luminosity = LuminosityDictionary[Type][Year]
                Weight     = WeightDictionary[Type]

                total = Cut("1")
                for cut in Cutlist:
                    if (variable  in cut) or (variable2 in cut)  : continue 
                  
                    #if variable2 in cut :continue 
                    total = total & cut 

                print total
#                if donminus1 == 0 and skimmed == 0 :
                    #print "skimming"
                    #treeDict[sample].CopyTree(total)
                    #mylistof_events = ROOT.TEntryList()
                    #mylist = ROOT.TEntryList()
                    #print "treeEntries1" + str(treeDict[sample].GetEntries())
                    #mylist = ROOT.R.TEntryList("mylist","mylist")
                    #treeDict[sample].Draw(">>mylist",total,"entrylist")
                    #mylist.Print()
                # print "type: " + str(type(treeDict[sample]))
#                    print "DEFAULT: " + str(treeDict[sample].GetEntries())
#                    print "type: " + str(type(treeDict[sample]))
                    #treeDict2[sample] =
                    #if Year == '1516' or Year == '18' or Year == "17":
                #treeDict[sample] = treeDict[sample].CopyTree(total)     
                #asrootpy(treeDict[sample])
                    #    print "type: " + str(type(treeDict[sample]))
                        #treeDict[sample] = treeDict2[sample]
                        #asrootpy(treeDict[sample])
                        #treeDict[sample] = treeDict2[sample]
                        #print "type: " + str(type(treeDict2[sample]))
                        #print "type2: " + str(type(treeDict2[sample]))
                    #    print "SKIMMED:  " + str(treeDict[sample].GetEntries())
                    #treeDict[sample] = treeDict2[sample]
                    #treeDict[sample].CopyTree(total)
                    #mylistof_events = treeDict[sample].GetEntryList()
                    #ROOT.R.TEntryList("mylist",mylist)
                    #print str(type(mylist))
                    #print str(mylist.GetN())
                    #ROOT.R.gDirectory.GetObject("mylist",mylist)
                    #ROOT.R.gDirectory.ls()
                    #GetObject("mylistof_events",mylistof_events)
                    #print str(mylist.GetN())
                    #mylist.Print()
                    #,"entrylist")
                    #mylistof_events.SetReapplyCut()
                # treeDict[sample].SetEntryList(mylistof_events)
                    #treeDict[sample].SetEntriesToProcess(mylistof_events)
                    #treeDict[sample].SetEventList(mylist)
                    #treeDict[sample].GetEntriesToProcess(mylistof_events)
                print "treeEntries2" + str(treeDict[sample].GetEntries())
    
                    

                SelectionCriteria = Cut(Luminosity) * Cut(Weight) * total
                print variable
                print variable2
                print SelectionCriteria 
                histogram = "Hist(" + nbins+ "," + xmin +"," + xmax+ ")"


                histogram2D = Hist2D(int(nbins),float(xmin),float(xmax),int(nbins2),float(xmin2),float(xmax2))
                temphist2D = Hist2D(int(nbins),float(xmin),float(xmax),int(nbins2),float(xmin2),float(xmax2))
                histogram2D.SetName("hist2")
                #histogram = Hist(int(nbins),float(xmin),float(xmax))
                if treeDict[sample].GetEntries() == 0:
                    temphist = Hist(int(nbins),float(xmin),float(xmax))
                else: 

                    #histogram2D.SetMinimum(0.0)
                    #histogram2D.SetMaximum(3.0)

                    histogram2D = treeDict[sample].Draw(variable + ":" + variable2 ,hist = histogram2D, selection = SelectionCriteria)

                    #histogram2D.SetMinimum(0.0)
                    #histogram2D.SetMaximum(3.0)
                    histogram2D.Draw("colz")
                    histogram2D.ProfileX().Draw("SAME")
                    #histogram2D.SetMinimum(0.0)
                    #histogram2D.SetMaximum(3.0)

                   #sampleStyleFunc(temphist,Type)
                    
                    #temphist.SetName(Name)
                    #temphist.overflow(1)
                    #temphist.merge_bins([(0, 1), (-2, -1)])
                    #temphist.Sumw2()
            # print "prebackgroundstacks"


                    #histpad.Update()
                    #histpad.Modified()
                    #canvas.clear()
                    #canvas.cd()
                    canvas.Update()
                    canvas.Modified()

                    #plotzjets(temphist)
                    ROOT.gPad.Update()
                    #palette = asrootpy(temphist.GetListOfFunctions().FindObject("palette"))
                    
                    #palette.SetY2NDC(0.7);
                    #palette.Draw("SAME")
                    #dataoutputfolder = os.path.join(outputfolder,"Data" + DataPeriods )
                    histogram2D.xaxis.SetTitle(xtitle)
                    histogram2D.xaxis.SetTitleOffset(1.5)
                    histogram2D.xaxis.set_label_size(int(canvasheight*labelscale*1.5))

                    histogram2D.yaxis.SetTitle(xtitle2)
                    histogram2D.yaxis.SetTitleOffset(1.5)
                    histogram2D.yaxis.set_label_size(int(canvasheight*labelscale*1.5))
                    #canvas.cd()
                    canvas.Update()
                    canvas.Modified()

                    #os.system("mkdir -p " +	dataoutputfolder  )
                    dataoutputfolder = os.path.join(outputfolder,"Data" + DataPeriods,Region)
                    os.system("mkdir -p " + dataoutputfolder )
                    canvas.Print(dataoutputfolder + "/log_"+ variable.replace("/","_")+ "_" + variable2.replace("/","_") + "_" + Region + "_"+systematics+".png")


                #backgroundstacks[LegendEntry].Add(temphist.Clone())

        #plotzjets(hist)

      #  skimmed = 1 


        

       # stack.yaxis.SetTitle(ytitle)
       # stack.yaxis.SetTitleOffset(2)
       # stack.yaxis.set_label_size(int(canvasheight*labelscale*1.5))
    
       # canvas.cd()



        #dataoutputfolder = os.path.join(outputfolder,"Data" + DataPeriods )
        #os.system("mkdir -p " +	dataoutputfolder  )
        #os.system("mkdir -p " + os.path.join(dataoutputfolder,Region) )
        #os.system("mkdir -p " + os.path.join(dataoutputfolder,Region,"N-1") )



       # filenamevariable = variable.replace("/","_").replace("_1000","")
       # if donminus1:
       #     canvas.Print(dataoutputfolder + "/" + Region + "/N-1/log_"+ filenamevariable+ "_" + variable2 + "_" + Region + "_"+systematics+".png")
       # else:
       #     canvas.Print(dataoutputfolder + "/" + Region + "/log_"+ filenamevariable+ "_" + variable2 + "_" + Region + "_"+systematics+".png")
        #canvas.Print(dataoutputfolder + "/" + Region + "/log_"+ filenamevariable+ "_" + Region + "_"+systematics+".pdf")
        #canvas.Print(dataoutputfolder + "/" + Region + "/log_"+ filenamevariable+ "_" + Region + "_"+systematics+".eps")
     #   histpad.SetLogy(0)
        #stack.SetMinimum(0.0)
        #stack.SetMaximum(3*stack.sum.GetMaximum())
        #canvas.Print(dataoutputfolder + "/" + Region + "/lin_"+ filenamevariable+ "_" + Region + "_"+systematics+".png")
       # canvas.Print(dataoutputfolder + "/" + Region + "/lin_"+ filenamevariable+ "_" + Region + "_"+systematics+".pdf")
      #  canvas.Print(dataoutputfolder + "/" + Region + "/lin_"+ filenamevariable+ "_" + Region + "_"+systematics+".eps")

     #   tn = time.time()
        #print "[CANVAS][PLOTTED]"
     #   print "[CANVAS][PLOTTED]" + str(round(tn - t0,0)) + "seconds"
     #   t0 = time.time() 






