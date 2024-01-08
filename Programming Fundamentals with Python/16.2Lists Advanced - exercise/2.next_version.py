
version = input().split(".")
version = [int(x) for x in version]
version[-1] += 1
for index in range(len(version) - 1, - 1, - 1):
    if version[index] > 9 and index != 0:
        version[index] = 0
        if index - 1 >= 0:  # застраховка за първия символ да не е под нула
            version[index - 1] += 1
print(".".join(str(number) for number in version))

# version = int(input().replace(".", "")) + 1
# print(".".join(str(version)))


# def check_num(x: int, y: int):
#     if x >= 10:
#         x = 0
#         y += 1
#
#     return x, y
#
#
# n1, n2, n3 = [int(x) for x in input().split(".")]
#
# n3 += 1
# n3, n2 = check_num(n3, n2)
# n2, n1 = check_num(n2, n1)
#
# print(f"{n1}.{n2}.{n3}")
