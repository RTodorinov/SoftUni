
count = int(input())
synonyms = {}

for _ in range(count):
    word = input()
    synonym = input()

    if word not in synonyms.keys():  # това е метод за създаване на лист в речник и добавяне на стойности в него
        synonyms[word] = []
    synonyms[word].append(synonym)

for word, all_synonyms in synonyms.items():
    print(f"{word} - {', '.join(all_synonyms)}")
