#new tab for create matching figures
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from new_DAQCommand import *
import sys
import logging
import subprocess
import os
import signal
import time
import glob
import select
import os.path


class checking_match_tab(QWidget):
	def __init__(self):
		super().__init__()
		
		#set up all the buttons and textbox in this tab
		btn(self, "List", 650,100, self.click_list) #List the lastest files for plot
		btn(self, "Check",750,100, self.check_figure) #plot the checking figure
		self.setTitleLabel()
		self.setimage()
		self.setCombolist()
		
		self.show()
		
	#set the title of this tab
	def setTitleLabel(self):
		self.label = QLabel(self)
		self.label.setText("Checking Matching Figure")
		self.label.setFont(QFont("Arial",30))
		self.label.move(300,20)
		
	#Set image space for list of file
	def setimage(self):
		self.graphicsView = QGraphicsView(self)
		self.scene = QGraphicsScene()
		self.pixmap = QGraphicsPixmapItem()
		self.scene.addItem(self.pixmap)
		self.graphicsView.setScene(self.scene)
		
		self.graphicsView.move(50,100)
		self.graphicsView.resize(500,600)
		
		
	#create combolist for root files
	def setCombolist(self):
		self.combolist = QComboBox(self)
		self.combolist.move(650,150)
		self.combolist.addItems([])
		self.combolist.currentTextChanged.connect(self.on_combobox_func)

	#update the file names we want to plot
	def on_combobox_func(self,text):
		self.current_text = text
		
	#find the lastest 5 root files
	def click_list(self):
		path = '/home/milliqan/data/'
		#path = '/Users/mr-right/physics/research/'
		os.chdir(path)
		files = sorted(os.listdir(os.getcwd()),key=os.path.getmtime)
		files_new = files[-10:]
		files_list = []
		print(files_new)
		for filename in files_new:
			if filename.startswith("MilliQan"):
				files_list.append(filename)
		files_list = files_list[-5:]
		#update the list to combolist
		self.combolist.clear()
		self.combolist.addItems(files_list)
		
	#matching the data we choose with the data we already matched
	def check_figure(self):
		filename = self.current_text
		filestring = 'root "/home/milliqan/MilliDAQ/gui/MilliQanGUI/checkMatching.cpp(\\"' + filename +  ' \\")"'
		#os.system("echo Compiling " + file)
		#os.system("g++ " + file + " -o run.exe")
		#os.system("echo Running")
		#os.system("echo ---------------")
		os.system(filestring)
		img = QPixmap('/home/milliqan/MilliDAQ/plots/TestPDF.pdf')
		self.pixmap.setPixmap(img)
		#checkingMatching(self.current_text)
		
		
	
