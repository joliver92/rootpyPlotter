import math
def calculateNFs(backgroundstacks,datastack,Region,VVCRlist,TOPCRlist,ABCDlist):
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
        
def SetNegativeYieldsToZero(stack,nbins):
    for hist in stack:
        for i in range(1,int(nbins)+1):
            if hist.GetBinContent(i) < 0.0:
                print "negative bin content set to 0.0"
                hist.SetBinContent(i,0.0) 
