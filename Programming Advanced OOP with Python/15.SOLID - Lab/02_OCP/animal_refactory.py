from abc import ABC, abstractmethod
from typing import List


class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass


class Dog(Animal):
    def make_sound(self) -> str:
        return "woof-woof"


class Cat(Animal):
    def make_sound(self) -> str:
        return "meow"


class Bird(Animal):
    def make_sound(self) -> str:
        return "pi-pi"


def animal_sound(animals_: List[Animal]) -> None:
    for animal in animals_:
        print(animal.make_sound())


animals = [Dog(), Cat(), Bird()]
animal_sound(animals)
