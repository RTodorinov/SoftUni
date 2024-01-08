
import re
pattern = r"\+359 2 \d{3} \d{4}\b|\+359-2-\d{3}-\d{4}\b"
phone_numbers = input()
matches = re.findall(pattern, phone_numbers)
print(*matches, sep=', ')

# import re
# matching_pattern = "(\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4})\\b"
# phone_numbers = input()
# matches = re.findall(matching_pattern, phone_numbers)
# print(", ".join(matches))

#  пример когато имаме различен текст за мачване с един pattern
# text1 = input()
# text2 = input()
# text3 = input()
#
# pattern = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"
#
# regex_pattern = re.compile(pattern)  # първо го компилираме
# matches = regex_pattern.findall(text1)
# matches2 = regex_pattern.findall(text2)
# matches3 = regex_pattern.findall(text3)
