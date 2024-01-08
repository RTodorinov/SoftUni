
string = input()  # the string to search for capital letters

capital_indices = [i for i in range(len(string)) if string[i].isupper()]

print(capital_indices)  # output the list of capital letters indices

# word = input()
# list_to_print = []
# for el in range(len(word)):
#     if word[el].isalpha() and word[el].isupper():
#         list_to_print.append(el)
# print(list_to_print)
