from modules.Car import Car
from modules.Vehicle import Vehicle


class Lorry(Car):
    def __init__(self, model: str, year: int,
                 miles_in_thousands: float, high: float,
                 length: float, width: float):
        Vehicle.__init__(self, model, year, miles_in_thousands)
        self.high = high
        self.length = length
        self.width = width

    def __str__(self):
        my_string = super(Car, self).__str__() + ", High={}, Length={}, Width={}". \
            format(self.high, self.length, self.width)
        return my_string

    def __repr__(self):
        my_string = super(Car, self).__repr__() + \
                    f',"{self.high}","{self.length}",{self.width})'
        return my_string

    def get_sum_of_delivered_load(self, distance_per_km: int):
        volume = self.width * self.length * self.width
        if volume < 20:
            sum = distance_per_km * 5
            return sum
        elif volume < 35:
            sum = distance_per_km * 12
            return sum
        elif volume < 60:
            sum = distance_per_km * 17
            return sum
        elif volume < 120:
            sum = distance_per_km * 20
            return sum
        else:
            print("we can't deliver the load ")
        
    def __del__(self):
        super(Car,self).__del__()
