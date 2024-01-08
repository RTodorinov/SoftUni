# Вашата задача е да напишете програма, която да изчислява процента на билетите за всеки тип от
# продадените билети: студентски(student), стандартен(standard) и детски(kid), за всички прожекции.
# Трябва да изчислите и колко процента от залата е запълнена за всяка една прожекция.
# Вход
# Входът е поредица от цели числа и текст:
# •	На първия ред до получаване на командата "Finish" - име на филма – текст
# •	На втори ред – свободните места в салона за всяка прожекция – цяло число [1 … 100]
# •	За всеки филм, се чете по един ред до изчерпване на свободните места в залата или до получаване на командата "End":
# Типа на закупения билет - текст ("student", "standard", "kid")
# Изход
# На конзолата трябва да се печатат следните редове:
# •	След всеки филм да се отпечата, колко процента от кино залата е пълна
# "{името на филма} - {процент запълненост на залата}% full."
# •	При получаване на командата "Finish" да се отпечатат четири реда:
# "Total tickets: {общият брой закупени билети за всички филми}"
# "{процент на студентските билети}% student tickets."
# "{процент на стандартните билети}% standard tickets."
# "{процент на детските билети}% kids tickets."

# създаваме си променливи да пазят сумите от съответните билети
standard_sum = 0
student_sum = 0
kid_sum = 0

while True:  # първия цикъл проверява прожекциите
    movie_name = input()

    if movie_name == "Finish":
        break
    seats = int(input())  # на всяка прожекция добавяме променлива за свободните места
    sold_tickets = 0  # на всяка прожекция нулираме продадените билети

    while sold_tickets < seats:  # втория цикъл проверява билетите кога ще достигнат свободните места
        command = input()       # и какъв е типът на билета

        if command == "End":
            break

        if command == "student":
            student_sum += 1
        if command == "standard":
            standard_sum += 1
        elif command == "kid":
            kid_sum += 1

        sold_tickets += 1

    print(f"{movie_name} - {sold_tickets / seats * 100:.2f}% full.")

total_tickets = standard_sum + student_sum + kid_sum

print(f"Total tickets: {total_tickets}")
print(f"{student_sum / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_sum / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_sum / total_tickets * 100:.2f}% kids tickets.")
