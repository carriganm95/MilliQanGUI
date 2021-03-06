#!/user/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#from MilliDAQ.python.Demonstrator import *
from Demonstrator import *
from new_DAQCommand import *
from triggerBoard import *
import sys
import logging
import subprocess
import os
import signal
import time
import glob
import select
import os.path
import json


#class for long runing function which need to be killed
class worker(QObject):
    def __init__(self):
        super().__init__()
        
        #set a variable for file
        self.p = None


    finished = pyqtSignal()
	
	#Run DAQcommand start on terminal
    def clicked_start(self):
        p = subprocess.Popen("DAQCommand start", shell=True) #Run this command in terminal
        time.sleep(5)		#The time counter sleep for 0.5 second
        pid = p.pid
        tail_pid = subprocess.Popen("ps aux | grep -i 'tail -f /var/log/MilliDAQ.log' | pgrep 'tail'", shell=True, stdout=subprocess.PIPE).communicate()[0] #find the tail we open
        tail_pid = int(tail_pid)
        os.kill(tail_pid, signal.SIGINT) #kill the tail we don't want
        p.terminate() #kill the variable we use
        self.finished.emit()

    #Run DAQCommand status on terminal
    def clicked_status(self):
        p1 = subprocess.Popen("DAQCommand status", shell= True) #Run this command in terminal
        time.sleep(5)			#The time counter sleep for 0.5 second
        pid1 = p1.pid
        tail1_pid = subprocess.Popen("ps aux | grep -i 'tail -f /var/log/MilliDAQ.log' | pgrep 'tail'", shell = True,stdout = subprocess.PIPE).communicate()[0] #find the tail we open
        tail1_pid = int(tail1_pid)
        os.kill(tail1_pid,signal.SIGINT) #kill the tail
        p1.terminate() #kill the variable we use
        self.finished.emit()
            
	#Run DAQCommand stop on terminal
    def clicked_stop(self):
        p2 = subprocess.Popen("DAQCommand stop", shell= True) #Run this command in terminal
        time.sleep(5) 				#The time counter sleep for 0.5 second
        pid2 = p2.pid
        tail2_pid = subprocess.Popen("ps aux | grep -i 'tail -f /var/log/MilliDAQ.log' | pgrep 'tail'", shell = True,stdout = subprocess.PIPE).communicate()[0] #find the tail we open
        tail2_pid = int(tail2_pid)
        os.kill(tail2_pid,signal.SIGINT)	#kill the tail
        p2.terminate()		#kill the variable we use

        self.finished.emit()

#the mean tab for Runing DAQcommand
class daqcommand_tab(QWidget):
    def __init__(self):
        super().__init__()
        self.contents = []
        self.content_temp = []
        self.configList = []
        self.triggerList = []
		
	#set up every button, textbox and list on GUI
        self.startbtn = btnlongrun(self, "start",150,150,self.longrun_start) #start the detector
        btn(self,"reconfigure",550,200,self.clickReconfigure) #reconfigure the detector with different file
        btn(self,"set trigger",650,150,self.clickSetTrigger) #set new trigger
        btn(self,"help",750,200,self.message) #give user a help message
        self.stopbtn = btnlongrun(self,"Stop",300,150,self.longrun_stop) #Stop the detector
        self.statusbtn = btnlongrun(self,"status",450,150,self.longrun_status) #Status the outcome from the detector
        btn(self,"list",250,200,self.clicked_list) #list the file we have to reconfigure
		
		
	#set up the rest things in this tab
        self.Setlabel()
        self.SetReconfigureList()
        self.SetTextEdit()
        self.SetqTimer()
        self.Setimage()
        self.SetTriggerList()
	
        
        self.show()

#set the logo of Milliqan
    def Setimage(self):
        self.label = QLabel(self)
        #self.pixmap = QPixmap('/Users/mr-right/physics/research2/MilliQanGUI/MicrosoftTeams-image.png')
        self.pixmap = QPixmap('Images/MilliQanLogo.png')
        self.label.setPixmap(self.pixmap.scaled(310,120))
        self.label.move(50,10)
        self.label.adjustSize()
        #self.resize(self.pixmap.width(), self.pixmap.height())
        
    def Setlabel(self):
        self.label = QLabel(self)
        self.label.setText("MilliQan DAQCommand")
        #self.label.setStyleSheet("border: 1px solid black;")
        self.label.setFont(QFont('Arial',30))
        self.label.move(400,50)
        self.label.adjustSize()
    
        
    # To connect a combo box use: combo.activated[str].connect(self.onChanged)
    
    #create combolist for files we want to reconfigure
    def SetReconfigureList(self):
        self.reconfiglist = QComboBox(self)
        self.reconfiglist.move(450,200)
        self.reconfiglist.addItems([])
        self.reconfiglist.currentTextChanged.connect(self.reconfigureCommand)
	
	#Give user help about this GUI
    
    #update the file name to command we use on terminal
    def reconfigureCommand(self, text):                                                    
        self.reconfigure_text  = "DAQCommand reconfigure ../../config/" + text
      
    #update the terminal information to textbox
    def clickReconfigure(self):                                                                
        p3 = subprocess.Popen(self.reconfigure_text, shell= True)
        time.sleep(5)
        pid3 = p3.pid
        tail3_pid = subprocess.Popen("ps aux | grep -i 'tail -f /var/log/MilliDAQ.log' | pgrep 'tail'", shell = True,stdout = subprocess.PIPE).communicate()[0]
        tail3_pid = int(tail3_pid)
        os.kill(tail3_pid,signal.SIGINT)
        p3.terminate()
   
    #create combolist for files we want to reconfigure
    def SetTriggerList(self):
        self.triggerlist = QComboBox(self)
        self.triggerlist.move(550,150)
        self.triggerlist.addItems([])
        self.triggerlist.currentTextChanged.connect(self.triggerCommand)

    #update the file name to command we use on terminal
    def triggerCommand(self, text):
        self.trigger_text  = "DAQCommand setTrigger ../../config/" + text
 
    def clickSetTrigger(self):
        p = subprocess.Popen(self.trigger_text, shell = True)
        time.sleep(5)
        pid = p.pid
        tail_pid = subprocess.Popen("ps aux | grep -i 'tail -f /var/log/MilliDAQ.log' | pgrep 'tail'", shell = True,stdout = subprocess.PIPE).communicate()[0]
        tail_pid = int(tail_pid)
        os.kill(tail_pid, signal.SIGINT)
        p.terminate()
    
    #list the file can configure
    def updateConfigCombo(self):
        self.reconfiglist.clear()
        self.reconfiglist.addItems(self.configList)
        
    def updateTriggerCombo(self):
        self.triggerlist.clear()
        self.triggerlist.addItems(self.triggerList)

	#Auto update textbox which will print the information show in terminal
    def SetTextEdit(self):
        self.QTE = QTextEdit(self)
        self.QTE.move(150,250)
        self.QTE.resize(700,400)
        #with open('/Users/mr-right/physics/research2/textexample.log') as f:
        with open('/var/log/MilliDAQ.log') as f :
            self.contents = f.readlines()
    
	#Auto timer which will count time
    def SetqTimer(self):
        self.qtimer = QTimer()
        self.qtimer.setInterval(1000) #the number inside is millisecond
        self.qtimer.timeout.connect(self.refreshText)
        self.qtimer.start()
        
	#refresh text in the textbox
    def refreshText(self):
        self.content_temp = self.contents
        linenumber = len(self.content_temp)
        #with open('/Users/mr-right/physics/research2/textexample.log') as f:
        with open('/var/log/MilliDAQ.log') as f :
            self.contents = f.readlines()

        if self.contents != self.content_temp:
            for i in self.contents[linenumber-1:-1]:
                self.QTE.append(i)
                QCoreApplication.processEvents()
                
    #help windom massage
    def message(self):
        self.msg = QMessageBox(self)
        
        self.msg.setText("DAQCommand: \nstart                  -- start the run\n\nstop                   -- stop the run\n\nprint [configuration | board | rates | status]: \nprint configure  -- print the current V1743Configuration parameters: trigger mode, thresholds, etc\n\nprint board      -- print information about the V1743 board: connection, firmware versions, etc\n\nprint rates       -- print DQM information: trigger rates, missed triggers, etc\n\nprint status     -- print DAQ information: state, configuration path, etc\n\nreconfigure <file.xml> -- stop the run, read/apply a new configuration file, then start\n\nYou can use combo box to choose the information you want to print out. \nYou can use the reconfigure button to reconfigure the file we generate. \nThe new drop down menu will show which trigger we are runing and you can change it by set button \nIn the end text box will udapate the information about detector in real time")
        
        self.msg.setWindowTitle("This is the help window")
        self.retval = self.msg.exec_()
        
	#long run start which can start a new thread to start a new run
    def longrun_start(self):
        # Create a QThread object
        self.threadstart = QThread()
        # Create a worker object
        self.workerstart = worker()
        # Move worker to the thread
        self.workerstart.moveToThread(self.threadstart)
        # Connect signals and slots
        self.threadstart.started.connect(self.workerstart.clicked_start)
        self.workerstart.finished.connect(self.threadstart.quit)
        self.workerstart.finished.connect(self.workerstart.deleteLater)
        self.threadstart.finished.connect(self.threadstart.deleteLater)
        # Start the thread
        self.threadstart.start()
        # Final resets
        self.startbtn.setEnabled(False)
        self.threadstart.finished.connect(
            lambda: self.startbtn.setEnabled(True)
        )

	#long run stop which can start a new thread to start a new run
    def longrun_stop(self):
        # Create a QThread object
        self.threadstop = QThread()
        # Create a worker object
        self.workerstop = worker()
        # Move worker to the thread
        self.workerstop.moveToThread(self.threadstop)
        # Connect signals and slots
        self.threadstop.started.connect(self.workerstop.clicked_stop)
        self.workerstop.finished.connect(self.threadstop.quit)
        self.workerstop.finished.connect(self.workerstop.deleteLater)
        self.threadstop.finished.connect(self.threadstop.deleteLater)
    
        # Start the thread
        self.threadstop.start()
        # Final resets
        self.stopbtn.setEnabled(False)
        self.threadstop.finished.connect(
            lambda: self.stopbtn.setEnabled(True)
        )
 
	#long run status which can start a new thread to start a new run
    def longrun_status(self):
        # Create a QThread object
        self.threadstatus = QThread()
        # Create a worker object
        self.workerstatus = worker()
        # Move worker to the thread
        self.workerstatus.moveToThread(self.threadstatus)
        # Connect signals and slots
        self.threadstatus.started.connect(self.workerstatus.clicked_status)
        self.workerstatus.finished.connect(self.threadstatus.quit)
        self.workerstatus.finished.connect(self.workerstatus.deleteLater)
        self.threadstatus.finished.connect(self.threadstatus.deleteLater)
        
        # Start the thread
        self.threadstatus.start()
        # Final resets
        self.statusbtn.setEnabled(False)
        self.threadstatus.finished.connect(
        lambda: self.statusbtn.setEnabled(True)
        )

    #function can list the file inside config
    def clicked_list(self):
        self.configList =[]
        for filename in os.listdir("../../config/daqConfig/"):
            if not filename.endswith(".py"): continue
            self.configList.append(filename)
        for filename in os.listdir("../../config/triggerConfig/"):
            if not filename.endswith(".py"): continue
            self.triggerList.append(filename)
        self.updateConfigCombo()
        self.updateTriggerCombo()
        
	



