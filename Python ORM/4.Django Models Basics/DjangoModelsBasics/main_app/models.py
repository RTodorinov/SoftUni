from datetime import date

from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=30)
    email_address = models.EmailField()
    photo = models.URLField()
    birth_date = models.DateField()
    works_full_time = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)


class Department(models.Model):

    class Locations(models.TextChoices):  # creating choices
        SOFIA = "Sofia", "Sofia"
        PLOVDIV = "Plovdiv", "Plovdiv"
        BURGAS = "Burgas", "Burgas"
        VARNA = "Varna", "Varna"

    code = models.CharField(
        max_length=4,
        primary_key=True,  # make PK
        unique=True
    )
    name = models.CharField(
        max_length=50,
        unique=True
    )
    employees_count = models.PositiveIntegerField(
        default=1,
        verbose_name="Employees Count"  # this will see users for title
    )
    location = models.CharField(
        max_length=20,
        choices=Locations
    )
    last_edited_on = models.DateTimeField(
        auto_now=True,  # set to the current date and time every time the object is saved
        editable=False
    )


class Project(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    budget = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,  # optional
        null=True  # optional
    )

    duration_in_days = models.PositiveIntegerField(
        verbose_name="Duration in Days",
        blank=True,
        null=True
    )

    estimated_hours = models.FloatField(
        verbose_name="Estimated Hours",
        blank=True,
        null=True
    )

    start_date = models.DateField(
        default=date.today(),  # set to the current date when the object was first created.
        verbose_name="Start Date",
        blank=True,
        null=True
    )

    created_on = models.DateTimeField(
        editable=False,
        auto_now_add=True  # set to the current date and time when the object is first created.
    )

    last_edited_on = models.DateTimeField(
        auto_now_add=True,  # set to the current date and time every time the object is saved
        editable=False
    )
