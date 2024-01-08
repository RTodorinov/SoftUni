class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dict_tuple = tuple(dictionary.items())  # още тук обръщаме това което ни се подава към тюпъл.
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.dict_tuple):
            i = self.idx
            self.idx += 1
            return self.dict_tuple[i]
        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
print("---------------------------------------------")
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
