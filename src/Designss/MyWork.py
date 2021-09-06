from PyQt5 import QtWidgets
 
from Designss.mydesign import Ui_MainWindow  # importing our generated file
 
import sys
from Designss import MyReg
class mywindow(QtWidgets.QMainWindow):
 
	def __init__(self):
 
		super(mywindow, self).__init__()
 
		self.ui = Ui_MainWindow()
    
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.btnClicked)
	
	def btnClicked(self):
		self.ui.label.setText("Button Clicked")
		application = MyReg.mywindow()
		application.show()
 

app = QtWidgets.QApplication([])
 
application = mywindow()
 
application.show()
 
sys.exit(app.exec())