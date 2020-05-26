from datetime import datetime

class CentralOffice:
        
    @staticmethod
    def notifyIncorrectPin(time, pin, sector):
        print(f'time: {time}, pin: {pin}, sector: {sector}')
	# send to some random server

    @staticmethod
    def sendReport(text):
        print(f'Sent report to central office {text}')

    @staticmethod
    def notifyIncorrectPin(time, pin, sector):
        print(f'time: {time}, pin: {pin}, sector: {sector}')
        # send to some random server

    def notifyDroneLostConnection():
        time = datetime.now()
        print(f'Drone Lost Connection at: {time}')

    def notifySilentAlarm(card, reason):
        time = datetime.now()
        print(f'!!! Silent Alarm !!!, {time}, {card}, {reason}')

    def sendReport(incident):
        time = datetime.now()
        print(f'Anonynmous Incident Report, {incident}, {time}')


