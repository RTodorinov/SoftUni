# from collections import deque
#
# colors_string = deque(input().split())
#
# main_colors = ['red', 'blue', 'yellow']
# secondary_colors = {'orange': ['red', 'yellow'],
#                     'purple': ['red', 'blue'],
#                     'green': ['blue', 'yellow']}
# collected_colors = []
#
# while colors_string:
#     first_string = colors_string.popleft()
#     last_string = colors_string.pop() if colors_string else ''
#
#     if first_string + last_string in main_colors or first_string + last_string in secondary_colors:
#         collected_colors.append(first_string + last_string)
#     elif last_string + first_string in main_colors or last_string + first_string in secondary_colors:
#         collected_colors.append(last_string + first_string)
#     else:
#         if len(first_string) > 1:
#             colors_string.insert(len(colors_string) // 2, first_string[:-1])
#         if len(last_string) > 1:
#             colors_string.insert(len(colors_string) // 2, last_string[:-1])
#
# for color in collected_colors:
#     if color in secondary_colors:
#         for el in secondary_colors[color]:
#             if el not in collected_colors:
#                 collected_colors.remove(color)
#                 break
#
# print(collected_colors)

from collections import deque

substring = deque(input().split())

colors = {
    "all colors": ("red", "yellow", "blue", "orange", "purple", "green"),
    "required colors": {
        "orange": ("red", "yellow"),
        "purple": ("red", "blue"),
        "green": ("yellow", "blue")
    }
}

result = []

while substring:
    last_part = ""
    if len(substring) > 1:
        last_part = substring.pop()
    first_part = substring.popleft()
    for color in (first_part + last_part, last_part + first_part):
        if color in colors["all colors"]:
            result.append(color)
            break
    else:
        for item in (first_part[:-1], last_part[:-1]):
            if item:
                substring.insert(len(substring) // 2, item)

for color, req_colors in colors["required colors"].items():
    if any(x not in result and color in result for x in req_colors):
        result.remove(color)

print(result)
