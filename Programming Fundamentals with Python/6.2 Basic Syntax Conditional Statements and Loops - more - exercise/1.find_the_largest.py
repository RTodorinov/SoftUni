
num = int(input())  # the given number

# convert the number to a list of digits, sort them in descending order, and join them back into a string
sorted_digits_str = ''.join(sorted(str(num), reverse=True))

# convert the resulting string of digits back to an integer
largest_num = int(sorted_digits_str)

print(largest_num)  # output the largest number

# same with for loop
# num = int(input())  # the given number
#
# # convert the number to a list of digits
# digits = [int(d) for d in str(num)]
#
# # sort the digits in descending order using a for loop
# for i in range(len(digits)):
#     for j in range(i + 1, len(digits)):
#         if digits[j] > digits[i]:
#             digits[i], digits[j] = digits[j], digits[i]
#
# # join the sorted digits together into a string and convert it back to an integer
# largest_num = int(''.join([str(d) for d in digits]))
#
# print(largest_num)  # output the largest number
