/*
Simple macro showing how to access branches from the delphes output root file,
loop over events, and plot simple quantities such as the jet pt and the di-electron invariant
mass.

root -l examples/Example1.C'("delphes_output.root")'
*/

#ifdef __CLING__
R__LOAD_LIBRARY(libDelphes.so)
#include "classes/DelphesClasses.h"
#include "external/ExRootAnalysis/ExRootTreeReader.h"
#endif

//------------------------------------------------------------------------------

void JJ_mu_Vm(const char *inputFile)
{
  gSystem->Load("libDelphes");

  // Create chain of root trees
  TChain chain("Delphes");
  chain.Add(inputFile);

  // Create object of class ExRootTreeReader
  ExRootTreeReader *treeReader = new ExRootTreeReader(&chain);
  Long64_t numberOfEntries = treeReader->GetEntries();

  TClonesArray *branchMuon = treeReader->UseBranch("Muon");
  TClonesArray *branchJet = treeReader->UseBranch("Jet");
  TClonesArray *branchMet = treeReader->UseBranch("MissingET");

  // Book histograms
  TH1 *histPTMu = new TH1F("PT del muon", "PT(#mu)", 50, 80.0, 100.0);
  //TH1 *histPT1 = new TH1F("mom. transv. 1", "P_T(#mu_{1})", 50, 10.0, 80.0);
  //TH1 *histPT2 = new TH1F("mom. transv. 2", "P_T(#mu_{2})", 50, 10.0, 60.0);
  //TH1 *histDR = new TH1F("Delta R", "#Delta R", 50, 0, 4.0);
  // Loop over all events
  int num_Jet;  int num_Mu; 
 
  for(Int_t entry = 0; entry < numberOfEntries; ++entry)
  {
    // Load selected branches with data from specified event
    treeReader->ReadEntry(entry);
	num_Jet = branchJet -> GetEntries();
	num_Mu = branchMuon -> GetEntries();
	
	Muon *muon;	Jet *jet1, *jet2;	MissingET *miss; //CLASES DE LAS VARIABLES 
	if(num_Jet>1 and !num_Mu==1){	//CUMPLE LOS REQUERIMIENTOS ELEGIDOS
	muon = (Muon*) branchMuon -> At(0); 	//APUNTAR LOS DATOS ASIGNADOS
	cout << entry <<" ; " << num_Mu << " ; " <<  num_Jet <<" . . . ";
//GRAFICAR LOS PT DEL MUON
 	
//histPTMu->Fill(muon.PT);	
	
	}


//    Muon *muon1;

    // If event contains at least 2 muons
    /*if(branchMuon->GetEntries() > 1)
    {
      // Take first two electrons
      muon1 = (Muon *) branchMuon->At(0);
      muon2 = (Muon  *) branchMuon->At(1);

      // Plot their invariant mass
      histMass->Fill(((muon1->P4()) + (muon2->P4())).M());
      histPT1 -> Fill(muon1 -> PT);	histPT2 -> Fill(muon2 -> PT);
      histDR -> Fill(sqrt((muon1 -> Eta)*(muon1 -> Eta)+(muon1 -> Phi)*(muon1 -> Phi)));
	
    }*/
//	// contar los eventos
//	if(sqrt((muon1 -> Eta)*(muon1 -> Eta)+(muon1 -> Phi)*(muon1 -> Phi))>3.0 && sqrt((muon1 -> Eta)*(muon1 -> Eta)+(muon1 -> Phi)*(muon1 -> Phi))<3.2)
//	{cout << "Backtoback event " << entry << endl;}
//	// contar los eventos
//	if(sqrt((muon1 -> Eta)*(muon1 -> Eta)+(muon1 -> Phi)*(muon1 -> Phi))<.2)
//	{cout << "Paralel particles " << entry << endl;}

  }

  // Show resulting histograms
//  TFile *f=new TFile(".root","recreate");
//  TCanvas *c1 = new TCanvas("c1","c1");
  
//  histMass->GetXaxis()->SetTitle("Mass [GeV]");
//  histMass->GetYaxis()->SetTitle("Frecuencias");
//  histMass->GetXaxis()->SetLabelSize(.05);
//  histMass->GetYaxis()->SetLabelSize(.05);
//  histMass->GetXaxis()->SetTitleSize(.05);
//  histMass->GetYaxis()->SetTitleSize(.05);
  
//  histPTMu->Draw();
//  histPTMu->Write();
//  f->Close();

/*  c1 -> SaveAs("mass.png");
  
  TCanvas *c2 = new TCanvas("c2", "c2");
  histPT1->GetXaxis()->SetTitle("Mass [GeV]");
  histPT1->GetYaxis()->SetTitle("Frecuencias");
  histPT1->GetXaxis()->SetLabelSize(.05);
  histPT1->GetYaxis()->SetLabelSize(.05);
  histPT1->GetXaxis()->SetTitleSize(.05);
  histPT1->GetYaxis()->SetTitleSize(.05);
  histPT1 ->Draw();
  c2 -> SaveAs("pt1.png");
  
  TCanvas *c3 = new TCanvas("c3", "c3");
  histPT2->GetXaxis()->SetTitle("Mass [GeV]");
  histPT2->GetYaxis()->SetTitle("Frecuencias");
  histPT2->GetXaxis()->SetLabelSize(.05);
  histPT2->GetYaxis()->SetLabelSize(.05);
  histPT2->GetXaxis()->SetTitleSize(.05);
  histPT2->GetYaxis()->SetTitleSize(.05);
  histPT2->Draw();
  histPT2 ->Draw();
  c3 -> SaveAs("pt2.png");

  TCanvas *c4 = new TCanvas("c4", "c4");
  histDR->Draw();
  histDR ->Draw();
  c4 -> SaveAs("DR.png");

*/
}



