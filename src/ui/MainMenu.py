from PyQt5 import QtCore, QtGui, QtWidgets
from .ActivityLogWindow import Ui_ActivityLogWindow
from .DeleteUserWidget import Ui_DeleteUserWidget
from .DroneWindow import Ui_DroneWindow
from .InsertUserWidget import Ui_InsertUserWidget
from .SilentAlarmWidget import Ui_SilentAlarmWidget
from .IncidentReport import Ui_IncidentReportWindow
from .NotificationWidget import Ui_NotificationWidget

from .notif_util import sample_notification

class Ui_MainMenuWindow(object):
    def __init__(self, ctx):
        self.ctx = ctx

    def showNotification(self, text):
        print (f'Main Menu Notification: {text}')

    def _activity_log_clicked(self):
        # sample_notification(self.ctx)

        # return
        self.ActivityLogWindow = QtWidgets.QMainWindow()
        self.ui_activity_log = Ui_ActivityLogWindow(self.ctx)
        self.ui_activity_log.setupUi(self.ActivityLogWindow)
        self.ActivityLogWindow.show()

    def _delete_button_clicked(self):
        self.DeleteUserWindow = QtWidgets.QMainWindow()
        self.ui_delete_window = Ui_DeleteUserWidget(self.ctx)
        self.ui_delete_window.setupUi(self.DeleteUserWindow)
        self.DeleteUserWindow.show()

    def _drone_button_clicked(self):
        self.DroneControlWindow = QtWidgets.QMainWindow()
        self.ui_drone_control = Ui_DroneWindow(self.ctx)
        self.ui_drone_control.setupUi(self.DroneControlWindow)
        self.DroneControlWindow.show()

    def _incident_submission_clicked(self):
        self.IncidentSubmissionWindow = QtWidgets.QMainWindow()
        self.ui_report = Ui_IncidentReportWindow(self.ctx)
        self.ui_report.setupUi(self.IncidentSubmissionWindow)
        self.IncidentSubmissionWindow.show()

    def _insert_button_clicked(self):
        self.InsertButtonWindow = QtWidgets.QMainWindow()
        self.ui_insert = Ui_InsertUserWidget(self.ctx)
        self.ui_insert.setupUi(self.InsertButtonWindow)
        self.InsertButtonWindow.show()

    def _silent_alarm_clicked(self):
        self.SilentAlarmWindow = QtWidgets.QMainWindow()
        self.ui_alarm = Ui_SilentAlarmWidget(self.ctx)
        self.ui_alarm.setupUi(self.SilentAlarmWindow)
        self.SilentAlarmWindow.show()

    def setupUi(self, MainMenuWindow):
        MainMenuWindow.setObjectName("MainMenuWindow")
        MainMenuWindow.resize(424, 254)
        self.centralwidget = QtWidgets.QWidget(MainMenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ActivityLogButton = QtWidgets.QPushButton(self.centralwidget)
        self.ActivityLogButton.setGeometry(QtCore.QRect(10, 20, 131, 23))
        self.ActivityLogButton.setObjectName("ActivityLogButton")
        self.DroneControlButton = QtWidgets.QPushButton(self.centralwidget)
        self.DroneControlButton.setGeometry(QtCore.QRect(10, 140, 131, 23))
        self.DroneControlButton.setObjectName("DroneControlButton")
        self.InsertUserButton = QtWidgets.QPushButton(self.centralwidget)
        self.InsertUserButton.setGeometry(QtCore.QRect(10, 60, 131, 23))
        self.InsertUserButton.setObjectName("InsertUserButton")
        self.DeleteUserButton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteUserButton.setGeometry(QtCore.QRect(10, 100, 131, 23))
        self.DeleteUserButton.setObjectName("DeleteUserButton")
        self.IncidentSubmissionButton = QtWidgets.QPushButton(self.centralwidget)
        self.IncidentSubmissionButton.setGeometry(QtCore.QRect(10, 180, 131, 23))
        self.IncidentSubmissionButton.setObjectName("IncidentSubmissionButton")
        self.SilentAlarmButton = QtWidgets.QPushButton(self.centralwidget)
        self.SilentAlarmButton.setGeometry(QtCore.QRect(10, 220, 131, 23))
        self.SilentAlarmButton.setObjectName("SilentAlarmButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(160, 40, 256, 171))
        self.listWidget.setObjectName("listWidget")

        self.LatestIncidentsText = QtWidgets.QLabel(self.centralwidget)
        self.LatestIncidentsText.setGeometry(QtCore.QRect(160, 20, 131, 21))
        self.LatestIncidentsText.setObjectName("LatestIncidentsText")
        self.IncidentNumberText = QtWidgets.QLabel(self.centralwidget)
        self.IncidentNumberText.setGeometry(QtCore.QRect(160, 221, 251, 20))
        self.IncidentNumberText.setObjectName("IncidentNumberText")
        MainMenuWindow.setCentralWidget(self.centralwidget)

        ## Click Listeners
        self.ActivityLogButton.clicked.connect(self._activity_log_clicked)
        self.DeleteUserButton.clicked.connect(self._delete_button_clicked)
        self.DroneControlButton.clicked.connect(self._drone_button_clicked)
        self.IncidentSubmissionButton.clicked.connect(self._incident_submission_clicked)
        self.InsertUserButton.clicked.connect(self._insert_button_clicked)
        self.SilentAlarmButton.clicked.connect(self._silent_alarm_clicked)

        ## how to attach notifications
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item.setText("Check In - Now - Front Desk")

        self.retranslateUi(MainMenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MainMenuWindow)

    def retranslateUi(self, MainMenuWindow):
        self.MainMenuWindow = MainMenuWindow
        _translate = QtCore.QCoreApplication.translate
        MainMenuWindow.setWindowTitle(_translate("MainMenuWindow", "Safeguard"))
        self.ActivityLogButton.setText(_translate("MainMenuWindow", "Activity Log"))
        self.DroneControlButton.setText(_translate("MainMenuWindow", "Drone Control"))
        self.InsertUserButton.setText(_translate("MainMenuWindow", "Insert User"))
        self.DeleteUserButton.setText(_translate("MainMenuWindow", "Delete User"))
        self.IncidentSubmissionButton.setText(_translate("MainMenuWindow", "Incident Submission"))
        self.SilentAlarmButton.setText(_translate("MainMenuWindow", "Silent Alarm"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.LatestIncidentsText.setText(_translate("MainMenuWindow", "Latest Incidents:"))
        self.IncidentNumberText.setText(_translate("MainMenuWindow", "# Incident(s)"))
