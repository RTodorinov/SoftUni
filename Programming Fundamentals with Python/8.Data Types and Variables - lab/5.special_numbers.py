
# resolved with converting data types "int" to "str"
n = int(input())
# For range of n inclusive we iterate and convert to string for easy work with characters
for num in range(1, n + 1):
    is_special = False
    num_as_str = str(num)
    sum_digits = 0

    # Calculate sum digits
    for char in num_as_str:
        sum_digits += int(char)

    # Decide if is it special
    if sum_digits == 5 or sum_digits == 7 or sum_digits == 11:
        is_special = True
    print(f"{num} -> {is_special}")

# # resolved with calculations
# n = int(input())
# # For range of n inclusive we iterate
# for num in range(1, n + 1):
#     sum_of_digits = 0
#     digits = num
#
#     while digits > 0:  # we use while we have number == while digit:
#         sum_of_digits += digits % 10  # we get last digit from digits and put it in sum_of_digits
#         digits = digits // 10  # we can use == int(digit / 10) to remove last digit that we use and to iterate only
#         # with remaining numbers to add them to sum_of_digits
#
#     if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
#         print(f"{num} -> True")
#     else:
#         print(f"{num} -> False")
