
while True:
    word = input()
    if word == "SoftUni":
        continue
    elif word == "End":
        break
    for ch in word:
        print(f"{ch}{ch}", end="")    # print(ch + ch, end="")
    print()

# while True:
#     word = input()
#     if word == "SoftUni":
#         continue
#     elif word == "End":
#         break
#     converted_word = ""
#     for ch in word:
#         converted_word += 2 * ch
#     print(converted_word)
