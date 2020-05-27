from . import IncidentClassifier

class PeopleClassifier(IncidentClassifier):
    def __init__(self, incidentOccured, isPeople):
        super().__init__(self, incidentOccured)
        self.isPeople = isPeople