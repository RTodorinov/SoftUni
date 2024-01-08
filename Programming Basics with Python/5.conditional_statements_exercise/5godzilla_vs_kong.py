#  Снимките за дългоочаквания филм "Годзила срещу Конг" започват.
#  Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли,
#  дали предвидените средства са достатъчни за снимането на филма.
#  За снимките  ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
# •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.

film_budget = float(input())

extras = int(input())
clothing_price = float(input())

decor_price = film_budget * 0.10  # смятаме 10% от бюджета.

if extras > 150:
    clothing_price *= 0.90  # смятаме отстъпката 10% на облеклото при повече от 150 статиста.

total_clothing_price = extras * clothing_price
total_money = decor_price + total_clothing_price

if total_money <= film_budget:
    print("Action!")
    print(f"Wingard starts filming with {film_budget - total_money:.2f} leva left.")
if total_money > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {total_money - film_budget:.2f} leva more.")
#  тук може да се ползва и else за да не ползваме втори if
#  else:
#  print("Not enough money!")
#  print(f"Wingard needs {total_money - film_budget:.2f} leva more.")
