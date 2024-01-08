# Частно училище организира лагери за учениците по време на ваканциите.
# В зависимост от вида на ваканцията (пролетна, лятна или зимна) и
# вида на групата (момчета/момичета или смесена) цената на нощувката в хотела е различна, както и спортът,
# който ще практикуват учениците.
# 	                 Зимна ваканция	Пролетна ваканция	Лятна ваканция
# момчета/момичета	 9.60	        7.20	            15
# смесена група	     10	            9.50	            20
# Училището получава отстъпка от крайната цена, в зависимост от броя на настанените в хотела ученици:
# •	Ако броят на учениците е 50 или повече, училището получава 50% отстъпка
# •	Ако броят на учениците е 20 или повече и в същото време по-малък от 50, училището получава 15% отстъпка
# •	Ако броят на учениците е 10 или повече и в същото време по-малък от 20, училището получава 5% отстъпка
# В таблицата по-долу са дадени спортовете, които ще се практикуват в зависимост от вида на ваканцията и групата:
# 	                 Зимна ваканция	Пролетна ваканция	Лятна ваканция
# момичета	         Gymnastics	    Athletics	        Volleyball
# момчета	         Judo	        Tennis	            Football
# смесена група	     Ski	        Cycling	            Swimming
# Да се напише програма, която пресмята цената, която ще заплати училището за нощувките и принтира спорта,
# който ще се практикува от учениците.
# Вход
# От конзолата се четат 4 реда:
# 1.	Сезонът – текст - “Winter”, “Spring” или “Summer”;
# 2.	Видът на групата – текст - “boys”, “girls” или “mixed”;
# 3.	Брой на учениците – цяло число в интервала [1 … 10000];
# 4.	Брой на нощувките – цяло число в интервала [1 … 100].
# Изход
# На конзолата се отпечатва 1 ред:
# •	Спортът, който са практикували учениците и цената за нощувките, която е заплатило училището,
# форматирана до втория знак след десетичната запетая, в следния формат:
# "{спортът} {цената} lv.“

year_seasons = input()
group_type = input()
students_count = int(input())
nights_count = int(input())

sport_type = ''
price = 0

if group_type == "boys":
    if year_seasons == "Winter":
        sport_type = "Judo"
        price = students_count * nights_count * 9.60
    elif year_seasons == "Spring":
        sport_type = "Tennis"
        price = students_count * nights_count * 7.20
    elif year_seasons == "Summer":
        sport_type = "Football"
        price = students_count * nights_count * 15

elif group_type == "girls":
    if year_seasons == "Winter":
        sport_type = "Gymnastics"
        price = students_count * nights_count * 9.60
    elif year_seasons == "Spring":
        sport_type = "Athletics"
        price = students_count * nights_count * 7.20
    elif year_seasons == "Summer":
        sport_type = "Volleyball"
        price = students_count * nights_count * 15

elif group_type == "mixed":
    if year_seasons == "Winter":
        sport_type = "Ski"
        price = students_count * nights_count * 10
    elif year_seasons == "Spring":
        sport_type = "Cycling"
        price = students_count * nights_count * 9.50
    elif year_seasons == "Summer":
        sport_type = "Swimming"
        price = students_count * nights_count * 20

if students_count >= 50:
    price *= 0.50
elif students_count >= 20:
    price *= 0.85
elif students_count >= 10:
    price *= 0.95

print(f"{sport_type} {price:.2f} lv.")
