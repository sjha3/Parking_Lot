from spot import Spot, Spot_Type
class Vehicle:
    def __init__(self, num, m, s):
        print('Init vehicle with num ', num, ' model : ', m, ' size: ', s)
        self.num = num
        self.model = m
        self.size = s

class Car(Vehicle):
    def __init__(self, num, m):
        print('Init car with num ', num, ' model : ', m, ' size: ', Spot_Type.regular)
        super().__init__(num, m, Spot_Type.regular)
class Bike(Vehicle):
    def __init__(self, num, m):
        print('Init Bike with num ', num, ' model : ', m, ' size: ', Spot_Type.compat)
        super().__init__(num, m, Spot_Type.compat)
class Bus(Vehicle):
    def __init__(self, num, m):
        print('Init Bus with num ', num, ' model : ', m, ' size: ', Spot_Type.large)
        super().__init__(num, m, Spot_Type.large)