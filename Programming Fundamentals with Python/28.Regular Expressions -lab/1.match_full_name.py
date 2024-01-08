#  ^[A-Z][a-z]+\s[A-Z][a-z]+\b
#  \b[A-Z][a-z]+ [A-Z][a-z]+\b

import re
names = input()
regex = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
matches = re.findall(regex, names)  # gives list of tuples
print(" ".join(matches))
