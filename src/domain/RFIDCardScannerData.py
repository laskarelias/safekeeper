
class RFIDCardScannerData:
    def __init__(self, sector, isCheckIn):
        self.sector = sector
        self.isCheckIn = isCheckIn

    def accessLevelCheck(self):
        return True

    def isSectorAllowed(self):
        return True