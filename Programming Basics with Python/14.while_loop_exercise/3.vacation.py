''' Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее да събере
необходимата сума. Тя спестява или харчи част от парите си всеки ден.
Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
Вход
От конзолата се четат:
•	Пари, нужни за екскурзията - реално число;
•	Налични пари - реално число.
След това многократно се четат по два реда:
•	Вид действие – текст с две възможности: "spend" или "save";
•	Сумата, която ще спести/похарчи - реално число.
Изход
Програмата трябва да приключи при следните случаи:
•	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
o	"You can't save the money."
o	"{Общ брой изминали дни}"
•	Ако Джеси събере парите за почивката, на конзолата се изписва:
o	"You saved the money for {общ брой изминали дни} days." '''

needed_vacation_money = float(input())
current_money = float(input())
spend_counter = 0
total_days_count = 0

while current_money < needed_vacation_money and spend_counter < 5:
    command = input()
    money = float(input())
    total_days_count += 1
    if command == "save":
        current_money += money
        spend_counter = 0
    elif command == "spend":
        current_money -= money
        spend_counter += 1
        if current_money < 0:
            current_money = 0
if spend_counter == 5:
    print("You can't save the money.")
    print(f"{total_days_count}")
if current_money >= needed_vacation_money:
    print(f"You saved the money for {total_days_count} days.")
