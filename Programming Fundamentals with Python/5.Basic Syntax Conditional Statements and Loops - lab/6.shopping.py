
# budget = int(input())
# current_price_as_string = input()
#
# while current_price_as_string != "End":
#     current_price = int(current_price_as_string)
#
#     budget -= current_price
#     if budget < 0:
#         print("You went in overdraft!")
#         exit()
#     current_price_as_string = input()
#
# print("You bought everything needed.")

# budget = int(input())
# current_price_as_string = input()
# IF_BREAK = False
# while current_price_as_string != "End":
#     current_price = int(current_price_as_string)
#
#     budget -= current_price
#     if budget < 0:
#         IF_BREAK = True
#         break
#     current_price_as_string = input()
#
# if IF_BREAK:
#     print("You went in overdraft!")
# else:
#     print("You bought everything needed.")

budget = int(input())
total_price = 0
while True:
    command = input()
    if command == "End":
        print("You bought everything needed.")
        break

    price = int(command)
    if total_price + price > budget:
        print("You went in overdraft!")
        break
    total_price += price
