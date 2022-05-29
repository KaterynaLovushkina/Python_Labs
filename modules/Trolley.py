from modules.Vehicle import Vehicle


class Trolleybus(Vehicle):
    def __init__(self, model: str, year: int,
                 miles_in_thousands: float, transmission: str,
                 luggage_place:bool):
        Vehicle.__init__(self, model, year, miles_in_thousands)
        self.transmission=transmission
        self.luggage_place=luggage_place

    def __str__(self):
        my_string = super().__str__() + f", Transmission={self.transmission}, Luggage place={self.luggage_place}"
        return my_string

    def __repr__(self):
        my_string = super().__repr__() + \
                    f',{self.transmission},{self.luggage_place})'
        return my_string

    def goForward(self, speed) -> None:
        print(f"The trolleybus {self.model}  is going with speed {speed} km per hour")

    def get_tanked(self, litres_of_fuel: float,
                   price_per_litre: float) -> None:
        cost = litres_of_fuel * price_per_litre
        print(f"The trolleybus {self.model}  is tanked for {cost} UAH")

    def __del__(self):
        super().__del__()