
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import logging
import subprocess
import os
import signal
import time
import glob
import select
import os.path

class tab3(QWidget):
	def __init__(self):
		super().__init__()
		self.setlabel()
		self.setlabel1()
		self.setlabel2()
		self.setlabel3()
		self.setlabel4()
		self.setlabel5()
		self.setlabel6()
		self.setlabel7()
		self.setlabel8()
		self.setlabel9()
		self.setlabel10()
		self.setlabel11()
		self.setlabel12()
		self.setlabel13()
		self.setlabel14()
		self.setlabel15()
		self.setlabel16()
		self.setlabel17()
		self.setlabel18()
		self.setbtn1()
		self.setbtn2()
		self.setbtn3()
		self.setbtn4()
		self.setbtn5()
		self.setbtn6()
		self.setbtn7()
		self.setbtn8()
		self.setbtn9()
		self.setbtn10()
		self.setbtn11()
		self.setbtn12()
		self.setbtn13()
		self.setbtn14()
		self.setbtn15()
		self.setbtn16()
		self.setbtn17()
		self.setbtn18()
		self.setTextbox1()
		self.setTextbox2()
		self.setTextbox3()
		self.setTextbox4()
		self.setTextbox5()
		self.setTextbox6()
		self.setTextbox7()
		
		self.show()
		
	
	def setlabel(self):
		self.label = QLabel(self)
		self.label.setText("Control Trigger Board")
		self.label.setFont(QFont("Arial",30))
		self.label.move(300,20)
	#output firmware version
	def setlabel1(self):
		self.label1 = QLabel(self)
		self.label1.setText("Firmware version")
		self.label1.move(50,100)
		
	def setbtn1(self):
		self.btn = QPushButton("update",self)
		self.btn.move(50,150)
		self.btn.clicked.connect(self.firmware)
	#output coincidence time
	def setlabel2(self):
		self.label2 = QLabel(self)
		self.label2.setText("coincidence time\nimport time below")
		self.label2.move(200,100)
		
	def setTextbox1(self):
		self.textbox1 = QLineEdit(self)
		self.textbox1.move(200,150)
		self.textbox1.resize(100,25)
		
	def setbtn2(self):
		self.btn2 = QPushButton("update",self)
		self.btn2.move(200,200)
		self.btn2.clicked.connect(self.coincidence)
	#output histogram to send
	def setlabel3(self):
		self.label3 = QLabel(self)
		self.label3.setText("Histogram to send\nimport histogram\nnumber below")
		self.label3.move(350,100)
		
	def setTextbox2(self):
		self.textbox2 = QLineEdit(self)
		self.textbox2.move(350,150)
		self.textbox2.resize(100,25)
		
	def setbtn3(self):
		self.btn3 = QPushButton("update",self)
		self.btn3.move(350,200)
		self.btn3.clicked.connect(self.histogram)
		
	#output Toggle Output Enable
	def setlabel4(self):
		self.label4 = QLabel(self)
		self.label4.setText("Toggle Output Enable")
		self.label4.move(500,100)
		
	def setbtn4(self):
		self.btn4 = QPushButton("update",self)
		self.btn4.move(500,150)
		self.btn4.clicked.connect(self.Toggle_output_enable)
		
	#output Toggle Clock input
	def setlabel5(self):
		self.label5 = QLabel(self)
		self.label5.setText("Toggle clock inputs")
		self.label5.move(650,100)
		
	def setbtn5(self):
		self.btn5 = QPushButton("update",self)
		self.btn5.move(650,150)
		self.btn5.clicked.connect(self.Toggle_clock_inputs)
		
	#output adjust clock phase
	def setlabel6(self):
		self.label6 = QLabel(self)
		self.label6.setText("Adjust Clock Phase")
		self.label6.move(800,100)
		
	def setbtn6(self):
		self.btn6 = QPushButton("update",self)
		self.btn6.move(800,150)
		self.btn6.clicked.connect(self.adjust_clock_phase)
		
	#output set Random seed
	def setlabel7(self):
		self.label7 = QLabel(self)
		self.label7.setText("Set Random Seed\nimport seed\nnumber below")
		self.label7.move(50,300)
		
	def setTextbox3(self):
		self.textbox3 = QLineEdit(self)
		self.textbox3.move(50,350)
		self.textbox3.resize(100,25)
		
	def setbtn7(self):
		self.btn7 = QPushButton("update",self)
		self.btn7.move(50,400)
		self.btn7.clicked.connect(self.random_seed)
		
	#output petprescale
	def setlabel8(self):
		self.label8 = QLabel(self)
		self.label8.setText("Set Prescale\nimport prescale\nnumber below")
		self.label8.move(200,300)
		
	def setTextbox4(self):
		self.textbox4 = QLineEdit(self)
		self.textbox4.move(200,350)
		self.textbox4.resize(100,25)
		
	def setbtn8(self):
		self.btn8 = QPushButton("update",self)
		self.btn8.move(200,400)
		self.btn8.clicked.connect(self.set_prescale)
		
	#output get active clock
	def setlabel9(self):
		self.label9 = QLabel(self)
		self.label9.setText("Get Active Clock")
		self.label9.move(350,300)
		
	def setbtn9(self):
		self.btn9 = QPushButton("update",self)
		self.btn9.move(350,350)
		self.btn9.clicked.connect(self.active_clock)
		
	#output toggle phase(up/down)
	def setlabel10(self):
		self.label10 = QLabel(self)
		self.label10.setText("Toggle Phase(up/down)")
		self.label10.move(500,300)
		
	def setbtn10(self):
		self.btn10 = QPushButton("update",self)
		self.btn10.move(500,350)
		self.btn10.clicked.connect(self.toggle_phase)
		
	#output Send Histogram
	def setlabel11(self):
		self.label11 = QLabel(self)
		self.label11.setText("Send Histogram")
		self.label11.move(650,300)
		
	def setbtn11(self):
		self.btn11 = QPushButton("update",self)
		self.btn11.move(650,350)
		self.btn11.clicked.connect(self.send_histogram)
		
	#output set dead time
	def setlabel12(self):
		self.label12 = QLabel(self)
		self.label12.setText("Set Dead Time\nimport time below")
		self.label12.move(800,300)
		
	def setTextbox5(self):
		self.textbox5 = QLineEdit(self)
		self.textbox5.move(800,350)
		self.textbox5.resize(100,25)
		
	def setbtn12(self):
		self.btn12 = QPushButton("update",self)
		self.btn12.move(800,400)
		self.btn12.clicked.connect(self.dead_time)
		
	#output adjust clock 1 phase
	def setlabel13(self):
		self.label13 = QLabel(self)
		self.label13.setText("adjust clock 1 Phase")
		self.label13.move(50,500)
		
	def setbtn13(self):
		self.btn13 = QPushButton("update",self)
		self.btn13.move(50,550)
		self.btn13.clicked.connect(self.adjust_clock1)
		
	#output Toggle Trigger Rolling
	def setlabel14(self):
		self.label14 = QLabel(self)
		self.label14.setText("Toggle Trigger Rolling")
		self.label14.move(200,500)
		
	def setbtn14(self):
		self.btn14 = QPushButton("update",self)
		self.btn14.move(200,550)
		self.btn14.clicked.connect(self.toggle_trigger)
		
	#output Set Input Trigger Mask
	def setlabel15(self):
		self.label15 = QLabel(self)
		self.label15.setText("Set input Trigger Mask\nimport mask below")
		self.label15.move(350,500)
		
	def setTextbox6(self):
		self.textbox6 = QLineEdit(self)
		self.textbox6.move(350,550)
		self.textbox6.resize(100,25)
		
	def setbtn15(self):
		self.btn15 = QPushButton("update",self)
		self.btn15.move(350,600)
		self.btn15.clicked.connect(self.trigger_mask)
		
	#output set trigger
	def setlabel16(self):
		self.label16 = QLabel(self)
		self.label16.setText("Set trigger\nimport trigger below")
		self.label16.move(500,500)
		
	def setTextbox7(self):
		self.textbox7 = QLineEdit(self)
		self.textbox7.move(500,550)
		self.textbox7.resize(100,25)
		
	def setbtn16(self):
		self.btn16 = QPushButton("update",self)
		self.btn16.move(500,600)
		self.btn16.clicked.connect(self.set_trigger)
		
	#output get clock cycles/last trigger fired
	def setlabel17(self):
		self.label17 = QLabel(self)
		self.label17.setText("Toggle Trigger Rolling")
		self.label17.move(650,500)
		
	def setbtn17(self):
		self.btn17 = QPushButton("update",self)
		self.btn17.move(650,550)
		self.btn17.clicked.connect(self.clock_cycle)
	
	#reset clock
	def setlabel18(self):
		self.label18 = QLabel(self)
		self.label18.setText("Reset Clock")
		self.label18.move(800,500)
		
	def setbtn18(self):
		self.btn18 = QPushButton("update",self)
		self.btn18.move(800,550)
		self.btn18.clicked.connect(self.reset_clock)

		
	def firmware(self):
		x=0
	def coincidence(self):
		x=1
	def histogram(self):
		x=2
	def Toggle_output_enable(self):
		x=3
	def Toggle_clock_inputs(self):
		x=4
	def adjust_clock_phase(self):
		x=5
	def random_seed(self):
		x=6
	def set_prescale(self):
		x=7
	def active_clock(self):
		x=8
	def toggle_phase(self):
		x =9
	def send_histogram(self):
		x =10
	def dead_time(self):
		x =11
	def adjust_clock1(self):
		x=12
	def toggle_trigger(self):
		x =13
	def	trigger_mask(self):
		x =14
	def set_trigger(self):
		x=15
	def clock_cycle(self):
		x=16
	def reset_clock(self):
		x=17
		

