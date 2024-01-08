bottles_count = int(input())

bottle = 750
dish = 5
pot = 15
detergent_total = bottles_count * bottle
total_dishes = total_pots = 0
cycle = 1

while True:
    dishes = input()
    if dishes == "End":
        break

    new_dishes = int(dishes)
    dishes = pots = 0
    if cycle % 3 == 0:
        detergent = pot
        pots = new_dishes

    else:
        detergent = dish
        dishes = new_dishes

    detergent_total -= detergent * new_dishes
    if detergent_total < 0:
        print(f"Not enough detergent, {abs(detergent_total)} ml. more necessary!")
        exit()
    total_dishes += dishes
    total_pots += pots
    cycle += 1

print(f"Detergent was enough!")
print(f"{total_dishes} dishes and {total_pots} pots were washed.")
print(f"Leftover detergent {detergent_total} ml.")
