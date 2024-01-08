def vowel_filter(function):
    def wrapper():
        str_list = function()
        vowels = [char for char in str_list if char.lower() in "aeiou"]
        return vowels
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "E"]


print(get_letters())
