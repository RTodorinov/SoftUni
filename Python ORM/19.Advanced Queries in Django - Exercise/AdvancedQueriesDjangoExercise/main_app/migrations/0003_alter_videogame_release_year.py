# Generated by Django 5.0.4 on 2024-07-25 08:10

import main_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_videogame_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='release_year',
            field=models.PositiveIntegerField(validators=[main_app.validators.RangeValueValidator(1990, 2023, message='The release year must be between 1990 and 2023')]),
        ),
    ]
