from motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUPTION = 8

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)