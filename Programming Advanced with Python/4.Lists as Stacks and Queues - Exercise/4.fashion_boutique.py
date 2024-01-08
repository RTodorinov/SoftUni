clothes_stack = [int(x) for x in input().split()]
rack_capacity = int(input())

clothes_rack = 0

while clothes_stack:
    clothes_rack += 1
    current_rack_capacity = rack_capacity

    while clothes_stack and clothes_stack[-1] <= current_rack_capacity:
        current_rack_capacity -= clothes_stack.pop()

print(clothes_rack)
