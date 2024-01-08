
# numbers = input().split()
# numbers_abs = []
#
# for el in numbers:
#     numbers_abs.append(abs(float(el)))
# print(numbers_abs)

numbers = input().split()
absolute_value = [abs(float(num)) for num in numbers]
print(absolute_value)
