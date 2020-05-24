# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SilentAlarmWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from .pin_util import pin_authorization


class Ui_SilentAlarmWidget(object):

    def __init__(self, ctx):
        self.ctx = ctx

    def _ok_click(self):
        pin_authorization(self.ctx, self.__on_pin_auth)

    def __on_pin_auth(self, result):
        print(f'Pin Auth for Silent Alarm: {result}')

        if result:
            print('Notifying central office')

        self.__window.close()

    def setupUi(self, SilentAlarmWidget):
        self.__window = SilentAlarmWidget
        SilentAlarmWidget.setObjectName("SilentAlarmWidget")
        SilentAlarmWidget.resize(209, 120)
        self.label = QtWidgets.QLabel(SilentAlarmWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(SilentAlarmWidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 10, 111, 70))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.OKButton = QtWidgets.QPushButton(SilentAlarmWidget)
        self.OKButton.setGeometry(QtCore.QRect(120, 90, 80, 23))
        self.OKButton.setObjectName("OKButton")
        self.CancelButton = QtWidgets.QPushButton(SilentAlarmWidget)
        self.CancelButton.setGeometry(QtCore.QRect(30, 90, 80, 23))
        self.CancelButton.setObjectName("CancelButton")

        # click listeners
        self.OKButton.clicked.connect(self._ok_click)

        self.retranslateUi(SilentAlarmWidget)
        QtCore.QMetaObject.connectSlotsByName(SilentAlarmWidget)

    def retranslateUi(self, SilentAlarmWidget):
        _translate = QtCore.QCoreApplication.translate
        SilentAlarmWidget.setWindowTitle(_translate("SilentAlarmWidget", "Silent Alarm"))
        self.label.setText(_translate("SilentAlarmWidget", "Description:"))
        self.OKButton.setText(_translate("SilentAlarmWidget", "Alarm"))
        self.CancelButton.setText(_translate("SilentAlarmWidget", "Cancel"))

    @staticmethod
    def fillDescription(text):
        print(text)
        return True