# 1.1 Computer Store
#
# total_price_net = 0
# special_customer = False
#
# while True:
#     command = input()
#
#     if command == "regular" or command == "special":
#         if command == "special":
#             special_customer = True
#         break
#
#     price_without_tax = float(command)
#
#     if price_without_tax < 0:
#         print("Invalid price!")
#     else:
#         total_price_net += price_without_tax
#
# if total_price_net:
#     # total_price_net != 0
#     total_price_with_tax = total_price_net * 1.20
#     tax = total_price_with_tax - total_price_net
#     if special_customer:
#         total_price_with_tax *= 0.90
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {total_price_net:.2f}$")
#     print(f"Taxes: {tax:.2f}$\n-----------")  # \n - new line
#     print(f"Total price: {total_price_with_tax:.2f}$")
# else:
#     print("Invalid order!")
#
# 1.2
#
# total_price_net = 0
# special_customer = False
#
# command = input()
#
# while command != "regular" and command != "special":
#
#     price_without_tax = float(command)
#
#     if price_without_tax < 0:
#         print("Invalid price!")
#     else:
#         total_price_net += price_without_tax
#
#     command = input()
#
#     if command == "special":
#         special_customer = True
#
# if total_price_net:
#     # total_price_net != 0
#     total_price_with_tax = total_price_net * 1.20
#     tax = total_price_with_tax - total_price_net
#     if special_customer:
#         total_price_with_tax *= 0.90
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {total_price_net:.2f}$")
#     print(f"Taxes: {tax:.2f}$\n-----------")  # \n - new line
#     print(f"Total price: {total_price_with_tax:.2f}$")
# else:
#     print("Invalid order!")
#
# 1.3
#
#
# def finding_total_price(total_price, price):
#     if price < 0:
#         print("Invalid price!")
#     else:
#         total_price += price
#     return total_price
#
#
# total_price_net = 0
# special_customer = False
#
# command = input()
#
# while command != "regular" and command != "special":
#
#     price_without_tax = float(command)
#
#     total_price_net = finding_total_price(total_price_net, price_without_tax)
#
#     command = input()
#
#     if command == "special":
#         special_customer = True
#
# if total_price_net:
#     # total_price_net != 0
#     total_price_with_tax = total_price_net * 1.20
#     tax = total_price_with_tax - total_price_net
#     if special_customer:
#         total_price_with_tax *= 0.90
#     print("Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {total_price_net:.2f}$")
#     print(f"Taxes: {tax:.2f}$\n-----------")  # \n - new line
#     print(f"Total price: {total_price_with_tax:.2f}$")
# else:
#     print("Invalid order!")
#
# 3.1
#
# neighborhood = [int(ch) for ch in input().split("@")]
# last_position = 0
#
# command = input()
#
# while command != "Love!":
#     jump, index = command.split(" ")
#     # list = command.split(" ")\n index = int(command[1])
#     last_position += int(index)
#
#     if last_position >= len(neighborhood):
#         last_position = 0
#
#     if neighborhood[last_position] != 0:
#         neighborhood[last_position] -= 2
#         if neighborhood[last_position] == 0:
#             print(f"Place {last_position} has Valentine's day.")
#     else:
#         print(f"Place {last_position} already had Valentine's day.")
#
#     command = input()
#
# print(f"Cupid's last position was {last_position}.")
# if sum(neighborhood) == 0:
#     print("Mission was successful.")
# else:
#     house_count = [1 for house in neighborhood if house != 0]
#     # house_count = len(neighborhood) - neighborhood.count(0)
#     print(f"Cupid has failed {sum(house_count)} places.")
#
# 3.2
#
#
# def cupid_jump(current_list, ind):
#     if current_list[ind] != 0:
#         current_list[ind] -= 2
#         if current_list[ind] == 0:
#             print(f"Place {ind} has Valentine's day.")
#     else:
#         print(f"Place {ind} already had Valentine's day.")
#     return current_list
#
#
# def final_result(current_list, position):
#     print(f"Cupid's last position was {position}.")
#     if sum(current_list) == 0:
#         print("Mission was successful.")
#     else:
#         count = 0
#         for ch in current_list:
#             if ch != 0:
#                 count += 1
#         print(f"Cupid has failed {count} places.")
#
#
# houses = [int(ch) for ch in input().split("@")]
# position = 0
#
# while True:
#     command = input()
#
#     if command == "Love!":
#         final_result(houses, position)
#         break
#
#     skip_command, new_position = command.split(" ")
#
#     current_position = int(new_position) + position
#     if current_position > len(houses) - 1:
#         current_position = 0
#
#     houses = cupid_jump(houses, current_position)
#     position = current_position
#
# 2.1
#
# array_with_integers = [int(ch) for ch in input().split(" ")]
#
# command = input()
#
# while command != "end":
#     current_list = command.split(" ")
#
#     if current_list[0] == "swap":
#         index_1, index_2 = int(current_list[1]), int(current_list[2])
#         # if 0 <= index_1 < len(array_with_integers): 1st example
#         # if 0 <= index_1 <= (len(array_with_integers) - 1) 2nd example
#         # if index_1 in range(0, len(array_with_integers)) 3th example
#         array_with_integers[index_1], array_with_integers[index_2] = array_with_integers[index_2], array_with_integers[
#             index_1]
#     elif current_list[0] == "multiply":
#         # [multiply, 1, 2]
#         index_1, index_2 = int(current_list[1]), int(current_list[2])
#         array_with_integers[index_1] *= array_with_integers[index_2]
#     elif current_list[0] == "decrease":
#         array_with_integers = [ch - 1 for ch in array_with_integers]
#         # for i in range(len(array_with_integers)):
#         #     array_with_integers[i] -= 1
#
#     command = input()
#
# # print(*array_with_integers, sep=", ")
# print(', '.join(str(ch) for ch in array_with_integers))
#
# 2.2
#
#
# def swap(first_index, second_index, current_list):
#     current_list[first_index], current_list[second_index] = current_list[second_index], current_list[first_index]
#     return current_list
#
#
# def multiply(first_index, second_index, current_list):
#     multiplier = current_list[second_index]
#     current_list[first_index] *= multiplier
#     return current_list
#
#
# def decrease(current_list):
#     for i in range(len(current_list)):
#         current_list[i] -= 1
#     return current_list
#
#
# array = [int(ch) for ch in input().split(" ")]
#
# while True:
#     command = input()
#
#     if command == "end":
#         break
#
#     current_command = command.split(" ")
#
#     if current_command[0] == "swap":
#         array = swap(int(current_command[1]), int(current_command[2]), array)
#     elif current_command[0] == "multiply":
#         array = multiply(int(current_command[1]), int(current_command[2]), array)
#     elif current_command[0] == "decrease":
#         array = decrease(array)
#
# print(', '.join(str(ch) for ch in array))
