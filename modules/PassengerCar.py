from modules.Car import Car
from modules.Vehicle import Vehicle


class PassengerCar(Car):
    def __init__(self, model: str, year: int,
                 miles_in_thousands: float, vin):
        Vehicle.__init__(self, model, year, miles_in_thousands)
        self.__vin = vin

    def __str__(self):
        my_string = super(Car, self).__str__() + ", Vin: {}".format(self.__vin)
        return my_string

    def __repr__(self):
        my_string = super(Car, self).__repr__() + \
                    f',"{self.__vin}")'
        return my_string

    def find_out_country_manufacture(self):
        if self.__vin == 2:
            print("The country manufacture is Canada")
        elif self.__vin == "YS-YW":
            print("The country manufacture is Sweden")
        elif self.__vin == "VA-VE":
            print("The country manufacture is Austria")
        elif self.__vin == "SA-SM":
            print("The country manufacture is United Kingdom")
        elif self.__vin == "W" or self.__vin == "SN-ST":
            print("The country manufacture is Germany")

        else:
            print("The car's manufacture is not recognised. We add more numbers letter0")

    def __dell__(self):
        super(Car, self).__dell__()