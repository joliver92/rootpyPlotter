from calculationtools import calculateNFs
BLINDEDLIST = ("SR2L_LOW", "SR2L_INT", "SR2L_HIGH","SR2L_ISR","SR3L_LOW","SR3L_INT","SR3L_HIGH","SR3L_ISR")
VVCRlist =("CR2L-VV","CR2L_ISR-VV","CR3L-VV","CR3L_ISR-VV")
TOPCRlist = ("CR2L-TOP","CR2L_ISR-TOP")
CRlist = VVCRlist + TOPCRlist
ABCDlist = ("A","B","D","VRC","VRD")
SRlist = ("SR2L_LOW", "SR2L_INT", "SR2L_HIGH","SR2L_ISR","SR3L_LOW","SR3L_INT","SR3L_HIGH","SR3L_ISR")

def produceTitle(Region,backgroundstacks):
    cutflowstring = "Samples:"
    for LegendEntry in backgroundstacks:
        if LegendEntry == 'Data': continue
        #if ( Region.startswith("SR")): continue
        cutflowstring += "& $" + LegendEntry + "$"
    cutflowstring += "&Total&CR Purity& CR NF& Data& Data/MC \\\ \\hline "
    #cutflowstring += "\\\ \\hline" 
    return cutflowstring

def produceBackgroundYields(Region,backgroundstacks,stack,datastack):
    yieldstring = Region 

    primaryyield = 0.0 
    #primarybackground = []
    #for LegendEntry in backgroundstacks:
    if Region in VVCRlist:
        primarybackground =("Diboson","VV")
    elif Region in TOPCRlist:
        primarybackground = ("Top","topOther","singleTop")
    else: 
        primarybackground = []
    totalyield, totalerror = stack.sum.integral(error=True,overflow=True)

    for LegendEntry in backgroundstacks:
        if Region.startswith("SR") and LegendEntry == "Data": continue
        backgroundyield,backgrounderror = backgroundstacks[LegendEntry].sum.integral(error=True,overflow=True)
        if LegendEntry in primarybackground:
            primaryyield += backgroundyield 
        yieldstring += "&$" + str(round(backgroundyield,2)) + "\pm" + str(round(backgrounderror,2)) + "$"
    yieldstring += "&$" + str(round(totalyield,2)) +"\pm" + str(round(totalerror)) + "$"
    if Region in VVCRlist+TOPCRlist:
        yieldstring += "&$" + str(round(primaryyield/totalyield,2)) 
        NormalisationFactor,NFerror = calculateNFs(backgroundstacks,datastack,Region,VVCRlist,TOPCRlist,ABCDlist)
        yieldstring += "&$" + str(round(NormalisationFactor,3)) +"\pm" + str(round(NFerror,3)) + "$"
    else:
        yieldstring = "& - & - "


    return yieldstring


def produceDataYields(Region,datastack,stack):
    if Region.startswith("SR"):
        yieldstring = "& - & - \\\ \\hline "
    else:
        datayield, dataerror   = datastack.sum.integral(error=True,overflow=True)
        totalyield, totalerror = stack.sum.integral(error=True,overflow=True)
        yieldstring = "&$" + str(round(datayield,0)) + "&" + str(round(datayield/totalyield,2)) + "$ \\\ \\hline"
    return yieldstring


def produceExtraInformation(Region,backgroundstacks,VVCRlist,TOPCRlist):
    primaryyield = 0.0 
    #primarybackground = []


    return yieldstring 


def produceRegionBreakdown(backgroundstacks,stack,datastack,Region,CRlist,SRlist,VVCRlist,TOPCRlist,ABCDlist):
    titlestring =  produceTitle(Region,backgroundstacks)
    yieldstring =  produceBackgroundYields(Region,backgroundstacks,stack,datastack)
    #yieldstring += produceExtraInformation(Region,backgroundstacks,VVCRlist,TOPCRlist)
    yieldstring += produceDataYields(Region,datastack,stack)

    return titlestring,yieldstring
