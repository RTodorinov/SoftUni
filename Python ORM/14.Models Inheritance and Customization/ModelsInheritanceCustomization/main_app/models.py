from datetime import date

from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

# example for meta class:
# class TimeDateModel(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True


class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    sound = models.CharField(max_length=100)

    @property
    def age(self):
        today = date.today()
        age = (today.year - self.birth_date.year
               - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day)))
        return age


class Mammal(Animal):
    fur_color = models.CharField(max_length=50)


class Bird(Animal):
    wing_span = models.DecimalField(max_digits=5, decimal_places=2)


class Reptile(Animal):
    scale_type = models.CharField(max_length=50)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)

    class Meta:
        abstract = True


class ZooKeeper(Employee):
    class AnimalChoices(models.TextChoices):
        MAMMALS = 'Mammals', 'Mammals'
        BIRDS = 'Birds', 'Birds'
        REPTILES = 'Reptiles', 'Reptiles'
        OTHERS = 'Others', 'Others'
    specialty = models.CharField(max_length=10, choices=AnimalChoices.choices)
    managed_animals = models.ManyToManyField(to=Animal)

    def clean(self):
        super().clean()

        if self.specialty not in self.AnimalChoices:
            raise ValidationError("Specialty must be a valid choice.")


class BooleanChoiceField(models.BooleanField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = (
            (True, 'Available'),
            (False, 'Not Available')
        )

        kwargs['default'] = True
        super().__init__(*args, **kwargs)


class Veterinarian(Employee):
    license_number = models.CharField(max_length=10)
    availability = BooleanChoiceField()

    def is_available(self):
        return self.availability


class ZooDisplayAnimal(Animal):
    class Meta:
        proxy = True

    def display_info(self):
        return f"Meet {self.name}! Species: {self.species}, born {self.birth_date}." \
                f" It makes a noise like '{self.sound}'."

    SPECIES_AT_RISK = ["Cross River Gorilla", "Orangutan", "Green Turtle"]

    def is_endangered(self):
        danger = self.species in self.SPECIES_AT_RISK
        return f"{self.species} is at risk!" if danger \
            else f"{self.species} is not at risk."

    # def __extra_info(self):
    #     extra_info = ''
    #     print(self.__dict__)
    #     if hasattr(self, 'mammal'):
    #         extra_info = f"Its fur color is {self.mammal.fur_color}."
    #     elif hasattr(self, 'bird'):
    #         extra_info = f"Its wingspan is {self.bird.wing_span} cm."
    #     elif hasattr(self, 'reptile'):
    #         extra_info = f"Its scale type is {self.reptile.scale_type}."
    #     return extra_info
