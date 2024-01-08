food_kg = float(input()) * 1000
hay_kg = float(input()) * 1000
cover_kg = float(input()) * 1000
guinea_pig_kgs = float(input()) * 1000

cover = guinea_pig_kgs / 3
food_eaten = 0

for day in range(1, 30 + 1):
    food_eaten += 300
    food_kg -= 300

    if day % 2 == 0:
        hay = food_kg * 0.05
        hay_kg -= hay
        food_eaten += hay

    if day % 3 == 0:
        cover_kg -= cover

if food_kg > 0 and hay_kg > 0 and cover_kg > 0:
    print(f"Everything is fine! Puppy is happy! Food:"
          f" {food_kg / 1000:.2f}, "
          f"Hay: {hay_kg / 1000:.2f}, "
          f"Cover: {cover_kg / 1000:.2f}.")
else:
    print("Merry must go to the pet store!")

# food = float(input()) * 1000
# hay = float(input()) * 1000
# cover = float(input()) * 1000
# pig_weight = float(input()) * 1000
#
# # month = 30 days       hay = food * 0.05    cover = pig_weight / 3
# day = 0
#
# for i in range(1, 31):
#     day += 1
#     food -= 300
#     if day % 2 == 0:
#         hay -= food * 0.05
#     if day % 3 == 0:
#         cover -= pig_weight / 3
#
# if day == 30 and (food <= 0 or hay <= 0 or cover <= 0):
#     print("Merry must go to the pet store!")
# else:
#     print(f"Everything is fine! Puppy is happy! Food: "
#           f"{food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")

# quantity_of_food, hay, cover, pig_weight = [float(input()) * 1000 for _ in range(4)]
#
# for day in range(1, 31):
#     quantity_of_food -= 300
#
#     if day % 2 == 0 or day % 3 == 0:
#         hay -= (quantity_of_food * 0.05)
#
#     if day % 3 == 0:
#         cover -= (pig_weight / 3)
#
#     if quantity_of_food <= 0 or hay <= 0 or cover <= 0:
#         print("Merry must go to the pet store!")
#         exit()
#
# print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food / 1000:.2f}, "
#       f"Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
