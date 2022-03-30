#include "TFile.h"
#include "TString.h"
#include "TBranch.h"
#include "TH1.h"
#include "TCanvas.h"
#include "TTree.h"
#include "../interface/DQM.h"
#include "../interface/DemonstratorConstants.h"
using namespace std;

void checkMatching(string file){

  TFile * input = new TFile(file, "READ");
  
  mdaq::GlobalEvent * evt = new mdaq::GlobalEvent();
  TTree * events = (TTree*)input->Get("Events");
  events->SetBranchAddress("event", &evt);

  TTree* metadataIn = (TTree*)input->Get("Metadata");

  mdaq::DemonstratorConfiguration * CurrentConfig = new mdaq::DemonstratorConfiguration();
  TString* meta_fileOpenTime = new TString();
  TString* meta_fileCloseTime = new TString();
  TString* meta_configFile = new TString();
  TString* meta_gitVersion = new TString();
  int meta_runNumber;
  int meta_subrunNumber;

  metadataIn->SetBranchAddress("configuration", &CurrentConfig);
  metadataIn->SetBranchAddress("fileOpenTime", &meta_fileOpenTime);
  metadataIn->SetBranchAddress("fileCloseTime", &meta_fileCloseTime);
  metadataIn->SetBranchAddress("runNumber", &meta_runNumber);
  metadataIn->SetBranchAddress("subrunNumber", &meta_subrunNumber);
  metadataIn->SetBranchAddress("configFileName", &meta_configFile);
  metadataIn->SetBranchAddress("gitVersion", &meta_gitVersion);
	

  TFile* output = new TFile("~/data/MilliQan_run196_testSync_May10_Matched.root", "RECREATE");
  mdaq::GlobalEvent * outEvent = new mdaq::GlobalEvent();
  mdaq::DemonstratorConfiguration * outConfig = new mdaq::DemonstratorConfiguration();
  TString* out_fileOpenTime = new TString();
  TString* out_fileCloseTime = new TString();
  TString* out_configFile = new TString();
  TString* out_gitVersion = new TString();
  int out_runNumber;
  int out_subrunNumber;

  TH1I* h_numBoardsMatched = new TH1I("h_numBoardsMatched", "Number of Boards Matched", 5, 0, 5);
  TH1I* h_unMatched = new TH1I("h_unMatched", "Unmatched Board Number", 4, 0, 4);

  TCanvas* c1 = new TCanvas("c1", "c1", 600, 600);
  TCanvas* c2 = new TCanvas("c2", "c2", 600, 600);

  for(int i=0; i < events->GetEntries(); i++){

  	bool boardMatched[nDigitizers] = {0};
  	int numMatched = 0;

  	events->GetEvent(i);

  	for(int digi = 0; digi < nDigitizers; digi++){
  		if(evt->digitizers[digi].TDC[6] != 0){
  			boardMatched[digi] = true;
  			numMatched++;
  		}
  	}

  	h_numBoardsMatched->Fill(numMatched);

        for(int digi = 0; digi < nDigitizers; digi++){
            //if only one board is matched it is the unmatched event
            if(numMatched == 1 && boardMatched[digi] == true) h_unMatched->Fill(digi);
            //if multiple boards are matched any unmatched board is filled
            else if(numMatched > 1 && boardMatched[digi] == false) h_unMatched->Fill(digi);
        }


  }


  c1->cd();
  h_numBoardsMatched->Draw("HIST TEXT");
  c2->cd();
  h_unMatched->Draw("HIST TEXT");

  c1->SaveAs("TestPDF.pdf");

  double oneBoard = h_numBoardsMatched->GetBinContent(2);
  double twoBoards = h_numBoardsMatched->GetBinContent(3);
  double threeBoards = h_numBoardsMatched->GetBinContent(4);
  double fourBoards = h_numBoardsMatched->GetBinContent(5);
	
	ofstream myfile;
	myfile.open("new example.txt");
	myfile << oneBoard << " " << twoBoards << " " << threeBoards << " " << fourBoards << endl;

	myfile << "Matching Efficiency: " << (fourBoards) / (double)(oneBoard + twoBoards + threeBoards + fourBoards) << endl;

	myfile.close();

}
