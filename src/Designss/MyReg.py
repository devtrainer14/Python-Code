'''
Created on Jun 3, 2019

@author: sipika
'''
from PyQt5 import QtWidgets
 
from .Reg import Ui_MainWindow  # importing our generated file
 
import sys
class mywindow(QtWidgets.QMainWindow):
 
    def __init__(self):
 
        super(mywindow, self).__init__()
 
        self.ui = Ui_MainWindow()
    
        self.ui.setupUi(self)
      
app = QtWidgets.QApplication([])
 

 
sys.exit(app.exec())