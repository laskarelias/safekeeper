from . import SecurityGuy

class ChiefSecurityGuy(SecurityGuy):
    def __init__(self, fullname, id, accessLevel, pin):
        super().__init__(self, fullname, id, accessLevel, pin)

        