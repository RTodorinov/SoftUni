# from collections import deque
#
# working_bees = deque(int(x) for x in input().split())
# nectar = [int(x) for x in input().split()]
# operations = deque(x for x in input().split())
#
# honey_made = 0
# operators = {
#     '+': lambda a, b: a + b,
#     '-': lambda a, b: a - b,
#     '*': lambda a, b: a * b,
#     '/': lambda a, b: a // b,
# }
#
# while working_bees and nectar:
#     bee = working_bees.popleft()
#     current_nectar = nectar.pop()
#
#     if current_nectar < bee:
#         working_bees.appendleft(bee)
#         continue
#     operation = operations.popleft()
#     if current_nectar > 0:
#         honey_made += abs(operators[operation](bee, current_nectar))
#
# print(f"Total honey made: {honey_made}")
#
# if working_bees:
#     print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
#
# if nectar:
#     print(f"Nectar left: {', '.join(str(x) for x in nectar)}")

from collections import deque


def calculate_honey(bee, symbol, nectar_):
    if symbol == '*':
        return abs(bee * nectar_)
    elif symbol == '+':
        return abs(bee + nectar_)
    elif symbol == '-':
        return abs(bee - nectar_)
    elif symbol == '/':
        return abs(bee / nectar_)


bees = deque([int(x) for x in input().split()])
nectar = deque([int(x) for x in input().split()])
symbols = deque(input().split())

honey_made = 0

while len(bees) != 0 and len(nectar) != 0:
    if bees[0] <= nectar[-1]:
        sym = symbols[0]
        if sym == '/' and nectar[-1] == 0:
            nectar.pop()
            bees.popleft()
            symbols.popleft()
            continue
        else:
            honey_made += calculate_honey(bees[0], sym, nectar[-1])
            nectar.pop()
            bees.popleft()
            symbols.popleft()
    else:
        nectar.pop()

print(f"Total honey made: {honey_made}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
