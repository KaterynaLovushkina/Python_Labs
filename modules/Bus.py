from modules.Vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, model: str, year: int, miles_in_thousands: float, driver, num_off_seats):
        Vehicle.__init__(self, model, year, miles_in_thousands)
        self.driver = driver
        self.num_off_seats = num_off_seats

    def __str__(self):
        my_string = super().__str__() + ", Driver={}, Number off seats={}". \
            format(self.driver, self.num_off_seats)
        return my_string

    def __repr__(self):
        '''Returns representation of the object'''
        return "{}({!r})".format(self.__class__.__name__, self.driver, self.num_off_seats)

    def goForward(self, speed) -> None:
        print("The bus {}  is going with speed {} km per hour".format(self.model, speed))

    def get_tanked(self, litres_of_fuel: float,
                   price_per_litre: float) -> None:
        cost = litres_of_fuel * price_per_litre
        print("The bus {}  is tanked for {} UAH".format(self.model, cost))

    def discover_type_of_bus(self):
        if 37 <= self.num_off_seats <= 41:
            print("The bus has 4 seats per row")
        elif 27 <= self.num_off_seats <= 30:
            print("The bus has 3 individual seats per row or 3 seats in a row(2+1)")
        elif 11 <= self.num_off_seats <= 20:
            print("The bus has 2 seats per row")
        else:
            print("We don't recognise type of bus")
