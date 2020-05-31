
from .Employee import Employee

class SecurityGuy(Employee):

    # simulate some database for
    pins = []

    def __init__(self, fullname, id, accessLevel, pin):
        super().__init__(fullname, id, accessLevel)
        self.pin = pin
        SecurityGuy.pins.append(pin)

    @staticmethod
    def doesPinExist(pin):
        # this is the database
        return pin in [1234, 5678, 1111, 0000, 9999] or pin in SecurityGuy.pins
