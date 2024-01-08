# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята,
# че Ви убеждава да напишете програма, която да изчисли колко  ще им струва,
# за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен.
# Различните цветя са с различни цени:
# цвете                 Роза   Далия   Лале    Нарцис    Гладиола
# Цена на брой в лева   5      3.80    2.80    3         2.50
# Съществуват следните отстъпки:
# Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
# От конзолата се четат 3 реда:
# Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# Брой цветя - цяло число;
# Бюджет - цяло число.
# Да се отпечата на конзолата на един ред:
# Ако бюджетът им е достатъчен -
# "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# Ако бюджета им е НЕ достатъчен -
# "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.

ROSES_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

flower_type = input()
flower_count = int(input())
budget = int(input())
total_price = 0

if flower_type == "Roses":
    if flower_count > 80:
        total_price = (ROSES_PRICE * flower_count) * 0.90
    else:
        total_price = ROSES_PRICE * flower_count

elif flower_type == "Dahlias":
    if flower_count > 90:
        total_price = (DAHLIAS_PRICE * flower_count) * 0.85
    else:
        total_price = DAHLIAS_PRICE * flower_count

elif flower_type == "Tulips":
    if flower_count > 80:
        total_price = (TULIPS_PRICE * flower_count) * 0.85
    else:
        total_price = TULIPS_PRICE * flower_count

elif flower_type == "Narcissus":
    if flower_count < 120:
        total_price = (NARCISSUS_PRICE * flower_count) * 1.15
    else:
        total_price = NARCISSUS_PRICE * flower_count

elif flower_type == "Gladiolus":
    if flower_count < 80:
        total_price = (GLADIOLUS_PRICE * flower_count) * 1.20
    else:
        total_price = GLADIOLUS_PRICE * flower_count

if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - total_price:.2f} leva left.")
if budget < total_price:
    print(f"Not enough money, you need {total_price - budget:.2f} leva more.")
