# Лятото е сезон с много променливо време и Виктор има нужда от вашата помощ.
# Напишете програма, която спрямо времето от денонощието и градусите да препоръча на Виктор
# какви дрехи да облече. Вашият приятел има различни планове за всеки етап от деня,
# които изискват и различен външен вид - може да ги видите от таблицата.
# От конзолата се четат точно два реда:
# Градусите - цяло число;
# Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".
# Време от денонощието / градуси    Morning               Afternoon                 Evening
#
# 10 <= градуси <= 18               Outfit = Sweatshirt   Outfit = Shirt            Outfit = Shirt
#                                   Shoes = Sneakers      Shoes = Moccasins         Shoes = Moccasins
#
# 18 < градуси <= 24                Outfit = Shirt        Outfit = T-Shirt          Outfit = Shirt
#                                   Shoes = Moccasins     Shoes = Sandals           Shoes = Moccasins
#
# градуси >= 25                     Outfit = T-Shirt      Outfit = Swim Suit        Outfit = Shirt
#                                   Shoes = Sandals       Shoes = Barefoot          Shoes = Moccasins
#
# Като изход да се отпечата на конзолата на един ред:
# "It's {градуси} degrees, get your {облекло} and {обувки}."

degrees = int(input())
day_time = input()
outfit = ""
shoes = ""

if 10 <= degrees <= 18:
    if day_time == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif day_time == "Afternoon" or day_time == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

elif 18 < degrees <= 24:
    if day_time == "Morning" or day_time == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif day_time == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"

elif degrees >= 25:
    if day_time == "Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif day_time == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif day_time == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
