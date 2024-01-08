# Магазин за цветя предлага 3 вида цветя: хризантеми, рози и лалета. Цените зависят от сезона.
# Сезон	                    Хризантеми	    Рози	        Лалета
# Пролет / Лято	            2.00 лв./бр.	4.10 лв./бр.	2.50 лв./бр.
# Есен / Зима	            3.75 лв./бр.	4.50 лв./бр.	4.15 лв./бр.
# В празнични дни цените на всички цветя се увеличават с 15%. Предлагат се следните отстъпки:
# •	За закупени повече от 7 лалета през пролетта – 5% от цената на целият букет.
# •	За закупени 10 или повече рози през зимата – 10% от цената на целият букет.
# •	За закупени повече от 20 цветя общо през всички сезони – 20% от цената на целият букет.
# Отстъпките се правят по така написания ред и могат да се наслагват!
# Всички отстъпки важат след оскъпяването за празничен ден!
# Цената за аранжиране на букета винаги е 2лв. Напишете програма, която изчислява цената за един букет.
# Входът се чете от конзолата и съдържа точно 5 реда:
# •	На първия ред е броят на закупените хризантеми – цяло число в интервала [0 ... 200]
# •	На втория ред е броят на закупените рози – цяло число в интервала [0 ... 200]
# •	На третия ред е броят на закупените лалета – цяло число в интервала [0 ... 200]
# •	На четвъртия ред е посочен сезона – [Spring, Summer, Аutumn, Winter]
# •	На петия ред е посочено дали денят е празник – [Y – да / N - не]
# Изход
# Да се отпечата на конзолата 1 число – цената на цветята, форматирана до вторият знак след десетичната запетая.

ARRANGEMENT_BOUQUET_PRICE = 2
chrysanthemum_count = int(input())
roses_count = int(input())
tulips_count = int(input())

year_season = input()
holiday = input()

flower_sum = 0
total_flower_count = chrysanthemum_count + roses_count + tulips_count

if year_season == "Spring":
    if holiday == "N" and total_flower_count > 20:
        if tulips_count > 7:
            flower_sum = (chrysanthemum_count * 2) + (roses_count * 4.10) + (tulips_count * 2.50)
            flower_sum *= 0.80
            flower_sum *= 0.95
            flower_sum += 2
        else:
            flower_sum = (chrysanthemum_count * 2) + (roses_count * 4.10) + (tulips_count * 2.50)
            flower_sum *= 0.80
            flower_sum += 2
    elif holiday == "N" and total_flower_count < 20:
        flower_sum = (chrysanthemum_count * 2) + (roses_count * 4.10) + (tulips_count * 2.50)
        flower_sum += 2
    elif holiday == "Y" and total_flower_count > 20:
        if tulips_count > 7:
            flower_sum = ((chrysanthemum_count * 2) + (roses_count * 4.10) + (tulips_count * 2.50)) * 1.15
            flower_sum *= 0.80
            flower_sum *= 0.95
            flower_sum += 2
        else:
            flower_sum = ((chrysanthemum_count * 2) + (roses_count * 4.10) + (tulips_count * 2.50)) * 1.15
            flower_sum *= 0.80
            flower_sum += 2
    elif holiday == "Y" and total_flower_count < 20:
        if tulips_count > 7:
            flower_sum = ((chrysanthemum_count * 2) + (roses_count * 4.10) + (tulips_count * 2.50)) * 1.15
            flower_sum *= 0.95
            flower_sum += 2
        else:
            flower_sum = ((chrysanthemum_count * 2) + (roses_count * 4.10) + (tulips_count * 2.50)) * 1.15
            flower_sum += 2

elif year_season == "Summer":
    if holiday == "N" and total_flower_count > 20:
        flower_sum = (chrysanthemum_count * 2) + (roses_count * 4.10) + (tulips_count * 2.50)
        flower_sum *= 0.80
        flower_sum += 2
    elif holiday == "N" and total_flower_count < 20:
        flower_sum = (chrysanthemum_count * 2) + (roses_count * 4.10) + (tulips_count * 2.50)
        flower_sum += 2
    elif holiday == "Y" and total_flower_count > 20:
        flower_sum = ((chrysanthemum_count * 2) + (roses_count * 4.10) + (tulips_count * 2.50)) * 1.15
        flower_sum *= 0.80
        flower_sum += 2
    elif holiday == "Y" and total_flower_count < 20:
        flower_sum = ((chrysanthemum_count * 2) + (roses_count * 4.10) + (tulips_count * 2.50)) * 1.15
        flower_sum += 2

elif year_season == "Autumn":
    if holiday == "N" and total_flower_count > 20:
        flower_sum = (chrysanthemum_count * 3.75) + (roses_count * 4.50) + (tulips_count * 4.15)
        flower_sum *= 0.80
        flower_sum += 2
    elif holiday == "N" and total_flower_count < 20:
        flower_sum = (chrysanthemum_count * 3.75) + (roses_count * 4.50) + (tulips_count * 4.15)
        flower_sum += 2
    elif holiday == "Y" and total_flower_count > 20:
        flower_sum = ((chrysanthemum_count * 3.75) + (roses_count * 4.50) + (tulips_count * 4.15)) * 1.15
        flower_sum *= 0.80
        flower_sum += 2
    elif holiday == "Y" and total_flower_count < 20:
        flower_sum = ((chrysanthemum_count * 3.75) + (roses_count * 4.50) + (tulips_count * 4.15)) * 1.15
        flower_sum += 2

elif year_season == "Winter":
    if holiday == "N" and total_flower_count > 20:
        if roses_count >= 10:
            flower_sum = (chrysanthemum_count * 3.75) + (roses_count * 4.50) + (tulips_count * 4.15)
            flower_sum *= 0.80
            flower_sum *= 0.90
            flower_sum += 2
        else:
            flower_sum = (chrysanthemum_count * 3.75) + (roses_count * 4.50) + (tulips_count * 4.15)
            flower_sum *= 0.80
            flower_sum += 2
    elif holiday == "N" and total_flower_count < 20:
        flower_sum = (chrysanthemum_count * 3.75) + (roses_count * 4.50) + (tulips_count * 4.15)
        flower_sum += 2
    elif holiday == "Y" and total_flower_count > 20:
        if roses_count >= 10:
            flower_sum = ((chrysanthemum_count * 3.75) + (roses_count * 4.50) + (tulips_count * 4.15)) * 1.15
            flower_sum *= 0.80
            flower_sum *= 0.90
            flower_sum += 2
        else:
            flower_sum = ((chrysanthemum_count * 3.75) + (roses_count * 4.50) + (tulips_count * 4.15)) * 1.15
            flower_sum *= 0.80
            flower_sum += 2
    elif holiday == "Y" and total_flower_count < 20:
        if roses_count >= 10:
            flower_sum = ((chrysanthemum_count * 3.75) + (roses_count * 4.50) + (tulips_count * 4.15)) * 1.15
            flower_sum *= 0.90
            flower_sum += 2
        else:
            flower_sum = ((chrysanthemum_count * 3.75) + (roses_count * 4.50) + (tulips_count * 4.15)) * 1.15
            flower_sum += 2

print(f"{flower_sum:.2f}")
