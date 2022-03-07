
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from triggerBoard.py import *
import sys
import logging
import subprocess
import os
import signal
import time
import glob
import select
import os.path

'''
#use for debug
def runClass(num):
	x= num
'''

class trigger_board_tab(QWidget):
	def __init__(self):
		super().__init__()
		
		#set up all the buttons and textbox in this tab
		self.setTitleLabel()
		self.setFirmwareBtn()
		self.setCoincidenceTimeBtn()
		self.setHistogramBtn()
		self.setToggleOutputBtn()
		self.setToggleClockInputBtn()
		self.setAdjustClockPhaseBtn()
		self.setRandomSeedBtn()
		self.setPrescaleBtn()
		self.setActiveClockBtn()
		self.setTogglePhaseBtn()
		self.setSendHistogramBtn()
		self.setDeadTimeBtn()
		self.setAdjustClock1Btn()
		self.setToggleTriggerRollingBtn()
		self.setInputTriggerMaskBtn()
		self.setTriggerBtn()
		self.setClockCyclesBtn()
		self.setReClockBtn()
	
		
		self.show()
		
	#Set the tile of this tab
	def setTitleLabel(self):
		self.label = QLabel(self)
		self.label.setText("Control Trigger Board")
		self.label.setFont(QFont("Arial",30))
		self.label.move(300,20)
		
	#output firmware version
	def setFirmwareBtn(self):
		self.btn = QPushButton("Firmware Version",self)
		self.btn.resize(120,120)
		self.btn.move(50,100)
		self.btn.clicked.connect(self.firmware)
		
	#output Toggle Output Enable
	def setToggleOutputBtn(self):
		self.btn4 = QPushButton("Toggle Output\n Enable",self)
		self.btn4.resize(120,120)
		self.btn4.move(200,100)
		self.btn4.clicked.connect(self.Toggle_output_enable)
		
	#output Toggle Clock input
	def setToggleClockInputBtn(self):
		self.btn5 = QPushButton("Toggle Clock\n Inputs",self)
		self.btn5.resize(120,120)
		self.btn5.move(350,100)
		self.btn5.clicked.connect(self.Toggle_clock_inputs)
		
	#output adjust clock phase
	def setAdjustClockPhaseBtn(self):
		self.btn6 = QPushButton("Adjust Clock\n Phase",self)
		self.btn6.resize(120,120)
		self.btn6.move(500,100)
		self.btn6.clicked.connect(self.adjust_clock_phase)
		
	#output get active clock
	def setActiveClockBtn(self):
		self.btn9 = QPushButton("Get Active\n Clock",self)
		self.btn9.resize(120,120)
		self.btn9.move(650,100)
		self.btn9.clicked.connect(self.active_clock)
		
	#output toggle phase(up/down)
	def setTogglePhaseBtn(self):
		self.btn10 = QPushButton("Toggle Phase",self)
		self.btn10.resize(120,120)
		self.btn10.move(800,100)
		self.btn10.clicked.connect(self.toggle_phase)
		
	#output Send Histogram
	def setSendHistogramBtn(self):
		self.btn11 = QPushButton("Send Histogram",self)
		self.btn11.resize(120,120)
		self.btn11.move(50,300)
		self.btn11.clicked.connect(self.send_histogram)

	#output adjust clock 1 phase
	def setAdjustClock1Btn(self):
		self.btn13 = QPushButton("Adjust Clock 1\n Phase",self)
		self.btn13.resize(120,120)
		self.btn13.move(200,300)
		self.btn13.clicked.connect(self.adjust_clock1)
		
	#output Toggle Trigger Rolling
	def setToggleTriggerRollingBtn(self):
		self.btn14 = QPushButton("Toggle Trigger\n Rolling",self)
		self.btn14.resize(120,120)
		self.btn14.move(350,300)
		self.btn14.clicked.connect(self.toggle_trigger)
		
	#output get clock cycles/last trigger fired
	def setClockCyclesBtn(self):
		self.btn17 = QPushButton("Toggle Trigger\n Rolling",self)
		self.btn17.resize(120,120)
		self.btn17.move(500,300)
		self.btn17.clicked.connect(self.clock_cycle)
		
	#reset clock
	def setReClockBtn(self):
		self.btn18 = QPushButton("Reset Clock",self)
		self.btn18.resize(120,120)
		self.btn18.move(650,300)
		self.btn18.clicked.connect(self.reset_clock)

	#output coincidence time
	def setCoincidenceTimeBtn(self):
		#set the textbox for user import time
		self.textbox1 = QLineEdit(self)
		self.textbox1.setPlaceholderText("Import time here")
		self.textbox1.move(800,300)
		self.textbox1.resize(120,25)
		
		#set up the button
		self.btn2 = QPushButton("Coincidence Time",self)
		self.btn2.resize(120,120)
		self.btn2.move(800,335)
		self.btn2.clicked.connect(self.coincidence)
	
	#output histogram to send
	def setHistogramBtn(self):
		#set the textbox for user import time
		self.textbox2 = QLineEdit(self)
		self.textbox2.setPlaceholderText("Import histogram number")
		self.textbox2.move(50,500)
		self.textbox2.resize(120,25)
		
		#set up the button
		self.btn3 = QPushButton("Histogram to Send",self)
		self.btn3.resize(120,120)
		self.btn3.move(50,535)
		self.btn3.clicked.connect(self.histogram)
		
	#output set Random seed
	def setRandomSeedBtn(self):
		#set textbox for user import time
		self.textbox3 = QLineEdit(self)
		self.textbox3.setPlaceholderText("Import seed here")
		self.textbox3.move(200,500)
		self.textbox3.resize(120,25)
		
		#set up the button
		self.btn7 = QPushButton("Set Random Seed",self)
		self.btn7.resize(120,120)
		self.btn7.move(200,535)
		self.btn7.clicked.connect(self.random_seed)
		
	#output petprescale
	def setPrescaleBtn(self):
		#set textbox for user to import prescale
		self.textbox4 = QLineEdit(self)
		self.textbox4.setPlaceholderText("Import prescale here")
		self.textbox4.move(350,500)
		self.textbox4.resize(120,25)
		
		#set btn
		self.btn8 = QPushButton("Set Prescale",self)
		self.btn8.resize(120,120)
		self.btn8.move(350,535)
		self.btn8.clicked.connect(self.set_prescale)
		
	#output set dead time
	def setDeadTimeBtn(self):
		#set textbox for user to import deadtime
		self.textbox5 = QLineEdit(self)
		self.textbox5.setPlaceholderText("Import deadtime here")
		self.textbox5.move(500,500)
		self.textbox5.resize(120,25)
		
		#set up btn
		self.btn12 = QPushButton("Set Dead Time",self)
		self.btn12.resize(120,120)
		self.btn12.move(500,535)
		self.btn12.clicked.connect(self.dead_time)
		
	#output Set Input Trigger Mask
	def setInputTriggerMaskBtn(self):
		#set textbox for user to import Trigger mask
		self.textbox6 = QLineEdit(self)
		self.textbox6.setPlaceholderText("Import mask here")
		self.textbox6.move(650,500)
		self.textbox6.resize(120,25)
		
		#set up btn
		self.btn15 = QPushButton("Set Input\n Trigger Mask",self)
		self.btn15.resize(120,120)
		self.btn15.move(650,535)
		self.btn15.clicked.connect(self.trigger_mask)
		
	#output set trigger
	def setTriggerBtn(self):
		#set textbox for user to import trigger number
		self.textbox7 = QLineEdit(self)
		self.textbox7.setPlaceholderText("Import trigger here")
		self.textbox7.move(800,500)
		self.textbox7.resize(120,25)
		
		#set up btn
		self.btn16 = QPushButton("Set Trigger",self)
		self.btn16.resize(120,120)
		self.btn16.move(800,535)
		self.btn16.clicked.connect(self.set_trigger)
	
	#defferent runing code for trigger board
	def firmware(self):
		runClass(0)
		
	def coincidence(self):
		#check user import something
		if self.textbox1.text() == "":
			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Information)
			msgBox.setText("please import a time")
		else:
			self.CoincidenceTime = int(self.textbox1.text())
			runClass(1,self.CoincidenceTime)
		
	def histogram(self):
		#check user import something
		if self.textbox2.text() == "":
			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Information)
			msgBox.setText("please import a histogram")
		else:
			self.HistogramNum = int(self.textbox2.text())
			runClass(2,self.HistogramNum)
	
	def Toggle_output_enable(self):
		runClass(3)
	
	def Toggle_clock_inputs(self):
		runClass(4)
	
	def adjust_clock_phase(self):
		runClass(5)
	
	def random_seed(self):
		#check user import something
		if self.textbox3.text() == "":
			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Information)
			msgBox.setText("please import a seed")
		else:
			self.seed = int(self.textbox3.text())
			runClass(6,self.seed)
	
	def set_prescale(self):
		#check user import something
		if self.textbox4.text() == "":
			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Information)
			msgBox.setText("please import a prescale")
		else:
			self.Prescale = int(self.textbox4.text())
			runClass(7,self.Prescale)
	
	def active_clock(self):
		runClass(8)
	
	def toggle_phase(self):
		runClass(9)
	
	def send_histogram(self):
		runClass(10)
	
	def dead_time(self):
		#check user import something
		if self.textbox5.text() == "":
			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Information)
			msgBox.setText("please import a time")
		else:
			self.DeadTime = int(self.textbox5.text())
			runClass(11,self.DeadTime)
	
	def adjust_clock1(self):
		runClass(12)
	
	def toggle_trigger(self):
		runClass(13)
	
	def	trigger_mask(self):
		#check user import something
		if self.textbox6.text() == "":
			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Information)
			msgBox.setText("please import a trigger mask")
		else:
			self.TriggerMask = int(self.textbox6.text())
			runClass(14,self.TriggerMask)
	
	def set_trigger(self):
		#check user import something
		if self.textbox7.text() == "":
			msgBox = QMessageBox()
			msgBox.setIcon(QMessageBox.Information)
			msgBox.setText("please import a trigger")
		else:
			self.TriggerNum = int(self.textbox7.text())
			runClass(15,self.TriggerNum)
	
	def clock_cycle(self):
		runClass(16)
	
	def reset_clock(self):
		runClass(17)
		


	
		
