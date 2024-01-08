# 1
# import re
#
# line = input()
# while line:
#     pattern = r"\d+"
#     matches = re.findall(pattern, line)
#     if matches:
#         print(' '.join(matches), end=" ")
#     line = input()

# 2
# import re
#
# sentence = input()
# pattern = r"\b_([A-Za-z0-9]+)\b"
# found_variables_names = re.findall(pattern, sentence)
# if found_variables_names:
#     print(','.join(found_variables_names))

# 3
# import re
#
# sentence = input()
# searched_word = input()
# pattern = fr"\b{searched_word}\b"
# matches = re.findall(pattern, sentence, re.IGNORECASE)
# print(len(matches))


# import re
#
# sentence = input()
# searched_word = input()
# pattern = fr"(?i)\b{searched_word}\b"
# matches = re.findall(pattern, sentence)
# print(len(matches))

# 4
'''
"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z]+[\-\.]*[a-z]+[\.][a-z]+[\.]*[a-z]+))"

"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b"
'''

# import re
#
# sentence = input()
# pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z]+[\-\.]*[a-z]+[\.][a-z]+[\.]*[a-z]+))"
# extracted_emails = re.findall(pattern, sentence)
# for extracted_email in extracted_emails:
#     print(extracted_email[0])

# 5
# import re
#
# command = input()
# bought_furniture = []
# total_money = 0
# pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)"
# while command != "Purchase":
#     match = re.search(pattern, command)
#     if match:
#         furniture, price, quantity = match.groups()
#         bought_furniture.append(furniture)
#         total_money += float(price) * int(quantity)
#     command = input()
# print("Bought furniture:")
# for furniture in bought_furniture:
#     print(furniture)
# print(f"Total money spend: {total_money:.2f}")

# 6

import re

valid_urls = []
pattern = r"(w{3}\.[A-Za-z0-9-\.]+\.[a-z]+)"
command = input()

while command:
    matches = re.search(pattern, command)
    if matches:
        valid_urls.append(matches.group(1))
    command = input()
for valid_url in valid_urls:
    print(valid_url)
