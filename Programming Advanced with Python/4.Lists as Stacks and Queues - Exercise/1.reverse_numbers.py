numbers = input().split()
reversed_stack = []
while numbers:
    reversed_stack.append(numbers.pop())
print(' '.join(reversed_stack))

# numbers = input().split()
#
# while numbers:
#     print(numbers.pop(), end=' ')
