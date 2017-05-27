import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from natGeo import natGeoWindow


class MainScreen(QMainWindow):
	
	def __init__(self):
		super(MainScreen, self).__init__()
		self.ui = natGeoWindow()
		self.ui.setupUi(self)
		
app = QApplication(sys.argv)
myapp = MainScreen()
myapp.setWindowTitle("NatGeo Picture Downloader")
myapp.show()
sys.exit(app.exec_())