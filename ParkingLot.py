import heapq
from spot import Spot_Type, Spot
from vehicle import Vehicle, Car, Bike, Bus

class ParkingLot:
    def __init__(self, id, compat, regular, large):
        self.id = id
        self.num_compat_spot = compat
        self.num_regular_spot = regular
        self.num_large_spot = large
        # heaps to store spots
        self.compat_spot_heap = []
        self.regular_spot_heap = []
        self.large_spot_heap = []

        for i in range(self.num_compat_spot):
            self.compat_spot_heap.append(i)
            heapq.heapify(self.compat_spot_heap)

        for i in range(compat, self.num_regular_spot):
            self.regular_spot_heap.append(i)
            heapq.heapify(self.regular_spot_heap)

        for i in range(regular, self.num_large_spot):
            self.large_spot_heap.append(i)
            heapq.heapify(self.large_spot_heap)

        #map to store vehicle.num => spot
        self.vehicle_to_spot_map = {}

    def is_parking_available(self, spottype):
        #mem = Spot_Type.spottype.value
        if spottype == Spot_Type.compat and len(self.compat_spot_heap) > 0:
            print('Compat Space is available')
            return True
        elif spottype == Spot_Type.regular and len(self.regular_spot_heap) > 0:
            print('Regular Space is available')
            return True
        elif spottype == Spot_Type.large and len(self.large_spot_heap) >0:
            print('Large spot is available')
            return True

        return  False

    def park(self, vehicle):
        if vehicle.size == Spot_Type.compat:
            self.park_bike(vehicle)
        elif vehicle.size == Spot_Type.regular:
            self.park_car(vehicle)
        elif vehicle.size == Spot_Type.large:
            self.park_bus(vehicle)

    def park_car(self, vehicle):
        if self.is_parking_available(Spot_Type.regular) == True:
            print('Parking is available for car')
            parking_spot = heapq.heappop(self.regular_spot_heap)
            print('Park it at ', parking_spot)
            self.vehicle_to_spot_map[vehicle.num] = parking_spot

    def park_bike(self, vehicle):
        if self.is_parking_available(Spot_Type.compat) == True:
            print('Parking is available for bike')
            parking_spot = heapq.heappop(self.compat_spot_heap)
            print("Park at", parking_spot)
            self.vehicle_to_spot_map[vehicle.num] = parking_spot
            print('Park it at ', parking_spot)

    def park_bus(self, vehicle):
        if self.is_parking_available(Spot_Type.large) == True:
            print('Parking is available for bus')
            parking_spot = heapq.heappop(self.large_spot_heap)
            self.vehicle_to_spot_map[vehicle.num] = parking_spot
            print('Park it at ', parking_spot)

    def remove(self, vehicle):
        if vehicle.size == Spot_Type.compat:
            self.remove_bike(vehicle)
        elif vehicle.size == Spot_Type.regular:
            self.remove_car(vehicle)
        elif vehicle.size == Spot_Type.large:
            self.remove_bus(vehicle)

    def remove_bike(self, vehicle):
        print('unParking  for bike', vehicle.num)
        parking_spot = self.vehicle_to_spot_map[vehicle.num]
        print('Bike was parked at ', parking_spot)
        heapq.heappush(self.compat_spot_heap, parking_spot)
        del self.vehicle_to_spot_map[vehicle.num]

    def remove_car(self, vehicle):
        print('unParking  for car')
        parking_spot = self.vehicle_to_spot_map[vehicle.num]
        print('Car was parked at ', parking_spot)
        heapq.heappush(self.regular_spot_heap, parking_spot)
        del self.vehicle_to_spot_map[vehicle.num]

    def remove_bus(self, vehicle):
        print('unParking  for bike')
        parking_spot = self.vehicle_to_spot_map[vehicle.num]
        print('Vehicle was parked at ', parking_spot)
        heapq.heappush(self.large_spot_heap, parking_spot)
        del self.vehicle_to_spot_map[vehicle.num]


def main():
    parking_lot = ParkingLot(111, 10, 100, 150)
    my_bike = Bike(11, "hero")
    my_bike1 = Bike(12, "atlas")
    my_car = Car(21, "lexus")
    my_car1 = Car(22, "mini-cooper")
    my_bus = Bus(31, "tata")
    parking_lot.park(my_bike)
    parking_lot.park(my_car)
    parking_lot.park(my_bus)
    parking_lot.park(my_car1)
    print(parking_lot.vehicle_to_spot_map)

    parking_lot.remove(my_bike)
    print(parking_lot.vehicle_to_spot_map)
    parking_lot.park(my_bike1)
    print(parking_lot.vehicle_to_spot_map)

if __name__ == "__main__":
    main()