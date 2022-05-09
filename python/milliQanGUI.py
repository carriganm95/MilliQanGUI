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
		#self.loggedIn = False
		self.initUI()
		#self.Login()
		
		#add tabs to the GUI
		self.tabs  = QTabWidget()
		self.tabs.addTab(daqcommand_tab(),"DAQCommand")
		self.tabs.addTab(configure_tab(),"Configuration File Maker")
		self.tabs.addTab(trigger_board_tab(),"Tigger board")
		self.tabs.addTab(checking_match_tab(),"Match Figure")
		
		self.layout = QVBoxLayout(self)
		self.layout.addWidget(self.tabs)
		self.setLayout(self.layout)
		
	#set up the general look of the GUI
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

	#def Login(self):
	#	form = LoginForm()
	#	form.show()

class LoginForm(QWidget):

	loggedSignal = pyqtSignal()
	loggedAdminSignal = pyqtSignal()
	GLOBAL_STATE = True

	def __init__(self):
		super().__init__()
		self.setWindowTitle('Login Form')
		self.resize(500, 120)
		self.show()		

		layout = QGridLayout()

		label_name = QLabel('<font size="4"> Username </font>')
		self.lineEdit_username = QLineEdit()
		self.lineEdit_username.setPlaceholderText('Please enter your username')
		layout.addWidget(label_name, 0, 0)
		layout.addWidget(self.lineEdit_username, 0, 1)

		label_password = QLabel('<font size="4"> Password </font>')
		self.lineEdit_password = QLineEdit()
		self.lineEdit_password.setPlaceholderText('Please enter your password')
		layout.addWidget(label_password, 1, 0)
		layout.addWidget(self.lineEdit_password, 1, 1)

		button_login = QPushButton('Login')
		button_login.clicked.connect(self.check_password)
		layout.addWidget(button_login, 2, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)
		button_login.clicked.connect(self.close)


		self.setLayout(layout)

	def check_password(self):
		msg = QMessageBox()

		if self.lineEdit_username.text() == 'Username' and self.lineEdit_password.text() == '000':
			msg.setText('Success')
			msg.exec_()
			self.loggedSignal.emit()
		elif self.lineEdit_username.text() == 'Admin' and self.lineEdit_password.text() == '111':
			msg.setText('Success')
			msg.exec_()
			self.loggedAdminSignal.emit()
		else:
			msg.setText('Incorrect Password')
			msg.exec_()
		
		#return self.accepted


#main function to run the GUI
if __name__ == '__main__':

	app = QApplication(sys.argv)
	login = LoginForm()
	tabwidget = TabWidget()
	login.loggedSignal.connect(tabwidget.showMaximized)
	login.loggedAdminSignal.connect(tabwidget.showMaximized)
	#tabwidget.show()
	sys.exit(app.exec_())

	#form = LoginForm()
	#form.show()

	#if(form.accepted):
	#	tabwidget = TabWidget()
	#	tabwidget.show()
	#sys.exit(app.exec_())
