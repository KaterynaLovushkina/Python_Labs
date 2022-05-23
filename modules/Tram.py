from modules.Vehicle import Vehicle


class Tram(Vehicle):
    def __init__(self, model: str, year: int, miles_in_thousands: float):
        Vehicle.__init__(self, model, year, miles_in_thousands)

    def __str__(self):
        st= super().__str__()
        return st

    def goForward(self, speed) -> None:
        print("The tram {}  is going with speed {} km per hour".format(self.model, speed))

    def get_tanked(self, litres_of_fuel: float,
                   price_per_litre: float) -> None:
        cost = litres_of_fuel * price_per_litre
        print("The tram {}  is tanked for {} UAH".format(self.model, cost))
