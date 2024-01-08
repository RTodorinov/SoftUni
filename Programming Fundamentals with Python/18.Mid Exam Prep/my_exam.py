#
# number_of_cities = int(input())
# total_profit = 0
# for city in range(1, number_of_cities + 1):
#     name_of_the_city = input()
#     income_current_city = float(input())
#     current_expenses = float(input())
#     if city % 5 == 0:
#         income_current_city *= 0.90
#     elif city % 3 == 0:
#         current_expenses *= 1.5
#     profit = income_current_city - current_expenses
#     total_profit += profit
#     print(f"In {name_of_the_city} Burger Bus earned {profit:.2f} leva.")
#
# print(f"Burger Bus total profit: {total_profit:.2f} leva.")

#
# friends = input().split(", ")
# command = input()
#
# while command != "Report":
#     parts = command.split()
#     action = parts[0]
#
#     if action == "Change":
#         index = int(parts[1])
#         new_name = parts[2]
#         if 0 <= index < len(friends):
#             print(f"{friends[index]} changed his username to {new_name}.")
#             friends[index] = new_name
#
#     else:
#         name_or_index = parts[-1]
#         if action == "Blacklist":
#             if name_or_index in friends:
#                 name_index = friends.index(name_or_index)
#                 friends[name_index] = "Blacklisted"
#                 print(f"{name_or_index} was blacklisted.")
#             else:
#                 print(f"{name_or_index} was not found.")
#         elif action == "Error":
#             index = int(name_or_index)
#             if 0 <= index < len(friends) and friends[index] != "Lost" and friends[index] != "Blacklisted":
#                 print(f"{friends[index]} was lost due to an error.")
#                 friends[index] = "Lost"
#     command = input()
#
# print(f"Blacklisted names: {friends.count('Blacklisted')}")
# print(f"Lost names: {friends.count('Lost')}")
# print(*friends)


# price_ratings = [int(x) for x in input().split(", ")]
# entry_point = int(input())
# type_of_items = input()
#
#
# def calculate_damage(price_ratings, entry_point, item_type):
#     ratings = price_ratings.copy()
#     entry_rating = ratings.pop(entry_point)
#
#     ratings_left = ratings[:entry_point]
#     ratings_right = ratings[entry_point:]
#
#     if item_type == "cheap":
#         damage_left = sum(r for r in ratings_left if r < entry_rating)
#         damage_right = sum(r for r in ratings_right if r < entry_rating)
#     else:
#         damage_left = sum(r for r in ratings_left if r >= entry_rating)
#         damage_right = sum(r for r in ratings_right if r >= entry_rating)
#
#     if damage_left >= damage_right:
#         return f"Left - {damage_left}"
#     else:
#         return f"Right - {damage_right}"
#
#
# result = calculate_damage(price_ratings, entry_point, type_of_items)
# print(result)

# friends = input().split(", ")
# command = input()
#
# while command != "Report":
#     parts = command.split()
#     action = parts[0]
#
#     if action == "Change":
#         index = int(parts[1])
#         new_name = parts[2]
#         if 0 <= index < len(friends):
#             print(f"{friends[index]} changed his username to {new_name}.")
#             friends[index] = new_name
#
#     else:
#         name_or_index = parts[-1]
#         if action == "Blacklist":
#             if name_or_index in friends:
#                 name_index = friends.index(name_or_index)
#                 friends[name_index] = "Blacklisted"
#                 print(f"{name_or_index} was blacklisted.")
#             else:
#                 print(f"{name_or_index} was not found.")
#         elif action == "Error":
#             index = int(name_or_index)
#             if 0 <= index < len(friends) and friends[index] != "Lost" and friends[index] != "Blacklisted":
#                 print(f"{friends[index]} was lost due to an error.")
#                 friends[index] = "Lost"
#     command = input()
#
# print(f"Blacklisted names: {friends.count('Blacklisted')}")
# print(f"Lost names: {friends.count('Lost')}")
# print(*friends)
