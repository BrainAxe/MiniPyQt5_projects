# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'natGeo.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import downloadPic


class natGeoWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(440, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.urlLabel = QtWidgets.QLabel(self.centralwidget)
        self.urlLabel.setGeometry(QtCore.QRect(160, 30, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.urlLabel.setFont(font)
        self.urlLabel.setObjectName("urlLabel")
        self.lineurl = QtWidgets.QLineEdit(self.centralwidget)
        self.lineurl.setGeometry(QtCore.QRect(40, 90, 361, 29))
        self.lineurl.setObjectName("lineurl")
        self.DownloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.DownloadButton.setGeometry(QtCore.QRect(50, 180, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.DownloadButton.setFont(font)
        self.DownloadButton.setObjectName("DownloadButton")
        self.DownloadButton.clicked.connect(self.imgDownload)
        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(260, 180, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ClearButton.setFont(font)
        self.ClearButton.setObjectName("ClearButton")
        self.ClearButton.clicked.connect(self.fclear)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(self.exitApp)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        #self.setFixedSize(self.layout.sizeHint())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    
    def exitApp(self):
        exit()
    

    def imgDownload(self):
        url = self.lineurl.text()
        result = downloadPic.download_wallpaper(url)
        self.statusbar.showMessage(result,5000)

    def fclear(self):
        self.lineurl.clear()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.urlLabel.setText(_translate("MainWindow", "Enter URL"))
        self.DownloadButton.setText(_translate("MainWindow", "Download"))
        self.ClearButton.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

