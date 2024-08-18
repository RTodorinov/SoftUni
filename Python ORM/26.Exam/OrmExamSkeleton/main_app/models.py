from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator

from main_app.managers import AstronautManager
from main_app.mixins import UpdatedMixin


class Astronaut(UpdatedMixin, models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
        help_text="Full name of the astronaut"
    )
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[RegexValidator(regex=r'^\d+$', message='Phone number must contain only digits.')],
        help_text="Phone number of the astronaut"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Indicates whether the astronaut is currently active"
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        help_text="Birth date of the astronaut"
    )
    spacewalks = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)],
        help_text="Number of spacewalks the astronaut has participated in"
    )

    objects = AstronautManager()

    def __str__(self):
        return self.name


class Spacecraft(UpdatedMixin, models.Model):
    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
        help_text="Name of the spacecraft"
    )
    manufacturer = models.CharField(
        max_length=100,
        help_text="Manufacturer of the spacecraft"
    )
    capacity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Number of astronauts the spacecraft can carry"
    )
    weight = models.FloatField(
        validators=[MinValueValidator(0.0)],
        help_text="Weight of the spacecraft in kilograms"
    )
    launch_date = models.DateField(
        help_text="Launch date of the spacecraft"
    )

    def __str__(self):
        return self.name


class Mission(UpdatedMixin, models.Model):
    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed')
    ]

    name = models.CharField(
        max_length=120,
        validators=[MinLengthValidator(2)],
        help_text="Name of the mission"
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="Detailed description of the mission"
    )
    status = models.CharField(
        max_length=9,
        choices=STATUS_CHOICES,
        default='Planned',
        help_text="Status of the mission"
    )
    launch_date = models.DateField(
        help_text="Launch date of the mission"
    )
    spacecraft = models.ForeignKey(
        Spacecraft,
        on_delete=models.CASCADE,
        help_text="Spacecraft associated with the mission"
    )
    astronauts = models.ManyToManyField(
        Astronaut,
        related_name='missions',
        help_text="Astronauts participating in the mission"
    )
    commander = models.ForeignKey(
        Astronaut,
        related_name='commanded_missions',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Commander of the mission"
    )

    def __str__(self):
        return self.name
