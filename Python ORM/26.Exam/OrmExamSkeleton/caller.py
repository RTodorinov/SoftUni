import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Astronaut, Mission, Spacecraft
from django.db.models import Count, Q, Sum, F, Avg
from django.db.models.functions import Coalesce


def get_astronauts(search_string=None):
    if search_string is None:
        return ""

    search_string = search_string.strip()
    astronauts = Astronaut.objects.filter(
        Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)
    ).order_by('name')

    if not astronauts.exists():
        return ""

    result = []
    for astronaut in astronauts:
        status = "Active" if astronaut.is_active else "Inactive"
        result.append(f"Astronaut: {astronaut.name}, phone number: {astronaut.phone_number}, status: {status}")

    return "\n".join(result)


def get_top_astronaut():
    astronauts = Astronaut.objects.get_astronauts_by_missions_count()

    if not astronauts.exists() or astronauts.first().mission_count == 0:
        return "No data."

    top_astronaut = astronauts.first()
    return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.mission_count} missions."

# def get_top_astronaut():
#     astronauts = Astronaut.objects.annotate(mission_count=Count('missions')).order_by('-mission_count', 'phone_number')
#
#     if not astronauts.exists() or astronauts.first().mission_count == 0:
#         return "No data."
#
#     top_astronaut = astronauts.first()
#     return f"Top Astronaut: {top_astronaut.name} with {top_astronaut.mission_count} missions."


def get_top_commander():
    commanders = Astronaut.objects.annotate(commanded_missions_count=Count('commanded_missions')).order_by(
        '-commanded_missions_count', 'phone_number')

    if not commanders.exists() or commanders.first().commanded_missions_count == 0:
        return "No data."

    top_commander = commanders.first()
    return f"Top Commander: {top_commander.name} with {top_commander.commanded_missions_count} commanded missions."


def get_last_completed_mission():
    last_completed_mission = Mission.objects.filter(status='Completed').order_by('-launch_date').first()

    if not last_completed_mission:
        return "No data."

    commander_name = last_completed_mission.commander.name if last_completed_mission.commander else "TBA"
    astronauts = last_completed_mission.astronauts.order_by('name')
    astronaut_names = ", ".join([astronaut.name for astronaut in astronauts])
    total_spacewalks = astronauts.aggregate(total=Coalesce(Sum('spacewalks'), 0))['total']

    return (f"The last completed mission is: {last_completed_mission.name}. "
            f"Commander: {commander_name}. "
            f"Astronauts: {astronaut_names}. "
            f"Spacecraft: {last_completed_mission.spacecraft.name}. "
            f"Total spacewalks: {total_spacewalks}.")


def get_most_used_spacecraft():
    most_used_spacecraft = Spacecraft.objects.annotate(num_missions=Count('mission')).order_by('-num_missions',
                                                                                               'name').first()

    if not most_used_spacecraft or most_used_spacecraft.num_missions == 0:
        return "No data."

    unique_astronauts = Astronaut.objects.filter(missions__spacecraft=most_used_spacecraft).distinct().count()

    return (f"The most used spacecraft is: {most_used_spacecraft.name}, "
            f"manufactured by {most_used_spacecraft.manufacturer}, "
            f"used in {most_used_spacecraft.num_missions} missions, "
            f"astronauts on missions: {unique_astronauts}.")


def decrease_spacecrafts_weight():
    affected_spacecrafts = Spacecraft.objects.filter(
        mission__status='Planned',
        weight__gte=200.0
    ).distinct()

    if not affected_spacecrafts.exists():
        return "No changes in weight."

    num_of_spacecrafts_affected = affected_spacecrafts.count()

    affected_spacecrafts.update(weight=F('weight') - 200.0)

    avg_weight = Spacecraft.objects.aggregate(avg_weight=Avg('weight'))['avg_weight']

    return (f"The weight of {num_of_spacecrafts_affected} spacecrafts has been decreased. "
            f"The new average weight of all spacecrafts is {avg_weight:.1f}kg")
