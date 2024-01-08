
def palindrome_filtered(word):
    if word == word[::-1]:
        return word


words = input().split(" ")
palindrome = input()

palindrome_list = [word for word in words if palindrome_filtered(word)]
palindrome_counter = palindrome_list.count(palindrome)
print(palindrome_list)
print(f"Found palindrome {palindrome_counter} times")


# words = input().split(" ")
# palindrome = input()
# palindromes = []
#
# # for word in words:
# #     if word == "".join(reversed(word)):  # We use the join() method with the reversed() method because
# #         palindromes.append(word)     # reversed() returns an iterator, not a string, so we should make it into one.
# [palindromes.append(word) for word in words if word == "".join(reversed(word))]
#
# print(f"{palindromes}")
# print(f"Found palindrome {palindromes.count(palindrome)} times")
