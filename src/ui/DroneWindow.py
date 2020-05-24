# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DroneWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DroneWindow(object):

    def __init__(self, ctx):
        self.ctx = ctx

    def setupUi(self, DroneWindow):
        DroneWindow.setObjectName("DroneWindow")
        DroneWindow.resize(532, 328)
        self.centralwidget = QtWidgets.QWidget(DroneWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CurrentSectorLabel = QtWidgets.QLabel(self.centralwidget)
        self.CurrentSectorLabel.setGeometry(QtCore.QRect(160, 300, 181, 21))
        self.CurrentSectorLabel.setObjectName("CurrentSectorLabel")
        self.CheckSectorLabel = QtWidgets.QLabel(self.centralwidget)
        self.CheckSectorLabel.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.CheckSectorLabel.setObjectName("CheckSectorLabel")
        self.CheckSectorInput = QtWidgets.QLineEdit(self.centralwidget)
        self.CheckSectorInput.setGeometry(QtCore.QRect(10, 30, 101, 23))
        self.CheckSectorInput.setObjectName("CheckSectorInput")
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(440, 300, 80, 23))
        self.CloseButton.setObjectName("CloseButton")
        self.RecallDroneButton = QtWidgets.QPushButton(self.centralwidget)
        self.RecallDroneButton.setGeometry(QtCore.QRect(10, 80, 91, 23))
        self.RecallDroneButton.setObjectName("RecallDroneButton")
        self.CheckSectorOKButton = QtWidgets.QPushButton(self.centralwidget)
        self.CheckSectorOKButton.setGeometry(QtCore.QRect(110, 30, 31, 23))
        self.CheckSectorOKButton.setObjectName("CheckSectorOKButton")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(160, 10, 361, 281))
        self.graphicsView.setObjectName("graphicsView")
        DroneWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DroneWindow)
        QtCore.QMetaObject.connectSlotsByName(DroneWindow)

    def retranslateUi(self, DroneWindow):
        _translate = QtCore.QCoreApplication.translate
        DroneWindow.setWindowTitle(_translate("DroneWindow", "Drone Control"))
        self.CurrentSectorLabel.setText(_translate("DroneWindow", "Currently Checking: SECTOR"))
        self.CheckSectorLabel.setText(_translate("DroneWindow", "Check Sector:"))
        self.CloseButton.setText(_translate("DroneWindow", "Close"))
        self.RecallDroneButton.setText(_translate("DroneWindow", "Recall Drone"))
        self.CheckSectorOKButton.setText(_translate("DroneWindow", "Go"))


    @staticmethod
    def chooseSector():
        sector = random.rand()
        print("Selected sector: ", sector)

    @staticmethod
    def chooseRecall():
        recall = random.rand()
        if recall < 100:
            print("recalling drone")
        else:
            print("no need to recall")