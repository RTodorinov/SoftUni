from typing import List, Union
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            if animal not in self.animals:
                self.animals.append(animal)
                self.__budget -= price
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__budget <= price and len(self.animals) < self.__animal_capacity:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str) -> str:
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget < total_salaries:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        total_money_for_care = sum([animal.money_for_care for animal in self.animals])
        if self.__budget < total_money_for_care:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total_money_for_care
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions.append(repr(animal))
            elif animal.__class__.__name__ == "Tiger":
                tigers.append(repr(animal))
            else:
                cheetahs.append(repr(animal))
        result = [f"You have {len(self.animals)} animals", f"----- {len(lions)} Lions:"]
        result.extend(lions)
        result.append(f"----- {len(tigers)} Tigers:")
        result.extend(tigers)
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        result.extend(cheetahs)

        return "\n".join(result)

    def workers_status(self):
        caretakers = []
        keepers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                keepers.append(repr(worker))
            elif worker.__class__.__name__ == "Caretaker":
                caretakers.append(repr(worker))
            else:
                vets.append(repr(worker))
        result = [f"You have {len(self.workers)} workers", f"----- {len(keepers)} Keepers:"]
        result.extend(keepers)
        result.append(f"----- {len(caretakers)} Caretakers:")
        result.extend(caretakers)
        result.append(f"----- {len(vets)} Vets:")
        result.extend(vets)

        return "\n".join(result)

    # def add_animal(self, animal: Animal, price: int) -> str:
    #     if self.__animal_capacity <= len(self.animals):
    #         return "Not enough space for animal"
    #     if self.__budget <= price:
    #         return "Not enough budget"
    #     self.animals.append(animal)
    #     self.__budget -= price
    #     return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    # def hire_worker(self, worker: Worker):
    #     if self.__workers_capacity <= len(self.workers):
    #         return "Not enough space for worker"
    #     self.workers.append(worker)
    #     return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    #  my choices:
    # def add_animal(self, animal: Animal, price: int):
    #     if self.__budget >= price and len(self.animals) < self.__animal_capacity:
    #         if animal not in self.animals:
    #             self.animals.append(animal)
    #             self.__budget -= price
    #             return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
    #     elif self.__budget <= price and len(self.animals) < self.__animal_capacity:
    #         return "Not enough budget"
    #     return "Not enough space for animal"
    #
    # def hire_worker(self, worker: Worker) -> str:
    #     if len(self.workers) < self.__workers_capacity:
    #         self.workers.append(worker)
    #
    #         return f"{worker.name} the {worker.__class__.__name__} hired successfully"
    #     return "Not enough space for worker"

    # def animals_status(self) -> str:
    #     return self.__print_status(self.animals, "Lion", "Tiger", "Cheetah")
    #
    # def workers_status(self) -> str:
    #     return self.__print_status(self.workers, "Keeper", "Caretaker", "Vet")
    #
    # @staticmethod
    # def __print_status(category: List[Union[Animal, Worker]], *args):
    #     elements = {arg: [] for arg in args}
    #     for element in category:
    #         elements[element.__class__.__name__].append(repr(element))
    #
    #     result = [f"You have {len(category)} {str(category[0].__class__.__bases__[0].__name__).lower()}s"]
    #     for key, value in elements.items():
    #         result.append(f"----- {len(value)} {key}s:")
    #         result.extend(value)
    #
    #     return "\n".join(result)
