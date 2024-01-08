from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass

    @abstractmethod
    def create_table(self):
        pass


class Chair:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Sofa:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Table:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return Chair('victorian chair')

    def create_sofa(self):
        return Sofa('victorian sofa')

    def create_table(self):
        return Table('victorian table')


class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair('modern chair')

    def create_sofa(self):
        return Sofa('modern sofa')

    def create_table(self):
        return Table('modern table')


class FuturisticFactory(AbstractFactory):
    style = "Futuristic"

    def create_chair(self):
        return Chair(f'{self.style} chair')

    def create_sofa(self):
        return Sofa(f'{self.style} sofa')

    def create_table(self):
        return Table(f'{self.style} table')
    