# Напишете програма, която отпечатва числата в диапазона от 1 до 1000,
# които завършват на 7.

# for i in range(1, 1000 + 1):
#     if i % 10 == 7:
#         print(i)
# или да ползваме цикъла със стъпка 10

for i in range(7, 1001, 10):
    print(i)
