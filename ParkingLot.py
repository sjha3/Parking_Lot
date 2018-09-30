import heapq
from spot import Spot_Type, Spot
from vehicle import Vehicle, Car, Bike, Bus

class ParkingLot:
    def __init__(self, id, compat, regular, large):
        self.__id = id
        self.__num_compat_spot = compat
        self.__num_regular_spot = regular
        self.__num_large_spot = large
        # heaps to store spots
        self.__compat_spot_heap = []
        self.__regular_spot_heap = []
        self.__large_spot_heap = []

        for i in range(self.__num_compat_spot):
            self.__compat_spot_heap.append(i)
            heapq.heapify(self.__compat_spot_heap)

        for i in range(compat, self.__num_regular_spot):
            self.__regular_spot_heap.append(i)
            heapq.heapify(self.__regular_spot_heap)

        for i in range(regular, self.__num_large_spot):
            self.__large_spot_heap.append(i)
            heapq.heapify(self.__large_spot_heap)

        #map to store vehicle.num => spot
        self.__vehicle_to_spot_map = {}

    def is_parking_available(self, spottype):
        #mem = Spot_Type.spottype.value
        if spottype == Spot_Type.compat and len(self.__compat_spot_heap) > 0:
            print('Compat Space is available')
            return True
        elif spottype == Spot_Type.regular and len(self.__regular_spot_heap) > 0:
            print('Regular Space is available')
            return True
        elif spottype == Spot_Type.large and len(self.__large_spot_heap) >0:
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
            parking_spot = heapq.heappop(self.__regular_spot_heap)
            print('Park it at ', parking_spot)
            self.__vehicle_to_spot_map[vehicle.num] = parking_spot

    def park_bike(self, vehicle):
        if self.is_parking_available(Spot_Type.compat) == True:
            print('Parking is available for bike')
            parking_spot = heapq.heappop(self.__compat_spot_heap)
            print("Park at", parking_spot)
            self.__vehicle_to_spot_map[vehicle.num] = parking_spot
            print('Park it at ', parking_spot)

    def park_bus(self, vehicle):
        if self.is_parking_available(Spot_Type.large) == True:
            print('Parking is available for bus')
            parking_spot = heapq.heappop(self.__large_spot_heap)
            self.__vehicle_to_spot_map[vehicle.num] = parking_spot
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
        parking_spot = self.__vehicle_to_spot_map[vehicle.num]
        print('Bike was parked at ', parking_spot)
        heapq.heappush(self.__compat_spot_heap, parking_spot)
        del self.__vehicle_to_spot_map[vehicle.num]

    def remove_car(self, vehicle):
        print('unParking  for car')
        parking_spot = self.__vehicle_to_spot_map[vehicle.num]
        print('Car was parked at ', parking_spot)
        heapq.heappush(self.__regular_spot_heap, parking_spot)
        del self.__vehicle_to_spot_map[vehicle.num]

    def remove_bus(self, vehicle):
        print('unParking  for bike')
        parking_spot = self.__vehicle_to_spot_map[vehicle.num]
        print('Vehicle was parked at ', parking_spot)
        heapq.heappush(self.__large_spot_heap, parking_spot)
        del self.__vehicle_to_spot_map[vehicle.num]

    def print_vehicle_to_spot_mapping(self):
        print(self.__vehicle_to_spot_map)

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
    print("intial parking lot")
    parking_lot.print_vehicle_to_spot_mapping()

    parking_lot.remove(my_bike)
    print('parking lot after removing bike 11')
    parking_lot.print_vehicle_to_spot_mapping()
    parking_lot.park(my_bike1)
    print('parking lot after parking bike12')
    parking_lot.print_vehicle_to_spot_mapping()

if __name__ == "__main__":
    main()