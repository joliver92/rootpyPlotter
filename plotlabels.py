import ROOT
from calculationtools import calculateNFs
def atlaslabel( input,defaultlabelsize,labelmargin):
    plottitle = ROOT.TLatex(labelmargin,0.87,input)
    plottitle.SetTextFont(43)
    plottitle.SetTextSize(defaultlabelsize*1.2)
    plottitle.SetNDC()
    plottitle.Draw()

def energylabel(input,defaultlabelsize,labelmargin):
    plottitle = ROOT.TLatex(labelmargin,0.805,input)
    plottitle.SetTextFont(43)
    plottitle.SetTextSize(defaultlabelsize*1.2)
    plottitle.SetNDC()
    plottitle.Draw()

def SRlabel(input,defaultlabelsize,labelmargin):
    plottitle = ROOT.TLatex(labelmargin,0.745,input)
    plottitle.SetTextFont(43)
    plottitle.SetTextSize(defaultlabelsize)
    plottitle.SetNDC()
    plottitle.Draw()

def topleftplotlabel(input,defaultlabelsize,labelmargin):
    plottitle = ROOT.TLatex(labelmargin,0.974,input)
    plottitle.SetTextFont(43)
    plottitle.SetTextSize(defaultlabelsize)
    plottitle.SetNDC()
    plottitle.Draw()

def toprightplotlabel(input,defaultlabelsize,labelmargin):
    plottitle = ROOT.TLatex(0.74,0.971,input)
    plottitle.SetTextFont(43)
    plottitle.SetTextSize(defaultlabelsize)
    plottitle.SetNDC()
    plottitle.Draw()



def drawXandYlabels(stack,datastack,xlabel,ylabel,defaultlabelsize,ratiopad,histpad,doRatio,labelmargin):
    histpad.cd()
    stack.yaxis.SetTitle(ylabel)
    stack.yaxis.SetTitleOffset(2)
    stack.yaxis.set_label_size(int(defaultlabelsize*1.5))

    if doRatio:
        ratiopad.cd()
        datastack.xaxis.SetTitle(xlabel)
        datastack.yaxis.SetTitle("Data/SM")
        datastack.yaxis.CenterTitle()
        datastack.xaxis.SetTitleOffset(3.4)
        datastack.yaxis.SetTitleOffset(2)
        datastack.xaxis.set_label_size(int(defaultlabelsize*1.5))
        datastack.yaxis.set_label_size(int(defaultlabelsize*1.5))
    else:
        histpad.cd()
        stack.xaxis.SetTitle(xlabel)
        stack.xaxis.SetTitleOffset(1.5)
        stack.xaxis.set_label_size(int(defaultlabelsize*1.5))
    histpad.cd()


def drawPlotInformation(DataPeriods,atlasStatus,RegionLabel,histpad,defaultlabelsize,labelmargin,donminus1):
        atlaslabel('#it{#bf{ATLAS}} ' + atlasStatus,defaultlabelsize,labelmargin)
        if(DataPeriods == '1516'):
            energylabel("13TeV, 36.2 fb^{-1}",defaultlabelsize,labelmargin)
            toprightplotlabel('#lower[0.4]{Rel21:Data1516}',defaultlabelsize,labelmargin)
        elif(DataPeriods== '17'):
            energylabel("13TeV, 43.9 fb^{-1}",defaultlabelsize,labelmargin)
            toprightplotlabel('#lower[0.4]{Rel21:Data17}',defaultlabelsize,labelmargin) 
        elif(DataPeriods== '18'):
            energylabel("13TeV, 36.2 fb^{-1}",defaultlabelsize,labelmargin)
            toprightplotlabel('#lower[0.4]{Rel21:Data18}',defaultlabelsize,labelmargin) 
        elif(DataPeriods=='15-17'):
            energylabel("13TeV, 80.1 fb^{-1}",defaultlabelsize,labelmargin)
            toprightplotlabel('#lower[0.4]{Rel21:Data15-17}',defaultlabelsize,labelmargin) 
        elif(DataPeriods=='15-18'):
            energylabel("13TeV, 116.3 fb^{-1}",defaultlabelsize,labelmargin)
            toprightplotlabel('#lower[0.4]{Rel21:Data15-18}',defaultlabelsize,labelmargin) 
        elif(DataPeriods=='17-18'):
            energylabel("13TeV, 80.1 fb^{-1}",defaultlabelsize,labelmargin)
            toprightplotlabel('#lower[0.4]{Rel21:Data17-18}',defaultlabelsize,labelmargin) 
        if donminus1:
            SRlabel( RegionLabel + " N-1",defaultlabelsize,labelmargin)
        else:
            SRlabel( RegionLabel ,defaultlabelsize,labelmargin)

        
def drawTopLeftInformation(Region,CRlist,VVCRlist,TOPCRlist,ABCDlist,donminus1,backgroundstacks,datastack,defaultlabelsize,labelmargin):
    if Region in CRlist and donminus1 == 0 :
        NormalisationFactor,NFerror = calculateNFs(backgroundstacks,datastack,Region,VVCRlist,TOPCRlist,ABCDlist)
        topleftplotlabel('NF: ' + str(round(NormalisationFactor,3)) + "\pm" + str(round(NFerror,3)) ,defaultlabelsize,labelmargin) 
    elif Region in ABCDlist and donminus1 == 0 :
        DataEstimate,DataEstimateError = calculateNFs(backgroundstacks,datastack,Region,VVCRlist,TOPCRlist,ABCDlist)
        topleftplotlabel('Data-MC(non): ' + str(round(DataEstimate,3)) + "\pm" + str(round(DataEstimateError,3)),defaultlabelsize,labelmargin ) 
    else:
        topleftplotlabel('NF Not Calculated',defaultlabelsize,labelmargin)





def generateYlabel(units,nbins,xmin,xmax):
    if 'eV' in units:
        binning = str(round((xmax - xmin)/nbins,0)).split('.')[0]
        ylabel = "Events/" + binning + units
    elif "1" in units:
        binning = ""
        units = ""
        ylabel = "Events"
    elif 'rad' in units:
        binning = str(round((xmax - xmin)/nbins,2))
        ylabel = "Events/" + binning + units
    elif units == '':
        binning = str(round((xmax - xmin)/nbins,2))
        ylabel = "Events/" + binning + units
    return ylabel



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
