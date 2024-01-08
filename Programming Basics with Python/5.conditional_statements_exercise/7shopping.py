#  Петър иска да купи N видеокарти, M процесора и P на брой рам памет.
#  Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка.
#  Важат следните цени:
# •	Видеокарта – 250 лв./бр.
# •	Процесор – 35% от цената на закупените видеокарти/бр.
# •	Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.

budget = float(input())

video_card_count = int(input())
procesor_count = int(input())
ram_count = int(input())

VIDEO_CARD_PRICE = 250
total_price_video_cards = video_card_count * 250

PROCESOR_PRICE = total_price_video_cards * 0.35  # 35% от цената на видео картите
RAM_PRICE = total_price_video_cards * 0.10  # 10% от цената на видео картите

total_price_procesor = procesor_count * PROCESOR_PRICE
total_price_rams = ram_count * RAM_PRICE
total_sum = total_price_video_cards + total_price_procesor + total_price_rams

if video_card_count > procesor_count:
    total_sum *= 0.85  # (1 - 0.15) може да се представи и така

if budget >= total_sum:
    print(f"You have {budget - total_sum:.2f} leva left!")
# if budget < total_sum:
else:
    print(f"Not enough money! You need {total_sum - budget:.2f} leva more!")
