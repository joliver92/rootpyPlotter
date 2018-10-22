#!/usr/env python

#from os import system
import os as os

PRE = ["RJ2LA"]
CR2L = ["CR2L-VV","CR2L-TOP","VR2L-VV","VR2L-TOP","VR2L-ZJETS","CR2L_ISR-VV","CR2L_ISR-TOP","VR2L_ISR-VV","VR2L_ISR-TOP","VR2L_ISR-ZJETS"]
CR3L = ["CR3L-VV","VR3L-VV","CR3L_ISR-VV","VR3L_ISR-VV"]
SR2L = ["SR2L_HIGH","SR2L_INT","SR2L_LOW","SR2L_ISR"]
SR3L = ["SR3L_HIGH","SR3L_INT","SR3L_LOW","SR3L_ISR"]

CR2LLIST = ["CR2L-VV","CR2L-TOP","VR3L_ISR-smallPTCM"]
ABCD=["AA","BB","DD","SR2L_LOW"]

TEST = ["CRZZ","CRWZ","CRZ","CRTOP","CRZZIS4LEP"]
number=0
outputlocation = "ABCDMETHOD2VALIDATION2015" +str(number) + "/ "
outputlocation = "ABCDMETHOD2VALIDATION2015 "
outputlocation = "NFStudiesOverflow "
outputlocation = "TEST " 
#os.system("mkdir -p " + outputlocation)

SR=["SR2L_LOW"]

#CR2L= ["CR2L-VV"]
#CR2L= ["CR3L-VV"]
outputlocation="ROOTPYORDEREDDICT1"
print outputlocation
print outputlocation[-1]

if outputlocation[-1] !=" ":
	print "outputlocation"
	outputlocation += "/ "

print outputlocation
os.system("mkdir -p " + outputlocation)


CR2L= ["SR2L_HIGH"]
#CR2L= ["CR2L-VV"]
CR2L = ["CR2L-VV","CR2L-TOP","CR2L_ISR-VV"]
for REGION in CR2L:
	os.system("python rootpyPlotter.py  --output " + outputlocation + " --region " + REGION + " --dataperiods 1516" )

#  samplesnew/ " + outputlocation + signalregion +" Nominal 0 CUTFLOW")
#	os.system("python plotSEPT.py  samples2018/ " + outputlocation + signalregion +" Nominal 0 NOCUTFLOW")



#    nodata = ["SR2L_ISR","2L2JHIGH","2L2JINT","2L2JLOW","2L2JCOMP","3LHIGH","3LINT","3LLOW","3LCOMP"]
#    dontDoData = 0
#    for x in nodata:
#        if signalregion == x :
#            print "dont do data"
#            dontDoData = 1
#        else:
#            dontDoData = 0

#    if dontDoData:
#        print "dont plot data"

#    else:
#        print "CR"
#        os.system("nohup python plotSEPT.py  samplesnew/ " + outputlocation + signalregion +" Nominal 1 >" + "TEST" + signalregion + ".txt &")

