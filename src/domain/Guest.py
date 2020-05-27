from . import HumanEntity

class Guest(HumanEntity):
    
    def __init__(self, expiryDate, id, accessLevel):
        self.expiryDate = expiryDate
        self.id = id
        self.accessLevel = accessLevel