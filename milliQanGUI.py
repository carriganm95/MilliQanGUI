#!/user/bin/env python3

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
        

    '''
    def readfile(self):
        self.QTE = QTextEdit(self)
        self.QTE.move(50,350)
        self.QTE.resize(500,300)
        f = open('/Users/mr-right/physics/research2/textexample.log')
        while f :
            contents = f.read()
        self.QTE.setPlainText(contents)
        self.finished.emit()
    '''

class gui(QMainWindow):
  
    def __init__(self):
        super().__init__()
        
        self.contents = []
        self.content_temp = []
        #set name and size
        #self.setWindowTitle("DAQCommand Window")
        self.title = 'DAQCommand GUI'
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 800
        self.initUI()
        self.onlyfile = []
        #set the button
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
    
        
    def SetComboPrint(self):
        self.comboprint = QComboBox(self)
        self.comboprint.move(450,150)
        self.comboprint.addItems(["Configure", "Board", "Rate", "Status"])
        
    # To connect a combo box use: combo.activated[str].connect(self.onChanged)
    def SetCombolistButton(self):
        self.printlistbtn = QPushButton("reconfigure", self)
        self.printlistbtn.move(550,250)
        self.printlistbtn.clicked.connect(self.on_clicled)
        
    def SetCombolist(self):
        self.combolist = QComboBox(self)
        self.combolist.move(450,250)
        self.combolist.addItems([])
        #self.combolist.currentTextChanged.connect(self.updateCombo)
        #self.combolist.currentTextChanged.connect(self.updateCombo)
        self.combolist.currentTextChanged.connect(self.on_combobox_func)
        
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
        
    def SetHelpButton(self):
        self.helpbtn = QPushButton("help",self)
        self.helpbtn.move(650, 250)
        self.helpbtn.clicked.connect(self.massage)
        
    def SetStartButton(self):
        self.startbtn = QPushButton("start",self)
        self.startbtn.move(150,150)
        self.startbtn.clicked.connect(self.longrun_start)
        
        
    def SetStopButton(self):
        self.stopbtn = QPushButton("Stop",self)
        self.stopbtn.move(250,150)
        self.stopbtn.clicked.connect(self.longrun_stop)
    
    
    
    def SetStatusButton(self):
        self.statusbtn = QPushButton("status",self)
        self.statusbtn.move(350,150)
        self.statusbtn.clicked.connect(self.longrun_status)
        
    def SetPrintButton(self):
        self.printbtn = QPushButton("print", self)
        self.printbtn.move(550,150)
        self.printbtn.clicked.connect(self.longrun_print)
    
    def SetListButton(self):
        self.listbtn = QPushButton("list",self)
        self.listbtn.move(250,250)
        self.listbtn.clicked.connect(self.clicked_list)
        
    def SetTextEdit(self):
        self.QTE = QTextEdit(self)
        self.QTE.move(150,350)
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

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = gui()
    sys.exit(app.exec_())
    
        
