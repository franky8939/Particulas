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

void ZtoMuMu_Delphes(const char *inputFile)
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
  TH1 *histMass = new TH1F("mass", "M_{inv}(#mu_{1}, #Mu_{2})", 50, 80.0, 100.0);
  TH1 *histPT1 = new TH1F("pt1", "PT(#mu_{1})", 50, 10.0, 80.0);
  TH1 *histPT2 = new TH1F("pt2", "PT(#Mu_{2})", 50, 10.0, 60.0);
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
  TCanvas *c1 = new TCanvas("MASAA","MASA");
  histMass->Draw();
  c1 -> SaveAs("mass.png");

  TCanvas *c2 = new TCanvas("c2", "c2");
  histPT1 ->Draw();
  c2 -> SaveAs("pt1.png");
  
  TCanvas *c3 = new TCanvas("c3", "c3");
  histPT2 ->Draw();
  c3 -> SaveAs("pt2.png");
}




