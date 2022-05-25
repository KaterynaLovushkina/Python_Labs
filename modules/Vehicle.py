from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, model: str, year: int, miles_in_thousands: float):
        self.__model = model
        self.__year = year
        self.__miles_in_thousands = miles_in_thousands

    @abstractmethod
    def goForward(self, speed: float) -> None:
        pass

    @abstractmethod
    def get_tanked(self, litres_of_fuel: int,
                   price_per_litre: float) -> None:
        pass

    @property
    def model(self):
        return self.__model

    def __str__(self):
        my_string = 'Vehicle: Model={}, Year={}, Miles in thousands={}'. \
            format(self.__model, self.__year, self.__miles_in_thousands)
        return my_string

    def __repr__(self):
        return f'Vehicle("{self.__model}","{self.__year}",{self.__miles_in_thousands}'

    def __del__(self):
        print("The object of {} class is deleted".format(self.__class__.__name__))
