# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Name_Game = QtWidgets.QLabel(self.centralwidget)
        self.Name_Game.setEnabled(False)
        self.Name_Game.setGeometry(QtCore.QRect(210, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Name_Game.setFont(font)
        self.Name_Game.setTextFormat(QtCore.Qt.PlainText)
        self.Name_Game.setObjectName("Name_Game")
        self.B_Start_Game = QtWidgets.QPushButton(self.centralwidget)
        self.B_Start_Game.setEnabled(False)
        self.B_Start_Game.setGeometry(QtCore.QRect(60, 172, 151, 111))
        self.B_Start_Game.setObjectName("B_Start_Game")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setEnabled(False)
        self.graphicsView.setVisible(False)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #MainWindow.



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lvl = 0
    def Load(self):
        self.Name_Game.setEnabled(True)
        self.B_Start_Game.setEnabled(True)

    def Edit(self):
        self.Name_Game.setVisible(False)
        self.B_Start_Game.setVisible(False)
        self.graphicsView.setVisible(False)
        if self.lvl == 0:
            self.Name_Game.setVisible((True))
            self.B_Start_Game.setVisible((True))
        #if self.lvl == 1:
            #self.graphicsView.setVisible((True))




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Name_Game.setText(_translate("MainWindow", "Agario"))
        self.B_Start_Game.setText(_translate("MainWindow", "Играть!!!"))

