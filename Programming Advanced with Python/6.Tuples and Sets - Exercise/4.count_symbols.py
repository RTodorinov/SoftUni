txt = tuple(input())

unique_symbols = sorted(set(txt))

for char in unique_symbols:
    print(f"{char}: {txt.count(char)} time/s")


# versiq s rechnik

# txt = tuple(input())
#
# unique_symbols = {}
# for char in txt:
#     if char not in unique_symbols:
#         unique_symbols[char] = 0
#     unique_symbols[char] += 1
#
# [print(f"{char}: {txt.count(char)} time/s") for char, value in sorted(unique_symbols.items())]
