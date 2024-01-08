# Дадени са 2*n-на брой числа.
# Първото и второто формират двойка, третото и четвъртото също и т.н.
# Всяка двойка има стойност – сумата от съставящите я числа.
# Напишете програма, която проверява дали всички двойки имат еднаква стойност или печата максималната разлика
# между две последователни двойки.
# Ако всички двойки имат еднаква стойност, отпечатайте "Yes, value={Value}" + стойността.
# В противен случай отпечатайте "No, maxdiff={Difference}" + максималната разлика.

# pairs = int(input())
# values = []   # тук се ползва лист за променливата
# for i in range(pairs):
#     first_number = int(input())
#     second_number = int(input())
#     value = first_number + second_number
#     values.append(value)
#
# if len(set(values)) == 1:
#     print(f"Yes, value={values[0]}")
# else:
#     diff = max(abs(values[i+1]-values[i]) for i in range(pairs-1))
#     print(f"No, diff={diff}")

pairs = int(input())
value = None  # Тези променливи ще се използват за проследяване на стойността на двойките и максималната
max_diff = 0  # разлика между последователни двойки.

for i in range(pairs):  # Това е цикъл, който повтаря n пъти.
    a = int(input())  # След това програмата изчислява сумата от двете числа и присвоява резултата на new_value.
    b = int(input())  # След това програмата проверява дали value все още е присвоена. Ако value е None,
    new_value = a + b  # тогава new_value се присвоява на value. Ако на value вече е присвоена стойност и
    if value is None:  # new_value е различна от value, тогава програмата изчислява абсолютната разлика между
        value = new_value  # new_value и value и я присвоява на diff. Ако diff е по-голяма от maxdiff, тогава maxdiff
    elif new_value != value:  # се актуализира с новата стойност на diff. И накрая, value се актуализира до
        max_diff = max(max_diff, abs(new_value - value))  # new_value,така че да може да се сравни със следващата
    value = new_value                                     # двойка числа в следващата итерация на цикъла.

if max_diff == 0:
    print(f"Yes, value={value}")
else:
    print(f"No, maxdiff={max_diff}")
#  Това, if  проверява дали maxdiff е 0. Ако е така, тогава всички двойки имат една и съща стойност и програмата
#  отпечатва "Yes, value=", последвана от стойността на двойките.
#  Ако maxdiff не е 0, тогава поне една двойка има различна стойност от другите и програмата отпечатва
#  "No, maxdiff=", последвано от максималната разлика между две последователни двойки.
