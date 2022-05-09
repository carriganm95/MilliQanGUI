
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from triggerBoard import *
from new_DAQCommand import *
import sys
import logging
import subprocess
import os
import signal
import time
import glob
import select

class trigger_board_tab(QWidget):
	def __init__(self):
		super().__init__()
		
		#set up all the buttons and textbox in this tab
		self.setTitleLabel()
		
		btn_size(self,"Firmware Version",50,100,self.firmware,120,120) #output firmware version
		btn_size(self,"Toggle Output\n Enable",200,100,self.Toggle_output_enable,120,120) #output Toggle Output Enable
		btn_size(self,"Toggle Clock\n Inputs",350,100,self.Toggle_clock_inputs,120,120) #output Toggle Clock input
		btn_size(self,"Adjust Clock\n Phase",500,100,self.adjust_clock_phase,120,120) #output adjust clock phase
		btn_size(self,"Get Active\n Clock",650,100,self.active_clock,120,120) #output get active clock
		btn_size(self,"Toggle Phase",800,100,self.toggle_phase,120,120) #output toggle phase(up/down)
		btn_size(self,"Send Histogram", 50,300,self.send_histogram,120,120) #output Send Histogram
		btn_size(self,"Adjust Clock 1\n Phase",200,300,self.adjust_clock1,120,120) #output adjust clock 1 phase
		btn_size(self,"Toggle Trigger\n Rolling",350,300,self.toggle_trigger,120,120) #output Toggle Trigger Rolling
		btn_size(self,"Clock cycles",500,300,self.clock_cycle,120,120) #output get clock cycles/last trigger fired
		btn_size(self,"Reset Clock",650,300,self.reset_clock,120,120) #reset clock
		self.setCoincidenceTimeBtn()
		self.setHistogramBtn()
		self.setRandomSeedBtn()
		self.setPrescaleBtn()
		self.setDeadTimeBtn()
		self.setInputTriggerMaskBtn()
		self.setTriggerBtn()
	
		
		self.show()
		
	#Set the tile of this tab
	def setTitleLabel(self):
		self.label = QLabel(self)
		self.label.setText("Control Trigger Board")
		self.label.setFont(QFont("Arial",30))
		self.label.move(300,20)


	#output coincidence time
	def setCoincidenceTimeBtn(self):
		#set the textbox for user import time
		self.textboxfortime = QLineEdit(self)
		self.textboxfortime.setPlaceholderText("Import time here")
		self.textboxfortime.move(800,300)
		self.textboxfortime.resize(120,25)
		
		#set up the button
		self.coincidencebtn = QPushButton("Coincidence Time",self)
		self.coincidencebtn.resize(120,120)
		self.coincidencebtn.move(800,335)
		self.coincidencebtn.clicked.connect(self.coincidence)
	
	#output histogram to send
	def setHistogramBtn(self):
		#set the textbox for user import time
		self.textboxforhistogram = QLineEdit(self)
		self.textboxforhistogram.setPlaceholderText("Import histogram number")
		self.textboxforhistogram.move(50,500)
		self.textboxforhistogram.resize(120,25)
		
		#set up the button
		self.histogramnumbtn = QPushButton("Histogram \nto Send",self)
		self.histogramnumbtn.resize(120,120)
		self.histogramnumbtn.move(50,535)
		self.histogramnumbtn.clicked.connect(self.histogram)
		
	#output set Random seed
	def setRandomSeedBtn(self):
		#set textbox for user import time
		self.textboxforrandomseed = QLineEdit(self)
		self.textboxforrandomseed.setPlaceholderText("Import seed here")
		self.textboxforrandomseed.move(200,500)
		self.textboxforrandomseed.resize(120,25)
		
		#set up the button
		self.randomseedbtn = QPushButton("Set Random Seed",self)
		self.randomseedbtn.resize(120,120)
		self.randomseedbtn.move(200,535)
		self.randomseedbtn.clicked.connect(self.random_seed)
		
	#output petprescale
	def setPrescaleBtn(self):
		#set textbox for user to import prescale
		self.textboxforprescale = QLineEdit(self)
		self.textboxforprescale.setPlaceholderText("Import prescale here")
		self.textboxforprescale.move(350,500)
		self.textboxforprescale.resize(120,25)
		
		#set btn
		self.prescalebtn = QPushButton("Set Prescale",self)
		self.prescalebtn.resize(120,120)
		self.prescalebtn.move(350,535)
		self.prescalebtn.clicked.connect(self.set_prescale)
		
	#output set dead time
	def setDeadTimeBtn(self):
		#set textbox for user to import deadtime
		self.textboxfordeadtime = QLineEdit(self)
		self.textboxfordeadtime.setPlaceholderText("Import deadtime here")
		self.textboxfordeadtime.move(500,500)
		self.textboxfordeadtime.resize(120,25)
		
		#set up btn
		self.deadtimebtn = QPushButton("Set Dead Time",self)
		self.deadtimebtn.resize(120,120)
		self.deadtimebtn.move(500,535)
		self.deadtimebtn.clicked.connect(self.dead_time)
		
	#output Set Input Trigger Mask
	def setInputTriggerMaskBtn(self):
		#set textbox for user to import Trigger mask
		self.textboxfortriggermask = QLineEdit(self)
		self.textboxfortriggermask.setPlaceholderText("Import mask here")
		self.textboxfortriggermask.move(650,500)
		self.textboxfortriggermask.resize(120,25)
		
		#set up btn
		self.triggermaskbtn = QPushButton("Set Input\n Trigger Mask",self)
		self.triggermaskbtn.resize(120,120)
		self.triggermaskbtn.move(650,535)
		self.triggermaskbtn.clicked.connect(self.trigger_mask)
		
	#output set trigger
	def setTriggerBtn(self):
		#set textbox for user to import trigger number
		self.textboxfortrigger = QLineEdit(self)
		self.textboxfortrigger.setPlaceholderText("Import trigger here")
		self.textboxfortrigger.move(800,500)
		self.textboxfortrigger.resize(120,25)
		
		#set up btn
		self.triggerbtn = QPushButton("Set Trigger",self)
		self.triggerbtn.resize(120,120)
		self.triggerbtn.move(800,535)
		self.triggerbtn.clicked.connect(self.set_trigger)
	
	#defferent runing code for trigger board
	def firmware(self):
		runClass(0)
		
	def coincidence(self):
		#check user import something
		if self.textboxfortime.text() == "":
			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Information)
			msgBox.setText("please import a time")
		else:
			self.CoincidenceTime = int(self.textboxfortime.text())
			runClass(1,self.CoincidenceTime)
		
	def histogram(self):
		#check user import something
		if self.textboxforhistogram.text() == "":
			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Information)
			msgBox.setText("please import a histogram")
		else:
			self.HistogramNum = int(self.textboxforhistogram.text())
			runClass(2,self.HistogramNum)
	
	def Toggle_output_enable(self):
		runClass(3)
	
	def Toggle_clock_inputs(self):
		runClass(4)
	
	def adjust_clock_phase(self):
		runClass(5)
	
	def random_seed(self):
		#check user import something
		if self.textboxforrandomseed.text() == "":
			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Information)
			msgBox.setText("please import a seed")
		else:
			self.seed = int(self.textboxforrandomseed.text())
			runClass(6,self.seed)
	
	def set_prescale(self):
		#check user import something
		if self.textboxforprescale.text() == "":
			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Information)
			msgBox.setText("please import a prescale")
		else:
			self.Prescale = int(self.textboxforprescale.text())
			runClass(7,self.Prescale)
	
	def active_clock(self):
		runClass(8)
	
	def toggle_phase(self):
		runClass(9)
	
	def send_histogram(self):
		runClass(10)
	
	def dead_time(self):
		#check user import something
		if self.textboxfordeadtime.text() == "":
			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Information)
			msgBox.setText("please import a time")
		else:
			self.DeadTime = int(self.textboxfordeadtime.text())
			runClass(11,self.DeadTime)
	
	def adjust_clock1(self):
		runClass(12)
	
	def toggle_trigger(self):
		runClass(13)
	
	def	trigger_mask(self):
		#check user import something
		if self.textboxfortriggermask.text() == "":
			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Information)
			msgBox.setText("please import a trigger mask")
		else:
			self.TriggerMask = int(self.textboxfortriggermask.text())
			runClass(14,self.TriggerMask)
	
	def set_trigger(self):
		#check user import something
		if self.textboxfortrigger.text() == "":
			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Information)
			msgBox.setText("please import a trigger")
		else:
			self.TriggerNum = int(self.textboxfortrigger.text())
			runClass(15,self.TriggerNum)
	
	def clock_cycle(self):
		runClass(16)
	
	def reset_clock(self):
		runClass(17)
		


	
		
