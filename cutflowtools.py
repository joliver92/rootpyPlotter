from calculationtools import calculateNFs
def produceRegionBreakdown(backgroundstacks,stack,datastack,Region,CRlist,SRlist,VVCRlist,TOPCRlist,ABCDlist):
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
        NormalisationFactor,NFerror = calculateNFs(backgroundstacks,datastack,Region,VVCRlist,TOPCRlist,ABCDlist)
        yieldstring += "&$" + str(round(NormalisationFactor,3)) +"\pm" + str(round(NFerror,3)) + "$"
    else:
        yieldstring += "& - & - "

    if Region in SRlist:
        yieldstring += "& - & - \\\ \\hline "
    else:
        yieldstring += "&$" + str(round(datayield,0)) + "&" + str(round(datayield/totalyield,2)) + "$  \\\ \\hline"

    return cutflowstring,yieldstring
