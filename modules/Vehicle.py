from abc import ABCMeta, abstractmethod


class Vehicle(object,metaclass=ABCMeta):

    def __init__(self, model: str, year: int, miles_in_thousands: float):
        self.model = model
        self.year = year
        self.miles_in_thousands = miles_in_thousands

    @abstractmethod
    def goForward(self, speed: float) -> None:
        pass

    @abstractmethod
    def get_tanked(self, litres_of_fuel: int,
                   price_per_litre: float) -> None:
        pass

    def __str__(self):
        my_string=f'Vehicle: Model={self.model}, Year={self.year}, Miles in thousands={self.miles_in_thousands}'
        return my_string
