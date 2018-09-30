from enum import Enum
class Spot_Type(Enum):
    compat = 0
    regular = 1
    large = 2

class Spot:
    def __int__(self, s, type, num):
        self.size = s
        self.spot_type = Spot_Type(type)
        self.number = num