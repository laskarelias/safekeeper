<<<<<<< HEAD
=======
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IncidentReportWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!
>>>>>>> c20687d4e68f6506f00e80ee167a2b806a537998
from PyQt5 import QtCore, QtGui, QtWidgets
from domain import SecurityIncident, CentralOffice, AccessLog
from .pin_util import pin_authorization

class Ui_IncidentReportWindow(object):

    def __init__(self, ctx):
        self.ctx = ctx

    def fillInDetails(self, timestamp=None, type=None, description=None, image=None):
        # begin sequence implementation here
        # todo
        if timestamp is None:
            timestamp = str(self.TimestampText.text())
            #if len(timestamp) == 0:
                #timestamp = time.now()
        
        # continue for others...
        incident = SecurityIncident()
        self.incident = incident
        #incident.fillInDetails(...)

        self.pinAuthorization()

    def pinAuthorization(self):
        pin_authorization(self.ctx, self._pinCallback)

    def _pinCallback(self, result):
        if result:
            # todo: show main menu
            AccessLog.writeIncidentToAccessLogs(self.incident)
        else:
            CentralOffice.sendReport(self.incident)
            AccessLog.writeIncidentToAccessLogs(self.incident)
            #todo: show popup

    def setupUi(self, IncidentReportWindow):
        IncidentReportWindow.setObjectName("IncidentReportWindow")
        IncidentReportWindow.resize(457, 177)
        self.centralwidget = QtWidgets.QWidget(IncidentReportWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.OKButton = QtWidgets.QPushButton(self.centralwidget)
        self.OKButton.setGeometry(QtCore.QRect(150, 150, 80, 21))
        self.OKButton.setObjectName("OKButton")
        self.TimestampText = QtWidgets.QLabel(self.centralwidget)
        self.TimestampText.setGeometry(QtCore.QRect(250, 0, 201, 31))
        self.TimestampText.setObjectName("TimestampText")
        self.IncidentTypeText = QtWidgets.QLabel(self.centralwidget)
        self.IncidentTypeText.setGeometry(QtCore.QRect(50, 30, 41, 21))
        self.IncidentTypeText.setObjectName("IncidentTypeText")
        self.IncidentTypeInput = QtWidgets.QLineEdit(self.centralwidget)
        self.IncidentTypeInput.setGeometry(QtCore.QRect(90, 30, 141, 23))
        self.IncidentTypeInput.setObjectName("IncidentTypeInput")
        self.DescriptionText = QtWidgets.QLabel(self.centralwidget)
        self.DescriptionText.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.DescriptionText.setObjectName("DescriptionText")
        self.DescriptionInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.DescriptionInput.setGeometry(QtCore.QRect(90, 60, 141, 81))
        self.DescriptionInput.setObjectName("DescriptionInput")
        self.ImageGraphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.ImageGraphicsView.setGeometry(QtCore.QRect(240, 30, 211, 141))
        self.ImageGraphicsView.setObjectName("ImageGraphicsView")
        IncidentReportWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(IncidentReportWindow)
        QtCore.QMetaObject.connectSlotsByName(IncidentReportWindow)

    def retranslateUi(self, IncidentReportWindow):
        _translate = QtCore.QCoreApplication.translate
        IncidentReportWindow.setWindowTitle(_translate("IncidentReportWindow", "Incident Report"))
        self.OKButton.setText(_translate("IncidentReportWindow", "Send"))
        self.TimestampText.setText(_translate("IncidentReportWindow", "Incident Time: DD/MM/YY HH:MM"))
        self.IncidentTypeText.setText(_translate("IncidentReportWindow", "Type:"))
        self.DescriptionText.setText(_translate("IncidentReportWindow", "Description:"))
