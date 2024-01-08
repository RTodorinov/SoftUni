
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

deck_of_cards = input().split()
number_of_shuffles = int(input())
for shuffle in range(number_of_shuffles):
    final_deck = []
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck::]
    for index_of_the_card in range(len(left_part)):
        final_deck.append(left_part[index_of_the_card])
        final_deck.append(right_part[index_of_the_card])
    deck_of_cards = final_deck
print(deck_of_cards)

# string = input()
# shuffles = int(input())
# list_string = string.split(" ")
# for _ in range(shuffles):
#     first_half = list_string[:len(list_string)//2]
#     second_half = list_string[len(list_string)//2:]
#
#     list_string = [letter for pair in zip(first_half, second_half) for letter in pair]
#
# print(list_string)
