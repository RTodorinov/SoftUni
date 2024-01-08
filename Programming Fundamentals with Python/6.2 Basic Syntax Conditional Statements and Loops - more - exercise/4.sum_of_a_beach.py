
input_string = input()
string_lower = input_string.lower()  # Convert the string to lowercase
word_count = {"sand": 0, "water": 0, "fish": 0, "sun": 0}

for word in word_count.keys():
    count = string_lower.count(word)
    word_count[word] = count

# Count the total number of words
total_words = sum(word_count.values())

print(f"{total_words}")
