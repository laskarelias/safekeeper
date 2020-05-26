class DroneControl:

    @staticmethod
    def connectToDrone():
        isConnected = False
        # check connection with drone
        if isConnected:
            return True
        else:
            return False

    @staticmethod
    def checkInactivity():
        newIncident = False
        # check for incidents
        if newIncident:
            print("stay")
            return True
        else:
            print("leave")
            return False

    @staticmethod
    def autoRecall(self):
        activity = self.checkInactivity()
        if activity:
            print("stay")
        else:
            print("leave")


    @staticmethod
    def recogniseIncident():
        #drone blackbox
        return True


    @staticmethod
    def photosAndLivestream():
        livestream = True
        photos = True
        return livestream, photos




    @staticmethod
    def backOnline(self):
        connection = False
        # Retry to connect
        if connection:
            print("Connected")
            return True
        else:
            print("recalling")
            self.autoRecall()
