"""
1. Read the two sequences - save the in deque
2. Define dictionary with key = word and value = word
3. While we have sequences, pop from the sequences
4. Iterate through every word in the searched words
  - remove all occurrences of the vowel and consonant in the value of the word dict
  - check if we have empty string as a value
  - print that a word was found and break loops
5. Print the rest of the needed output
"""
from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

words = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for word in words:
        words[word] = words[word].replace(vowel, '')
        words[word] = words[word].replace(consonant, '')

        if not words[word]:
            print(f"Word found: {word}")
            break
    else:
        continue

    break
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
