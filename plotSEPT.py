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


import os.path
import sys
import math
#import rootpy.defaults
from rootpy.io import root_open 
#from rootpy.defaults 
from rootpy.plotting import F1, Hist, HistStack, Canvas, Legend, Pad
from rootpy.tree import Tree
from rootpy.plotting.shapes import Line,Arrow
from rootpy.plotting.utils  import draw
from rootpy.plotting.views import StackView
from rootpy.plotting.style  import get_style, set_style
from rootpy.tree import Cut
from regiondefinitions import retreiveRegionInformation
from itertools import izip
import ROOT

from decimal import Decimal


ROOT.gROOT.SetBatch(True)
Hist.SetDefaultSumw2(True)

atlas="Internal"

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
ROOT.gStyle.SetPadBottomMargin(0.)
ROOT.gStyle.SetLineWidth(4)

#ROOT.gPad.SetBorderWidth(5)  

labelmargin=0.20 #Labeling

#==================== EDIT THESE ========================#
sqrts  = 13
whichSR = str(sys.argv[3])

if "CR" in whichSR:
    if "CRWZ" in whichSR:
	    yminimum = 1e-1
	    ymaximum = 1e8
    elif "CRZZ" in whichSR:
	    yminimum = 1e-1
	    ymaximum = 1e8
    elif "CRTOP" in whichSR:
	    yminimum = 1e-1
	    ymaximum = 1e8
    elif "CRZ" in whichSR:
        yminimum = 1e-1
        ymaximum = 1e8
    else:
        yminimum = 1e-1
        ymaximum = 1e3
elif "VR" in whichSR:
    yminimum = 1e-1
    ymaximum = 1e3
elif "SR" in whichSR:
    yminimum = 1e-1
    ymaximum = 1e2
else:
    yminimum = 1e-1
    ymaximum = 1e8

linestylelist      = ['solid','longdash','dotted','dashed','dashdot','verylongdashdot','longdashdotdotdot']
linestylelistReset = ['solid','longdash','dotted','dashed','dashdot','verylongdashdot','longdashdotdotdot']
#colorlist = ['#ffe259','#fee8a3','green']
colorlist      = ["#FFF59D","#3F5aB5","#64B5F6","#FFB74D","#FF8A65","#B0BEC5","#66BB6A","#78909C"]
#colorlist      = ["#FFF59D","#4DB6AC","#3F5aB5","#64B5F6","#FFB74D","#FF8A65","#B0BEC5","#66BB6A","#78909C"]
colorlistReset = ["#FFF59D","#3F5aB5","#64B5F6","#FFB74D","#FF8A65","#B0BEC5","#66BB6A","#78909C"]
#colorlistReset = ["#FFF59D","#4DB6AC","#3F5aB5","#64B5F6","#FFB74D","#FF8A65","#B0BEC5","#66BB6A","#78909C"]


sig_color      = ('chocolate','lawngreen','red')

#==================== Input Files =======================# 
datayear = "0"
if ("2017" in str(sys.argv[1])):
    samplelist = "samples2017.txt"
    datayear = "2017"
elif ("2018" in str(sys.argv[1])):
    samplelist = "samples2018.txt"
    datayear = "2018"
else:
    samplelist = "samples21.txt"
    datayear ="2015"

backgroundMC_location= str(sys.argv[1])

signalMC_location =str(sys.argv[1])
data_location=str(sys.argv[1])
outputfolder = str(sys.argv[2])
sampleLocation = str(sys.argv[1])
samplesExist = os.path.isfile(samplelist)
samplesFile = samplelist

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

if "2L" in whichSR:
    if "CR2L-VV" in whichSR:
        variable_list_file = "variablelist_2LVR.txt"
    elif "CR2L_ISR-VV" in whichSR:
        variable_list_file = "variablelist_ISRVR.txt"
    elif "VR2L_ISR-VV" in whichSR:
        variable_list_file = "variablelist_ISRVR.txt"
    else:    
        variable_list_file = "variablelist_2L.txt"
elif "ISR" in whichSR:
    variable_list_file = "variablelist_ISR.txt"
elif "3L" in whichSR:
    variable_list_file = "variablelist_3L.txt"

else:
    variable_list_file = "variable21.txt"

if whichSR in ABCDlist:
    variable_list_file = "variable_cutflow.txt"

if sys.argv[6] == "CUTFLOW":
    variable_list_file = "variable_cutflow.txt"

#variable_list_file = "variable21.txt"
if "SR2L" in whichSR:
    plotData = 0
    doRatio = 0
elif "SR3L" in whichSR:
    plotData = 0
    doRatio = 0
else:
    plotData = 1
    doRatio = 1
#doRatio = int(sys.argv[5])
#plotData = 1
#variable_list_file = "variable21.txt"
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

if samplesExist:
    with open(samplelist) as f:
        input = zip(*[line.split() for line in f])
        sampleList  = input[0]
        sampleNames = input[1]
        sampleTypes = input[2]
        sampleBools = input[3]


def samplestyle( isBKG,isSIGNAL,isDATA ):
    #print "INFO.SampleStyle"
    if( isBKG + isSIGNAL + isDATA != 1):
        print "error, miscategorisation"
    if isBKG:
        samplePlottype = "hist"
        sampleFill = "solid"
        sampleLinecolor ="black"
        sampleLinewidth = 0
        sampleFillcolor = colorlist[0]
        sampleLineStyle = "solid"
        #print colorlist[0]
        del colorlist[0]

    if isSIGNAL:
        samplePlottype = "hist"
        sampleFill = "0"
        sampleLinecolor ="red"
        sampleLinewidth = 5
        sampleFillcolor = "black"#signalcolorlist[0]
        sampleLineStyle = linestylelist[0]
        del linestylelist[0]    
    if isDATA:
        samplePlottype = "EP"
        sampleFill = "0"
        sampleLinecolor ="black"
        sampleLinewidth = 5
        sampleFillcolor = "black"
        #signalcolorlist[0]                                                                                                                                                               
        sampleLineStyle = "solid" #linestylelist[0]
        del linestylelist[0]
    return samplePlottype,sampleFill,sampleLinecolor,sampleLinewidth,sampleFillcolor,sampleLineStyle,colorlist,linestylelist


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


def plotsignalobjects(signals):
    for signal in signals:
        signal.Draw("Hist SAME X0")

def plotdataobjects(data):
    for dataset in data:
        dataset.SetMarkerStyle('circle')
        dataset.SetMarkerSize(3) 
        dataset.SetLineWidth(4)
        dataset.Draw("SAME EP")

def calculateNFs(backgrounds,backgroundnames,data):
    
    datavalue = 0.0
    correctedyield = 0.0
    correctederror = 0.0
    for dataset in data:
        datavalue,dataerror = dataset.integral(error=True, overflow=True)
    correctedyield = datavalue
    correctederror = dataerror*dataerror
    MCyield = 0.0
    MCerror = 0.0
    if whichSR in VVCRlist:
        primarybackground = "VV"
    elif whichSR in TOPCRlist:
        primarybackground = ("Top","topOther","singleTop")
    elif whichSR in ABCDlist:
        primarybackground = "Zjets"

    
    for (background,backgroundname) in zip(backgrounds,backgroundnames):
        if backgroundname not in primarybackground:
            correctedyield = correctedyield - background.integral(overflow=True)
            correctederror = correctederror + background.integral(error=True, overflow=True)[1]*background.integral(error=True, overflow=True)[1]
        if backgroundname in primarybackground:
            MCyield = MCyield + background.integral(overflow=True)
            MCerror = MCerror + background.integral(error=True,overflow=True)[1]*background.integral(error=True,overflow=True)[1]

    
    NF = correctedyield/MCyield    
    A = correctedyield 
    B = MCyield
    dA = math.sqrt(correctederror)
    dB = math.sqrt(MCerror)
   # print whichSR + "corrected output: " + correctedyield + "+/-" + correctederror 
    #f = open("ABCDCUTFLOW_" + whichSR + ".txt","w+")
    #f.write(correctedyield + "  " + correctederror)

    if whichSR in ABCDlist:
        NF = correctedyield
        nferror = math.sqrt(correctederror)
        return NF,nferror
    nferror= math.sqrt((1/B/B)*dA*dA + (A*A/B/B/B/B)*dB*dB)
    #nferror = NF*math.sqrt( correctederror/correctedyield/correctedyield + MCerror/MCyield/MCyield    )
    return NF,nferror
        
    


def plotratio(data,stack):
    histRatio = data[0].Clone()
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
            if data[0].GetBinContent(i)/stack.sum.GetBinContent(i) >= 2:
                xcoord = stack.sum.GetBinCenter(i)
                arrow = Arrow(xcoord,1.67,xcoord,1.87,0.015,"|>")
                arrow.SetAngle(50)
                arrow.SetLineWidth(6)
                arrow.SetLineColor(2)
                arrow.SetFillColor(2)
                arrow.Draw()
            if data[0].GetBinContent(i)/stack.sum.GetBinContent(i) <= -2:
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





def generatedatalegend(inputdata,inputstack):
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

        for dataset in inputdata:
            #print "total Data: ", str(dataset.Integral())
            if plotData:
                datalegend.AddEntry(dataset,label = "Data (" + str(round(dataset.integral(overflow=True),1)) +")",style ="EP")
            #dataset.SetMarkerStyle('circle')
            #dataset.SetMarkerSize(3) 
            #dataset.Draw("SAME EP")
        errorband = inputstack.sum.Clone()
        errorband.SetLineWidth(10)
        errorband.SetFillStyle(3244)
        errorband.SetFillColor(922)

        if whichSR == "A" or whichSR == "B" or  whichSR== "D" or whichSR== "VRC" or whichSR =="VRD":
            datalegend.AddEntry(inputstack.sum, label = "SM (" + str(round(float(inputstack.sum.integral(overflow=True)),1)) + "\pm" + str(round(float(inputstack.sum.integral(error= True, overflow=True)[1]),1)   ) + ")",style = "L")
        else:
            datalegend.AddEntry(inputstack.sum, label = "SM (" + str(round(float(inputstack.sum.integral(overflow=True)),1)) + ")",style = "L")
        datalegend.Draw("SAME")


def generatebackgroundlegend(backgrounds,backgroundnames,signals,signalnames):
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
    for (background,backgroundname) in zip(backgrounds,backgroundnames):
        if doRatio and stack.sum.integral(overflow=True) != 0 :
            relativeyield = str(round(100*background.integral(overflow=True)/stack.sum.integral(overflow=True),1))
            legend.AddEntry(background,label =backgroundname + " (" + relativeyield + "%)",style="F")
        else:
            absoluteyield,error = background.integral(error=True,overflow=True)
            absoluteyield = str(round(absoluteyield,1))
            error = str(round(error,1))
            legend.AddEntry(background,label =backgroundname + " (" + absoluteyield +")",style="F")
        
    for (signal,signalname) in zip(signals,signalnames):
        #print str(signalname) + ": " + str(signal.Integral())
        if doRatio and stack.sum.integral(overflow=True) !=0:
            relativeyield = str(round(100*signal.integral(overflow=True)/stack.sum.integral(overflow=True),1))
            legend.AddEntry(background,label =backgroundname + " (" + relativeyield + "%)",style="L")
        else:
            absoluteyield = str(round(signal.integral(overflow=True),1))
            legend.AddEntry(background,label =backgroundname + " (" + absoluteyield + ")",style="L")
        
        #relativeyield = str(round(100*signal.Integral()/stack.Integral(),1))
        #legend.AddEntry(signal,label = signalname + " (" + str(round(signal.Integral(),1)) + ")",style ="L")
        #signal.Draw("Hist SAME X0")
    legend.Draw("SAME");


def retreiveLumiWeight(sampleType):
    if sampleType in MC:
        isType = 0
        if sampleType == "MC2017":
            luminosity = "43.9e3"
        if sampleType == "MC2018":
            luminosity = "36.2e3"
        elif sampleType == "MC":
            luminosity = "36.2e3"
        else:
            luminosity = "36.2e3"

        #luminosity = "36.1e3"
        #luminosity = "43.9e3"
        weight  = Cut(luminosity+ "*trigMatch_1L2LTrigOR*pileupWeight*leptonWeight*bTagWeight*jvtWeight*FFWeight*genWeight*eventWeight")
                                  
       # print "retreive weight"
        #*pileupWeight*leptonWeight*bTagWeight*genWeight*eventWeight*jvtWeight
    if sampleType in DD:
        #if(variable not in MeVlist):
        #    variable = variable.replace("/1000","")
        isType = 0
        luminosity = "1"
        if sampleName == "Zjetsee":
            luminosity = "1"
        weight  = Cut(luminosity + "*trigMatch_1L2LTrigOR*pileupWeight*leptonWeight*bTagWeight*genWeight*eventWeight*jvtWeight")
    if sampleType in SIGNAL:
        isType = 1
        luminosity = "36.1"
        weight  = Cut(luminosity+ "*trigMatch_1L2LTrigOR*pileupWeight*leptonWeight*bTagWeight*genWeight*eventWeight*jvtWeight")
    if sampleType in DATA:
        isType = 2
        luminosity = "1"
        weight  = Cut("1")
    return luminosity,weight,isType


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

    rjhiggs ='391'
    rjwjets ='922'
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


def retreiveTree(rootfile):
    sample = sampleDict[rootfile]
    if("data15" in rootfile):
        print "[TREES][LOADING]: DATA15"
        tree = sample.data1516
    elif("data17" in rootfile):
        print "[TREES][LOADING]: DATA17"
        tree = sample.data17
    elif("data18" in rootfile):
        print "[TREES][LOADING]: DATA18"
        tree = sample.data
    elif("higgs" in rootfile):
        print "[TREES][LOADING]: HIGGS"
        tree = sample.higgs_NoSys
    elif("singleTop" in rootfile):
        print "[TREES][LOADING]: SINGLETOP"
        tree = sample.singleTop_NoSys
    elif("topOther" in rootfile):
        print "[TREES][LOADING]: TOPOTHER"
        tree = sample.topOther_NoSys
    elif("triboson" in rootfile):
        print "[TREES][LOADING]: TRIBOSON"
        tree = sample.triboson_NoSys
    elif("Vgamma" in rootfile):
        print "[TREES][LOADING]: VGAMMA"
        tree = sample.Vgamma_NoSys
    elif("Wjets" in rootfile):
        print "[TREES][LOADING]: WJETS"
        tree = sample.Wjets_NoSys
    elif("Zjets" in rootfile):
        print "[TREES][LOADING]: ZJETS"
        tree = sample.Zjets_NoSys
    elif("DY" in rootfile):
        print "[TREES][LOADING]: LOWMASSDY"
        tree = sample.lowMassDY_NoSys
    elif("diboson" in rootfile):
        print "[TREES][LOADING]: DIBOSON"
        tree = sample.diboson_NoSys
    elif("ttbar_dilep" in rootfile):
        print "[TREES][LOADING]: TTBAR_DILEP"
        tree = sample.ttbar_dilep_NoSys
    elif("ttbar" in rootfile):
        print "[TREES][LOADING]: TTBAR"
        tree = sample.ttbar_NoSys

    return tree





sampleDict = {}
treeDict = {}
for (rootfile,sampleName,sampleType,sampleBool) in zip(sampleList,sampleNames,sampleTypes, sampleBools):
    if sampleBool == "Plot":
        sampleDict[rootfile] = root_open(os.path.join(sampleLocation,rootfile))                
        treeDict[rootfile] = retreiveTree(rootfile)







for (variable,xmin,xmax,nbins,xtitle,ytitle,variable_bool) in zip(variable_list,xmin_list,xmax_list,nbins_list,xtitle_list,ytitle_list,variable_bool_list):
    if variable_bool == 'Plot':    
      
        #str(int(sys.argv[5]))
 
        canvas = Canvas(width=canvaswidth,height=int((1-(1-doRatio)*0.2)*canvasheight))
        canvas.SetFrameBorderMode(0)

        topmargins    = (1.0 , 1.0 )
        bottommargins = (0.0  , 0.4  )
        leftmargins   = (0.0  , 0.0  )
        rightmargins  = (0.0  , 0.0  )
        
        top    = topmargins[doRatio]
        bottom = bottommargins[doRatio]
        left   = leftmargins[doRatio]
        right  = 1 - rightmargins[doRatio]
 
        canvas.cd()

        histpad = Pad(left,bottom,right, top,color="white",bordersize =5)
        if not doRatio:
            histpad.SetBottomMargin(0.15)


        histpad.SetFrameBorderMode(0)

        histpad.Draw()
        histpad.SetLogy()
        histpad.cd()
        histpad.SetFrameBorderSize(2)
        histpad.SetFrameLineWidth(2);

        if(doRatio):
            canvas.cd()
            ratiopad    = Pad(left,0.00,right,bottom-0.02)
            ratiopad.SetBottomMargin(0.33)
            ratiopad.SetTopMargin(0.03)
            ratiopad.SetFrameLineWidth(2);
            ratiopad.Draw()
            histpad.cd()

        stack   = HistStack()
        #if "RJ" in whichSR :
        #    yminimum = 1e-1
        #    ymaximum = 1e8
        stack.SetMinimum(yminimum)
        stack.SetMaximum(ymaximum)
        samples = []
        backgrounds = []
        signals = []
        data    = []
        stackyield = 0
        errorsum   = 0 
        

        backgrounds = []
        backgroundnames = []
        temphistlist = []
        signalnames = []
        for (rootfile,sampleName,sampleType,sampleBool) in zip(sampleList,sampleNames,sampleTypes, sampleBools):
            if sampleBool in PLOT:

                if plotData == 0:
                    if "data" in rootfile:
                        continue 

                isBKG  = False
                isSIGNAL  = False
                isDATA = False                
                #print "sampleType: ", sampleType 
                luminosity,weight,isType = retreiveLumiWeight(sampleType)

                if isType==0:
                    isBKG=True
                elif isType ==1:
                    isSIGNAL=True
                elif isType ==2:
                    isDATA=True

                #sample = root_open(os.path.join(sampleLocation,rootfile))                
                #tree = retreiveTree(rootfile)
                #sample = sampleDict[rootfile]
                #tree = treeDict[rootfile]


                whichSR_label, cutlist,cutnames = retreiveRegionInformation(whichSR,sampleType) 
                #output whichSR_label and cutlist 
                samplePlottype,sampleFill,sampleLinecolor,sampleLinewidth,sampleFillcolor,sampleLineStyle,colorlist,linestylelist = samplestyle( isBKG,isSIGNAL,isDATA )
#                sampleFillcolor = colorAllocator(rootfile,"RJ")
                

                total = Cut("1")
                for cut in cutlist:
                    total = total & cut


                temphist = "hist" + sampleName
                histogram =temphist + "(" + nbins+ "," + xmin +"," + xmax+ ")"

                # temphist = Hist(int(nbins),float(xmin),float(xmax))
                # temphist.SetName(sampleName)

                temphist = treeDict[rootfile].Draw(variable + ">>" + histogram, selection = weight*total,
                                     drawstyle = samplePlottype,
                                     fillcolor = sampleFillcolor,
                                     fillstyle=sampleFill,
                                     linecolor=sampleLinecolor,
                                     linewidth = sampleLinewidth,
                                     linestyle=sampleLineStyle
                                     )
                temphist.SetName(sampleName)

                #temphist.SetName(sampleName)
                temphist.overflow(1)
                temphist.merge_bins([(0, 1), (-2, -1)])
                temphist.Sumw2()
               
                if isBKG:
                    backgrounds.append(temphist.Clone())
                    backgroundnames.append(sampleName)
                    #stack.Add(temphist)#temphist[-1])

                if isSIGNAL:
                    signalnames.append(sampleName)
                    signals.append(temphist.Clone())
                if isDATA:
                    data.append(temphist.Clone())



        backgroundnames_original = backgroundnames 

        zipped = zip(backgrounds, backgroundnames)
        zipped.sort( key=lambda x: x[0].integral(overflow=True))
        backgrounds,backgroundnames = zip(*zipped)

        for background in backgrounds:
            stack.Add(background)


        histpad.cd()
        plotstackobjects(stack)
        plotsignalobjects(signals)
        plotdataobjects(data) 

        zipped_again = zip(backgroundnames,backgrounds)
        zipped_again.sort(key = lambda x: backgroundnames_original.index(x[0]))
        backgroundnames,backgrounds = zip(*zipped_again)



        atlaslabel('#it{#bf{ATLAS}} ' + atlas)
        
        if (datayear == "2015"):
            energylabel("13TeV, 36.1 fb^{-1}")
            toprightplotlabel('#lower[0.4]{Rel21:Data1516}')
        elif(datayear=="2017"):
            energylabel("13TeV, 43.9 fb^{-1}")
            toprightplotlabel('#lower[0.4]{Rel21:Data17}')    
        elif(datayear=="2018"):
            energylabel("13TeV, 36.2 fb^{-1}")
            toprightplotlabel('#lower[0.4]{Rel21:Data18 mc16cd}') 
        SRlabel( whichSR_label)



        generatedatalegend(data,stack)
        generatebackgroundlegend(backgrounds,backgroundnames,signals,signalnames)
        
        stack.yaxis.SetTitle(ytitle)
        stack.yaxis.SetTitleOffset(2)
        stack.yaxis.set_label_size(int(canvasheight*labelscale*1.5))
    
        canvas.cd()
        if doRatio:
            stack.xaxis.set_label_size(0)
        else:
            stack.xaxis.SetTitle(xtitle)
            stack.xaxis.SetTitleOffset(1.5)
            stack.xaxis.set_label_size(int(canvasheight*labelscale*1.5))


        canvas.cd()
        if whichSR in CRlist:
            NormalisationFactor,NFerror = calculateNFs(backgrounds,backgroundnames,data)
            
            topleftplotlabel('NF: ' + str(round(NormalisationFactor,3)) + "\pm" + str(round(NFerror,3)) ) 
        elif whichSR in ABCDlist:
            NormalisationFactor,NFerror = calculateNFs(backgrounds,backgroundnames,data)
            topleftplotlabel('Data-MC(non): ' + str(round(NormalisationFactor,3)) + "\pm" + str(round(NFerror,3)) ) 
        else:
            topleftplotlabel('NF Not Applied')
     
        if doRatio:
            ratiopad.cd()
            plotratio(data,stack)
            ratiopad.Modified()
            ratiopad.Update()


        histpad.cd()

        del colorlist 
        colorlist = []
        for entry in colorlistReset:
            colorlist.append(entry)


#        print colorlist
        del linestylelist
        linestylelist = []
        for entry in linestylelistReset:
            linestylelist.append(entry)




        if variable == "nJet20":
            cutflowstring = "Samples:"
            yieldstring = whichSR
            primaryyield=0.0
            for (background,backgroundname) in zip(backgrounds,backgroundnames):
                cutflowstring = cutflowstring + "&" + backgroundname 
            cutflowstring = cutflowstring + "\\\ \\hline"
            for (background,backgroundname) in zip(backgrounds,backgroundnames):
                primarybackground = ""
                background.Sumw2()
                backgroundyield,cutflowerror = background.integral(error=True,overflow=True)
                backgroundyield = round( background.integral(error=True,overflow=True)[0],2)
                cutflowerror = str(round(background.integral(error=True,overflow=True)[1] ,2)    )
                if whichSR in VVCRlist:
                    primarybackground ="VV"
                elif whichSR in TOPCRlist:
                    primarybackground = ("Top","topOther","singleTop")

                if backgroundname in primarybackground:
                    primaryyield = primaryyield + backgroundyield 

                yieldstring = yieldstring + "&" + str(backgroundyield) + "\pm" + cutflowerror


            cutflowstring = cutflowstring + "&" + "Total &CR Purity& CR NF& Data& Data/MC"
            yieldstring = yieldstring + "&" + str(round(stack.sum.integral(error=True,overflow=True)[0], 2) ) + "\pm" + str(round(stack.sum.integral(error=True,overflow=True)[1], 2) )

            if whichSR in CRlist:
                yieldstring = yieldstring + "&" + str(round(primaryyield/stack.sum.integral(error=True,overflow=True)[0],2)    ) 
                yieldstring = yieldstring + "&" + str(round(NormalisationFactor,3)) + "\pm" + str(round(NFerror,3)) 
            else:
                yieldstring = yieldstring + "& - & - "

            if whichSR in SRlist:
                yieldstring = yieldstring + "& - & -" 
            else:
                yieldstring = yieldstring + "&" + str(round(data[0].integral(error=True,overflow=True)[0], 2) ) + "&" + str(round(data[0].integral(error=True,overflow=True)[0]/stack.sum.integral(error=True,overflow=True)[0],2)    )

            print cutflowstring
            print yieldstring

        os.system("mkdir -p " + os.path.join(outputfolder,whichSR) )
        if "/" in variable:
            newvariable = variable.replace("/","_")
            newvariable = newvariable.replace("_1000","")
            canvas.Print(outputfolder + "/" + whichSR + "/log_"+ newvariable+ "_" + whichSR + "_"+str(sys.argv[4])+".png")
        else:
            canvas.Print(outputfolder + "/" + whichSR + "/log_"  + variable + "_"+whichSR+ "_"+str(sys.argv[4])+".png")

        histpad.SetLogy(0)
        stack.SetMinimum(0.0)
        stack.SetMaximum(3*stack.sum.GetMaximum())
        if "/" in variable:
            newvariable = variable.replace("/","_")
            newvariable = newvariable.replace("_1000","")
            
            canvas.Print(outputfolder + "/" + whichSR + "/lin_"+ newvariable+ "_" + whichSR + "_"+str(sys.argv[4])+".png")
        else:
            canvas.Print(outputfolder + "/" + whichSR + "/lin_"  + variable + "_"+whichSR+ "_"+str(sys.argv[4])+".png")

