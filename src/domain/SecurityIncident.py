
class SecurityIncident:
    def fillInDetails(self, description, sector, time, securityGuyId, employeeid, cause, incidentType):
        self.description = description
        self.sector = sector
        self.time = time
        self.securityGuyId = securityGuyId
        self.employeeid = employeeid
        self.cause = cause
        self.incidentType = incidentType

    def setDetails(self, details):
        self.details = details
