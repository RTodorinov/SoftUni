
# strings = input().split()
# result = ""
#
# for word in strings:
#     n = len(word)
#     result += word * n
# print(result)

result = [word * len(word)for word in input().split()]
print("".join(result))

# result = [word * len(word)for word in input().split()]
# print(*result, sep="")

# print(''.join([f"{word * len(word)}" for word in input().split()]))
