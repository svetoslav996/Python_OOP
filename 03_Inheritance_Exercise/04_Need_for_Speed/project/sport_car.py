from car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUPTION = 10

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)