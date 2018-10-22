import os.path
import sys
import math
import argparse
from decimal import Decimal
import time 

from collections import OrderedDict
from itertools import izip
from decimal import Decimal
import time 

from rootpy import ROOT 
from rootpy.io import root_open 
from rootpy.io import Directory
from rootpy.plotting import F1, Hist, HistStack, Canvas, Legend, Pad
from rootpy.plotting.shapes import Line,Arrow
from rootpy.plotting.utils  import draw
from rootpy.plotting.views import StackView
from rootpy.plotting.style  import get_style, set_style
from rootpy import asrootpy
from rootpy.tree import Cut
from rootpy.tree import Tree

from regiondefinitions import retreiveRegionInformation

from samples import sampleConfiguration
from variables import variableDictionary

from plotlabels import atlaslabel
from plotlabels import energylabel
from plotlabels import SRlabel
from plotlabels import drawXandYlabels
from plotlabels import drawPlotInformation
from plotlabels import topleftplotlabel
from plotlabels import toprightplotlabel
from plotlabels import RegionYrange
from plotlabels import generateYlabel
from plotlabels import drawTopLeftInformation

from drawLegends import drawDataLegend
from drawLegends import drawBackgroundLegend

from sampleHandling import drawBackgrounds
from sampleHandling import drawData
from sampleHandling import drawRatio
from sampleHandling import drawsignalobjects
from sampleHandling import retreiveTree
from sampleHandling import treeloader
#from sampleHandling import sampleStyleFunc

from cutflowtools import produceRegionBreakdown
from calculationtools import calculateNFs
from calculationtools import SetNegativeYieldsToZero

def sampleStyleFunc(temphist,sample,sampleDictionary):
    fillcolor = sampleDictionary[sample]['fillcolor']
    Type = sampleDictionary[sample]['type']

    samplestyleDictionary = {
    'bkg' : {'plottype':'hist','filltype':'solid','linecolor':0,'linewidth':0},
    'sig' : {'plottype':'hist','filltype':'0'    ,'linecolor':'red'  ,'linewidth':5},
    'data': {'plottype':'EP'  ,'filltype':'0'    ,'linecolor':'black','linewidth':5}
    }
    temphist.drawstyle = samplestyleDictionary[Type]['plottype']
    temphist.fillcolor = sampleDictionary[sample]['fillcolor'] 
    temphist.fillstyle = samplestyleDictionary[Type]['filltype']
    temphist.linecolor = samplestyleDictionary[Type]['linecolor']
    temphist.linewidth = samplestyleDictionary[Type]['linewidth']
    temphist.linestyle = 'solid'





style = get_style('ATLAS')
titlesize=25
labelscale = 0.025
labelmargin=0.20 #Labeling
canvaswidth = 1500
canvasheight= 1600
defaultlabelsize = canvasheight*labelscale 
titlesize=defaultlabelsize*1.4


style.SetTitleSize(titlesize, "x")
style.SetTitleSize(titlesize,"y")
style.SetTitleYOffset(1)
style.SetTitleXOffset(1)
set_style(style)
ROOT.gStyle.SetPadBottomMargin(0.)
ROOT.gStyle.SetLineWidth(4)
ROOT.gROOT.SetBatch(True)
Hist.SetDefaultSumw2(True)

t0 = time.time()

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

DataPeriods = args.dataperiods 
Region = args.region 


doBreakdown = args.regionbreakdown
outputfolder = args.output
systematics  = args.systematics 
doRatio      = args.ratioplot 
donminus1    = args.nminus1 


BLINDEDLIST = ("SR2L_LOW", "SR2L_INT", "SR2L_HIGH","SR2L_ISR","SR3L_LOW","SR3L_INT","SR3L_HIGH","SR3L_ISR")
VVCRlist =("CR2L-VV","CR2L_ISR-VV","CR3L-VV","CR3L_ISR-VV")
TOPCRlist = ("CR2L-TOP","CR2L_ISR-TOP")
CRlist = VVCRlist + TOPCRlist
ABCDlist = ("A","B","D","VRC","VRD")
SRlist = ("SR2L_LOW", "SR2L_INT", "SR2L_HIGH","SR2L_ISR","SR3L_LOW","SR3L_INT","SR3L_HIGH","SR3L_ISR")

if Region.startswith("SR"): print "SIGNAL REGION"
#print "SR: "

if Region.startswith("SR"): 
    BLINDED = True
else:
    BLINDED = False

if BLINDED:
    plotData = 0
    doRatio  = 0 
else:
    plotData = 1 


atlasStatus="Internal"
sqrts  = 13
LegendExtraInformation = "Relative" #Absolute and None 

sampleLocationDictionary = OrderedDict()
sampleLocationDictionary['1516'] = "samplesnew"
sampleLocationDictionary['17'] = "samples2017"
sampleLocationDictionary['18'] = "samples2018"

#ROOT.gPad.SetBorderWidth(5)  

weightstring ="trigMatch_1L2LTrigOR*pileupWeight*leptonWeight*bTagWeight*genWeight*eventWeight*jvtWeight"
LuminosityDictionary = { 'data':{'1516':"1",'17':"1",'18':"1"},'bkg':{'1516':"36.2e3",'17':"43.9e3",'18':"36.2e3"},'sig':{'1516':"36.2e3",'17':"43.9e3",'18':"36.2e3"}  }
WeightDictionary    = {'data':"1", 'bkg': weightstring,'sig': weightstring}


sampleDictionary = sampleConfiguration(DataPeriods)

sampleDict = OrderedDict()
treeDict = OrderedDict()
treeDict2 = OrderedDict()
rootfileDictionary =  OrderedDict()

RegionLabel= retreiveRegionInformation(Region)[0]
Cutlist    = retreiveRegionInformation(Region)[1]
Cutnames   = retreiveRegionInformation(Region)[2]


#total = Cut("1")
#for cut in Cutlist:
#    if (variable in cut) and donminus1:continue 
#    total = total & cut 

    #treeDict2[sample] = retreiveTree(sample)

    #treeDict[sample] = treeDict2[sample].CopyTree(total)
    #del treeDict2[sample]
    #treeDict[sample] = treeDict2[sample]
    #asrootpy(treeDict[sample])
    
    #elist = ROOT.TEntryList("name","title",treeDict[sample])
    #treeDict[sample].Draw(">>elist",total,"entrylist")
    #ROOT.gDirectory
    #treeDict[sample].SetEntryList(elist)
    #print "passed: " + str(elist.GetN())

for sample in sampleDictionary:  
    Year = sampleDictionary[sample]['year']
    Filename = sampleDictionary[sample]['filename']
    Location = sampleLocationDictionary[Year]
    rootfileDictionary[sample] = root_open(os.path.join(Location,Filename))
    treeDict[sample] = retreiveTree(sample,sampleDictionary,rootfileDictionary)
    
#treeloader()

print "[ROOTFILES LOADED]" + str(round(time.time() - t0,2)) + "seconds"

variableDictionary = variableDictionary(Region,doBreakdown)
skimmed = 0
for variable in variableDictionary:
    nbins = int(variableDictionary[variable]['nbins'])
    xmin  = float(variableDictionary[variable]['xmin'])
    xmax  = float(variableDictionary[variable]['xmax'])
    xlabel = variableDictionary[variable]['latex']
    units = variableDictionary[variable]['units']
    ylabel = generateYlabel(units,nbins,xmin,xmax)

    print "[VARIABLE][" + variable  + "]" + str(round(time.time() - t0,0)) + "seconds"

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

    canvas.cd()
    #ratiopad    = Pad(leftmargins[1],0.00,1 - rightmargins[1],bottommargins[1]-0.02)
    ratiopad    = Pad(leftmargins[1],0.00,1 - rightmargins[1],bottommargins[1]-0.02)
    ratiopad.SetBottomMargin(0.33)
    ratiopad.SetTopMargin(0.03)
    ratiopad.SetFrameLineWidth(2);

    if(doRatio):
        ratiopad.Draw()
    histpad.cd()

    stack   = HistStack()
    datastack = HistStack() 
    
    yminimum, ymaximum = RegionYrange(Region)
    stack.SetMinimum(yminimum)
    stack.SetMaximum(ymaximum)

    total = Cut("1")
    for cut in Cutlist:
        if (variable in cut) and donminus1:continue 
        total = total & cut 


    backgroundstacks = OrderedDict()
    background = []
    for sample in sampleDictionary:
        if BLINDED and sample is 'Data': continue
        LegendEntry = sampleDictionary[sample]['legend']
        Type = sampleDictionary[sample]['type']
        backgroundstacks[LegendEntry] = HistStack()

    for sample in sampleDictionary:
        #Name         = sample 
        Type         = sampleDictionary[sample]['type']
        Year         = sampleDictionary[sample]['year']
        LegendEntry  = sampleDictionary[sample]['legend']
        #FillColor    = sampleDictionary[sample]['fillcolor']
        #rootfile     = sampleDictionary[sample]['filename']
        Luminosity   = LuminosityDictionary[Type][Year]
        Weight       = WeightDictionary[Type]

        if BLINDED and Type == 'data': 
            print "[BLINDED][" + sample  + "]" + str(round(time.time() - t0,0)) + "seconds"
            continue
            
        print "[DRAWING][" + sample  + "]" + str(round(time.time() - t0,0)) + "seconds"


        #SelectionCriteria = Cut(Luminosity) * Cut(Weight) * total
        #histogram = Hist(nbins,xmin,xmax)   
        temphist   = treeDict[sample].Draw(variable, hist= Hist(nbins,xmin,xmax),selection = Cut(Luminosity) * Cut(Weight) * total)
        temphist = temphist.merge_bins([(0,1),  (nbins,nbins+1)  ])
        sampleStyleFunc(temphist,sample,sampleDictionary)

        backgroundstacks[LegendEntry].Add(temphist.Clone())


    skimmed = 1 

    for key in backgroundstacks:
        #print "key: " + str(key )
        if 'Data' not in key:
            if 'Signal' in key:continue
            stack.Add(backgroundstacks[key].sum.Clone())
        if 'Data' in key and not BLINDED :
            datastack.Add(backgroundstacks[key].sum.Clone())

  #  print "type of stack.mergebins" + str(type(stack.merge_bins([(nbins,nbins+1)])))
    if doBreakdown:
        cutflowstring, yieldstring = produceRegionBreakdown(backgroundstacks,stack,datastack,Region,CRlist,SRlist,VVCRlist,TOPCRlist,ABCDlist)
        print "[BREAKDOWN][PRODUCED]"
        print cutflowstring        
        print yieldstring 

    SetNegativeYieldsToZero(stack,nbins)
    
    print "[BEFORE DRAW]" + str(round(time.time() - t0,2)) + "seconds"

    drawBackgrounds(stack)
    drawData(datastack,Region,BLINDEDLIST)
    drawsignalobjects(backgroundstacks)
    print "[AFTER DRAW]" + str(round(time.time() - t0,2)) + "seconds"


    if not BLINDED:
        histRatio = datastack.sum.Clone()
    else: 
        histRatio = stack.sum.Clone()
    if doRatio:
        ratiopad.cd()
        drawRatio(histRatio,stack,Region,BLINDEDLIST,nbins,xmin,xmax)

    #canvas.cd()
    histpad.cd()
    drawXandYlabels(stack,histRatio,xlabel,ylabel,defaultlabelsize,ratiopad,histpad,doRatio,labelmargin)
    drawPlotInformation(DataPeriods,atlasStatus,RegionLabel,histpad,defaultlabelsize,labelmargin,donminus1)
    drawTopLeftInformation(Region,CRlist,VVCRlist,TOPCRlist,ABCDlist,donminus1,backgroundstacks,datastack,defaultlabelsize,labelmargin)


    drawDataLegend(datastack,stack,plotData,BLINDEDLIST,defaultlabelsize,Region)
    drawBackgroundLegend(backgroundstacks,stack,LegendExtraInformation,defaultlabelsize,Region) 

   
    dataoutputfolder = os.path.join(outputfolder,"Data" + DataPeriods )

    os.system("mkdir -p " +	dataoutputfolder  )
    os.system("mkdir -p " + os.path.join(dataoutputfolder,Region) )
    os.system("mkdir -p " + os.path.join(dataoutputfolder,Region,"N-1") )


    filenamevariable = variable.replace("/","_").replace("_1000","")
    if donminus1:
        canvas.Print(dataoutputfolder + "/" + Region + "/N-1/log_"+ filenamevariable+ "_" + Region + "_"+systematics+".png")
    else:
        canvas.Print(dataoutputfolder + "/" + Region + "/log_"+ filenamevariable+ "_" + Region + "_"+systematics+".png")

    histpad.SetLogy(0)
    stack.SetMinimum(0.0)
    stack.SetMaximum(3*stack.sum.GetMaximum())

    canvas.Print(dataoutputfolder + "/" + Region + "/lin_"+ filenamevariable+ "_" + Region + "_"+systematics+".png")

    print "[CANVAS][PLOTTED]" + str(round(time.time() - t0,0)) + "seconds"
