# string = input()
# vowels = ["a", "o", "u", "e", "i", "o", "A", "O", "U", "E", "I"]
# no_vowels_string = "".join([x for x in string if x not in vowels])
# print(no_vowels_string)

# string = input()
# no_vowels = "".join([el for el in string if el.lower() not in ["a", "o", "u", "e", "i", "o"]])
# print(no_vowels)

# string = input()
# result = []
# for ch in string:
#     if ch.lower() not in ['a', 'o', 'u', 'e', 'i']:
#         result.append(ch)
# print("".join(result))


def remove_vowels_from_text(text):
    forbidden_letters = ['a', 'o', 'u', 'e', 'i']
    result = [ch for ch in string if ch.lower() not in forbidden_letters]
    return "".join(result)


string = input()
print(remove_vowels_from_text(string))
