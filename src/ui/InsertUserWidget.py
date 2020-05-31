from PyQt5 import QtCore, QtGui, QtWidgets
from .pin_util import pin_authorization
from domain import EmployeeSchedule
from domain import AccessLevel
from domain import DocumentAttachment
from domain import RFIDCardData


class Ui_InsertUserWidget(object):

    def __init__(self, ctx):
        self.ctx = ctx

    def insertData(self):
        # user inserted all the data
        # start sequence diagram implementation from here
        if self.isEmployee:
            registered = EmployeeSchedule.isRegistered()
            if registered:
                self.showMessage('already registered employee')
                return

            accessLevelValid = AccessLevel.isAccessLevelValid(True, 1)  # todo: add correct params
            if not accessLevelValid:
                self.showMessage('invalid access level')
                return

            fullNameValid = self.isFullNameValid()
            if not fullNameValid:
                self.showMessage('invalid full name')
                return

            expiryDateValid = self.isExpiryDateValid()
            if not expiryDateValid:
                self.showMessage('invalid expiry date')
                return

        # end if employee
        self.pinAuthorization()

    def isEmployee(self):
        return not self.GuestCheckBox.isChecked()

    def pinAuthorization(self):
        pin_authorization(self.ctx, self._pinCallback)

    def _pinCallback(self, result):
        if result:
            # todo: successful auth
            documentAttached = self.isDocumentAttached()
            if documentAttached and self.isEmployee():
                atch = DocumentAttachment(str(self.NotesText.text()))
                atch.save()

            # write rfid card
            # write access logs
            # show menu
        else:
            self.showMessage('pin auth fail')

    def showMessage(self, text):
        # todo: show message somewhere
        print(text)

    def isFullNameValid(self):
        name = str(self.NameInput.text)
        # todo: add more checks
        return ' ' in name

    def isExpiryDateValid(self):
        return True

    def isDocumentAttached(self):
        notes = str(self.NotesText.text())
        return notes is not None and len(notes) > 0

    def setupUi(self, InsertUserWidget):
        InsertUserWidget.setObjectName("InsertUserWidget")
        InsertUserWidget.resize(312, 228)
        self.centralwidget = QtWidgets.QWidget(InsertUserWidget)
        self.centralwidget.setObjectName("centralwidget")
        self.OKButton = QtWidgets.QPushButton(self.centralwidget)
        self.OKButton.setGeometry(QtCore.QRect(230, 200, 75, 23))
        self.OKButton.setObjectName("OKButton")
        self.CancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.CancelButton.setGeometry(QtCore.QRect(140, 200, 81, 23))
        self.CancelButton.setObjectName("CancelButton")
        self.NameInput = QtWidgets.QLineEdit(self.centralwidget)
        self.NameInput.setGeometry(QtCore.QRect(100, 20, 121, 20))
        self.NameInput.setObjectName("NameInput")
        self.AccessLevelInput = QtWidgets.QLineEdit(self.centralwidget)
        self.AccessLevelInput.setGeometry(QtCore.QRect(100, 80, 121, 21))
        self.AccessLevelInput.setObjectName("AccessLevelInput")
        self.NameText = QtWidgets.QLabel(self.centralwidget)
        self.NameText.setGeometry(QtCore.QRect(50, 20, 41, 20))
        self.NameText.setObjectName("NameText")
        self.AccessLevelText = QtWidgets.QLabel(self.centralwidget)
        self.AccessLevelText.setGeometry(QtCore.QRect(10, 80, 81, 21))
        self.AccessLevelText.setObjectName("AccessLevelText")
        self.NotesInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.NotesInput.setGeometry(QtCore.QRect(100, 140, 121, 51))
        self.NotesInput.setObjectName("NotesInput")
        self.NotesText = QtWidgets.QLabel(self.centralwidget)
        self.NotesText.setGeometry(QtCore.QRect(50, 140, 41, 20))
        self.NotesText.setObjectName("NotesText")
        self.AttachButton = QtWidgets.QPushButton(self.centralwidget)
        self.AttachButton.setGeometry(QtCore.QRect(230, 140, 75, 23))
        self.AttachButton.setObjectName("AttachButton")
        self.GuestCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.GuestCheckBox.setGeometry(QtCore.QRect(230, 20, 70, 21))
        self.GuestCheckBox.setObjectName("GuestCheckBox")
        self.IDText = QtWidgets.QLabel(self.centralwidget)
        self.IDText.setGeometry(QtCore.QRect(70, 51, 21, 20))
        self.IDText.setObjectName("IDText")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 121, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.ExpirationDateText = QtWidgets.QLabel(self.centralwidget)
        self.ExpirationDateText.setGeometry(QtCore.QRect(40, 110, 59, 21))
        self.ExpirationDateText.setObjectName("ExpirationDateText")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 110, 121, 23))
        self.lineEdit_2.setObjectName("lineEdit_2")
        InsertUserWidget.setCentralWidget(self.centralwidget)

        self.retranslateUi(InsertUserWidget)
        QtCore.QMetaObject.connectSlotsByName(InsertUserWidget)

    def retranslateUi(self, InsertUserWidget):
        _translate = QtCore.QCoreApplication.translate
        InsertUserWidget.setWindowTitle(_translate("InsertUserWidget", "Insert User"))
        self.OKButton.setText(_translate("InsertUserWidget", "Create"))
        self.CancelButton.setText(_translate("InsertUserWidget", "Cancel"))
        self.NameText.setText(_translate("InsertUserWidget", "Name:"))
        self.AccessLevelText.setText(_translate("InsertUserWidget", "Access Level:"))
        self.NotesText.setText(_translate("InsertUserWidget", "Notes:"))
        self.AttachButton.setText(_translate("InsertUserWidget", "Attach..."))
        self.GuestCheckBox.setText(_translate("InsertUserWidget", "Guest"))
        self.IDText.setText(_translate("InsertUserWidget", "ID:"))
        self.ExpirationDateText.setText(_translate("InsertUserWidget", "Expires:"))

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
