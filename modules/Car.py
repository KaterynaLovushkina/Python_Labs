from modules.Vehicle import Vehicle
from abc import ABCMeta


class Car(Vehicle,metaclass=ABCMeta):

    def __new__(cls, *args, **kwargs):
        if cls is Car:
            raise TypeError(
                "TypeError: Can't instantiate abstract class {name} directly".format(name=cls.__name__)
            )
        return object.__new__(cls)

    def __init__(self, model: str, year: int, miles_in_thousands: float):
        super().__init__(model, year, miles_in_thousands)

    def __str__(self):
        my_string = super(Vehicle, self).__str__()
        return my_string

    def goForward(self, speed) -> None:
        print("The car {}  is going with speed {} km per hour".format(self.model, speed))

    def get_tanked(self, litres_of_fuel: float,
                   price_per_litre: float) -> None:
        cost = litres_of_fuel * price_per_litre
        print("The car {}  is tanked for {} UAH".format(self.model, cost))
