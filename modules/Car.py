from modules.Vehicle import Vehicle
from abc import ABC


class Car(Vehicle, ABC):

    def __new__(cls, *args, **kwargs):
        if cls is Car:
            raise TypeError(
                "TypeError: Can't instantiate abstract class {name} directly".format(name=cls.__name__)
            )
        return object.__new__(cls)

    def __str__(self):
        my_string = super(Vehicle, self).__str__()
        return my_string

    def __repr__(self):
        my_string = super(Vehicle, self).__repr__()
        return my_string

    def goForward(self, speed) -> None:
        print(f"The car {self.model}  is going with speed {speed} km per hour")

    def get_tanked(self, litres_of_fuel: float,
                   price_per_litre: float) -> None:
        cost = litres_of_fuel * price_per_litre
        print(f"The car {self.model}  is tanked for {cost} UAH")
