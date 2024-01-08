def words_sorting(*words):
    words_dict = {word: sum(map(ord, word)) for word in words}
    if sum(words_dict.values()) % 2 == 0:
        sorted_words_dict = sorted(words_dict.items(), key=lambda kvp: kvp[0])
    else:
        sorted_words_dict = sorted(words_dict.items(), key=lambda kvp: -kvp[1])

    result = ""
    for word, value in sorted_words_dict:
        result += f"{word} - {value}\n"
    return result


# TEST CODE
print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
print("==================")
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
    ))
print("==================")
print(
    words_sorting(
        'cacophony',
        'accolade'
    ))
