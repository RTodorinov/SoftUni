
# import re
# pattern = "\\b(?P<day>\\d{2})([-.\\/])(?P<month>[A-Z][a-z]{2})\\2(?P<year>\\d{4})\\b"
# text = input()
# matches = re.findall(pattern, text)
# for match in matches:
#     print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")

# import re
# pattern = r"\b(?P<day>\d{2})([-.\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b"
# text = input()
# matches = re.findall(pattern, text)
# for match in matches:
#     print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")


#  когато имаме наименувани групи ги вадим през finditer с match.groupdict()
import re

pattern = r"\b(?P<Day>\d{2})([-.\/])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})\b"
text = input()

matches = re.finditer(pattern, text)
for match in matches:
    match_data = match.groupdict()
    print(f"Day: {match_data['Day']}, Month: {match_data['Month']}, Year: {match_data['Year']}")
