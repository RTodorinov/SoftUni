from project.supply.supply import Supply


class Drink(Supply):
    TYPE = "Drink"

    def __init__(self, name: str):
        super().__init__(name, 15)

    def details(self):
        return f"{self.TYPE}: {self.name}, {self.energy}"
