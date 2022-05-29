from typing import List
from modules.PassengerCar import PassengerCar
from modules.Tram import Tram
from modules.Trolley import Trolleybus
from modules.Bus import Bus
from modules.Lorry import Lorry
from modules.Vehicle import Vehicle


def process_vehicles(vehicles: List[Vehicle]) -> None:
    for vehicle in vehicles:
        if issubclass(type(vehicle), Vehicle):
            print(vehicle)


if __name__ == '__main__':
    tram = Tram("JJJ", 1999, 100)
    trolleybus = Trolleybus("SSS", 1999, 60, "automatically", True)
    car1 = PassengerCar("BMV", 2008, 80, "YS-YW")
    bus1 = Bus("SSS", 1999, 100, "Kyrylo", 28)
    lorry1 = Lorry("Simon Loos", 1999, 55, 4.3, 10, 3.2)

    vehicles = [car1, tram, trolleybus, bus1, lorry1]
    process_vehicles(vehicles)
    print()
    tram.goForward(60)
    trolleybus.get_tanked(60, 69)
    car1.find_out_country_manufacture()
    bus1.discover_type_of_bus()
    print("The sum is: {} UAH".format(lorry1.get_sum_of_delivered_load(240)))
    print()
