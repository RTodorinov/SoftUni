from collections import deque


def calculate_honey(bee, symbol, nectar):
    if symbol == '*':
        return abs(bee * nectar)
    elif symbol == '+':
        return abs(bee + nectar)
    elif symbol == '-':
        return abs(bee - nectar)
    elif symbol == '/':
        return abs(bee / nectar)


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

