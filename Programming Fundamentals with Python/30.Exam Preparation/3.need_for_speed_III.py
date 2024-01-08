def drive(cars_dict, split_command):
    current_car_brand = split_command[1]
    current_car_distance = int(split_command[2])
    current_car_fuel = int(split_command[3])
    if current_car_fuel > cars_dict[current_car_brand]["FUEL"]:
        print("Not enough fuel to make that ride")
    else:
        cars_dict[current_car_brand]["FUEL"] -= current_car_fuel
        cars_dict[current_car_brand]["MILEAGE"] += current_car_distance
        print(f"{current_car_brand} driven for {current_car_distance} kilometers. {current_car_fuel} liters of fuel consumed.")

    if cars_dict[current_car_brand]["MILEAGE"] >= 100000:
        print(f"Time to sell the {current_car_brand}!")
        del cars_dict[current_car_brand]
    return cars_dict


def refuel(cars_dict, split_command):
    current_car_brand = split_command[1]
    current_car_fuel = int(split_command[2])
    fuel_before_refill = cars_dict[current_car_brand]["FUEL"]
    cars_dict[current_car_brand]["FUEL"] = min(cars_dict[current_car_brand]["FUEL"] + current_car_fuel, 75)
    print(f"{current_car_brand} refueled with {cars_dict[current_car_brand]['FUEL'] - fuel_before_refill} liters")
    return cars_dict


def revert(cars_dict, split_command):
    current_car_brand = split_command[1]
    current_car_kilometers = int(split_command[2])
    cars_dict[current_car_brand]["MILEAGE"] -= current_car_kilometers
    if cars_dict[current_car_brand]["MILEAGE"] < 10000:
        cars_dict[current_car_brand]["MILEAGE"] = 10000
    else:
        print(f"{current_car_brand} mileage decreased by {current_car_kilometers} kilometers")
    return cars_dict


cars = {}
number_of_cars = int(input())
for car in range(number_of_cars):
    car_brand, mileage_value, fuel_value = input().split("|")
    cars[car_brand] = {"MILEAGE": int(mileage_value), "FUEL": int(fuel_value)}

command = input()
while command != "Stop":
    command = command.split(" : ")
    action = command[0]
    if action == "Drive":
        cars = drive(cars, command)
    elif action == "Refuel":
        cars = refuel(cars, command)
    elif action == "Revert":
        cars = revert(cars, command)
    command = input()

for car_brand, values in cars.items():
    print(f"{car_brand} -> Mileage: {values['MILEAGE']} kms, Fuel in the tank: {values['FUEL']} lt.")
