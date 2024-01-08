def genrange(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


for num in genrange(1, 10):
    print(num)
print((genrange(1, 10)))
print(list(genrange(1, 10)))
