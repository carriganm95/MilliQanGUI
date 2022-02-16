#!/user/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MilliDAQ.python.Demonstrator import *
from tab3 import *
#from Demonstrator import *
import sys
import logging
import subprocess
import os
import signal
import time
import glob
import select
import os.path



cfg = Demonstrator()

logging.basicConfig(format = "%(message)s",level = logging.INFO)


class worker(QObject):
    def __init__(self):
        super().__init__()
        
        self.p = None


    finished = pyqtSignal()

    def clicked_start(self):
        p = subprocess.Popen("DAQCommand start", shell=True)
        time.sleep(5)
        pid = p.pid
        tail_pid = subprocess.Popen("ps aux | grep -i 'tail -f /var/log/MilliDAQ.log' | pgrep 'tail'", shell=True, stdout=subprocess.PIPE).communicate()[0]
        tail_pid = int(tail_pid)
        os.kill(tail_pid, signal.SIGINT)
        p.terminate()
        self.finished.emit()

    
    def clicked_status(self):
        p1 = subprocess.Popen("DAQCommand status", shell= True)
        time.sleep(5)
        pid1 = p1.pid
        tail1_pid = subprocess.Popen("ps aux | grep -i 'tail -f /var/log/MilliDAQ.log' | pgrep 'tail'", shell = True,stdout = subprocess.PIPE).communicate()[0]
        tail1_pid = int(tail1_pid)
        os.kill(tail1_pid,signal.SIGINT)
        p1.terminate()
        self.finished.emit()
                
    def clicked_stop(self):
        p2 = subprocess.Popen("DAQCommand stop", shell= True)
        time.sleep(5)
        pid2 = p2.pid
        tail2_pid = subprocess.Popen("ps aux | grep -i 'tail -f /var/log/MilliDAQ.log' | pgrep 'tail'", shell = True,stdout = subprocess.PIPE).communicate()[0]
        tail2_pid = int(tail2_pid)
        os.kill(tail2_pid,signal.SIGINT)
        p2.terminate()

        self.finished.emit()
        
    def clicked_print(self):
        p3 = subprocess.Popen("DAQCommand print", shell= True)
        time.sleep(5)
        pid3 = p3.pid
        tail3_pid = subprocess.Popen("ps aux | grep -i 'tail -f /var/log/MilliDAQ.log' | pgrep 'tail'", shell = True,stdout = subprocess.PIPE).communicate()[0]
        tail3_pid = int(tail3_pid)
        os.kill(tail3_pid,signal.SIGINT)
        p3.terminate()

        self.finished.emit()
        
class TabWidget(QDialog):
  
    def __init__(self):
        super().__init__()
   
        self.title = 'DAQCommand GUI'
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 800
        self.initUI()
        
        self.tabs  = QTabWidget()
        self.tabs.addTab(daqcommand_tab(),"DAQCommand")
        self.tabs.addTab(configure_tab(),"Configure Maker")
        self.tabs.addTab(trigger_board_tab(),"Tigger board")
        
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
        #self.show()
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        if False and sys.platform.startswith("darwin"):
            QApplication.setStyle(QStyleFactory.create('macintosh'))
            QApplication.setPalette(QApplication.style().standardPalette())
        elif sys.platform.startswith("linux") or sys.platform.startswith("win") or sys.platform.startswith("darwin"):
            darkPalette = QPalette()
            darkPalette.setColor(QPalette.Window, QColor(53,53,53))
            darkPalette.setColor(QPalette.WindowText, Qt.white)
            darkPalette.setColor(QPalette.Base, QColor(25,25,25))
            darkPalette.setColor(QPalette.AlternateBase, QColor(53,53,53))
            darkPalette.setColor(QPalette.ToolTipBase, Qt.darkGray)
            darkPalette.setColor(QPalette.ToolTipText, Qt.white)
            darkPalette.setColor(QPalette.Text, Qt.white)
            darkPalette.setColor(QPalette.Button, QColor(53,53,53))
            darkPalette.setColor(QPalette.ButtonText, Qt.white)
            darkPalette.setColor(QPalette.BrightText, Qt.red)
            darkPalette.setColor(QPalette.Link, QColor(42, 130, 218))
            darkPalette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            darkPalette.setColor(QPalette.HighlightedText, Qt.black)
            darkPalette.setColor(QPalette.Disabled, QPalette.Window, Qt.lightGray)
            darkPalette.setColor(QPalette.Disabled, QPalette.WindowText, Qt.gray)
            darkPalette.setColor(QPalette.Disabled, QPalette.Base, Qt.darkGray)
            darkPalette.setColor(QPalette.Disabled, QPalette.ToolTipBase, Qt.darkGray)
            darkPalette.setColor(QPalette.Disabled, QPalette.ToolTipText, Qt.white)
            darkPalette.setColor(QPalette.Disabled, QPalette.Text, Qt.gray)
            darkPalette.setColor(QPalette.Disabled, QPalette.Button, QColor(73,73,73))
            darkPalette.setColor(QPalette.Disabled, QPalette.ButtonText, Qt.lightGray)
            darkPalette.setColor(QPalette.Disabled, QPalette.BrightText, Qt.lightGray)
            darkPalette.setColor(QPalette.Disabled, QPalette.Highlight, Qt.lightGray)
            darkPalette.setColor(QPalette.Disabled, QPalette.HighlightedText, Qt.gray)
        #self.setStyleSheet("background-color: Dark grey;")
            QApplication.setStyle(QStyleFactory.create('Fusion'))
            QApplication.setPalette(darkPalette)
       
#the mean tab for Runing DAQcommand
class daqcommand_tab(QWidget):
    def __init__(self):
        super().__init__()
        self.contents = []
        self.content_temp = []
        self.onlyfile = []

        self.SetStartButton()
        self.SetStartButton()
        self.SetStopButton()
        self.SetStatusButton()
        self.SetPrintButton()
        self.SetComboPrint()
        self.SetListButton()
        self.Setlabel()
        self.SetCombolist()
        self.SetCombolistButton()
        self.SetTextEdit()
        self.SetqTimer()
        self.Setimage()
        self.SetHelpButton()
        
        self.show()

#set the logo of Milliqan
    def Setimage(self):
        self.label = QLabel(self)
        self.pixmap = QPixmap('/Users/mr-right/physics/research2/MilliQanGUI/MicrosoftTeams-image.png')
		#self.pixmap = QPixmap('Images/MilliQanLogo.png')
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
    def SetCombolistButton(self):
        self.printlistbtn = QPushButton("reconfigure", self)
        self.printlistbtn.move(550,200)
        self.printlistbtn.clicked.connect(self.on_clicled)
        
    def SetCombolist(self):
        self.combolist = QComboBox(self)
        self.combolist.move(450,200)
        self.combolist.addItems([])
        #self.combolist.currentTextChanged.connect(self.updateCombo)
        #self.combolist.currentTextChanged.connect(self.updateCombo)
        self.combolist.currentTextChanged.connect(self.on_combobox_func)
        
    def SetHelpButton(self):
        self.helpbtn = QPushButton("help",self)
        self.helpbtn.move(750, 200)
        self.helpbtn.clicked.connect(self.massage)
        
    def on_combobox_func(self, text):                                                    # +++
        self.current_text  = "DAQCommand reconfigure ../../config/" + text
        
    def on_clicled(self):                                                                # +++
        #subprocess.Popen(self.current_text, shell= True)
        p3 = subprocess.Popen(self.current_text, shell= True)
        time.sleep(5)
        pid3 = p3.pid
        tail3_pid = subprocess.Popen("ps aux | grep -i 'tail -f /var/log/MilliDAQ.log' | pgrep 'tail'", shell = True,stdout = subprocess.PIPE).communicate()[0]
        tail3_pid = int(tail3_pid)
        os.kill(tail3_pid,signal.SIGINT)
        p3.terminate()
    
    def updateCombo(self):
        self.combolist.clear()
        self.combolist.addItems(self.onlyfile)
        
    def SetStartButton(self):
        self.startbtn = QPushButton("start",self)
        self.startbtn.move(150,150)
        self.startbtn.clicked.connect(self.longrun_start)
        
        
    def SetStopButton(self):
        self.stopbtn = QPushButton("Stop",self)
        self.stopbtn.move(300,150)
        self.stopbtn.clicked.connect(self.longrun_stop)
    
    
    def SetStatusButton(self):
        self.statusbtn = QPushButton("status",self)
        self.statusbtn.move(450,150)
        self.statusbtn.clicked.connect(self.longrun_status)
        
    def SetComboPrint(self):
        self.comboprint = QComboBox(self)
        self.comboprint.move(600,150)
        self.comboprint.addItems(["Configure", "Board", "Rate", "Status"])
        
    def SetPrintButton(self):
        self.printbtn = QPushButton("print", self)
        self.printbtn.move(750,150)
        self.printbtn.clicked.connect(self.longrun_print)
    
    def SetListButton(self):
        self.listbtn = QPushButton("list",self)
        self.listbtn.move(250,200)
        self.listbtn.clicked.connect(self.clicked_list)
        
    def SetTextEdit(self):
        self.QTE = QTextEdit(self)
        self.QTE.move(150,250)
        self.QTE.resize(700,400)
		#with open('/var/log/MilliDAQ.log') as f :
        with open('/Users/mr-right/physics/research2/textexample.log') as f :
            self.contents = f.readlines()
        #self.QTE.setObjectName("status information")
        #self.QTE.setPlainText(self.contents)
    
        
    def SetqTimer(self):
        self.qtimer = QTimer()
        self.qtimer.setInterval(1000)
        self.qtimer.timeout.connect(self.refreshText)
        self.qtimer.start()
        
    def refreshText(self):
        self.content_temp = self.contents
        linenumber = len(self.content_temp)
        #with open('/var/log/MilliDAQ.log') as f :
        with open('/Users/mr-right/physics/research2/textexample.log') as f :
            self.contents = f.readlines()

        if self.contents != self.content_temp:
            for i in self.contents[linenumber-1:-1]:
                self.QTE.append(i)
                QCoreApplication.processEvents()
                
    def massage(self):
        self.msg = QMessageBox(self)
        #self.msg.setIcon(QMessageBox.Information)
        self.msg.setText("DAQCommand: \nstart                  -- start the run\n\nstop                   -- stop the run\n\nprint [configuration | board | rates | status]: \nprint configure  -- print the current V1743Configuration parameters: trigger mode, thresholds, etc\n\nprint board      -- print information about the V1743 board: connection, firmware versions, etc\n\nprint rates       -- print DQM information: trigger rates, missed triggers, etc\n\nprint status     -- print DAQ information: state, configuration path, etc\n\nreconfigure <file.xml> -- stop the run, read/apply a new configuration file, then start\n\nYou can use combo box to choose the information you want to print out. \nYou can use the reconfigure button to reconfigure the file we generate. \nIn the end text box will udapate the information about detector in real time")
        
        self.msg.setWindowTitle("This is the help window")
        self.retval = self.msg.exec_()
        
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
        '''
        self.threadstart.finished.connect(
            lambda: self.stepLabel.setText("Long-Running Step: 0")
        )
        '''
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
        '''
        self.threadstop.finished.connect(
            lambda: self.stepLabel.setText("Long-Running Step: 0")
        )
        '''
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
        '''
        self.threadstatus.finished.connect(
            lambda: self.stepLabel.setText("Long-Running Step: 0")
        )
        '''
    
    def longrun_print(self):
    # Create a QThread object
        self.threadprint = QThread()
    # create a worker object
        self.workerprint = worker()
    #Move worker to the thread
        self.workerprint.moveToThread(self.threadprint)
    #Connect signals and slots
        self.threadprint.started.connect(self.workerprint.clicked_print)
        self.workerprint.finished.connect(self.threadprint.quit)
        self.workerprint.finished.connect(self.workerprint.deleteLater)
        self.threadprint.finished.connect(self.threadprint.deleteLater)
    
    # Start the thread
        self.threadprint.start()
    #Final Results
        self.printbtn.setEnabled(False)
        self.threadprint.finished.connect(
            lambda: self.printbtn.setEnabled(True)
        )
    
    def clicked_list(self):
        self.onlyfile =[]
        for filename in glob.glob("../../config/*.py"):
            self.onlyfile.append(filename.split('/')[-1])
            
        for file in self.onlyfile:
            print(filename,'\n')
        
        self.updateCombo()

class configure_tab(QWidget):
	def __init__(self):
		super().__init__()
		self.list_dgtz = []
		self.list_channel = []
		self.list_group = []
		self.Dgtz = "0"
		self.Channel = "0"
		self.Group = "0"
		self.enabletype = "True"
		self.polaritytype = "risingEdge"
		self.textvalue1 = ""
		self.textvalue2 = ""
		self.textvalue3 = ""
		self.triggertype = "software"
		self.triggerlogic = "logicOr"
		self.filename = ""
	
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
	
	def setTitleLabel(self):
		self.label12 = QLabel(self)
		self.label12.setText("Python Configure Maker")
        #self.label.setStyleSheet("border: 1px solid black;")
		self.label12.setFont(QFont("Arial",30))
		self.label12.move(300,20)
		#self.label12.resize(150,50)
        
	def setTextEdit(self):
		self.QTE = QTextEdit(self)
		self.QTE.move(500,100)
		self.QTE.resize(400,500)
        
	def setCombolistDgtz(self):
		self.comboboxdgtz = QComboBox(self)
		self.comboboxdgtz.move(100,150)
		for dgtz in range(len(cfg.Digitizers)):
			self.list_dgtz.append(str(dgtz))
		self.comboboxdgtz.addItems(self.list_dgtz)
		self.comboboxdgtz.currentTextChanged.connect(self.update_dgtz)
		
		self.label8 = QLabel(self)
		self.label8.setText("Digitizers")
		self.label8.move(100,100)
		
	def update_dgtz(self,value):
		#global self.Dgtz
		self.Dgtz = value
	
	def setCombolistchannel(self):
		self.comboboxchannel = QComboBox(self)
		self.comboboxchannel.move(100,250)
		for channel in range(16):
			self.list_channel.append(str(channel))
		self.comboboxchannel.addItems(self.list_channel)
		self.comboboxchannel.currentTextChanged.connect(self.update_channel)
		
		self.label9 = QLabel(self)
		self.label9.setText("Channel")
		self.label9.move(100,200)
		
	def update_channel(self,value):
		#global self.Channel
		self.Channel = value
	
	def setTriggerEnableBtn(self):
		self.label3 = QLabel(self)
		self.label3.setText("triggerEnable")
		self.label3.move(200,250)
	
		self.comboboxtype = QComboBox(self)
		self.comboboxtype.move(310,250)
		self.comboboxtype.addItems(["True","False"])
		self.comboboxtype.currentTextChanged.connect(self.update_triggerenable)
	
	def update_triggerenable(self,value):
		#global self.enabletype
		self.enabletype = value
	
	def setTriggerPolarityBtn(self):
		self.label4 = QLabel(self)
		self.label4.setText("triggerPolarity")
		self.label4.move(200,300)
	
		self.comboboxtype2 = QComboBox(self)
		self.comboboxtype2.move(310,300)
		self.comboboxtype2.addItems(["risingEdge","fallingEdge"])
		self.comboboxtype2.currentTextChanged.connect(self.update_triggerpolarity)
	
	def update_triggerpolarity(self,value):
		#global self.polaritytype
		self.polaritytype = "Channel." + value
	
	def setTriggerThresholdBtn(self):
		self.label4 = QLabel(self)
		self.label4.setText("triggerThreshold")
		self.label4.move(200,350)

		self.textbox1 = QLineEdit(self)
		self.textbox1.move(310,350)
		self.textbox1.resize(100,30)
		#self.textvalue1 = self.textbox1.text()
		#print(self.textvalue1)
	
	
	def setCombolistGroup(self):
		self.comboboxgroup = QComboBox(self)
		self.comboboxgroup.move(100,450)
		for group in range(8):
			self.list_group.append(str(group))
		self.comboboxgroup.addItems(self.list_group)
		self.comboboxgroup.currentTextChanged.connect(self.update_group)

		self.label10 = QLabel(self)
		self.label10.setText("Group")
		self.label10.move(100,400)
		
	def update_group(self,value):
		#global self.Group
		self.Group = value
	
	def setTriggerDelayBtn(self):
		self.label6 = QLabel(self)
		self.label6.setText("TriggerDelay")
		self.label6.move(200,450)

		self.textbox2 = QLineEdit(self)
		self.textbox2.move(300,450)
		self.textbox2.resize(100,30)
		#self.textvalue2 = self.textbox2.text()
	
	def setTriggerTypeBtn(self):
		self.label1 = QLabel(self)
		self.label1.setText("TriggerType")
		self.label1.move(100,550)

		self.comboboxtype3 = QComboBox(self)
		self.comboboxtype3.move(200,550)
		self.comboboxtype3.addItems(["software","normal","auto","external","externalAndNormal","externalOrNormal","none"])
		self.comboboxtype3.currentTextChanged.connect(self.update_triggertype)
	
	def update_triggertype(self,value):
		#global self.triggertype
		self.triggertype = "TriggerType." + value
	
	def setGroupTriggerLogicBtn(self):
		self.label2 = QLabel(self)
		self.label2.setText("GroupTriggerLogic")
		self.label2.move(100,650)
	
		self.comboboxtype4 = QComboBox(self)
		self.comboboxtype4.move(250,650)
		self.comboboxtype4.addItems(["logicOr","logicAnd"])
		self.comboboxtype4.currentTextChanged.connect(self.update_grouptriggerlogic)
	
	def update_grouptriggerlogic(self,value):
		#global self.triggerlogic
		self.triggerlogic = value
	
	def setMaxNumEventsBtn(self):
		self.label7 = QLabel(self)
		self.label7.setText("MaxNumEventsBLT")
		self.label7.move(100,700)
	
		self.textbox3 = QLineEdit(self)
		self.textbox3.move(250,700)
		self.textbox3.resize(100,30)
		#self.textvalue3 = self.textbox3.text()
	
	def setfilename(self):
		self.label11 = QLabel(self)
		self.label11.setText("Please type the file name you want below")
		self.label11.setFont(QFont('Arial',15))
		self.label11.move(500,610)
		
		self.textbox4 = QLineEdit(self)
		self.textbox4.move(500,650)
		self.textbox4.resize(150,30)
		#self.textvalue4 = self.textbox4.text()
	
	def setSavebtn(self):
		self.savebtn = QPushButton("Create",self)
		self.savebtn.move(500,700)
		self.savebtn.clicked.connect(self.save)
		
	def save(self):
		self.textvalue1 = self.textbox1.text()
		self.textvalue2 = self.textbox2.text()
		self.textvalue3 = self.textbox3.text()
		self.textvalue4 = self.textbox4.text() + ".py"
		self.filename = os.path.join("../../config",self.textvalue4)
		self.DGTZ = "cfg.Digitizers["
		go = True
		if os.path.exists(self.filename) :
			self.buttonReply = QMessageBox.question(self,"Message box","This file is already exist do you want to rewrite it",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
			if self.buttonReply == QMessageBox.Yes :
				go = True
			else:
				go = False
				
		if go == True :
			f = open(self.filename,"w+")
			f.write("from Demonstrator import *\n")
			f.write("cfg = Demonstrator()\n")
			f.write("for dgtz in cfg.Digitizers:\n")
			f.write("        dgtz.IRQPolicy.use = False\n")
			f.write("        for iChannel, channel in enumerate(dgtz.channels):\n")
			f.write("        channel.enable = True\n")
			f.write("                channel.triggerEnable = False\n")
			self.text1 = self.DGTZ + self.Dgtz + "].TriggerType.type = " + self.triggertype +"\n"
			f.write(self.text1)
			self.QTE.append(self.text1)
			self.text2 = self.DGTZ + self.Dgtz + "].GroupTriggerLogic.logic = " + self.triggerlogic + "\n"
			f.write(self.text2)
			self.QTE.append(self.text2)
			self.text3 = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerEnable = " + self.enabletype +  "\n"
			f.write(self.text3)
			self.QTE.append(self.text3)
			if self.textvalue1 != "" :
				self.text4 = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerThreshold = " + self.textvalue1 + "\n"
				f.write(self.text4)
				self.QTE.append(self.text4)
			self.text5 = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerPolarity = " + self.polaritytype + "\n"
			f.write(self.text5)
			self.QTE.append(self.text5)
			if self.textvalue2 != "" :
				self.text6 = self.DGTZ + self.Dgtz + "].MaxNumEventsBLT = " + self.textvalue2 + "\n"
				f.write(self.text6)
				self.QTE.append(self.text6)
			if self.textvalue3 != "" :
				self.text7 = self.DGTZ + self.Dgtz + "].groups[" + self.Group + "].triggerDelay = " + self.textvalue3 + "\n"
				f.write(self.text7)
				self.QTE.append(self.text7)
			
			f.close()
		
	def setAppendbtn(self):
		self.appendbtn = QPushButton("append",self)
		self.appendbtn.move(600,700)
		self.appendbtn.clicked.connect(self.appendfile)
		
	def appendfile(self):
		self.DGTZ = "cfg.Digitizers["
		f = open(self.filename,"r+")
		text = f.read()

		self.text1 = self.DGTZ + self.Dgtz + "].TriggerType.type = " + self.triggertype +"\n"
		if self.text1 not in text :
			f.write(self.text1)
			self.QTE.append(self.text1)
		#else :
			#print("ok")
		self.text2 = self.DGTZ + self.Dgtz + "].GroupTriggerLogic.logic = " + self.triggerlogic + "\n"
		if self.text2 not in text :
			f.write(self.text2)
			self.QTE.append(self.text2)
		self.text3 = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerEnable = " + self.enabletype +  "\n"
		if self.text3 not in text :
			f.write(self.text3)
			self.QTE.append(self.text3)
		if self.textvalue1 != "" :
			self.text4 = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerThreshold = " + self.textvalue1 + "\n"
			if self.text4 not in text :
				f.write(self.text4)
				self.QTE.append(self.text4)
		self.text5 = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerPolarity = " + self.polaritytype + "\n"
		if self.text5 not in text :
			f.write(self.text5)
			self.QTE.append(self.text5)
		if self.textvalue2 != "" :
			self.text6 = self.DGTZ + self.Dgtz + "].MaxNumEventsBLT = " + self.textvalue2 + "\n"
			if self.text6 not in text :
				f.write(self.text6)
				self.QTE.append(self.text6)
		if self.textvalue3 != "" :
			self.text7 = self.DGTZ + self.Dgtz + "].groups[" + self.Group + "].triggerDelay = " + self.textvalue3 + "\n"
			if self.text7 not in text :
				f.write(self.text7)
				self.QTE.append(self.text7)
		f.close()

	def SetHelpButton(self):
		self.helpbtn = QPushButton("help",self)
		self.helpbtn.move(200, 100)
		self.helpbtn.clicked.connect(self.massage)
        
	def massage(self):
		self.msg = QMessageBox(self)
        #self.msg.setIcon(QMessageBox.Information)
		self.msg.setText("This tab is using for creating configure file for MiliQan detector.\nYou can create a new file with the name you want by click create.\nWhen you want to add other digitizer or channel or group just modify the information and click append.")
        
		self.msg.setWindowTitle("This is the help window")
		self.retval = self.msg.exec_()
if __name__ == '__main__':
	app = QApplication(sys.argv)
	tabwidget = TabWidget()
	tabwidget.show()
	sys.exit(app.exec_())
