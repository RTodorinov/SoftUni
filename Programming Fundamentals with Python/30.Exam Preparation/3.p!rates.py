def plunder(event, current_command):
    city = events_data[1]
    people_killed = int(events_data[2])
    stolen_gold = int(events_data[3])
    print(f"{city} plundered! {stolen_gold} gold stolen, {people_killed} citizens killed.")
    cities[city]["population"] -= people_killed
    cities[city]["gold"] -= stolen_gold
    if cities[city]["population"] <= 0 or cities[city]["gold"] <= 0:
        del cities[city]
        print(f"{city} has been wiped off the map!")
    return cities


def prosper(event, current_command):
    city = events_data[1]
    increased_gold = int(events_data[2])
    if increased_gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        cities[city]["gold"] += increased_gold
        print(f"{increased_gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")
    return cities


data = input()
cities = {}
while data != "Sail":
    data = data.split("||")
    city = data[0]
    population = int(data[1])
    gold = int(data[2])

    if city not in cities:
        cities[city] = {"population": population, "gold": gold}
    else:
        cities[city]["population"] += population
        cities[city]["gold"] += gold

    data = input()

events_data = input()

while events_data != "End":
    events_data = events_data.split("=>")
    command = events_data[0]
    if command == "Plunder":
        cities = plunder(cities, events_data)
    elif command == "Prosper":
        cities = prosper(cities, events_data)

    events_data = input()

if not cities:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
for town, values in cities.items():
    print(f"{town} -> Population: {values['population']} citizens, Gold: {values['gold']} kg")
