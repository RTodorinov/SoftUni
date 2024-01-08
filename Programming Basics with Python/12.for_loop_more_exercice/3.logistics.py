# Отговаряте за логистиката на различни товари.
# В зависимост от теглото на товара е нужно различно превозно средство.
# Цената на тон, за която се превозва товара е различна за всяко превозно средство:
# •	До 3 тона – микробус (200 лева на тон)
# •	От 4 до 11 тона – камион (175 лева на тон)
# •	12 и повече тона – влак (120 лева на тон)
# Вашата задача е да изчислите средната цена на тон превозен товар, както и процента на тоновете
# превозвани с всяко превозно средство, спрямо общото тегло(в тонове) на всички товари.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – броя на товарите за превоз – цяло число в интервала [1...1000]
# •	За всеки един товар на отделен ред – тонажа на товара – цяло число в интервала [1...1000]
# Изход
# Да се отпечатат на конзолата 4 реда, както следва:
# •	Първи ред – средната цена на тон превозен товар (закръглена до втория знак след дес. запетая);
# •	Втори ред – процентът тона превозвани с микробус (процент между 0.00% и 100.00%);
# •	Трети ред – процентът  тона превозвани с камион (процент между 0.00% и 100.00%);
# •	Четвърти ред – процентът тона превозвани с влак (процент между 0.00% и 100.00%).

cargo_number = int(input())
microbus_cargo, truck_cargo, train_cargo = 0, 0, 0

for _ in range(cargo_number):
    number = int(input())

    if number <= 3:
        microbus_cargo = microbus_cargo + number
    elif 4 <= number <= 11:
        truck_cargo = truck_cargo + number
    elif number >= 12:
        train_cargo = train_cargo + number

cargo_sum = microbus_cargo + truck_cargo + train_cargo
total_cargo = (microbus_cargo * 200 + truck_cargo * 175 + train_cargo * 120) / cargo_sum

print(f"{total_cargo:.2f}")
print(f"{(microbus_cargo / cargo_sum) * 100:.2f}%")
print(f"{(truck_cargo / cargo_sum) * 100:.2f}%")
print(f"{(train_cargo / cargo_sum) * 100:.2f}%")