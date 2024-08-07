# Generated by Django 5.0.4 on 2024-07-01 20:12

from django.db import migrations


def update_rarity(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')

    for item in item_model.objects.all():
        if item.price <= 10:
            item.rarity = "Rare"
        elif item.price <= 20:
            item.rarity = "Very Rare"
        elif item.price <= 30:
            item.rarity = "Extremely Rare"
        else:
            item.rarity = "Mega Rare"

        item.save()  # TODO: optimize


def reverse_rarity(apps, schema_editor):
    item_model = apps.get_model('main_app', 'Item')

    for item in item_model.objects.all():
        item.rarity = item_model._meta.get_field('rarity').default
        item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_item'),
    ]

    operations = [
        migrations.RunPython(update_rarity, reverse_rarity)
    ]
