import re

pattern = r"(.+?)\>(\d{3})?\|([a-z]{3})\|([A-Z]{3})\|([^<>]+)\<\1"

n = int(input())

for _ in range(n):
    password = input()

    match = re.fullmatch(pattern, password)
    if match:
        middle_groups = "".join(group for group in match.groups()[1:] if group)
        print("Password: " + middle_groups)
    else:
        print("Try another password!")
