''' На благотворително събитие плащанията за закупените продукти винаги се редуват: плащане в брой и плащане с карта.
Установени са следните правила за заплащане:
•	Ако продуктът надвишава 100лв., за него не може да се плати в брой
•	Ако продуктът е на цена под 10лв., за него не може да се плати с кредитна карта
Програмата приключва или след като получим команда "End" или след като средствата бъдат събрани.
Вход
От конзолата се четат:
•	Сумата, която се очаква да бъде събрана от продажбите - цяло число в интервала [1 ... 10000]
На всеки следващ ред, до получаване на командата "End" или докато не се съберат нужните средства:
цените на предметите, които ще бъдат закупени - цяло число в интервала [1 ... 500]
Изход
На конзолата да се отпечата:
•	При успешна транзакция: "Product sold!"
•	При неуспешна транзакция: "Error in transaction!"
•	Ако сумата на всички закупени продукти надвиши или достигне очакваната сума, програмата трябва да приключи и на
конзолата да се изпишат два реда:
"Average CS: {средно плащане в кеш на човек}"
"Average CC: {средно плащане с карта на човек}"
Плащанията трябва да бъдат форматирани до втората цифра след десетичния знак.
При получаване на команда "End", да се изпише един ред:
"Failed to collect required money for charity." '''

# expected_sum = int(input())
#
# total_sum = 0
# cash_counter = 0
# card_counter = 0
# cash = 0
# card = 0
# price = ''
#
# while total_sum < expected_sum:
#     if price == 'End':
#         break
#     for i in range(2):  # if i == 0 плащане в брой. if i == 1 плащане с карта
#         price = input()
#         if price == 'End':
#             print(f"Failed to collect required money for charity.")
#             break
#         if i == 0:  # плащане в брой
#             if int(price) <= 100:
#                 cash += int(price)
#                 cash_counter += 1
#                 print(f"Product sold!")
#             else:
#                 print(f"Error in transaction!")
#         else:  # плащане с карта
#             if int(price) < 10:
#                 print(f"Error in transaction!")
#             else:
#                 card += int(price)
#                 card_counter += 1
#                 print(f"Product sold!")
#         total_sum = cash + card
#         if total_sum >= expected_sum:
#             break
# cash_average = cash / cash_counter
# card_average = card / card_counter
# if total_sum >= expected_sum:
#     print(f"Average CS: {cash_average:.2f}")
#     print(f"Average CC: {card_average:.2f}")

expected_sum = int(input())

total_sum = 0
cash_counter = 0
card_counter = 0
cash = 0
card = 0
price = ''

while total_sum < expected_sum and price != 'End':
    i = 0
    while i < 2 and total_sum < expected_sum:
        price = input()
        if price == 'End':
            break
        if i == 0:  # плащане в брой
            if int(price) <= 100:
                cash += int(price)
                cash_counter += 1
                print(f"Product sold!")
            else:
                print(f"Error in transaction!")
        else:  # плащане с карта
            if int(price) < 10:
                print(f"Error in transaction!")
            else:
                card += int(price)
                card_counter += 1
                print(f"Product sold!")
        total_sum = cash + card
        i += 1

if total_sum >= expected_sum:
    cash_average = cash / cash_counter
    card_average = card / card_counter
    print(f"Average CS: {cash_average:.2f}")
    print(f"Average CC: {card_average:.2f}")
else:
    print(f"Failed to collect required money for charity.")
