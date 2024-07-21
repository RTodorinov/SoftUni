import os
import django
from django.db.models import QuerySet, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


# from django.core.management import call_command -> to automate migrations
# call_command('makemigrations')
# call_command('migrate')

# Import your models here


from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


# Create queries within functions


def create_pet(name: str, species: str) -> str:
    pet = Pet.objects.create(  # create make pet and save it to the database in one go
        name=name,
        species=species,
    )

    # pet = Pet(name=name, species=species) -> create instance of pet
    # between we can do other things
    # pet.save() -> then save it to database

    return f"{pet.name} is a very cute {pet.species}!"


# print(create_pet('Buddy', 'Dog'))
# print(create_pet('Whiskers', 'Cat'))
# print(create_pet('Rocky', 'Hamster'))


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool) -> str:
    artifact = Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical,
    )

    return f"The artifact {artifact.name} is {artifact.age} years old!"


def rename_artifact(artifact: Artifact, new_name: str) -> None:
    # Artifact.objects.filter(is_magical=True, age__gt=250).update(name=new_name) -> for all artifacts
    # Artifact.objects.filter(is_magical=True, age__gt=250, pk=artifact.pk).update(name=new_name) -> for one artifact
    if artifact.is_magical and artifact.age > 250:  # here this is optimal choice
        artifact.name = new_name
        artifact.save()
    else:
        artifact.name = artifact.name
        artifact.save()


def delete_all_artifacts() -> None:
    Artifact.objects.all().delete()


# print(create_artifact('Ancient Sword', 'Lost Kingdom', 500, 'A legendary sword with a rich history', True))
# artifact_object = Artifact.objects.get(name='Ancient Sword')
# rename_artifact(artifact_object, 'Ancient Shield')
# print(artifact_object.name)
# print(create_artifact('Crystal Amulet', 'Mystic Forest', 300, 'A magical amulet believed to bring good fortune', True))
# artifact_object = Artifact.objects.get(name='Crystal Amulet')
# rename_artifact(artifact_object, 'Stone Ring')
# print(artifact_object.name)
# print(create_artifact('Stone Tablet', 'Ruined Temple', 1000, 'An ancient tablet covered in mysterious inscriptions', False))
# artifact_object = Artifact.objects.get(name='Crystal Amulet')
# rename_artifact(artifact_object, 'Iron Goblet')
# print(artifact_object.name)

# delete_all_artifacts()


def show_all_locations() -> str:
    locations = Location.objects.all().order_by('-id')

    return "\n".join(str(l) for l in locations)


# print(show_all_locations())


def create_location(name: str, region: str, population: int, description: str, is_capital: bool) -> str:
    location = Location.objects.create(  # create make pet and save it to the database in one go
        name=name,
        region=region,
        population=population,
        description=description,
        is_capital=is_capital,
    )
    return f"The base is populated with info"


# print(create_location('Sofia', 'Sofia Region', 1329000, 'The capital of Bulgaria and the largest city in the country', False))
# print(create_location('Plovdiv', 'Plovdiv Region', 346942, 'The second-largest city in Bulgaria with a rich historical heritage', False))
# print(create_location('Varna', 'Varna Region', 330486, 'A city known for its sea breeze and beautiful beaches on the Black Sea', False))


def new_capital() -> None:
    # Location.objects.filter(id=1).update(is_capital=True)
    location = Location.objects.first()
    location.is_capital = True
    location.save()


# print(new_capital())


def get_capitals() -> QuerySet:
    return Location.objects.filter(is_capital=True).values('name')


# print(get_capitals())


def delete_first_location() -> None:
    Location.objects.first().delete()


# delete_first_location()


def apply_discount() -> None:
    cars = Car.objects.all()

    for car in cars:
        percentage_off = sum(int(digit) for digit in str(car.year)) / 100  # 2014 => "2014" => 2 + 0 + 1 + 4 => 7 / 100 => 0.07
        discount = float(car.price) * percentage_off  # 1000 * 0.07 => 70
        car.price_with_discount = float(car.price) - discount  # 1000 - 70 => 930
        car.save()


# apply_discount()


def create_car(model: str,	year: int,	color: str, price: float, price_with_discount: float) -> str:
    cars = Car.objects.create(
        model=model,
        year=year,
        color=color,
        price=price,
        price_with_discount=price_with_discount
    )
    return f"The base is populated with info"


# print(create_car('Mercedes C63 AMG', 2019,	'white', 120000.00, 0))
# print(create_car('Audi Q7 S line',	2023,	'black',	183900.00, 0))
# print(create_car('Chevrolet Corvette',	2021,	'dark grey',	199999.00, 0))


def get_recent_cars() -> QuerySet:
    return Car.objects.filter(year__gt=2020).values('model', 'price_with_discount')


# print(get_recent_cars())


def delete_last_car() -> None:
    Car.objects.last().delete()


# delete_last_car()


def show_unfinished_tasks() -> str:
    unfinished_tasks = Task.objects.filter(is_finished=False)

    return "\n".join(str(t) for t in unfinished_tasks)


# print(show_unfinished_tasks())


def create_task(title: str,	description: str, due_date: str, is_finished: bool):
    tasks = Task.objects.create(
        title=title,
        description=description,
        due_date=due_date,
        is_finished=is_finished,
    )


# print(create_task('Sample Task', 'This is a sample task description', '2023-10-31', False))


def complete_odd_tasks() -> None:
    # for task in Task.objects.all():
    #     if task.id % 2 == 1:
    #         task.is_finished = True
    #         task.save()
    #  better version bellow
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 == 1:
            task.is_finished = True

    Task.objects.bulk_update(tasks, ['is_finished'])


# complete_odd_tasks()

def encode_and_replace(text: str, task_title: str) -> None:
    decoded_text = ''.join(chr(ord(symbol) - 3) for symbol in text)
    Task.objects.filter(title=task_title).update(description=decoded_text)

    # tasks_with_matching_title = Task.objects.filter(title=task_title)
    # for task in tasks_with_matching_title:
    #     task.description = decoded_text
    #     # task.save()  # choice one
    #
    # Task.objects.bulk_update(tasks_with_matching_title, ['description'])


# encode_and_replace("Zdvk#wkh#glvkhv$", "Sample Task")


def get_deluxe_rooms():
    deluxe_rooms = HotelRoom.objects.filter(room_type="Deluxe")
    even_deluxe_rooms = [str(r) for r in deluxe_rooms if r.id % 2 == 0]

    return "\n".join(even_deluxe_rooms)


# print(get_deluxe_rooms())


def create_room(room_number: int, room_type: str, capacity: int, amenities: str, price_per_night: float, is_reserved: bool):
    rooms = HotelRoom.objects.create(
        room_number=room_number,
        room_type=room_type,
        capacity=capacity,
        amenities=amenities,
        price_per_night=price_per_night,
        is_reserved=is_reserved,
    )


# create_room(401, 'Standard', 2, 'Tv', 100.00, False)
# create_room(501, 'Deluxe', 3, 'Wi-Fi', 200.00, False)
# create_room(601, 'Deluxe', 6, 'Jacuzzi', 400.00, False)
# create_room(701, 'Deluxe', 8, 'Sauna', 500.00, True)


# def increase_room_capacity() -> None:
#     rooms = HotelRoom.objects.all().order_by('id')
#     previous_room_capacity = None
#     for room in rooms:
#         if not room.is_reserved:
#             continue
#         if previous_room_capacity is not None:
#             room.capacity += previous_room_capacity
#         else:
#             room.capacity += room.id
#
#         previous_room_capacity = room.capacity
#
#     HotelRoom.objects.bulk_update(rooms, ['capacity'])

def increase_room_capacity():
    rooms = HotelRoom.objects.all().order_by('id')

    previous_capacity = 0

    for i, room in enumerate(rooms):
        if room.is_reserved:
            if i == 0 or not rooms[i - 1].is_reserved:
                room.capacity += room.id
            else:
                room.capacity += previous_capacity

            room.save()

        previous_capacity = room.capacity

# increase_room_capacity()


def reserve_first_room() -> None:
    first_room = HotelRoom.objects.first()
    first_room.is_reserved = True
    first_room.save()


def delete_last_room() -> None:
    room = HotelRoom.objects.last()
    if not room.is_reserved:
        room.delete()


new_character = Character(
    name="Aragorn",
    class_name="Warrior",
    level=10,
    strength=15,
    dexterity=12,
    intelligence=10,
    hit_points=100,
    inventory="Sword, Shield, Healing Potion"
)

# new_character.save()


character1 = Character.objects.create(
    name='Gandalf',
    class_name='Mage',
    level=10,
    strength=15,
    dexterity=20,
    intelligence=25,
    hit_points=100,
    inventory='Staff of Magic, Spellbook',
)


character2 = Character.objects.create(
    name='Hector',
    class_name='Warrior',
    level=12,
    strength=30,
    dexterity=15,
    intelligence=10,
    hit_points=150,
    inventory='Sword of Troy, Shield of Protection',
)

# character1.save()
# character2.save()


def update_characters() -> None:
    Character.objects.filter(class_name="Mage").update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7
    )
    Character.objects.filter(class_name="Warrior").update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4
    )
    Character.objects.filter(class_name__in=["Assassin", "Scout"]).update(
        inventory="The inventory is empty"
    )
    # UPDATE table
    # SET
    # intelligence = intelligence - 7,
    # level = level + 3
    # WHERE class_name = "Mage"


# update_characters()


def fuse_characters(first_character: Character, second_character: Character) -> None:
    fusion_name = first_character.name + " " + second_character.name
    class_name = "Fusion"
    level = (first_character.level + second_character.level) // 2
    strength = (first_character.strength + second_character.strength) * 1.2
    dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    hit_points = first_character.hit_points + second_character.hit_points
    if first_character.class_name in ["Mage", "Scout"]:
        inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        inventory = "Dragon Scale Armor, Excalibur"
    Character.objects.create(
        name=fusion_name,
        class_name=class_name,
        level=level,
        strength=strength,
        dexterity=dexterity,
        intelligence=intelligence,
        hit_points=hit_points,
        inventory=inventory
    )

    first_character.delete()
    second_character.delete()


# fuse_characters(character1, character2)


def grand_dexterity() -> None:
    Character.objects.update(dexterity=30)


def grand_intelligence() -> None:
    Character.objects.update(intelligence=40)


def grand_strength() -> None:
    Character.objects.update(strength=50)


def delete_characters() -> None:
    Character.objects.filter(inventory="The inventory is empty").delete()
