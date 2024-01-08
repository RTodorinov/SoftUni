
CAPACITY = 255
fills = int(input())
total_liters = 0

for _ in range(fills):
    litters = int(input())
    total_liters += litters
    if total_liters > CAPACITY:
        total_liters -= litters
        print("Insufficient capacity!")
        continue
print(total_liters)


# CAPACITY = 255
# fills = int(input())
# total_liters = 0
#
# for _ in range(fills):
#     litters = int(input())
#     if total_liters + litters > CAPACITY:
#         print("Insufficient capacity!")
#     else:
#         total_liters += litters
# print(total_liters)

