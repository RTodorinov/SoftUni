''' Напишете програма, която чете число n, въведено от потребителя,
и отпечатва всички числа  ≤  n от редицата: 1, 3, 7, 15, 31, ….
Всяко следващо число се изчислява като умножим предишното с 2 и добавим 1. '''

n = int(input())
counter = 1

while counter <= n:
    print(counter)  # когато искаме да хванем първата стойност на брояча
    counter = counter * 2 + 1  # на всяко завъртане на цикъла се пресмята докато усовието горе стане false.

