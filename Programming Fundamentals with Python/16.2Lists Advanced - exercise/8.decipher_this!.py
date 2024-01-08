
# secret_words = input().split()
# deciphered_words = []
# deciphered_digits = []
#
# for word in secret_words:
#
#     digit_symbols = ""
#     char_symbols = ""
#
#     for symbol in word:
#         if symbol.isdigit():
#             digit_symbols += symbol
#         else:
#             char_symbols += symbol
#     deciphered_digits.append(int(digit_symbols))
#
#     if len(char_symbols) != 1:
#         char_symbols = f"{char_symbols[-1]}{char_symbols[1:-1]}{char_symbols[0]}"
#     deciphered_words.append(char_symbols)
#
# for n, w in zip(deciphered_digits, deciphered_words):
#     print(f"{chr(n)}{w}", end=" ")
