
elements = input().split()
bakery = {}

for idx in range(0, len(elements), 2):  # въртим през дължината на листа и ползваме индекс
    key = elements[idx]
    value = elements[idx + 1]
    bakery[key] = int(value)  # добавяме цифровата стойност с int

print(bakery)
