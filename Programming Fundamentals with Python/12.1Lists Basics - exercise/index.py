# primer 1
# input_elements = input().split()
# result = []
#
# for element in input_elements:
#     number = int(element)
#     result.append(-number)
#
# print(result)

# primer 2
# factor = int(input())
# count = int(input())
#
# result = []
#
# for num in range(1, count + 1):
#     result.append(num * factor)
#
# print(result)

# primer 2.2
# factor = int(input())
# count = int(input())
#
# result = []
# current_number = factor
#
# for num in range(1, count + 1):
#     result.append(current_number)
#     current_number += factor
#
# print(result)

# primer 2.3
# factor = int(input())
# count = int(input())
#
# result = []
#
# for i in range(factor, factor * count + 1, factor):
#     result.append(i)
#
# print(result)

# primer 2.4
# factor = int(input())
# count = int(input())
#
# print(list(range(factor, factor * count + 1, factor)))

# task 3
# cards = input().split()
# first_team = []
# second_team = []
#
# should_terminate = False
# for card in cards:
#     if card in first_team or card in second_team:
#         continue
#
#     card_args = card.split("-")
#     team_name = card_args[0]
#     player_number = card_args[1]
#
#     is_first_team = team_name == "A"  # True or False
#     if is_first_team:
#         first_team.append(card)
#     else:
#         second_team.append(card)
#     if len(first_team) > 4 or len(second_team) > 4:
#         should_terminate = True
#         break
#
# print(f"Team A - {11 - len(first_team)}; Team B - {11 - len(second_team)}")
# if should_terminate:
#     print("Game was terminated")

# cards = input().split()
# first_team_A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# second_team_B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# should_terminate = False
# for card in cards:
#     card_args = card.split("-")
#     team_name = card_args[0]
#     player_number = int(card_args[1])
#
#     if team_name == "A":
#         if player_number in first_team_A:
#             first_team_A.remove(player_number)
#     elif team_name == "B":
#         if player_number in second_team_B:
#             second_team_B.remove(player_number)
#
#     if len(first_team_A) < 7 or len(second_team_B) < 7:
#         should_terminate = True
#         break
#
# print(f"Team A - {len(first_team_A)}; Team B - {len(second_team_B)}")
# if should_terminate:
#     print("Game was terminated")

# task 4
# numbers = input().split(", ")
# beggars_count = int(input())
#
# beggars = [0] * beggars_count
#
# for idx in range(len(numbers)):
#     beggar_idx = idx % beggars_count
#     num = int(numbers[idx])
#     beggars[beggar_idx] += num
#
# print(beggars)

# numbers = input().split(", ")
# beggars_count = int(input())
#
# beggars = [0] * beggars_count
# pointer = 0
# for idx in range(len(numbers)):
#     num = int(numbers[idx])
#     beggars[pointer] += num
#     pointer += 1
#     if pointer >= beggars_count:
#         pointer = 0
#
# print(beggars)

# task 5
# cards = input().split()
# count_shuffles = int(input())
#
# for _ in range(count_shuffles):
#     first_half = []
#     second_half = []
#
#     for idx in range(1, len(cards) - 1):
#         card = cards[idx]
#         if idx < len(cards) / 2:
#             first_half.append(card)
#         else:
#             second_half.append(card)
#
#     shuffled = []
#     first_part_idx = 0
#     second_part_idx = 0
#     for idx in range(len(first_half) * 2):
#         if idx % 2 == 0:
#             shuffled.append(second_half[second_part_idx])
#             second_part_idx += 1
#         else:
#             shuffled.append(first_half[first_part_idx])
#             first_part_idx += 1
#
#     cards = [cards[0]] + shuffled + [cards[-1]]
#
# print(cards)

# обръщане на лист от стринговете в числа
# numbers_as_str = input().split()  # вкарваме в лист числата като стрингове
# numbers = []
#
# for el in numbers_as_str:
#     numbers.append(int(el))  # обръщаме стринговете в числа от списъка
# print(numbers)

# numbers = [int(x) for x in input().split()]# кратък запис на горното
# print(numbers)
# работи само за числа

# task 6
# numbers = [int(x) for x in input().split()]
# count = int(input())
#
# for _ in range(count):
#     min_number = min(numbers)
#     numbers.remove(min_number)
#
# print(", ".join([str(x) for x in numbers]))

# task 6.1
# numbers = [int(x) for x in input().split()]
# count = int(input())
#
# for _ in range(count):
#     min_number = min(numbers)
#     numbers.remove(min_number)
#
# for idx in range(len(numbers)):
#     num = numbers[idx]
#     if idx == len(numbers) - 1:
#         print(num)
#     else:
#         print(num, end=", ")

# task 6.2
# numbers = [int(x) for x in input().split()]
# count = int(input())
#
# sorted_nums = sorted(numbers)
#
# for idx in range(count):
#     numbers.remove(sorted_nums[idx])
#
# print(numbers)

# task 8
# cells = input().split("#")
# water = int(input())
# processed_cells = []
# total_fire = 0
# for cell in cells:
#     cell_args = cell.split(" = ")
#     level = cell_args[0]
#     value = int(cell_args[1])
#
#     if level == "High" and (value < 81 or value > 125):
#         continue
#     if level == "Medium" and (value < 51 or value > 80):
#         continue
#     if level == "Low" and (value < 1 or value > 50):
#         continue
#     if value > water:
#         continue
#
#     water -= value
#     total_fire += value
#     processed_cells.append(value)
#
# print("Cells:")
# for cell in processed_cells:
#     print(f" - {cell}")
# effort = total_fire * 0.25
# print(f"Effort: {effort:.2f}")
# print(f"Total Fire: {total_fire}")

# task 7
# gifts = input().split()
# while True:
#     line = input()
#     if line == "No Money":
#         break
#     command_args = line.split()
#     command = command_args[0]
#     gift = command_args[1]
#
#     if command == "OutOfStock":
#         for idx in range(len(gifts)):
#             if gifts[idx] == gift:
#                 gifts[idx] = "None"
#     elif command == "Required":
#         idx = int(command_args[2])
#         if 0 <= idx < len(gifts):
#             gifts[idx] = gift
#     elif command == "JustInCase":
#         gifts[-1] = gift
#
# for gift in gifts:
#     if gift == "None":
#         continue
#     print(gift, end=" ")

my_list = [1, 2, 3, 5, 7, 6, 8, 2, 9, 4]
my_list.sort(reverse=True)
print(my_list)

print(my_list.pop())
print(my_list)

print(my_list.pop(0))
print(my_list)

my_list.insert(5, "Rosen")
print(my_list)

number = my_list.index(2)
print(number)

list2 = [3, 3, 3, "proba"]
my_list.append(list2.pop())
print(my_list)

my_list_2 = my_list
my_list_2.pop()
print(my_list_2)
print(my_list)

my_list_2 = my_list.copy()
my_list_2.pop()
print(my_list_2)
print(my_list)

#  фор цикъл през листа за намиране на индекса на повтарящ се елемент "apple"
fruits = ["apple", "apple", "banana", "cherry", "apple"]
index = (i for i, value in enumerate(fruits) if value == "apple")
print(list(index))

numbers = [2, 7, 11, 15]
target_number = 9
list_of_found_indexes = []
for index in range(0, len(numbers)-1):
    current_sum = int(numbers[index]) + int(numbers[index+1])
    if current_sum == target_number:
        list_of_found_indexes.append(index)
        list_of_found_indexes.append(index+1)
        break
print(list_of_found_indexes)

# съкратени записи за обхождане на лист и обръщането му в инт.
nums_as_strings = ["1", "2", "3"]
nums = list(map(int, nums_as_strings))
nums1 = [int(el) for el in nums_as_strings]
print(nums)
print(nums1)

# съкратени записи за сортиране чрез filter и % за извеждане на четно или нечетно число
nums_as_int = [1, 2, 3, 4]
nums = list(filter(lambda x: x % 2 == 0, nums_as_int))
nums1 = [el for el in nums_as_int if el % 2 == 0]
print(nums)
print(nums1)
# съкратен запис и ползване на lambda и map  за да увеличим всеки елемент с 1
nums_as_int = [1, 2, 3, 4]
nums = map(lambda x: x + 1, nums_as_int)
for el in nums:
    print(el)


# 1

list_of_numbers = input().split()
opposite_numbers = []
for element in list_of_numbers:
    current_number = -int(element)
    opposite_numbers.append(current_number)
print(opposite_numbers)

# 2
factor = int(input())
count = int(input())
list_of_numbers = []
for multiplier in range(1, count + 1):
    list_of_numbers.append(factor * multiplier)
print(list_of_numbers)

# 3

team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
players_sent_off = input().split()
game_was_terminated = False
for player in players_sent_off:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        game_was_terminated = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_was_terminated:  # if game_was_terminated == True:
    print("Game was terminated")

# 4

money_as_string = input().split(", ")
number_of_beggars = int(input())
money_as_digits = []
for element in money_as_string:
    money_as_digits.append(int(element))
final_sums = []
start_index = 0
while start_index < number_of_beggars:
    sum_for_current_beggar = 0
    for current_index in range(start_index, len(money_as_digits), number_of_beggars):
        sum_for_current_beggar += money_as_digits[current_index]
    final_sums.append(sum_for_current_beggar)
    start_index += 1
print(final_sums)

# 5

deck_of_cards = input().split()
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck:]
    for card_index in range(len(right_part)):
        final_deck.append(left_part[card_index])
        final_deck.append(right_part[card_index])
    deck_of_cards = final_deck
print(final_deck)

# 8


cells = input().split("#")
amount_of_water = int(input())
total_fire = 0
total_effort = 0
fire_out_cells = []
high = range(81, 125 + 1)
medium = range(51, 80 + 1)
low = range(1, 50 + 1)
for cell in cells:
    type_of_fire, cell_value = cell.split(" = ")
    cell_value = int(cell_value)
    cell_is_valid = False
    if type_of_fire == "High":
        if cell_value in high:
            cell_is_valid = True
    elif type_of_fire == "Medium":
        if cell_value in medium:
            cell_is_valid = True
    elif type_of_fire == "Low":  # else:
        if cell_value in low:
            cell_is_valid = True
    if cell_is_valid:
        if amount_of_water >= cell_value:
            amount_of_water -= cell_value
            fire_out_cells.append(cell_value)
            total_fire += cell_value
            total_effort += cell_value * 0.25
print("Cells:")
for fire_out_cell in fire_out_cells:
    print(f"- {fire_out_cell}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")

# 9

items = input().split("|")
budget = float(input())
sell_prices = []
profit = 0
train_ticket = 150
for item in items:
    type, buying_price = item.split("->")
    buying_price = float(buying_price)
    price_is_valid = False
    if type == "Clothes":
        if buying_price <= 50.00:
            price_is_valid = True
    elif type == "Shoes":
        if buying_price <= 35.00:
            price_is_valid = True
    elif type == "Accessories":
        if buying_price <= 20.50:
            price_is_valid = True
    if price_is_valid:
        if budget >= buying_price:
            budget -= buying_price
            sell_price = buying_price * 1.40
            profit += sell_price - buying_price
            sell_prices.append(sell_price)
# Option 1
for sell_price in sell_prices:
    print(f"{sell_price:.2f}", end=" ")
print()

# Option 2
# print(" ".join([f"{sell_price:.2f}" for sell_price in sell_prices]))

# Option 3
# sell_prices_as_string = []
# for sell_price in sell_prices:
#     sell_prices_as_string.append(f"{sell_price:.2f}")
# print(" ".join(sell_prices_as_string))

print(f"Profit: {profit:.2f}")
total_income = budget + sum(sell_prices)
if total_income >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")

# 10

events = input().split("|")
total_energy = 100
total_coins = 100
factory_is_open = True
for event in events:
    event_items = event.split("-")
    type_of_event = event_items[0]
    event_value = int(event_items[1])
    if type_of_event == "rest":
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == "order":
        if total_energy >= 30:  # order can be completed
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            factory_is_open = False
            break
if factory_is_open:  # if factory is open == True
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
else:
    print(f"Closed! Cannot afford {type_of_event}.")

my_list = [1, 8, 4, 89, 43, 2, 132, 2, 2, "Gosho", "gosho"]

# my_list.sort(reverse=True)
# print(my_list)
#
# my_list.pop()
# print(my_list)
# my_list.pop(2)
# print(my_list)
# my_list.append(my_list.pop(2))
# print(my_list)


# my_list.insert(3, "Atanas")
# print(my_list)

# number = my_list.index(2)
# print(number)
#
# repetition = my_list.count(2)
# print(repetition)
#
# my_list.reverse()
# print(my_list)
# print(my_list[::-1])
#
# del my_list[3]
# print(my_list)
#
my_list.remove("Gosho")
print(my_list)
my_list.remove("Pesho")
print(my_list)

