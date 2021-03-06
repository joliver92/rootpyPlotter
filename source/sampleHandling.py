from rootpy.plotting.shapes import Line,Arrow


def treeloader():
    global sampleDictionary
    global sampleLocationDictionary
    global treeDict
    
    for sample in sampleDictionary:  
        Year = sampleDictionary[sample]['year']
        Filename = sampleDictionary[sample]['filename']
        Location = sampleLocationDictionary[Year]
        rootfileDictionary[sample] = root_open(os.path.join(Location,Filename))
        treeDict[sample] = retreiveTree(sample,sampleDictionary,rootfileDictionary)
     

def retreiveTree(sample,sampleDictionary,rootfileDictionary):
    Filename = sampleDictionary[sample]['filename']
    rootfile  = rootfileDictionary[sample]

    if("data15" in Filename):
        tree = rootfile.data1516
    elif("data17" in Filename):
        tree = rootfile.data17
    elif("data18" in Filename):
        tree = rootfile.data
    elif("higgs" in Filename):
        tree = rootfile.higgs_NoSys
    elif("singleTop" in Filename):
        tree = rootfile.singleTop_NoSys
    elif("topOther" in Filename):
        tree = rootfile.topOther_NoSys
    elif("triboson" in Filename):
        tree = rootfile.triboson_NoSys
    elif("Vgamma" in Filename):
        tree = rootfile.Vgamma_NoSys
    elif("Wjets" in Filename):
        tree = rootfile.Wjets_NoSys
    elif("Zjets" in Filename):
        tree = rootfile.Zjets_NoSys
    elif("DY" in Filename):
        tree = rootfile.lowMassDY_NoSys
    elif("diboson" in Filename):
        tree = rootfile.diboson_NoSys
    elif("ttbar_dilep" in Filename):
        tree = rootfile.ttbar_dilep_NoSys
    elif("ttbar" in Filename):
        tree = rootfile.ttbar_NoSys

    return tree






def drawBackgrounds(stack):
    temphist = stack.sum.Clone()
    #temphist.merge_bins([(nbins,nbins+1)])
    stack.Draw()
    stack.sum.SetFillStyle(0)
    stack.sum.SetLineColor("black")
    stack.sum.SetLineWidth(4)
    stack.sum.SetMarkerSize(0)
    
    stack.sum.Draw("Hist SAME")

    errorband = stack.sum.Clone()
    errorband.SetMarkerSize(0)
    errorband.SetLineWidth(10)
    errorband.SetFillStyle(3244)
    errorband.SetFillColor(922)

    errorband.Draw("SAME E2P")




def drawsignalobjects(backgroundstacks):
    for LegendEntry in backgroundstacks:
        if 'Signal' in LegendEntry:
            backgroundstacks[LegendEntry].sum.Draw("Hist SAME X0")


def drawData(datastack,Region,BLINDEDLIST):
    if Region not in BLINDEDLIST:
        datastack.sum.SetMarkerStyle('circle')
        datastack.sum.SetMarkerSize(3) 
        datastack.sum.SetLineWidth(4)
        datastack.sum.Draw("SAME EP")


def drawRatio(histRatio,stack,Region,BLINDEDLIST,nbins,xmin,xmax):
    #histRatio = datastack.sum.Clone()
    #histRatio.merge_bins([(0, 1), (-2, -1)])

    tempDataStack = histRatio.Clone()
    ratioMinimum=0
    ratioMaximum=2
    histRatio.SetMinimum(ratioMinimum)
    histRatio.SetMaximum(ratioMaximum)
    histRatio.yaxis.divisions = 5
    histRatio.Divide(stack.sum)

    if Region not in BLINDEDLIST: 
        histRatio.Draw("PE")
    
    line = Line(float(xmin)+1e-2*float(xmax),1.,float(xmax)-1e-2*float(xmax),1.);
    line.SetLineWidth(4);
    line.SetLineColor("red");
    line.Draw();
    

    if Region not in BLINDEDLIST:
        histRatio.Draw("SAME EP")

    MCerrorband = stack.sum.Clone()
    MCerrorband.SetLineWidth(10)
    MCerrorband.SetFillStyle(3244)
    MCerrorband.SetFillColor(922)


    for i in range(1,int(nbins)+1):
        if stack.sum.GetBinContent(i) != 0:
            if tempDataStack.GetBinContent(i)/stack.sum.GetBinContent(i) >= 2:
                xcoord = stack.sum.GetBinCenter(i)
                arrow = Arrow(xcoord,1.67,xcoord,1.87,0.015,"|>")
                arrow.SetAngle(50)
                arrow.SetLineWidth(6)
                arrow.SetLineColor(2)
                arrow.SetFillColor(2)
                arrow.Draw()
            if tempDataStack.GetBinContent(i)/stack.sum.GetBinContent(i) <= -2:
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
#    return histRatio
