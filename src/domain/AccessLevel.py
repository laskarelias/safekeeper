
class AccessLevel:
    @staticmethod
    def isAccessLevelValid(lvl):
        return (lvl.guestsAllowed and lvl.level < 2) or (lvl.level >= 3 and not lvl.guestsAllowed)

    def __init__(self, guestsAllowed, level):
        self.guestsAllowed = guestsAllowed
        self.level = level