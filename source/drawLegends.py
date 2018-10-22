from rootpy.plotting import Legend
def drawDataLegend(inputdatastack,inputstack,plotData,BLINDEDLIST,defaultlabelsize,Region):
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
                                      textsize    = defaultlabelsize,
                                      header      = None)
        datalegend.SetLineColor(0)


        if plotData:
            if Region not in BLINDEDLIST:
                datalegend.AddEntry(inputdatastack.sum,label = "Data [" + str(round(inputdatastack.sum.integral(overflow=True),1)) +"]",style ="EP")

        errorband = inputstack.sum.Clone()
        errorband.SetLineWidth(10)
        errorband.SetFillStyle(3244)
        errorband.SetFillColor(922)

        if Region == "A" or Region == "B" or  Region== "D" or Region== "VRC" or Region =="VRD":
            datalegend.AddEntry(inputstack.sum, label = "SM [" + str(round(float(inputstack.sum.integral(overflow=True)),1)) + "\pm" + str(round(float(inputstack.sum.integral(error= True, overflow=True)[1]),1)   ) + "]",style = "L")
        else:
            datalegend.AddEntry(inputstack.sum, label = "SM [" + str(round(float(inputstack.sum.integral(overflow=True)),1)) + "]",style = "L")
        datalegend.Draw("SAME")


def drawBackgroundLegend(backgroundstacks,stack,LegendExtraInformation,defaultlabelsize,Region):
    legend_entries=4 #figure out how to remove this magic number

    margin      = 0.30
    rightmargin = 0.07
    topmargin   = 0.05
    entryheight = 0.045
    entrysep    = 0.06

    legend = Legend(legend_entries, leftmargin  = 0.49,
                                      topmargin   = topmargin           ,
                                      rightmargin = rightmargin         ,
                                      entryheight = entryheight       ,
                                      entrysep    = entrysep            ,
                                      margin      = margin              ,
                                      textfont    = 43                  ,
                                      textsize    = defaultlabelsize,
                                      header      = None                )

    legend.SetLineColor(0)

    totalyield,totalerror = stack.sum.integral(error=True, overflow=True)

    for LegendGroup in backgroundstacks:
        if LegendGroup is 'Data': continue

        backgroundyield,backgrounderror = backgroundstacks[LegendGroup].sum.integral(error=True,overflow=True)
        if LegendExtraInformation == "Relative" and totalyield!=0:
            relativeyield = str(round(100*backgroundyield/totalyield,1))
            legend.AddEntry(backgroundstacks[LegendGroup].sum,label=LegendGroup + " [" + relativeyield + "%]",style="F" )
        elif LegendExtraInformation == "Absolute":
            legend.AddEntry(backgroundstacks[LegendGroup].sum,label =LegendGroup + " (" + str(round(backgroundyield,1)) +")",style="F")
        else:
            legend.AddEntry(backgroundstacks[LegendGroup].sum,label =LegendGroup ,style="F")

    legend.Draw("SAME");
