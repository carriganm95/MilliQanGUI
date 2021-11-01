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

logging.basicConfig(format = "%(message)s",level = logging.INFO)

class worker(QObject):
    def __init__(self):
        super().__init__()
        
        self.p = None


    finished = pyqtSignal()

    def clicked_start(self):
        print("DAQCommand start")
        p = subprocess.Popen("DAQCommand start", shell=True)
        time.sleep(5)
        pid = p.pid
        tail_pid = subprocess.Popen("ps aux | grep -i 'tail -f /var/log/MilliDAQ.log' | pgrep 'tail'", shell=True, stdout=subprocess.PIPE).communicate()[0]
        tail_pid = int(tail_pid)
        print("Tail PID:", tail_pid)
        print("Process PID %d" % (pid))
        os.kill(tail_pid, signal.SIGINT)
        p.terminate()
        self.finished.emit()

    
    def clicked_status(self):
        p1 = subprocess.Popen("DAQCommand status", shell= True)
        time.sleep(5)
        pid1 = p1.pid
        tail1_pid = subprocess.Popen("ps aux | grep -i 'tail -f /var/log/MilliDAQ.log' | pgrep 'tail'", shell = True,stdout = subprocess.PIPE).communicate()[0]
        tail1_pid = int(tail1_pid)
        print("tail pid", tail1_pid)
        os.kill(tail1_pid,signal.SIGINT)
        p1.terminate()
        self.finished.emit()
                
    def clicked_stop(self):
        print("DAQCommand stop")
        #subprocess.popen("DAQCommand stop")
        p2 = subprocess.Popen("DAQCommand stop", shell= True)
        time.sleep(5)
        pid2 = p2.pid
        tail2_pid = subprocess.Popen("ps aux | grep -i 'tail -f /var/log/MilliDAQ.log' | pgrep 'tail'", shell = True,stdout = subprocess.PIPE).communicate()[0]
        tail2_pid = int(tail2_pid)
        print("tail pid", tail2_pid)
        os.kill(tail2_pid,signal.SIGINT)
        p2.terminate()

        self.finished.emit()
        
    def clicked_print(self):
        print("DAQCommand print")
        p3 = subprocess.Popen("DAQCommand print", shell= True)
        time.sleep(5)
        pid3 = p3.pid
        tail3_pid = subprocess.Popen("ps aux | grep -i 'tail -f /var/log/MilliDAQ.log' | pgrep 'tail'", shell = True,stdout = subprocess.PIPE).communicate()[0]
        tail3_pid = int(tail3_pid)
        print("tail pid", tail3_pid)
        os.kill(tail3_pid,signal.SIGINT)
        p3.terminate()

        self.finished.emit()
        

class gui(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        #set name and size
        self.setWindowTitle("DAQCommand Window")
        self.title = 'DAQCommand GUI'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 300
        self.initUI()
        
        #set the button
        self.SetStartButton()
        self.SetStopButton()
        self.SetStatusButton()
        self.SetPrintButton()
        self.SetComboPrint()
        self.SetListButton()
        self.Setlabel()
        
        self.show()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        
    def Setlabel(self):
        self.label = QLabel(self)
        self.label.setText("Button to operate the DAQCommand")
        self.label.adjustSize()
        self.label.move(200,50)
        
    
        
    def SetComboPrint(self):
        self.comboprint = QComboBox(self)
        self.comboprint.move(350,150)
        self.comboprint.addItems(["Configure", "Board", "Rate", "Status"])
        
    # To connect a combo box use: combo.activated[str].connect(self.onChanged)
        
    def SetStartButton(self):
        self.startbtn = QPushButton("start",self)
        self.startbtn.move(50,150)
        self.startbtn.clicked.connect(self.longrun_start)
        
        
    def SetStopButton(self):
        self.stopbtn = QPushButton("Stop",self)
        self.stopbtn.move(150,150)
        self.stopbtn.clicked.connect(self.longrun_stop)
    
    
    
    def SetStatusButton(self):
        self.statusbtn = QPushButton("status",self)
        self.statusbtn.move(250,150)
        self.statusbtn.clicked.connect(self.longrun_status)
        
    def SetPrintButton(self):
        self.printbtn = QPushButton("print", self)
        self.printbtn.move(450,150)
        self.printbtn.clicked.connect(self.longrun_print)
    '''
    def SetListButton(self):
        self.listbtn = QPushButton("list",self)
        self.listbtn.move(150,250)
        self.listbtn.clicked.connect(self.clicked_list)
    '''
    
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
        '''
        self.threadprint.finished.connect(
            lambda: self.stepLabel.setText("Long-Running Step: 0")
            )
            '''
    '''
    def clicked_start(self):
        print("DAQCommand start")
        
    def clicked_status(self):
        alert = QMessageBox()
        alert.setText("gooo")
        alert.exec()
        
    def clicked_stop(self):
        print("DAQCommand stop")
    
    def clicked_print(self):
        print("DAQCommand print")
    
    '''
    def clicked_list(self):
        onlyfile = []
        for file in glob.glob("*.py"):
            onlyfile.append(file)
            
        for file in onlyfile:
            print(file,'\n')
          
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = gui()
    sys.exit(app.exec_())
    
        
