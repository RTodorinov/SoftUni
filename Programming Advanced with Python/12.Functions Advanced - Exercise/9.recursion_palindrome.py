# def palindrome(word, index):
#     if index == len(word) // 2:
#         return f"{word} is a palindrome"
#     if word[index] != word[-1 - index]:
#         return f"{word} is not a palindrome"
#     return palindrome(word, index + 1)


# def palindrome(word, idx):
#     if idx == len(word) // 2:
#         return f"{word} is a palindrome"
#     if word[idx] == word[-idx-1]:
#         print(word[-idx-1])
#         return palindrome(word, idx+1)
#     else:
#         return f"{word} is not a palindrome"


def palindrome(word, idx):
    if word == word[::-1]:
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print()
print(palindrome("peter", 0))
