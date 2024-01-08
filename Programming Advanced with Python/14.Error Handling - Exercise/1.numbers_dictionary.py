numbers_dictionary = {}
line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        # numbers_dictionary[number_as_string] = number - if we want to do it without else
    except ValueError:
        print("The variable number must be an integer")
    else:
        numbers_dictionary[number_as_string] = number
    line = input()

line = input()

while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)
