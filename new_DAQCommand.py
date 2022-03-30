from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#from MilliDAQ.python.Demonstrator import *
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


def btn(self, name,x,y,connect):
	btnnew = QPushButton(name,self)
	btnnew.move(x,y)
	btnnew.clicked.connect(connect)
	
def btn_size(self,name,x,y,connect,x1,y1):
	newbtn = QPushButton(name,self)
	newbtn.resize(x1,y1)
	newbtn.move(x,y)
	newbtn.clicked.connect(connect)
	
def setlabel(self, text,x,y):
	label = QLabel(self)
	label.setText(text)
	#label.setFont(QFont('Arial',30))
	label.move(x,y)
	label.adjustSize()
'''
class daqcommand_tab(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
		btn(self, "good",100,100,self.on_click)
		
		self.show()
	def initUI(self):
		self.setWindowTitle("buttton")
		self.setGeometry(10,10,300,300)
		
	def on_click(self):
		print('work')
		
if __name__=='__main__':
	app = QApplication(sys.argv)
	ex = daqcommand_tab()
	sys.exit(app.exec_())
'''
	
