# Да се напише програма, която чете текст (стринг), въведен от потребителя,
# и изчислява и отпечатва сумата от стойностите на гласните букви според таблицата по-долу:
# буква	    a	e	i	o	u
# стойност	1	2	3	4	5

word = input()
suma = 0

for i in range(0, len(word)):
    if word[i] == "a":
        suma += 1
    if word[i] == "e":
        suma += 2
    if word[i] == "i":
        suma += 3
    if word[i] == "o":
        suma += 4
    if word[i] == "u":
        suma += 5
print(suma)
