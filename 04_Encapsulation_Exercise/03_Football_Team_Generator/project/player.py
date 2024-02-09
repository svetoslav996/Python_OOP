class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.name = name
        self.sprint = sprint
        self.dribble = dribble
        self.passing = passing
        self.shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return f"Player: {self.name}\n" + \
            f"Sprint: {self.__sprint}\n" + \
            f"Dribble: {self.__dribble}\n" + \
            f"Passing: {self.__passing}\n" + \
            f"Shooting: {self.__shooting}\n"