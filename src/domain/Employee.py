from .HumanEntity import HumanEntity

class Employee(HumanEntity):

    def __init__(self, fullname, id, accessLevel):
        super().__init__(fullname)
        self.id = id
        self.accessLevel = accessLevel

