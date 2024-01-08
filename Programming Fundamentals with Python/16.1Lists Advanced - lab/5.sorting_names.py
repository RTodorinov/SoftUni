
# names = input().split(", ")
# sorted_names = sorted(names, key=lambda x: (-len(x), x))
#
# print(sorted_names)


def sort_names():
    names = input().split(", ")
    sorted_names = sorted(names, key=lambda x: (-len(x), x))
    # създава tuple с два елемента първо по дължината на името
    # и после по азбучен ред на името
    return sorted_names


result = sort_names()
print(result)

