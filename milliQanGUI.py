#!/user/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from MilliDAQ.python.Demonstrator import *
import sys
import logging
import subprocess
import os
import signal
import time
import glob
import select

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
        self.tabs.addTab(tab1(),"Tab 1")
        self.tabs.addTab(tab2(),"Tab 2")
        
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
            
class tab1(QWidget):
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

    def Setimage(self):
        self.label = QLabel(self)
        self.pixmap = QPixmap('/Users/mr-right/physics/research2/MilliQanGUI/MicrosoftTeams-image.png')
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
        with open('/var/log/MilliDAQ.log') as f :
        #with open('/Users/mr-right/physics/research2/textexample.log') as f :
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
        with open('/var/log/MilliDAQ.log') as f :
        #with open('/Users/mr-right/physics/research2/textexample.log') as f :
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

class tab2(QWidget):
	def __init__(self):
		super().__init__()
		self.list1 = []
		self.list2 = []
		self.list3 = []
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
	
		self.setCombolistDgtz()
		self.setCombolistchannel()
		self.setCombolistGroup()
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
		self.setcomboboxtype1()
		self.setcomboboxtype2()
		self.setcomboboxtype3()
		self.setcomboboxtype4()
		self.settextbox1()
		self.settextbox2()
		self.settextbox3()
		self.setsave()
		self.setappend()
	
	def setCombolistDgtz(self):
		self.comboboxdgtz = QComboBox(self)
		self.comboboxdgtz.move(100,100)
		for dgtz in range(len(cfg.Digitizers)):
			self.list1.append(str(dgtz))
		self.comboboxdgtz.addItems(self.list1)
		self.comboboxdgtz.currentTextChanged.connect(self.update1)
		
	def setlabel8(self):
		self.label8 = QLabel(self)
		self.label8.setText("Digitizers")
		self.label8.move(100,50)
		
	def update1(self,value):
		#global self.Dgtz
		self.Dgtz = value
	
	def setCombolistchannel(self):
		self.comboboxchannel = QComboBox(self)
		self.comboboxchannel.move(100,200)
		for channel in range(16):
			self.list2.append(str(channel))
		self.comboboxchannel.addItems(self.list2)
		self.comboboxchannel.currentTextChanged.connect(self.update2)
		
	def setlabel9(self):
		self.label9 = QLabel(self)
		self.label9.setText("Channel")
		self.label9.move(100,150)
		
	def update2(self,value):
		#global self.Channel
		self.Channel = value
	
	def setlabel3(self):
		self.label3 = QLabel(self)
		self.label3.setText("triggerEnable")
		self.label3.move(200,200)
	
	def setcomboboxtype1(self):
		self.comboboxtype = QComboBox(self)
		self.comboboxtype.move(310,200)
		self.comboboxtype.addItems(["True","False"])
		self.comboboxtype.currentTextChanged.connect(self.update4)
	
	def update4(self,value):
		#global self.enabletype
		self.enabletype = value
	
	def setlabel4(self):
		self.label4 = QLabel(self)
		self.label4.setText("triggerPolarity")
		self.label4.move(200,250)
	
	def setcomboboxtype2(self):
		self.comboboxtype2 = QComboBox(self)
		self.comboboxtype2.move(310,250)
		self.comboboxtype2.addItems(["risingEdge","fallingEdge"])
		self.comboboxtype2.currentTextChanged.connect(self.update5)
	
	def update5(self,value):
		#global self.polaritytype
		self.polaritytype = "Channel." + value
	
	def setlabel5(self):
		self.label4 = QLabel(self)
		self.label4.setText("triggerThreshold")
		self.label4.move(200,300)
	
	def settextbox1(self):
		self.textbox1 = QLineEdit(self)
		self.textbox1.move(310,300)
		self.textbox1.resize(100,40)
		self.textvalue1 = self.textbox1.text()
	
	
	def setCombolistGroup(self):
		self.comboboxgroup = QComboBox(self)
		self.comboboxgroup.move(100,400)
		for group in range(8):
			self.list3.append(str(group))
		self.comboboxgroup.addItems(self.list3)
		self.comboboxgroup.currentTextChanged.connect(self.update3)
	
	def setlabel10(self):
		self.label10 = QLabel(self)
		self.label10.setText("Group")
		self.label10.move(100,350)
		
	def update3(self,value):
		#global self.Group
		self.Group = value
	
	def setlabel6(self):
		self.label6 = QLabel(self)
		self.label6.setText("TriggerDelay")
		self.label6.move(200,400)
	
	def settextbox2(self):
		self.textbox2 = QLineEdit(self)
		self.textbox2.move(300,400)
		self.textbox2.resize(100,40)
		self.textvalue2 = self.textbox2.text()
	
	def setlabel1(self):
		self.label1 = QLabel(self)
		self.label1.setText("TriggerType")
		self.label1.move(100,500)
	
	def setcomboboxtype3(self):
		self.comboboxtype3 = QComboBox(self)
		self.comboboxtype3.move(200,500)
		self.comboboxtype3.addItems(["software","normal","auto","external","externalAndNormal","externalOrNormal","none"])
		self.comboboxtype3.currentTextChanged.connect(self.update6)
	
	def update6(self,value):
		#global self.triggertype
		self.triggertype = "TriggerType." + value
	
	def setlabel2(self):
		self.label2 = QLabel(self)
		self.label2.setText("GroupTriggerLogic")
		self.label2.move(100,600)
	
	def setcomboboxtype4(self):
		self.comboboxtype4 = QComboBox(self)
		self.comboboxtype4.move(200,600)
		self.comboboxtype4.addItems(["logicOr","logicAnd"])
		self.comboboxtype4.currentTextChanged.connect(self.update7)
	
	def update7(self,value):
		#global self.triggerlogic
		self.triggerlogic = value
	
	def setlabel7(self):
		self.label7 = QLabel(self)
		self.label7.setText("MaxNumEventsBLT")
		self.label7.move(100,700)
	
	def settextbox3(self):
		self.textbox3 = QLineEdit(self)
		self.textbox3.move(250,700)
		self.textbox3.resize(100,40)
		self.textvalue3 = self.textbox3.text()
	
	def setsave(self):
		self.savebtn = QPushButton("save",self)
		self.savebtn.move(500,400)
		self.savebtn.clicked.connect(self.save)
		
	def save(self):
		self.DGTZ = "cfg.Digitizers["
		f = open("test_board.py","w+")
		f.write("from Demonstrator import *\r\n")
		f.write("cfg = Demonstrator()\r\n")
		f.write("for dgtz in cfg.Digitizers:\r\n")
		f.write("        dgtz.IRQPolicy.use = False\r\n")
		f.write("        for iChannel, channel in enumerate(dgtz.channels):\r\n")
		f.write("        channel.enable = True\r\n")
		f.write("                channel.triggerEnable = False\r\n")
		self.text1 = self.DGTZ + self.Dgtz + "].TriggerType.type = " + self.triggertype +"\r\n"
		f.write(self.text1)
		self.text2 = self.DGTZ + self.Dgtz + "].GroupTriggerLogic.logic = " + self.triggerlogic + "\r\n"
		f.write(self.text2)
		self.text3 = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerEnable = " + self.enabletype +  "\r\n"
		f.write(self.text3)
		self.text4 = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerThreshold = " + self.textvalue1 + "\r\n"
		f.write(self.text4)
		self.text4 = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerPolarity = " + self.polaritytype + "\r\n"
		f.close()
		
	def setappend(self):
		self.appendbtn = QPushButton("append",self)
		self.appendbtn.move(500,500)
		self.appendbtn.clicked.connect(self.appendfile)
		
	def appendfile(self):
		self.DGTZ = "cfg.Digitizers["
		f = open("test_board.py","a")
		self.text1 = self.DGTZ + self.Dgtz + "].TriggerType.type = " + self.triggertype +"\r\n"
		f.write(self.text1)
		self.text2 = self.DGTZ + self.Dgtz + "].GroupTriggerLogic.logic = " + self.triggerlogic + "\r\n"
		f.write(self.text2)
		self.text3 = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerEnable = " + self.enabletype +  "\r\n"
		f.write(self.text3)
		self.text4 = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerThreshold = " + self.textvalue1 + "\r\n"
		f.write(self.text4)
		self.text4 = self.DGTZ + self.Dgtz + "].channels[" + self.Channel + "].triggerPolarity = " + self.polaritytype + "\r\n"
		f.close()

		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	tabwidget = TabWidget()
	tabwidget.show()
	sys.exit(app.exec_())
