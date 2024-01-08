
resource = input()
collected_resources = {}

while resource != "stop":
    quantity = int(input())
    if resource not in collected_resources:
        collected_resources[resource] = 0
    collected_resources[resource] += quantity

    resource = input()

for resource, quantity in collected_resources.items():
    print(f"{resource} -> {quantity}")


# collected_resources = {}
# while True:
#     resource = input()
#     if resource == "stop":
#         break
#
#     quantity = int(input())
#     if resource in collected_resources:
#         collected_resources[resource] += quantity
#     else:
#         collected_resources[resource] = quantity

# for resource, quantity in collected_resources.items():
#     print(f"{resource} -> {quantity}")

# results = [f"{resource} -> {quantity}" for resource, quantity in collected_resources.items()]
# print("\n".join(results))

# [print(f"{resource} -> {quantity}") for resource, quantity in collected_resources.items()]
