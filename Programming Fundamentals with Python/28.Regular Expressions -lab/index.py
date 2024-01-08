'''
\d  - Returns a match where the string contains digits (numbers from 0-9)
\D  - Returns a match where the string DOES NOT contain digits
\b  - Returns a match where the specified characters are at the beginning or at the end of a word
\s  - Returns a match where the string contains a white space character
\S  - Returns a match where the string DOES NOT contain a white space character
\w  - Returns a match where the string contains any word characters
      (characters from a to Z, digits from 0-9, and the underscore _ character)
\W  - Returns a match where the string DOES NOT contain any word characters
\   - Signals a special sequence (can also be used to escape special characters)
.   - Any character (except newline character)
+   - One or more occurrences
?   - between 0 and 1 times (може да го има или да го няма за стойност в скобите пред този знак)
*   - Zero or more occurrences
|   - Either or - или едното или другото
()  - Capture and group
{}  - Exactly the specified number of occurrences
^   - Starts with (да започва реда)
$   - Ends with
[arn] - Returns a match where one of the specified characters (a, r, or n) are present
[^arn] - Returns a match for any character EXCEPT a, r, and n
[a-n]  - Returns a match for any lower-case character, alphabetically between a and n(по ASCII table)
[0123] - Returns a match where any of the specified digits (0,1,2, or 3) are present
[0-9]  - Returns a match for any digit between 0 and 9
[0-5][0-9] - Returns a match for any two-digit numbers from 00 and 59
[a-zA-Z]   - Returns a match for any character alphabetically between a and z,lower case OR upper case

[A-Za-z0-9] - мачва букви и цифри само
(?P<name>) - именувана група
(^|(?<=\s)) - positive lookbehind
(^|(?<!\s)) - negative lookbehind

($|(?=\s))  - positive lookahead
($|(?!\s))  - negative lookahead
"(.*)" - greedy search
"(.*?)" - non greedy search
functions:
findall - returns a list containing all matches
search - returns a match object if there is a match anywhere in the string
split - returns a list where the string has been split at each match
sub - replace one or many matches with a string
t{3,} - match 3 or more characters t
https://www.w3schools.com/python/python_regex.asp
https://pynative.com/python-regex-flags/
https://www.geeksforgeeks.org/python-regex-lookbehind/
'''

# import re
# text = "The rain in Spain"
# print(re.sub("ai", "$$", text))

import re
text = "I am 12 years old."
print(re.sub(r"\d+", "$$", text))
