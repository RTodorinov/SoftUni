# 1. Exchange Integers
a, b = input(), input()
print(f'Before:\na = {a}\nb = {b}\nAfter:\na = {b}\nb = {a}')

# 2. Prime Number Checker
# number = int(input())
# print(number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1)))

# 3. Decrypting Messages
# key = int(input())
# print(''.join([chr(ord(input()) + key) for _ in range(int(input()))]))

# 4. Balanced Brackets
# bracket = 0
# for ch in [input() for _ in range(int(input()))]:
#     if ch == '(': bracket += 1
#     elif ch == ')': bracket -= 1
#     if bracket not in (0, 1): print("UNBALANCED"); exit()
# print('BALANCED')
