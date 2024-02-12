from animal import Bird
from ..food import Food


class Hen(Bird):
    ALLOWED_FOODS = ['Fruit', 'Vegetable', 'Meat', 'Seed']
    WEIGTHT_INCREMENTAL = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Cluck'


class Owl(Bird):
    ALLOWED_FOODS = ['Meat']
    WEIGTHT_INCREMENTAL = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Hoot Hoot'