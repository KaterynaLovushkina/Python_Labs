from modules.Vehicle import Vehicle


class Tram(Vehicle):
    def __init__(self, model: str, year: int, miles_in_thousands: float):
        Vehicle.__init__(self, model, year, miles_in_thousands)

    def __str__(self):
        st = super().__str__()
        return st

    def __repr__(self):
        my_string = super().__repr__()+")"
        return my_string

    def goForward(self, speed) -> None:
        print(f"The tram {self.model}  is going with speed {speed} km per hour")

    def get_tanked(self, litres_of_fuel: float,
                   price_per_litre: float) -> None:
        cost = litres_of_fuel * price_per_litre
        print(f"The tram {self.model}  is tanked for {cost} UAH")

    def __del__(self):
        super().__del__()
