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

void ZtoMuMu(const char *inputFile)
{
  gSystem->Load("libDelphes");

  // Create chain of root trees
  TChain chain("Delphes");
  chain.Add(inputFile);

  // Create object of class ExRootTreeReader
  ExRootTreeReader *treeReader = new ExRootTreeReader(&chain);
  Long64_t numberOfEntries = treeReader->GetEntries();

  TClonesArray *branchMuon = treeReader->UseBranch("Muon");

  // Book histograms
  TH1 *histMass = new TH1F("Masa invariante", "M_{inv}(#mu_{1}, #mu_{2})", 50, 80.0, 100.0);
  TH1 *histPT1 = new TH1F("mom. transv. 1", "P_T(#mu_{1})", 50, 10.0, 80.0);
  TH1 *histPT2 = new TH1F("mom. transv. 2", "P_T(#mu_{2})", 50, 10.0, 60.0);
  // Loop over all events
  for(Int_t entry = 0; entry < numberOfEntries; ++entry)
  {
    // Load selected branches with data from specified event
    treeReader->ReadEntry(entry);

    Muon *muon1, *muon2;

    // If event contains at least 2 muons
    if(branchMuon->GetEntries() > 1)
    {
      // Take first two electrons
      muon1 = (Muon *) branchMuon->At(0);
      muon2 = (Muon  *) branchMuon->At(1);

      // Plot their invariant mass
      histMass->Fill(((muon1->P4()) + (muon2->P4())).M());
      histPT1 -> Fill(muon1 -> PT);	histPT2 -> Fill(muon2 -> PT);
    }


  }

  // Show resulting histograms
  TFile *f=new TFile("mass.root","recreate");
  TCanvas *c1 = new TCanvas("c1","c1");
  
  histMass->GetXaxis()->SetTitle("Mass [GeV]");
  histMass->GetYaxis()->SetTitle("Frecuencias");
  histMass->GetXaxis()->SetLabelSize(.05);
  histMass->GetYaxis()->SetLabelSize(.05);
  histMass->GetXaxis()->SetTitleSize(.05);
  histMass->GetYaxis()->SetTitleSize(.05);
  
  histMass->Draw();
  histMass->Write();
  f->Close();

  c1 -> SaveAs("mass.png");
  
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


 
}




