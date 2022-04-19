#!/user/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#from MilliDAQ.python.Demonstrator import *
from TriggerBoardTab import *
from DAQCommandTab import *
from ConfigurationFileTab import *
from Demonstrator import *
from MatchFigureTab import *
import sys
import logging
import subprocess
import os
import signal
import time
import glob
import select
import os.path


#main function for the QUI
class TabWidget(QDialog):
  
    def __init__(self):
        super().__init__()
		
		#define the main windows for GUI
        self.title = 'DAQCommand GUI'
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 800
        self.initUI()
        
        #add tabs to the GUI
        self.tabs  = QTabWidget()
        self.tabs.addTab(daqcommand_tab(),"DAQCommand")
        self.tabs.addTab(configure_tab(),"Configuration File Maker")
        self.tabs.addTab(trigger_board_tab(),"Tigger board")
        self.tabs.addTab(checking_match_tab(),"Match Figure")
        
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        
        #self.show()
	#set up the general look of the QUI
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #set the windows to black style
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

#main function to run the GUI
if __name__ == '__main__':
	app = QApplication(sys.argv)
	tabwidget = TabWidget()
	tabwidget.show()
	sys.exit(app.exec_())
