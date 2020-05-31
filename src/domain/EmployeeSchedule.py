
class EmployeeSchedule:
    
    @staticmethod
    def isPinActiveNow(pin) -> bool:
        if pin == 9999: # select this pin to be inactive (this is the database)
            return False
        if pin == 1234: # active pin
            return True

    @staticmethod
    def isCurrentShiftActive(shift):
        return True

    @staticmethod
    def isRegistered():
        #todo: implement later
        return False