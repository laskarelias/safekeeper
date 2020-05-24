# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeleteUserWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteUserWidget(object):

    def __init__(self, ctx):
        self.ctx = ctx

    def setupUi(self, DeleteUserWidget):
        DeleteUserWidget.setObjectName("DeleteUserWidget")
        DeleteUserWidget.resize(289, 231)
        self.DeleteButton = QtWidgets.QPushButton(DeleteUserWidget)
        self.DeleteButton.setGeometry(QtCore.QRect(200, 200, 75, 23))
        self.DeleteButton.setObjectName("DeleteButton")
        self.NotesText = QtWidgets.QLabel(DeleteUserWidget)
        self.NotesText.setGeometry(QtCore.QRect(20, 140, 41, 21))
        self.NotesText.setObjectName("NotesText")
        self.NotesInput = QtWidgets.QPlainTextEdit(DeleteUserWidget)
        self.NotesInput.setGeometry(QtCore.QRect(70, 140, 111, 51))
        self.NotesInput.setObjectName("NotesInput")
        self.AttachButton = QtWidgets.QPushButton(DeleteUserWidget)
        self.AttachButton.setGeometry(QtCore.QRect(200, 140, 75, 23))
        self.AttachButton.setObjectName("AttachButton")
        self.SearchUserGroup = QtWidgets.QGroupBox(DeleteUserWidget)
        self.SearchUserGroup.setGeometry(QtCore.QRect(10, 10, 271, 121))
        self.SearchUserGroup.setObjectName("SearchUserGroup")
        self.NameInput = QtWidgets.QLineEdit(self.SearchUserGroup)
        self.NameInput.setGeometry(QtCore.QRect(60, 30, 113, 20))
        self.NameInput.setText("")
        self.NameInput.setObjectName("NameInput")
        self.NameText = QtWidgets.QLabel(self.SearchUserGroup)
        self.NameText.setGeometry(QtCore.QRect(10, 30, 47, 20))
        self.NameText.setObjectName("NameText")
        self.GuestCheckBox = QtWidgets.QCheckBox(self.SearchUserGroup)
        self.GuestCheckBox.setGeometry(QtCore.QRect(190, 30, 70, 21))
        self.GuestCheckBox.setObjectName("GuestCheckBox")
        self.IDInput = QtWidgets.QLineEdit(self.SearchUserGroup)
        self.IDInput.setGeometry(QtCore.QRect(60, 60, 113, 20))
        self.IDInput.setObjectName("IDInput")
        self.IDText = QtWidgets.QLabel(self.SearchUserGroup)
        self.IDText.setGeometry(QtCore.QRect(20, 60, 31, 20))
        self.IDText.setObjectName("IDText")
        self.RFIDText = QtWidgets.QLabel(self.SearchUserGroup)
        self.RFIDText.setGeometry(QtCore.QRect(10, 90, 47, 21))
        self.RFIDText.setObjectName("RFIDText")
        self.ScanButton = QtWidgets.QPushButton(self.SearchUserGroup)
        self.ScanButton.setGeometry(QtCore.QRect(190, 90, 75, 23))
        self.ScanButton.setObjectName("ScanButton")
        self.RFIDCodeText = QtWidgets.QLabel(self.SearchUserGroup)
        self.RFIDCodeText.setGeometry(QtCore.QRect(80, 90, 71, 21))
        self.RFIDCodeText.setObjectName("RFIDCodeText")
        self.CancelButton = QtWidgets.QPushButton(DeleteUserWidget)
        self.CancelButton.setGeometry(QtCore.QRect(110, 200, 80, 23))
        self.CancelButton.setObjectName("CancelButton")
        self.SearchUserGroup.raise_()
        self.DeleteButton.raise_()
        self.NotesText.raise_()
        self.NotesInput.raise_()
        self.AttachButton.raise_()
        self.CancelButton.raise_()

        self.retranslateUi(DeleteUserWidget)
        QtCore.QMetaObject.connectSlotsByName(DeleteUserWidget)

    def retranslateUi(self, DeleteUserWidget):
        _translate = QtCore.QCoreApplication.translate
        DeleteUserWidget.setWindowTitle(_translate("DeleteUserWidget", "Delete User"))
        self.DeleteButton.setText(_translate("DeleteUserWidget", "Delete"))
        self.NotesText.setText(_translate("DeleteUserWidget", "Notes:"))
        self.AttachButton.setText(_translate("DeleteUserWidget", "Attach..."))
        self.SearchUserGroup.setTitle(_translate("DeleteUserWidget", "Search user..."))
        self.NameText.setText(_translate("DeleteUserWidget", "Name:"))
        self.GuestCheckBox.setText(_translate("DeleteUserWidget", "Guest"))
        self.IDText.setText(_translate("DeleteUserWidget", "ID:"))
        self.RFIDText.setText(_translate("DeleteUserWidget", "RFID:"))
        self.ScanButton.setText(_translate("DeleteUserWidget", "Scan"))
        self.RFIDCodeText.setText(_translate("DeleteUserWidget", "RFID Code"))
        self.CancelButton.setText(_translate("DeleteUserWidget", "Cancel"))

@staticmethod
    def insertData(data):
        # Query to Database
        return data

    @staticmethod
    def pinAuthorization(pin):
        flag = False
        # QUERY
        if flag:
            return True
        else:
            return False

    @staticmethod
    def isDocumentAttached():
        isAttached = True
        # checker algo
        if isAttached:
            return True
        else:
            return False

    @staticmethod
    def saveDocument():
        # save to DB
        return True

    @staticmethod
    def disableRFIDCard():
        card = None
        # scan rfid card
        # remove from DB
        return True

    @staticmethod
    def writeToAccessLogs():
        # write to logs
        return True

    @staticmethod
    def isNotRegistered():
        exists = False
        # check DB
        if exists:
            return True
        else:
            return False

    @staticmethod
    def isRFIDCardValid():
        card = None
        # scan rfid card
        if card:
            return True
        else:
            return False

    @staticmethod
    def readRFIDCard():
        card = None
        data = None
        # scan card
        return data

    @staticmethod
    def isFullNameValid(name):
        if len(name) > 5:
            return True
        else:
            return False