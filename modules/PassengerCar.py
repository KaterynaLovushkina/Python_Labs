from modules.Car import Car
from modules.Vehicle import Vehicle


class PassengerCar(Car):
    def __init__(self, model: str, year: int,
                 miles_in_thousands: float, vin: str):
        Vehicle.__init__(self, model, year, miles_in_thousands)
        self.vin = vin

    def __str__(self):
        my_string = super(Car, self).__str__() + ", Vin: {}".format(self.vin)
        return my_string

    def __repr__(self):
        my_string = super(Car, self).__repr__() + \
                    f',"{self.vin}")'
        return my_string

    def find_out_country_manufacture(self):
        if self.vin == "WQ-RT":
            print("The country manufacture is Canada")
        elif self.vin == "YS-YW":
            print("The country manufacture is Sweden")
        elif self.vin == "VA-VE":
            print("The country manufacture is Austria")
        elif self.vin == "SA-SM":
            print("The country manufacture is United Kingdom")
        elif self.vin == "W" or self.vin == "SN-ST":
            print("The country manufacture is Germany")

        else:
            print("The car's manufacture is not recognised. We add more numbers letter0")

    def __del__(self):
        super(Car, self).__del__()