from project.divers.base_diver import BaseDiver


# class ScubaDiver(BaseDiver):
#     def __init__(self, name: str):
#         super().__init__(name, oxygen_level=540)
#
#     def miss(self, time_to_catch: int):
#         reduction_percentage = 0.3
#         reduction_amount = max(0, int(time_to_catch * reduction_percentage))
#
#         if self.oxygen_level - reduction_amount < 0:
#             self.oxygen_level = 0
#             self.update_health_status()
#         else:
#             self.oxygen_level -= reduction_amount
#
#     def renew_oxy(self):
#         self.oxygen_level = 540
class ScubaDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, oxygen_level=540)

    def miss(self, time_to_catch: int):
        reduction_percentage = 0.3
        reduction_amount = max(0, int(time_to_catch * reduction_percentage))

        if self.oxygen_level - reduction_amount < 0:
            self.oxygen_level = 0
            self.update_health_status()
        else:
            self.oxygen_level -= reduction_amount

    def renew_oxy(self):
        self.oxygen_level = 540
