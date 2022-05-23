from modules.Vehicle import Vehicle


class Trolleybus(Vehicle):
    def __init__(self, model: str, year: int,
                 miles_in_thousands: float, transmission: str,
                 luggage_place:bool):
        Vehicle.__init__(self, model, year, miles_in_thousands)
        self.transmission=transmission
        self.luggage_place=luggage_place

    def __str__(self):
        my_string = super().__str__() + ", Transmission={}, Luggage place={}". \
            format(self.transmission, self.luggage_place)
        return my_string

    def __repr__(self):
        '''Returns representation of the object'''
        return "{}({!r})".format(self.__class__.__name__, self.transmission, self.luggage_place)

    def goForward(self, speed) -> None:
        print("The trolleybus {}  is going with speed {} km per hour".format(self.model, speed))

    def get_tanked(self, litres_of_fuel: float,
                   price_per_litre: float) -> None:
        cost = litres_of_fuel * price_per_litre
        print("The trolleybus {}  is tanked for {} UAH".format(self.model, cost))