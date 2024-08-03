# Generated by Django 5.0.4 on 2024-07-25 07:58

import main_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=2, validators=[main_app.validators.RangeValueValidator(0, 10, message='Value must be between 0.0 and 10.0')]),
        ),
    ]