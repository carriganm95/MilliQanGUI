
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

class trigger_board_tab(QWidget):
	def __init__(self):
		super().__init__()
		
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
		
	
	def setTitleLabel(self):
		self.label = QLabel(self)
		self.label.setText("Control Trigger Board")
		self.label.setFont(QFont("Arial",30))
		self.label.move(300,20)
	#output firmware version
	def setFirmwareBtn(self):
		self.label1 = QLabel(self)
		self.label1.setText("Firmware version")
		self.label1.move(50,100)
		
		self.btn = QPushButton("update",self)
		self.btn.move(50,150)
		self.btn.clicked.connect(self.firmware)
	#output coincidence time
	def setCoincidenceTimeBtn(self):
		self.label2 = QLabel(self)
		self.label2.setText("coincidence time\nimport time below")
		self.label2.move(200,100)
		
		self.textbox1 = QLineEdit(self)
		self.textbox1.move(200,150)
		self.textbox1.resize(100,25)
		
		self.btn2 = QPushButton("update",self)
		self.btn2.move(200,200)
		self.btn2.clicked.connect(self.coincidence)
	#output histogram to send
	def setHistogramBtn(self):
		self.label3 = QLabel(self)
		self.label3.setText("Histogram to send\nimport histogram\nnumber below")
		self.label3.move(350,100)
		
		self.textbox2 = QLineEdit(self)
		self.textbox2.move(350,170)
		self.textbox2.resize(100,25)
		
		self.btn3 = QPushButton("update",self)
		self.btn3.move(350,200)
		self.btn3.clicked.connect(self.histogram)
		
	#output Toggle Output Enable
	def setToggleOutputBtn(self):
		self.label4 = QLabel(self)
		self.label4.setText("Toggle Output Enable")
		self.label4.move(500,100)
		
		self.btn4 = QPushButton("update",self)
		self.btn4.move(500,150)
		self.btn4.clicked.connect(self.Toggle_output_enable)
		
	#output Toggle Clock input
	def setToggleClockInputBtn(self):
		self.label5 = QLabel(self)
		self.label5.setText("Toggle clock inputs")
		self.label5.move(650,100)
		
		self.btn5 = QPushButton("update",self)
		self.btn5.move(650,150)
		self.btn5.clicked.connect(self.Toggle_clock_inputs)
		
	#output adjust clock phase
	def setAdjustClockPhaseBtn(self):
		self.label6 = QLabel(self)
		self.label6.setText("Adjust Clock Phase")
		self.label6.move(800,100)
		
		self.btn6 = QPushButton("update",self)
		self.btn6.move(800,150)
		self.btn6.clicked.connect(self.adjust_clock_phase)
		
	#output set Random seed
	def setRandomSeedBtn(self):
		self.label7 = QLabel(self)
		self.label7.setText("Set Random Seed\nimport seed\nnumber below")
		self.label7.move(50,300)
		
		self.textbox3 = QLineEdit(self)
		self.textbox3.move(50,370)
		self.textbox3.resize(100,25)
		
		self.btn7 = QPushButton("update",self)
		self.btn7.move(50,400)
		self.btn7.clicked.connect(self.random_seed)
		
	#output petprescale
	def setPrescaleBtn(self):
		self.label8 = QLabel(self)
		self.label8.setText("Set Prescale\nimport prescale\nnumber below")
		self.label8.move(200,300)
		
		#set textbox
		self.textbox4 = QLineEdit(self)
		self.textbox4.move(200,370)
		self.textbox4.resize(100,25)
		#set btn
		self.btn8 = QPushButton("update",self)
		self.btn8.move(200,400)
		self.btn8.clicked.connect(self.set_prescale)
		
	#output get active clock
	def setActiveClockBtn(self):
		self.label9 = QLabel(self)
		self.label9.setText("Get Active Clock")
		self.label9.move(350,300)
		
		self.btn9 = QPushButton("update",self)
		self.btn9.move(350,350)
		self.btn9.clicked.connect(self.active_clock)
		
	#output toggle phase(up/down)
	def setTogglePhaseBtn(self):
		self.label10 = QLabel(self)
		self.label10.setText("Toggle Phase")
		self.label10.move(500,300)
		
		self.btn10 = QPushButton("update",self)
		self.btn10.move(500,350)
		self.btn10.clicked.connect(self.toggle_phase)
		
	#output Send Histogram
	def setSendHistogramBtn(self):
		self.label11 = QLabel(self)
		self.label11.setText("Send Histogram")
		self.label11.move(650,300)
		
		self.btn11 = QPushButton("update",self)
		self.btn11.move(650,350)
		self.btn11.clicked.connect(self.send_histogram)
		
	#output set dead time
	def setDeadTimeBtn(self):
		self.label12 = QLabel(self)
		self.label12.setText("Set Dead Time\nimport time below")
		self.label12.move(800,300)
		
		self.textbox5 = QLineEdit(self)
		self.textbox5.move(800,350)
		self.textbox5.resize(100,25)
		
		self.btn12 = QPushButton("update",self)
		self.btn12.move(800,400)
		self.btn12.clicked.connect(self.dead_time)
		
	#output adjust clock 1 phase
	def setAdjustClock1Btn(self):
		self.label13 = QLabel(self)
		self.label13.setText("adjust clock 1 Phase")
		self.label13.move(50,500)
		
		self.btn13 = QPushButton("update",self)
		self.btn13.move(50,550)
		self.btn13.clicked.connect(self.adjust_clock1)
		
	#output Toggle Trigger Rolling
	def setToggleTriggerRollingBtn(self):
		self.label14 = QLabel(self)
		self.label14.setText("Toggle Trigger Rolling")
		self.label14.move(200,500)
		
		self.btn14 = QPushButton("update",self)
		self.btn14.move(200,550)
		self.btn14.clicked.connect(self.toggle_trigger)
		
	#output Set Input Trigger Mask
	def setInputTriggerMaskBtn(self):
		self.label15 = QLabel(self)
		self.label15.setText("Set input Trigger Mask\nimport mask below")
		self.label15.move(350,500)
		
		self.textbox6 = QLineEdit(self)
		self.textbox6.move(350,550)
		self.textbox6.resize(100,25)
		
		self.btn15 = QPushButton("update",self)
		self.btn15.move(350,600)
		self.btn15.clicked.connect(self.trigger_mask)
		
	#output set trigger
	def setTriggerBtn(self):
		self.label16 = QLabel(self)
		self.label16.setText("Set trigger\nimport trigger below")
		self.label16.move(500,500)
		
		self.textbox7 = QLineEdit(self)
		self.textbox7.move(500,550)
		self.textbox7.resize(100,25)
		
		self.btn16 = QPushButton("update",self)
		self.btn16.move(500,600)
		self.btn16.clicked.connect(self.set_trigger)
		
	#output get clock cycles/last trigger fired
	def setClockCyclesBtn(self):
		self.label17 = QLabel(self)
		self.label17.setText("Toggle Trigger Rolling")
		self.label17.move(650,500)
		
		self.btn17 = QPushButton("update",self)
		self.btn17.move(650,550)
		self.btn17.clicked.connect(self.clock_cycle)
	
	#reset clock
	def setReClockBtn(self):
		self.label18 = QLabel(self)
		self.label18.setText("Reset Clock")
		self.label18.move(800,500)
		
		self.btn18 = QPushButton("update",self)
		self.btn18.move(800,550)
		self.btn18.clicked.connect(self.reset_clock)

		
	def firmware(self):
		runClass(0)
		
	def coincidence(self):
		self.CoincidenceTime = int(self.textbox1.text())
		runClass(1,self.CoincidenceTime)
		
	def histogram(self):
		self.HistogramNum = int(self.textbox2.text())
		runClass(2,self.HistogramNum)
	
	def Toggle_output_enable(self):
		runClass(3)
	
	def Toggle_clock_inputs(self):
		runClass(4)
	
	def adjust_clock_phase(self):
		runClass(5)
	
	def random_seed(self):
		self.seed = int(self.textbox3.text())
		runClass(6,self.seed)
	
	def set_prescale(self):
		self.Prescale = int(self.textbox4.text())
		runClass(7,self.Prescale)
	
	def active_clock(self):
		runClass(8)
	
	def toggle_phase(self):
		runClass(9)
	
	def send_histogram(self):
		runClass(10)
	
	def dead_time(self):
		self.DeadTime = int(self.textbox5.text())
		runClass(11,self.DeadTime)
	
	def adjust_clock1(self):
		runClass(12)
	
	def toggle_trigger(self):
		runClass(13)
	
	def	trigger_mask(self):
		self.TriggerMask = int(self.textbox6.text())
		runClass(14,self.TriggerMask)
	
	def set_trigger(self):
		self.TriggerNum = int(self.textbox7.text())
		runClass(15,self.TriggerNum)
	
	def clock_cycle(self):
		runClass(16)
	
	def reset_clock(self):
		runClass(17)
		

