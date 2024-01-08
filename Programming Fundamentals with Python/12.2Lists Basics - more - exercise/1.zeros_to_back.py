
numbers_as_string = input().split(", ")
numbers_as_digits = [int(el) for el in numbers_as_string]
for idx in range(len(numbers_as_digits)):  # така намираме на кой индекс има 0
    if numbers_as_digits[idx] == 0:
        numbers_as_digits.remove(numbers_as_digits[idx])
        numbers_as_digits.append(0)
print(numbers_as_digits)
