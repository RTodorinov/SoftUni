money = 0

while True:
    destination = input()
    if destination == "End":
        break
    trip_cost = float(input())
    while True:
        saved_money = float(input())
        money += saved_money
        if money >= trip_cost:
            print(f"Going to {destination}!")
            money = 0
            break
