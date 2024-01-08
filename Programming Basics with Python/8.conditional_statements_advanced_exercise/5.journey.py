# Млад програмист разполага с определен бюджет и свободно време в даден сезон.
# Напишете програма, която да приема на входа бюджета и сезона, а на изхода
# да изкарва къде ще почива програмистът и колко ще похарчи.
# Бюджетът определя дестинацията, а сезонът - колко от бюджета ще изхарчи.
# Ако е лято ще почива на къмпинг, а зимата в хотел. Ако е в Европа, независимо от сезона,
# ще почива в хотел. Всеки къмпинг или хотел, според дестинацията, има собствена цена,
# която отговаря на даден процент от бюджета:
# При 100 лв. или по-малко - някъде в България:
# Лято - 30% от бюджета;
# Зима - 70% от бюджета.
# При 1000 лв. или по малко - някъде на Балканите:
# Лято - 40% от бюджета;
# Зима - 80% от бюджета.
# При повече от 1000 лв. - някъде из Европа:
# При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.
# Вход
# Входът се чете от конзолата и се състои от два реда, въведени от потребителя:
# Бюджет - реално число;
# Един от двата възможни сезона - "summer” или "winter”.
# Изход
# На конзолата трябва да се отпечатат два реда:
#  "Somewhere in [дестинация]" измежду "Bulgaria", "Balkans" и "Europe"
# "{Вид почивка} - {Похарчена сума}":
# Почивката може да е между "Camp" и "Hotel"
# Сумата трябва да бъде форматирана с точност до вторият знак след десетичната запетая

budget = float(input())
season = input()
price = 0
destination = None
type_vacation = None

if budget <= 100:
    destination = "Bulgaria"

    if season == "summer":
        price = budget * 0.30
        type_vacation = "Camp"
    elif season == "winter":
        price = budget * 0.70
        type_vacation = "Hotel"

elif budget <= 1000:
    destination = "Balkans"

    if season == "summer":
        price = budget * 0.40
        type_vacation = "Camp"
    elif season == "winter":
        price = budget * 0.80
        type_vacation = "Hotel"

elif budget > 1000:
    destination = "Europe"
    price = budget * 0.90
    type_vacation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_vacation} - {price:.2f}")