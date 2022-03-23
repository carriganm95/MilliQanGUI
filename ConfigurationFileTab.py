#!/user/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#from MilliDAQ.python.Demonstrator import *
from Demonstrator import *
import sys
import logging
import subprocess
import os
import signal
import time
import glob
import select
import os.path

#finde the demonstartor information from that file
cfg = Demonstrator()

logging.basicConfig(format = "%(message)s",level = logging.INFO)

#class for configuration file Tab
class configure_tab(QWidget):
	def __init__(self):
		super().__init__()
		#set up different variable we will use in configure tab
		self.list_dgtz = [] 	#list for digitizer number
		self.list_channel = []	#list for Channel number
		self.list_group = []	#list for group number
		self.Dgtz = "0"			#Current digitizer
		self.Channel = "0"		#Current channel
		self.Group = "0"		#Current Group
		self.enabletype = "True"			#Current enabletype
		self.polaritytype = "risingEdge"	#Current polaritytyoe
		self.textvalue1 = ""				#Current value in textbox1
		self.textvalue2 = ""				#Current value in textbox2
		self.textvalue3 = ""				#Current value in textbox3
		self.triggertype = "software"		#Current triggerType
		self.triggerlogic = "logicOr"		#Current triggerlogic
		self.filename = ""					#Current file name
	
		#set up all the buttons and textbox on tab
		self.setCombolistDgtz()
		self.setCombolistchannel()
		self.setCombolistGroup()
		self.setTriggerEnableBtn()
		self.setTriggerPolarityBtn()
		self.setTriggerThresholdBtn()
		self.setTriggerDelayBtn()
		self.setTriggerTypeBtn()
		self.setGroupTriggerLogicBtn()
		self.setMaxNumEventsBtn()
		self.setfilename()
		self.setTitleLabel()

		self.setSavebtn()
		self.setAppendbtn()
		self.setTextEdit()
		self.SetHelpButton()
	
	#set title for this tab
	def setTitleLabel(self):
		self.labeltitle = QLabel(self)
		self.labeltitle.setText("Python Configuration Maker")
		#self.label.setStyleSheet("border: 1px solid black;")
		self.labeltitle.setFont(QFont("Arial",30))
		self.labeltitle.move(300,20)
		#self.label12.resize(150,50)
	
	#Set textbox for information we create in file

	def setTextEdit(self):
		self.QTE = QTextEdit(self)
		self.QTE.move(500,100)
		self.QTE.resize(400,500)
        
	#List for digitizers
	def setCombolistDgtz(self):
		self.comboboxdgtz = QComboBox(self)
		self.comboboxdgtz.move(100,150)
		for dgtz in range(len(cfg.Digitizers)):
			self.list_dgtz.append(str(dgtz))
		self.comboboxdgtz.addItems(self.list_dgtz)
		self.comboboxdgtz.currentTextChanged.connect(self.update_dgtz)
		
		self.labelcombodgtz = QLabel(self)
		self.labelcombodgtz.setText("Digitizers")
		self.labelcombodgtz.move(100,100)
	
	#Function to update digitizer number
	def update_dgtz(self,value):
		#global self.Dgtz
		self.Dgtz = value
		
	#List for Channel
	def setCombolistchannel(self):
		self.comboboxchannel = QComboBox(self)
		self.comboboxchannel.move(100,250)
		for channel in range(16):
			self.list_channel.append(str(channel))
		self.comboboxchannel.addItems(self.list_channel)
		self.comboboxchannel.currentTextChanged.connect(self.update_channel)
		
		self.labecombochannel = QLabel(self)
		self.labecombochannel.setText("Channel")
		self.labecombochannel.move(100,200)
		
	#Function to update channel number
	def update_channel(self,value):
		#global self.Channel
		self.Channel = value
	
	#Choose triigerenable
	def setTriggerEnableBtn(self):
		self.labeltriggerenable = QLabel(self)
		self.labeltriggerenable.setText("triggerEnable")
		self.labeltriggerenable.move(200,250)
	
		self.comboboxtype = QComboBox(self)
		self.comboboxtype.move(310,250)
		self.comboboxtype.addItems(["True","False"])
		self.comboboxtype.currentTextChanged.connect(self.update_triggerenable)
	
	#function to update enable type
	def update_triggerenable(self,value):
		#global self.enabletype
		self.enabletype = value
	
	#choose trigger polarity type
	def setTriggerPolarityBtn(self):
		self.labeltriggerpolarity = QLabel(self)
		self.labeltriggerpolarity.setText("triggerPolarity")
		self.labeltriggerpolarity.move(200,300)
	
		self.comboboxtpolarity = QComboBox(self)
		self.comboboxtpolarity.move(310,300)
		self.comboboxtpolarity.addItems(["risingEdge","fallingEdge"])
		self.comboboxtpolarity.currentTextChanged.connect(self.update_triggerpolarity)
	
	#function to update polarity type
	def update_triggerpolarity(self,value):
		#global self.polaritytype
		self.polaritytype = "Channel." + value
	
	#Choose trigger Threshold
	def setTriggerThresholdBtn(self):
		self.labeltriggerthreshold = QLabel(self)
		self.labeltriggerthreshold.setText("triggerThreshold")
		self.labeltriggerthreshold.move(200,350)

		self.textboxtriggerthreshold = QLineEdit(self)
		self.textboxtriggerthreshold.move(310,350)
		self.textboxtriggerthreshold.resize(100,30)

	
	#Choose Group
	def setCombolistGroup(self):
		self.comboboxgroup = QComboBox(self)
		self.comboboxgroup.move(100,450)
		for group in range(8):
			self.list_group.append(str(group))
		self.comboboxgroup.addItems(self.list_group)
		self.comboboxgroup.currentTextChanged.connect(self.update_group)

		self.labelcombogroup = QLabel(self)
		self.labelcombogroup.setText("Group")
		self.labelcombogroup.move(100,400)
		
	#update group number
	def update_group(self,value):
		#global self.Group
		self.Group = value
	
	#Choose Trigger delay
	def setTriggerDelayBtn(self):
		self.labeltriggerdelay = QLabel(self)
		self.labeltriggerdelay.setText("TriggerDelay")
		self.labeltriggerdelay.move(200,450)

		self.textboxtriggerdelay = QLineEdit(self)
		self.textboxtriggerdelay.move(300,450)
		self.textboxtriggerdelay.resize(100,30)
		#self.textvalue2 = self.textbox2.text()
	
	#Choose trigger type
	def setTriggerTypeBtn(self):
		self.labeltriggertype = QLabel(self)
		self.labeltriggertype.setText("TriggerType")
		self.labeltriggertype.move(100,550)

		self.comboboxtriggertype = QComboBox(self)
		self.comboboxtriggertype.move(200,550)
		self.comboboxtriggertype.addItems(["software","normal","auto","external","externalAndNormal","externalOrNormal","none"])
		self.comboboxtriggertype.currentTextChanged.connect(self.update_triggertype)
	
	#update triggertype
	def update_triggertype(self,value):
		#global self.triggertype
		self.triggertype = "TriggerType." + value
	
	#Choose Group trigger Logic
	def setGroupTriggerLogicBtn(self):
		self.label2 = QLabel(self)
		self.label2.setText("GroupTriggerLogic")
		self.label2.move(100,650)
	
		self.comboboxtype4 = QComboBox(self)
		self.comboboxtype4.move(250,650)
		self.comboboxtype4.addItems(["logicOr","logicAnd"])
		self.comboboxtype4.currentTextChanged.connect(self.update_grouptriggerlogic)
	
	#update group trigger logic
	def update_grouptriggerlogic(self,value):
		#global self.triggerlogic
		self.triggerlogic = value
	
	#Choose max number events
	def setMaxNumEventsBtn(self):
		self.label7 = QLabel(self)
		self.label7.setText("MaxNumEventsBLT")
		self.label7.move(100,700)
	
		self.textbox3 = QLineEdit(self)
		self.textbox3.move(250,700)
		self.textbox3.resize(100,30)
		#self.textvalue3 = self.textbox3.text()
	
	#set up file name btn
	def setfilename(self):
		self.label11 = QLabel(self)
		self.label11.setText("Please type the file name you want below")
		self.label11.setFont(QFont('Arial',15))
		self.label11.move(500,610)
		
		self.textbox4 = QLineEdit(self)
		self.textbox4.move(500,650)
		self.textbox4.resize(150,30)
		#self.textvalue4 = self.textbox4.text()
	
	#set up save file btn
	def setSavebtn(self):
		self.savebtn = QPushButton("Create",self)
		self.savebtn.move(500,700)
		self.savebtn.clicked.connect(self.save)
		
	#Use the information user want to create a new file
	def save(self):
		#update value to template value
		self.textvalue1 = self.textbox1.text()
		self.textvalue2 = self.textbox2.text()
		self.textvalue3 = self.textbox3.text()
		self.textvalue4 = self.textbox4.text() + ".py"
		self.filename = os.path.join("../../config",self.textvalue4)
		self.DGTZ = "cfg.Digitizers["
		go = True
		#Check the file if it is already exist
		if os.path.exists(self.filename) :
			self.buttonReply = QMessageBox.question(self,"Message box","This file is already exist do you want to rewrite it",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
			if self.buttonReply == QMessageBox.Yes :
				go = True
			else:
				go = False
				
		#print imformation into the new file
		if go == True :
			f = open(self.filename,"w+")
			f.write("from Demonstrator import *\n")
			f.write("cfg = Demonstrator()\n")
			f.write("for dgtz in cfg.Digitizers:\n")
			f.write("		 dgtz.IRQPolicy.use = False\n")
			f.write("		 for iChannel, channel in enumerate(dgtz.channels):\n")
			f.write("		 channel.enable = True\n")
			f.write("				 channel.triggerEnable = False\n")
			self.triggertypetemp = self.DGTZ + self.Dgtz + "].TriggerType.type = " + self.triggertype +"\n"
			f.write(self.triggertypetemp)
			self.QTE.append(self.triggertypetemp)
			self.grouptriggerlogictemp = self.DGTZ + self.Dgtz + "].GroupTriggerLogic.logic = " + self.triggerlogic + "\n"
			f.write(self.grouptriggerlogictemp)
			self.QTE.append(self.grouptriggerlogictemp)
			self.triggerenabletemp = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerEnable = " + self.enabletype +  "\n"
			f.write(self.triggerenabletemp)
			self.QTE.append(self.triggerenabletemp)
			if self.textvalue1 != "" :
				self.triggerthresholdtemp = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerThreshold = " + self.textvalue1 + "\n"
				f.write(self.triggerthresholdtemp)
				self.QTE.append(self.triggerthresholdtemp)
			self.triggerpolaritytemp = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerPolarity = " + self.polaritytype + "\n"
			f.write(self.triggerpolaritytemp)
			self.QTE.append(self.triggerpolaritytemp)
			if self.textvalue2 != "" :
				self.maxnumeventsblttemp = self.DGTZ + self.Dgtz + "].MaxNumEventsBLT = " + self.textvalue2 + "\n"
				f.write(self.maxnumeventsblttemp)
				self.QTE.append(self.maxnumeventsblttemp)
			if self.textvalue3 != "" :
				self.triggerdelaytemp = self.DGTZ + self.Dgtz + "].groups[" + self.Group + "].triggerDelay = " + self.textvalue3 + "\n"
				f.write(self.triggerdelaytemp)
				self.QTE.append(self.triggerdelaytemp)
			
			f.close()
		
	#set up append btn
	def setAppendbtn(self):
		self.appendbtn = QPushButton("append",self)
		self.appendbtn.move(600,700)
		self.appendbtn.clicked.connect(self.appendfile)
	
	#Append more information to the file user just create
	def appendfile(self):
		self.DGTZ = "cfg.Digitizers["
		f = open(self.filename,"r+")
		text = f.read()

		self.triggertypetemp = self.DGTZ + self.Dgtz + "].TriggerType.type = " + self.triggertype +"\n"
		if self.triggertypetemp not in text :
			f.write(self.triggertypetemp)
			self.QTE.append(self.triggertypetemp)
		self.grouptriggerlogictemp = self.DGTZ + self.Dgtz + "].GroupTriggerLogic.logic = " + self.triggerlogic + "\n"
		if self.grouptriggerlogictemp not in text :
			f.write(self.grouptriggerlogictemp)
			self.QTE.append(self.grouptriggerlogictemp)
		self.triggerenabletemp = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerEnable = " + self.enabletype +  "\n"
		if self.triggerenabletemp not in text :
			f.write(self.triggerenabletemp)
			self.QTE.append(self.triggerenabletemp)
		if self.textvalue1 != "" :
			self.triggerthresholdtemp = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerThreshold = " + self.textvalue1 + "\n"
			if self.triggerthresholdtemp not in text :
				f.write(self.triggerthresholdtemp)
				self.QTE.append(self.triggerthresholdtemp)
		self.triggerpolaritytemp = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerPolarity = " + self.polaritytype + "\n"
		if self.triggerpolaritytemp not in text :
			f.write(self.triggerpolaritytemp)
			self.QTE.append(self.triggerpolaritytemp)
		if self.textvalue2 != "" :
			self.maxnumeventsblttemp = self.DGTZ + self.Dgtz + "].MaxNumEventsBLT = " + self.textvalue2 + "\n"
			if self.maxnumeventsblttemp not in text :
				f.write(self.maxnumeventsblttemp)
				self.QTE.append(self.maxnumeventsblttemp)
		if self.textvalue3 != "" :
			self.triggerdelaytemp = self.DGTZ + self.Dgtz + "].groups[" + self.Group + "].triggerDelay = " + self.textvalue3 + "\n"
			if self.triggerdelaytemp not in text :
				f.write(self.triggerdelaytemp)
				self.QTE.append(self.triggerdelaytemp)
		f.close()
	
	#set up help btn
	def SetHelpButton(self):
		self.helpbtn = QPushButton("help",self)
		self.helpbtn.move(200, 100)
		self.helpbtn.clicked.connect(self.massage)
        
	#help message to remind user how to use this gui
	def message(self):
		self.msg = QMessageBox(self)
		#self.msg.setIcon(QMessageBox.Information)
		self.msg.setText("This tab is using for creating python configuration files for the MiliQan detector.\nYou can create a new file with the name you want by clicking create.\nWhen you want to add other digitizers, channels, or groups just modify the information and click append.")
		
		self.msg.setWindowTitle("This is the help window")
		self.retval = self.msg.exec_()
