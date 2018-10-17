from rootpy.tree import Cut

def retreiveRegionInformation(Region,sampleType="MC"):
    cutnames = [] 
    RegionLabel = ""
    cutlist = ""

    if Region == "RJ2LA":
        cutlist = [Cut("1"),Cut("is2Lep2Jet==1 && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1] > 30")]
        RegionLabel="2L2J-Preselection"
        cutnames = ["Total","2L2J-Preselection"]

    if Region == "CRZ":
        cutlist = [Cut("1"),Cut("is2Lep2Jet==1 && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1] > 30 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && mll_RJ>80. && mll_RJ<100.")]
        RegionLabel="CR-Z"
        cutnames = ["Total","CR-Z"]
    if Region == "CRWZ":
        cutlist = [Cut("1"),Cut("is3Lep2Jet==1 && lepPt[0]>25 && lepPt[1]>25 &&lepPt[2]>20 && jetPt[0]>30 && jetPt[1] > 30 && nBJet30_MV2c10_FixedCutBEff_77 == 0 ")]
        RegionLabel="CR-WZ"
        cutnames = ["Total","CR-WZ"]
    if Region == "CRZZ":
        cutlist = [Cut("1"),Cut("nLep_base == nLep_signal && nLep_base == 4  && nJet20 >=2 && lepPt[0]>25 && nBJet20_MV2c10_FixedCutBEff_77 == 0")]
        RegionLabel="CR-ZZ"
        cutnames = ["Total","CR-ZZ"]
    if Region == "CRZZIS4LEP":
        cutlist = [Cut("1"),Cut("is4Lep2Jet && lepPt[0]>25 && nBJet20_MV2c10_FixedCutBEff_77 == 0")]
        RegionLabel="CR-ZZ"
        cutnames = ["Total","CR-ZZ"]
        
    if Region == "CRTOP":
        cutlist = [Cut("1"),Cut("is2Lep2Jet==1 && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1] > 30 && nBJet20_MV2c10_FixedCutBEff_77 > 0 ")]
        RegionLabel="CR-TOP"
        cutnames = ["Total","CR-TOP"]


    if Region == "CR2L-VV":
        cutlist = [Cut("1"), 
                   Cut("(is4Lep2Jet || (is3Lep2Jet && mTl3>70 && mTl3<100))"),
                   Cut("lept1sign_VR*lept2sign_VR<0"),
                   Cut("abs(lept1sign_VR)==abs(lept2sign_VR) "),
                   Cut("lept1Pt_VR>25"),
                   Cut("lept2Pt_VR>25"),
                   Cut("jetPt[0]>30"),
                   Cut("jetPt[1]>30"),
                   Cut("nJet20 >= 2"),
                   Cut("nBJet20_MV2c10_FixedCutBEff_77 ==0"), 
                   Cut("mll_RJ_VR>80 &&mll_RJ_VR<100"),
                   Cut("mjj>20"),
                   Cut("R_minH2P_minH3P_VR>0.2"),
                   Cut("dphiVP_VR>0.3 && dphiVP_VR<2.8"),
                   Cut("H5PP_VR>200"),Cut("RPT_HT5PP_VR < 0.05")]
        cutnames = ["Total","Preselection","n_{b}^{20,77} veto", "80<m_{ll}<100","m_{jj}>20", "\\frac{minH2P}{minH3P}","0.3<d\phi^{VP}_{VR}<2.8","H5PP_VR>200","RPT_H5PP_VR"]
        RegionLabel = "CR2L-VV"

    if Region == "CR2L-TOP":
        RegionLabel = "CR2L-TOP"
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nJet20 >=2"),
                   Cut("nBJet20_MV2c10_FixedCutBEff_77 ==1"),
                   Cut("mll_RJ>80. && mll_RJ<100."),
                   Cut("mjj>40 && mjj<250"),
                   Cut("R_minH2P_minH3P>0.5"), 
                   Cut("dphiVP>0.3 && dphiVP<2.8"), 
                   Cut("RPT_HT5PP<0.05"), 
                   Cut("H5PP>400")]
        cutnames =["Total","Preselection","Z-window","40<mjj<250","R_minH2P_minH3P>0.5","0.3<dphiVP<2.8","RPT_HT5PP<0.05","H5PP>400"]


    if Region == "VR2L-VV":
        cutlist = [Cut("1"),
                   Cut("(is2Lep2Jet) && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nJet20 >=2"),
                   Cut("nBJet20_MV2c10_FixedCutBEff_77==0 "),
                   Cut("mll_RJ>80 && mll_RJ<100"), 
                   Cut("(mjj>40 && mjj<70) || (mjj>90 && mjj<500)"), 
                   Cut("R_minH2P_minH3P>0.4 && R_minH2P_minH3P<0.8"), 
                   Cut("RPT_HT5PP< 0.05"),
                   Cut("dphiVP>0.3 && dphiVP<2.8"), 
                   Cut("H2PP>250"), 
                   Cut("H5PP>400")]
        cutnames = ["Total",
                    "Preselection",
                    "n_{b}^{20,77} veto",
                    "Z-window",
                    "40<mjj<70,90<mjj<500",
                    "0.4<R_minH2P_minH3P<0.8",
                    "RPT_H5PP<0.05",
                    "0.3<dphiVP<2.8",
                    "H2PP>250",
                    "H5PP>400"]

    if Region == "VR2L-TOP":# normally has a b-tag veto
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])!=abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30"),
                   Cut("nBJet20_MV2c10_FixedCutBEff_77==1"),
                   Cut("(mll_RJ>20 && mll_RJ<80) || mll_RJ>100"),
                   Cut("mjj>40 && mjj<250"),
                   Cut("RPT_HT5PP<0.05"),
                   Cut("R_minH2P_minH3P>0.5"),
                   Cut("dphiVP>0.3 && dphiVP<2.8"),
                   Cut("H5PP>400")]
        cutnames =["Total"]

    if Region == "VR2L-ZJETS":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30"),
                   Cut("nJet20==2"),
                   Cut("mll_RJ>80.&&mll_RJ<100"),
                   Cut("(mjj<60.0 || mjj>100.)"),
                   Cut("RPT_HT5PP<0.05"),
                   Cut("H2PP/H5PP>0.35 && H2PP/H5PP<0.6"),
                   Cut("H5PP>300")]
        cutnames = ["Total",
                    "Preselection",
                    "nJet20=2",
                    "80<m_{ll}<100",
                    "60<mjj || mjj>100",
                    "RPT_HT5PP<0.05",
                    "H2PP/H5PP>0.35",
                    "H2PP/H5PP<0.6",
                    "H5PP>300"]

    if Region == "CR2L_ISR-TOP":
        cutlist = [Cut("1"),
                   Cut("is2L2JInt==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25. && lepPt[1]>25. && jetPt[0]>30. && jetPt[1]>30."), 
                   Cut("nBJet20_MV2c10_FixedCutBEff_77==1"),
                   Cut("MZ>50. && MZ<200."),
                   Cut("MJ>50. && MJ<200."),
                   Cut("dphiISRI>2.8"),
                   Cut("RISR > 0.40 && RISR<0.75"),
                   Cut("PTISR>180."),
                   Cut("PTI>100."),
                   Cut("PTCM<20."),
                   Cut("NjS==2 && NjISR<3")]
        cutnames= ["Total",
                   "n_{b}^{20,77}=1",
                   "50<MZ<200",
                   "50<MJ<200",
                   "dphiISRI>2.8",
                   "0.4<RISR<0.75",
                   "PTISR>180",
                   "PTI>100",
                   "PTCM<20",
                   "NJS=2, NJISR<3"]
    if Region == "VR2L_ISR-TOP": # normally has a b-tag veto
        cutlist = [Cut("1"),
                   Cut("is2L2JInt==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])!=abs(lepFlavor[1]) && lepPt[0]>25. && lepPt[1]>25. && jetPt[0]>30. && jetPt[1]>30."), 
                   Cut("nBJet20_MV2c10_FixedCutBEff_77==1"),
                   Cut("MZ>50. && MZ<200."),
                   Cut("MJ>50. && MJ<200."),
                   Cut("dphiISRI>2.8"),
                   Cut("RISR > 0.40 && RISR<0.75"),
                   Cut("PTISR>180."),
                   Cut("PTI>100."),
                   Cut("PTCM>20."),
                   Cut("NjS==2 && NjISR<3")]
        cutnames =["Total",
                    "Preselection",
                    "nb=1",
                    "50<MZ<200",
                    "50<MJ<200",
                    "dphiISRI>2.8",
                    "0.4<RISR<0.75",
                    "PTISR>180",
                    "PTI>100",
                    "PTCM>20",
                    "NJS=2,NJISR<3"]
    #CHECK MZ MJ
    if Region == "CR2L_ISR-VV":
        cutlist = [Cut("1"),
                   Cut("(is3Lep3Jet==1 || is4Lep3Jet==1) && lept1sign_VR*lept2sign_VR<0 && abs(lept1sign_VR)==abs(lept2sign_VR) && lept1sign_VR*lept2sign_VR<0 && abs(lept1sign_VR)==abs(lept2sign_VR) && lept1Pt_VR>25. && lept2Pt_VR>25. && jetPt[0]>30. && jetPt[1]>30. &&nBJet20_MV2c10_FixedCutBEff_77==0 && MZ_VR>80. && MZ_VR<100."),
                   Cut("MJ_VR>20."),
                   Cut("dphiISRI_VR>2.0"),
                   Cut("RISR_VR > 0.0 && RISR_VR<0.5"),
                   Cut("PTISR_VR>50."),
                   Cut("PTI_VR>50."),
                   Cut("PTCM_VR<30.")]
        cutnames = ["Total",
                    "Preselection",
                    "n_{b}^{20,77} =0",
                    "80<MZ_{VR}<100",
                    "MJ_{VR}>20",
                    "dphiISRIVR >2.0",
                    "0.0<RISR_VR<0.5",
                    "PTISRVR>50",
                    "PTIVR>50",
                    "PTCMVR<30"]
    #CHECK
    if Region == "VR2L_ISR-VV":
        cutlist = [Cut("1"),
                   Cut("(is3Lep3Jet==1 || is4Lep3Jet==1) && lept1sign_VR*lept2sign_VR<0 && abs(lept1sign_VR)==abs(lept2sign_VR)&& lept1Pt_VR>25. && lept2Pt_VR>25. && jetPt[0]>20. && jetPt[1]>20. && nBJet20_MV2c10_FixedCutBEff_77==0"),
                   Cut("(MZ_VR>20. && MZ_VR<80) || MZ_VR > 100 "),
                   Cut("MJ_VR>20"),
                   Cut("RISR_VR>0. && RISR_VR<1"), 
                   Cut("PTISR_VR>70"), 
                   Cut("PTI_VR>70"), 
                   Cut("PTCM_VR<30"),
                   Cut("dphiISRI_VR>2.0")]
        cutnames = ["Total","Preselection","20<MZ_{VR}<80 || MZ>100","MJVR>20","0<RISRVR<1.0","PTISRVR>70","PTIVR>70","PTCMVR<30","dphiISRI_VR>2.0"]
    if Region == "VR2L-ZJETS":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nJet20==2 && mll_RJ>80.&&mll_RJ<100"), 
                   Cut("(mjj<60.0 || mjj>100.)"), 
                   Cut("RPT_HT5PP<0.05"), 
                   Cut("H2PP/H5PP>0.35 && H2PP/H5PP<0.6"), 
                   Cut("H5PP>300")]
        cutnames = ["Total","Preselection","mjj<60||mjj>100","RPT_HT5PP<0.05","0.35<H2PP/H5PP<0.6","H5PP>300"]
    if Region == "VR2L_ISR-ZJETS":
        cutlist = [Cut("1"),
                   Cut("is2L2JInt==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25. && lepPt[1]>25. && jetPt[0]>30. && jetPt[1]>30. && nBJet20_MV2c10_FixedCutBEff_77==0 && MZ>80. && MZ<100."),
                   Cut("(MJ<50. || MJ>110.)"),
                   Cut("dphiISRI>2."),
                   Cut("RISR > 0.20 && RISR<0.75"),
                   Cut("PTISR>100."),
                   Cut("PTI>80."),
                   Cut("PTCM<20."),
                   Cut("NjS==2 && NjISR<3")]
        cutnames = ["Total","Preselection","MJ<50||MJ>100","dphiISRI>2","0.2<RISR<0.75","PTISR>100","PTI>80","PTCM<20","NJS=2,NJISR<3"]
    if Region == "SR2L_HIGH":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && nJet20>=2 && mll_RJ>80 && mll_RJ<100"),
                   Cut("mjj>60 && mjj<100"), 
                   Cut("R_minH2P_minH3P>0.8"), 
                   Cut("RPT_HT5PP< 0.05"), 
                   Cut("dphiVP>0.3 && dphiVP<2.8"), 
                   Cut("H5PP>800")]
        cutnames = ["Total","Preselection","60<mjj<100","R_minH2P_minH3P>0.8","RPT_HT5PP<0.05","0.3<dphiVP<2.8","H5PP>800"]

    if Region == "SR2L_HIGH_2018":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && nJet20>=2 && mll_RJ>80 && mll_RJ<100"),
                   Cut("mjj>60 && mjj<100"),  
                   Cut("RPT_HT5PP< 0.05"), 
                   Cut("dphiVP>0.3 && dphiVP<2.8")]
        cutnames = ["Total","Preselection","60<mjj<100","RPT_HT5PP<0.05","0.3<dphiVP<2.8"]

    if Region == "SR2L_INT_2018":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && nJet20>=2 && mll_RJ>80 && mll_RJ<100"), 
                   Cut("mjj>60 && mjj<100"),
                   Cut("RPT_HT5PP<0.05"),
                   Cut("dphiVP>0.6 && dphiVP<2.6") ]
        cutnames = ["Total","Preselection","60<mjj<100","RPT_HT5PP<0.05","0.6<dphiVP<2.6"]



    if Region == "SR2L_INT":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && nJet20>=2 && mll_RJ>80 && mll_RJ<100"), 
                   Cut("mjj>60 && mjj<100"),
                   Cut("R_minH2P_minH3P>0.8"),
                   Cut("RPT_HT5PP<0.05"),
                   Cut("dphiVP>0.6 && dphiVP<2.6"),
                   Cut("H5PP>600") ]
        cutnames = ["Total","Preselection","60<mjj<100","R_minH2P_minH3P>0.8","RPT_HT5PP<0.05","0.6<dphiVP<2.6","H5PP>600"]

    if Region == "SR2L_LOW":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>70 && mjj<90"),
                   Cut("H2PP/H5PP>0.35 && H2PP/H5PP<0.6"),
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$70<mjj<90$","$0.35<H2PP/H5PP<0.6$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]



        
    if Region =="SR2L_ISR":
        RegionLabel ="SR2L_ISR"
        cutlist   = [ Cut("1"),
                        Cut("is2L2JInt==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0"),
                        Cut("(nJet20 > 2)"),
                        Cut("(MZ>80 && MZ<100)"),
                        Cut(" MJ>50 && MJ<110"),
                        Cut("NjS==2 &&NjISR<3"),
                        Cut("dphiISRI>2.8"),
                        Cut("RISR  > 0.40 && RISR < 0.75"),
                        Cut("PTISR > 180 "),
                        Cut("PTI   > 100"),
                        Cut("PTCM  < 20")
                    ]
        cutnames = ["Total",
                    "Preselection",
                    "Mjj window",
                    "NjS=2,NjISR\\textless3",
                    "$dphiISRI \\textgreater 2.8$",
                    "$0.4 \\textless RISR \\textless 0.75$",
                    "$PTISR \\textgreater 180GeV$",
                    "$PTI \\textgreater 100GeV$",
                    "$PTCM \\textless 20GeV$"
                    ]


    if Region == "VR2L_High-Zjets":
        cutlist = [Cut("is2Lep2Jet && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25. && lepPt[1]>25. && jetPt[0]>30. && jetPt[1]>30. && nBJet20_MV2c10_FixedCutBEff_77==0 && mll_RJ>80. && mll_RJ<100. && (mjj<60.0 || (mjj>100.&& mjj<180)) && H5PP>600. && RPT_HT5PP<0.05 && R_minH2P_minH3P>0.4 && dphiVP>0.3 && dphiVP<2.8")]
        cutnames = ["VR2L_High-Zjets"]
        
    if Region == "VR2L_Low-Zjets":
        cutlist = [Cut("is2Lep2Jet && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25.00 && lepPt[1]>25.00 && jetPt[0]>30.00 && jetPt[1]>30.00 && mll_RJ>80.&&mll_RJ<100.00 && (mjj<60.0 || (mjj>100.&& mjj<180)) && nJet20==2 && nBJet20_MV2c10_FixedCutBEff_77==0 && RPT_HT5PP<0.05 && H2PP/H5PP>0.35 && H2PP/H5PP<0.6 && H5PP>400.00")]
        cutnames = ["VR2L_Low-Zjets"]
    if Region == "CR3L-VV":
        cutlist = [Cut("1"),
                   Cut("is3Lep && ((lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1])) || (lepCharge[0]*lepCharge[2]<0 && abs(lepFlavor[0])==abs(lepFlavor[2])) || (lepCharge[1]*lepCharge[2]<0 && abs(lepFlavor[1])==abs(lepFlavor[2]))) && lepPt[0]>60. && lepPt[1]>40. && lepPt[2]>30."),
                   Cut("nBJet20_MV2c10_FixedCutBEff_77==0"),
                   Cut("nJet20<3"),
                   Cut("mll_RJ>75. && mll_RJ<105"),
                   Cut("mTW>0. && mTW<70."),
                   Cut("R_minH2P_minH3P>0."),
                   Cut("H4PP>250."),
                   Cut("R_HT4PP_H4PP>0.75"),
                   Cut("RPT_HT4PP<0.2")]

        cutnames = ["Total","Preselection","n_{b}^{20,77}=0","nJet20<3","75<mll<105","mTW<70","R_minH2P_minH3P>0.0","H4PP>250.","R_HT4PP_H4PP>0.75","RPT_HT4PP<0.2"]

    if Region == "CR3L-VV-mimiccheck":
        cutlist = [Cut("1"), Cut("nLep_base==3"),
                    Cut("((lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1])) || (lepCharge[0]*lepCharge[2]<0 && abs(lepFlavor[0])==abs(lepFlavor[2])) || (lepCharge[1]*lepCharge[2]<0 && abs(lepFlavor[1])==abs(lepFlavor[2])))"),
                    Cut("nLep_signal == 3"),
                    Cut("lepPt[0]>60. && lepPt[1]>40. && lepPt[2]>30."),
                    Cut("nJet20<3"),
                    Cut("nBJet20_MV2c10_FixedCutBEff_77==0"),
                    Cut("mll_RJ>75. && mll_RJ<105"),
                    Cut("mTW>0. && mTW<70."),
                    Cut("H4PP>250."),
                    Cut("RPT_HT4PP<0.2"),
                    Cut("R_HT4PP_H4PP>0.75")]
        cutnames = ["Total","nLepBase==3","OSSF","nLepSig==3","lepPt[60,40,30]","nJet<3",  "n_{b}^{20,77}=0",  "75<mll<105","mTW<70" ,"H4PP>250.","RPT_HT4PP<0.2","R_HT4PP_H4PP>0.75"]

    
    if Region == "VR3L-VV":
        cutlist = [Cut("1"),
                   Cut("is3Lep && ((lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1])) || (lepCharge[0]*lepCharge[2]<0 && abs(lepFlavor[0])==abs(lepFlavor[2])) || (lepCharge[1]*lepCharge[2]<0 && abs(lepFlavor[1])==abs(lepFlavor[2]))) && lepPt[0]>60. && lepPt[1]>40. && lepPt[2]>30."),
                   Cut("nBJet20_MV2c10_FixedCutBEff_77==0"),
                   Cut("nJet20<3"),
                   Cut("mll_RJ>75. && mll_RJ<105."),
                   Cut("mTW>70.0 && mTW<100."),
                   Cut("R_minH2P_minH3P>0."),
                   Cut("H4PP>250."),
                   Cut("R_HT4PP_H4PP>0.75"),
                   Cut("RPT_HT4PP<0.2")]
        cutnames = ["Total","Preselection","n_{b}^{20,77}=0","nJet20<3","75<mll<105","70<mTW<100","R_minH2P_minH3P>0.0","H4PP>250.","R_HT4PP_H4PP>0.75","RPT_HT4PP<0.2"]
    if Region == "CR3L_ISR-VV":
        cutlist = [Cut("1"),
                   Cut("is3LInt && ( (lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1])) || (lepCharge[0]*lepCharge[2]<0 && abs(lepFlavor[0])==abs(lepFlavor[2])) || (lepCharge[1]*lepCharge[2]<0 && abs(lepFlavor[1])==abs(lepFlavor[2])) ) && lepPt[0]>25 && lepPt[1]>25 && lepPt[2]>20"),
                   Cut("nBJet20_MV2c10_FixedCutBEff_77==0 && nJet20 >=1"),
                   Cut("dphiISRI>2.0"),
                   Cut("RISR > 0.55 && RISR<1.0"),
                   Cut("mll_RJ>75. && mll_RJ<105."),
                   Cut("mTW<100."),
                   Cut("PTISR>80.0"),
                   Cut("PTI>60."),
                   Cut("PTCM<25.")]
        cutnames = ["Total","Preselection","n_{b}^{20,77}=0","dphiISRI>2.0","0.55<RISR<1.0","75<mll<105","mTW<100","PTISR>80.0","PTI>60","PTCM<25."]

    if Region == "VR3L_ISR-VV":
        cutlist = [Cut("1"),
                   Cut("is3LInt && ( (lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1])) || (lepCharge[0]*lepCharge[2]<0 && abs(lepFlavor[0])==abs(lepFlavor[2])) || (lepCharge[1]*lepCharge[2]<0 && abs(lepFlavor[1])==abs(lepFlavor[2])) ) && lepPt[0]>25 && lepPt[1]>25 && lepPt[2]>20"),
                   Cut("nBJet20_MV2c10_FixedCutBEff_77==0"),
                   Cut("mll_RJ>75. && mll_RJ<105."),
                   Cut("nJet20 >=1"),
                   Cut("dphiISRI>2.0"),
                   Cut("RISR > 0.55 && RISR<1.0"),
                   Cut("mTW>60.0"),
                   Cut("PTISR>80.0"),
                   Cut("PTI>60."),
                   Cut("PTCM>25.")]
        cutnames = ["Total","Preselection","nb =0", "75<mll<105","nJet20>=1","dphiISRI>2.0","0.55<RISR<1.0","mTW>60.0","PTISR>80.0","PTI>60.0","PTCM>25"]

    if Region == "SR3L_HIGH":
        cutlist = [Cut("1"),
                   Cut("is3Lep && (((lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1])) || (lepCharge[0]*lepCharge[2]<0 && abs(lepFlavor[0])==abs(lepFlavor[2])) || (lepCharge[1]*lepCharge[2]<0 && abs(lepFlavor[1])==abs(lepFlavor[2])))) && lepPt[0]>60. && lepPt[1]>60. && lepPt[2]>40. && nBJet20_MV2c10_FixedCutBEff_77==0 && nJet20<3 && mll_RJ>75. && mll_RJ<105."),
                   Cut("mTW>150."),
                   Cut("R_HT4PP_H4PP > 0.75"),
                   Cut("R_minH2P_minH3P>0.8"),
                   Cut("H4PP > 550."),
                   Cut("RPT_HT4PP < 0.2")]
        cutnames = ["Total","Preselection","mTW>150","R_HT4PP_H4PP>0.75","R_minH2P_minH3P>0.8","H4PP>550","RPT_HT4PP<0.2"]
    if Region == "SR3L_INT":
        cutlist = [Cut("1"),
                   Cut("is3Lep && (((lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1])) || (lepCharge[0]*lepCharge[2]<0 && abs(lepFlavor[0])==abs(lepFlavor[2])) || (lepCharge[1]*lepCharge[2]<0 && abs(lepFlavor[1])==abs(lepFlavor[2])))) && lepPt[0]>60. && lepPt[1]>50. && lepPt[2]>30. && nBJet20_MV2c10_FixedCutBEff_77==0 && nJet20<3 && mll_RJ>75. && mll_RJ<105."),
                   Cut("mTW>130."),
                   Cut("R_HT4PP_H4PP > 0.8"),
                   Cut("R_minH2P_minH3P>0.75"),
                   Cut("H4PP > 450."),
                   Cut("RPT_HT4PP < 0.15")]
        cutnames = ["Total","Preselection","mTW>130","R_HT4PP_H4PP>0.8","R_minH2P_minH3P>0.75","H4PP>450","RPT_HT4PP<0.15"]
    if Region == "SR3L_LOW":
        cutlist = [Cut("1"),
                   Cut("is3Lep && (((lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1])) || (lepCharge[0]*lepCharge[2]<0 && abs(lepFlavor[0])==abs(lepFlavor[2])) || (lepCharge[1]*lepCharge[2]<0 && abs(lepFlavor[1])==abs(lepFlavor[2])))) && lepPt[0]>60. && lepPt[1]>40. && lepPt[2]>30. &&nBJet20_MV2c10_FixedCutBEff_77==0 && nJet20==0 && mll_RJ>75. && mll_RJ<105."),
                   Cut("mTW>100."),
                   Cut("R_HT4PP_H4PP > 0.9"),
                   Cut("H4PP > 250"), 
                   Cut("RPT_HT4PP < 0.05")]
        cutnames = ["Total","Preselection","mTW>100","R_HT4PP_H4PP>0.9","H4PP>250","RPT_HT4PP<0.05"]

    if Region == "SR3L_ISR":
        cutlist = [Cut("1"),
                   Cut("is3LInt && (((lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1])) || (lepCharge[0]*lepCharge[2]<0 && abs(lepFlavor[0])==abs(lepFlavor[2])) || (lepCharge[1]*lepCharge[2]<0 && abs(lepFlavor[1])==abs(lepFlavor[2])))) && lepPt[0]>25. && lepPt[1]>25. && lepPt[2]>20. && nBJet20_MV2c10_FixedCutBEff_77==0 && nJet20>=1 && nJet20<4 && mll_RJ>75 && mll_RJ<105"),
                   Cut("mTW>100"),
                   Cut("dphiISRI>2.0"),
                   Cut("RISR>0.55 && RISR<1.0"),
                   Cut("PTISR>100"),
                   Cut("PTI>80"),
                   Cut("PTCM<25")]
        cutnames = ["Total","Preselection","mTW>100","dphiISRI>2.0","0.55<RISR<1.0","PTISR>100","PTI>80","PTCM<25"]




    # ABCD RH2PPH5PP VS MJJ IMPLIMENTATION.
    if Region == "ABCD":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]



    if Region == "A":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>20 && mjj<70"),
                   Cut("H2PP/H5PP>0.35 && H2PP/H5PP<0.6"),
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]




    if Region == "B":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>20 && mjj<70"),
                   Cut("H2PP/H5PP>0.05 && H2PP/H5PP<0.35"),                
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]

    if Region == "D":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>70 && mjj<90"),
                   Cut("H2PP/H5PP>0.05 && H2PP/H5PP<0.35"),                
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]

    if Region == "E":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>90 && mjj<150"),
                   Cut("H2PP/H5PP>0.05 && H2PP/H5PP<0.35"),                
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]




    if Region == "AS1":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>40 && mjj<70"),
                   Cut("H2PP/H5PP>0.35 && H2PP/H5PP<0.6"),
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]

    if Region == "BS1":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>40 && mjj<70"),
                   Cut("H2PP/H5PP>0.05 && H2PP/H5PP<0.35"),                
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]

    if Region == "BS2":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>20 && mjj<70"),
                   Cut("H2PP/H5PP>0.1 && H2PP/H5PP<0.35"),                
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]

    if Region == "DS2":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>70 && mjj<90"),
                   Cut("H2PP/H5PP>0.1 && H2PP/H5PP<0.35"),                
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]

    if Region == "ES2":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>90 && mjj<150"),
                   Cut("H2PP/H5PP>1.0 && H2PP/H5PP<0.35"),                
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]

    if Region == "VR":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>90 && mjj<150"),
                   Cut("H2PP/H5PP>0.35 && H2PP/H5PP<0.6"),
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$90<mjj<150$","$0.35<H2PP/H5PP<0.6$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]



    #ABCD VALIDATION REGION  IMPLIMENTATION

    if Region == "AV":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>20 && mjj<50"),
                   Cut("H2PP/H5PP>0.35 && H2PP/H5PP<0.6"),
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]


    if Region == "BV":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>20 && mjj<50"),
                   Cut("H2PP/H5PP>0.05 && H2PP/H5PP<0.35"),                
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]

    if Region == "DV":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>70 && mjj<90"),
                   Cut("H2PP/H5PP>0.05 && H2PP/H5PP<0.35"),                
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]
    # VALIDATION REGION DEFINITIONS:
    if Region == "VRA":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>50 && mjj<70"),
                   Cut("H2PP/H5PP>0.35 && H2PP/H5PP<0.6"),
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]


    if Region == "VRB":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>50 && mjj<70"),
                   Cut("H2PP/H5PP>0.05 && H2PP/H5PP<0.35"),                
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]

    if Region == "VRD":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>90 && mjj<150"),
                   Cut("H2PP/H5PP>0.05 && H2PP/H5PP<0.35"),                
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]

    if Region == "VRC":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>90 && mjj<150"),
                   Cut("H2PP/H5PP>0.35 && H2PP/H5PP<0.6"),
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$90<mjj<150$","$0.35<H2PP/H5PP<0.6$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]


    # RPTH5PP ABCD IMPLIMENTATION 
    if Region == "ABCD2":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("H2PP/H5PP>0.35 && H2PP/H5PP<0.6"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]



    if Region == "A2":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>20 && mjj<70"),
                   Cut("H2PP/H5PP>0.35 && H2PP/H5PP<0.6"),
                   Cut("RPT_HT5PP<0.05"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$70<mjj<90$","$0.35<H2PP/H5PP<0.6$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]

    if Region == "B2":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>20 && mjj<70"),
                   Cut("H2PP/H5PP>0.35 && H2PP/H5PP<0.6"),
                   Cut("RPT_HT5PP>0.05 && RPT_HT5PP<1.0"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        cutnames = ["$Total$","$Preselection$","$70<mjj<90$","$0.35<H2PP/H5PP<0.6$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]

    if Region == "C2":
        cutlist = [Cut("1"),
                   Cut("is2Lep2Jet==1 && lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1]) && lepPt[0]>25 && lepPt[1]>25 && jetPt[0]>30 && jetPt[1]>30 && nBJet20_MV2c10_FixedCutBEff_77==0 && (nJet20==2) && (mll_RJ>80 && mll_RJ<100)"),
                   Cut("mjj>70 && mjj<90"),
                   Cut("H2PP/H5PP>0.35 && H2PP/H5PP<0.6"),
                   Cut("RPT_HT5PP>0.05 && RPT_HT5PP<1.0"),
                   Cut("minDphi>2.4"),
                   Cut("H5PP>400") ]
        
        cutnames = ["$Total$","$Preselection$","$70<mjj<90$","$0.35<H2PP/H5PP<0.6$","$RPT_HT5PP<0.05$","$minDphi>2.4$","$H5PP>400$"]

    if Region == "VR3L_ISR-smallPTCM":
        cutlist = [Cut("1"),
                   Cut("is3LInt && (((lepCharge[0]*lepCharge[1]<0 && abs(lepFlavor[0])==abs(lepFlavor[1])) || (lepCharge[0]*lepCharge[2]<0 && abs(lepFlavor[0])==abs(lepFlavor[2])) || (lepCharge[1]*lepCharge[2]<0 && abs(lepFlavor[1])==abs(lepFlavor[2])))) && lepPt[0]>25. && lepPt[1]>25. && lepPt[2]>20. && nBJet20_MV2c10_FixedCutBEff_77==0 && nJet20>=1 && nJet20<4 "),
                   Cut("mll_RJ>75 && mll_RJ<105"),
                   Cut("mTW>60"),
                   Cut("dphiISRI>2.0"),
                   Cut("RISR>0.55 && RISR<1.0"),
                   Cut("PTISR<80"),
                   Cut("PTI>60"),
                   Cut("PTCM<25")]
        cutnames = ["TOTAL","PRESELECTION","Mll","mTW","dphiISRI","RISR","PTISR","PTI","PTCM"]



    if (RegionLabel == ""):
         RegionLabel = Region

    if cutlist == "":
        print "no cutlist applied"

    return RegionLabel, cutlist, cutnames