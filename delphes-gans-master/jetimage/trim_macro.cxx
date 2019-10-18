#ifdef __CLING__
R__LOAD_LIBRARY(libDelphes.so)
#include "classes/DelphesClasses.h"
#include "external/ExRootAnalysis/ExRootTreeReader.h"
#endif

//reads .root file and prints comma-separated list of subjets for leading pT jet in each event
void trim_macro(char* fil){
    gSystem->Load("libDelphes");
    TChain chain("Delphes");
    chain.Add(fil);
    ExRootTreeReader *treeReader = new ExRootTreeReader(&chain);
    Long64_t numberOfEntries = treeReader->GetEntries();
    TClonesArray *branchJet = treeReader->UseBranch("Jet");

    for(Int_t entry = 0; entry<numberOfEntries; ++entry){
        treeReader->ReadEntry(entry);
        if(branchJet->GetEntries()>0) {
            Jet *jet = (Jet*) branchJet->At(0); //only take leading jet
            cout<<entry<<",";
            for(int i = 0; i<5; i++){
                for(int j = 0; j<4; j++){
                    cout<<jet->TrimmedP4[i][j]<<",";
                }
            }

        }
    }
    cout<<endl;
}
