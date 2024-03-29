class Trainer:
    id = 1

    def __init__(self, name: str):
        self.id = Trainer.get_next_id()
        self.name = name

    @staticmethod
    def get_next_id():
        result = Trainer.id
        Trainer.id += 1
        return result

    def __repr__(self):
        f"Trainer <{self.id}> {self.name}"