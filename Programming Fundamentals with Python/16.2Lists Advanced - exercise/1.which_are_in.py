
# first_string = input().split(", ")
# second_string = input().split(', ')
# substrings = []
# for element in first_string:
#     for second_element in second_string:
#         if element in second_element:
#             substrings.append(element)
#             break
# print(substrings)

# first_sequence = input().split(", ")
# second_sequence = input().split(", ")
# substrings = [first_word for first_word in first_sequence
#               if any(first_word in second_word for second_word in second_sequence)]
# print(substrings)


def find_substrings(first_sequence, second_sequence):
    substrings = []
    for element in first_sequence:
        for second_element in second_sequence:
            if element in second_element:
                substrings.append(element)
                break
    return substrings


first_string = input().split(", ")
second_string = input().split(', ')
result = find_substrings(first_string, second_string)
print(result)
