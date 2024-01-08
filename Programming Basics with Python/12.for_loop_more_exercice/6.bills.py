# Напишете програма която да пресмята средният разход за месец на семейство за даден период време.
# За всеки месец разходите са следните:
# •	За ток – всеки месец е различен, ще се чете от конзолата
# •	за вода – 20 лв.
# •	за интернет – 15 лв.
# •	за други – събират се тока, водата и интернета за месеца и към сумата се прибавят 20%.
# За всеки разход трябва да се пресметне колко общо е платено за всички месеци.
# Входът се чете от конзолата:
# •	Първи ред – месеците за които се търси средният разход – цяло число в интервала [1...100]
# •	За всеки месец – сметката за ток – реално число в интервала [1.00...1000.00]
# Изход
# Да се отпечата на конзолата 5 реда:
# •	1ви ред: "Electricity: {ток за всички месеци} lv"
# •	2ри ред: "Water: {вода за всички месеци} lv"
# •	3ти ред: "Internet: {интернет за всички месеци} lv"
# •	4ти ред: "Other: {други за всички месеци} lv"
# •	5ти ред: "Average: {средно всички разходи за месец} lv"
# Всички числа трябва да са форматирана до вторият знак след запетаята.

electricity_sum, water_sum, internet_sum, other_sum = 0, 0, 0, 0
months_average = int(input())

for month in range(months_average):
    number = float(input())
    month += 1
    electricity_sum += float(number)
    water_sum += 20
    internet_sum += 15
    other_sum += (float(number) + 20 + 15) * 0.20 + (float(number) + 20 + 15)

print(f"Electricity: {electricity_sum:.2f} lv")
print(f"Water: {water_sum:.2f} lv")
print(f"Internet: {internet_sum:.2f} lv")
print(f"Other: {other_sum:.2f} lv")
print(f"Average: {(electricity_sum + water_sum + internet_sum + other_sum) / months_average:.2f} lv")
