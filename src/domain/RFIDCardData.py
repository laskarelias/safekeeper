from hardware import RFIDCardScanner
import datetime

class RFIDCardData:
    def __init__(self, expiration, employeeId, isGuest):
        self.expiration = expiration
        self.employeeId = employeeId
        self.isGuest = isGuest

    def writeRFIDCard(self, expiration = None, employeeId = None, isGuest = None):
        if expiration is not None:
            self.expiration = expiration
            print('new expiration set')
        if employeeId is not None:
            self.employeeId = employeeId
            print('new employeeId set')
        if isGuest is not None:
            self.isGuest = isGuest
            print('new isGuest set')

    
    def readRFIDCardData(self):
        print
        return self.expiration, self.employeeId, self.isGuest

    def isRFIDCardExpired(self):
        if self.expiration >= datetime.datetime.today().day:
            return False
        else:
            return True
        
    
    