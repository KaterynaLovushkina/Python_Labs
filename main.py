from modules.PassengerCar import PassengerCar
from modules.Tram import Tram
from modules.Trolley import Trolleybus
from modules.Bus import Bus
from modules.Lorry import Lorry


if __name__ == '__main__':
    tram=Tram("JJJ",1999,100)
    trolleybus=Trolleybus("SSS",1999,60,"automatically", True)
    car1 = PassengerCar("BMV", 2008, 80, "YS-YW")
    bus1=Bus("SSS",1999,100,"Kyrylo",28)
    lorry1=Lorry("Simon Loos",1999,55,4.3,10,3.2)

    print(tram)
    print(trolleybus)
    print(car1)
    print(bus1)
    print(lorry1)
    print()

    tram.goForward(60)
    trolleybus.get_tanked(60,69)
    car1.find_out_country_manufacture()
    bus1.discover_type_of_bus()
    print("The sum is: {} UAH".format(lorry1.get_sum_of_delivered_load(240)))



