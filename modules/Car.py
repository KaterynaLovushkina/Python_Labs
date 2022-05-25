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
        print("The car {}  is going with speed {} km per hour".format(self.__model, speed))

    def get_tanked(self, litres_of_fuel: float,
                   price_per_litre: float) -> None:
        cost = litres_of_fuel * price_per_litre
        print("The car {}  is tanked for {} UAH".format(self.__model, cost))
