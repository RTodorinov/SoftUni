
# num = int(input())
#
# # If given number is greater than 1
# if num > 1:
#     # Iterate from 2 to n / 2
#     for i in range(2, int(num/2)+1):
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(False)  # "is not a prime number"
#             break
#     else:
#         print(True)  # "is a prime number"
# else:
#     print(False)  # "is not a prime number"

from math import sqrt
num = int(input())
prime_flag = 0
if num > 1:
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            prime_flag = 1
            break
    if prime_flag == 0:
        print("True")
    else:
        print("False")
else:
    print("False")
