from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    TYPE = "PredatoryFish"

    def __init__(self, name: str, points: float):
        super().__init__(name, points, 90)

    def fish_details(self) -> str:
        return f"{self.TYPE}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"
