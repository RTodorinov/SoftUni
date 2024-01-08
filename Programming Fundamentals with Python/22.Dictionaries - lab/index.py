
#  създаване на речници
#  empty dictionary
my_dict = {}

#  dictionary with strings
my_dict = {"fruit": "apple", "vegetable": "cucumber"}

# creating with dict() function and adding kvp to it alone:
animals = dict(dog="beagle", cat="bengal")
animals["monkey"] = "babun"
print(animals)

# write a dictionary on multiple lines:
my_dict = {
    "fruit": "apple",
    "vegetable": "cucumber"
}

#  когато търсим по ключ трябва да внимаваме за типа данни и когато е стринг дали е с главна буква
#  речниците не поддържат индексации при тях се търси по ключ или по стойност на ключа
my_dict = {"fruit": "apple", "vegetable": "cucumber"}
print(my_dict["fruit"])
print(my_dict.get("vegetable"))
print(my_dict.get("grass"))  # това се ползва при if else защото с директното достъпване може да ни даде грешка
print(my_dict["grass"])

# речниците са променяеми : можем да добавяме или да сменяме стойности на вече съществуващи данни
animals = {"Котка": "cat", "куче": "dog"}
print(animals)
animals["Котка"] = "new value"
animals["Прасе"] = "pig"
print(animals)
print(len(animals))

animals = {"Котка": "cat", "куче": "dog"}
if "Котка" in animals:
    print(animals["Котка"])
# #  горното е еквивалент на :
print(animals.get("Котка"))
#  и двете са safe начин за търсене на ключ в речника

#  ключовете не се променят и не могат да се дублират като са и чувствителни към големината на буквите
#  променят се само стойностите към ключовете а те могат да бъдат : int, str, list, tuple, dict ..

# през речниците се итерира през ключа или през стойностите или и през двете.
# 1.итерация през ключовете:
nums = {1: "one", 2: "two", 0: "zero"}

for el in nums:
    print(el)

nums = {1: "one", 2: "two", 0: "zero"}

for el in nums.keys():
    print(el)

nums = {1: "one", 2: "two", 0: "zero"}
print(nums.keys())

# използваме keys() метода да извадим само ключовете от речника
# чрез тях можем и да сменяме стойностите които са записани в тях:
squares = {1: 1, 2: 4, 3: 9}
for key in squares.keys():
    squares[key] *= 2
print(squares)
# result : {1: 2, 2: 8, 3: 18}

# изваждане на стойностите на речника:
nums = {1: "one", 2: "two", 0: "zero"}
print(nums.values())

nums = {1: "one", 2: "two", 0: "zero"}

for el in nums.values():
    print(el)

# итерация и през двете ключ и стойност:
nums = {1: "one", 2: "two", 0: "zero"}
print(nums.items())

nums = {1: "one", 2: "two", 0: "zero"}

for key, value in nums.items():
    print(key, value)

nums = {1: "one", 2: "two", 0: "zero"}

for key in nums:
    print(key, nums[key])

# примери с лист и индекс и двата начина на достъпване на елементите:
ex_list = [1, 2, 3]
for index in range(len(ex_list)):
    print(index, ex_list[index])

ex_list = [1, 2, 3]
for index, el in enumerate(ex_list):
    print(index, el)

# търсене на ключ през стойност
nums = {1: "one", 2: "two", 0: "zero"}
searched_values = "two"
for key, value in nums.items():
    if value == searched_values:
        print(key)

# два различни начина за търсене през value, ако махнем break ще намери и повторенията
nums = {1: "one", 2: "two", 0: "zero"}
searched_values = "two"
for value in nums.values():
    if value == searched_values:
        print("found in that dict")
        break

if searched_values in nums.values():
    print("found in that dict")

# търсене дали има такъв ключ в речника:
nums = {1: "one", 2: "two", 0: "zero"}
if 1 in nums.keys():
    print(nums[1])

# copy() връща копие на речника
my_dict = {1: 'apple', 2: 'banana'}
copied_dict = my_dict.copy()
print(my_dict == copied_dict)


nums = {1: "one", 2: "two", 0: "zero", 22: "two"}
print(nums.pop(1))  # премахва kvp но връща стойноста която е премахната
print(nums)

nums = {1: "one", 2: "two", 0: "zero", 22: "two"}
print(nums.popitem())  # премахва последната стойност но я запазва като тюпъл стойност
print(nums)

nums = {1: "one", 2: "two", 0: "zero", 22: "two"}
keys, values = nums.popitem()  # премахва последната стойност но я запазва като тюпъл стойност
print(nums)
print(keys, values)

nums = {1: "one", 2: "two", 0: "zero", 22: "two"}
keys, values = nums.popitem()
print(nums)
del nums[2]  # аналогична команда на pop(2)
print(nums)
del nums  # премахва и речника и референцията към него
print(nums)

nums = {1: "one", 2: "two", 0: "zero", 22: "two"}
keys, values = nums.popitem()  # премахва последната двойка ключ и стойност
print(nums)
nums.clear()  # премахва елементите на списъка но не и самия него
print(nums)

# # създаване на dict от list където индекса ще е ключ а стойността ще е value
ex_list = [100, 105, 300]
my_dict = {}
for index, el in enumerate(ex_list):
    my_dict[index] = el
print(my_dict)
# # горното но с компрехеншън
ex_list = [100, 105, 300]
my_dict = {index: el for index, el in enumerate(ex_list)}
print(my_dict)
# # проверка за четност на индексите
ex_list = [100, 105, 300]
my_dict = {index: el for index, el in enumerate(ex_list) if index % 2 == 0}
print(my_dict)
# # проверка за четност и нечетност на индексите
ex_list = [100, 105, 300]
my_dict = {index: ("even" if index % 2 == 0 else "odd") for index, el in enumerate(ex_list)}
print(my_dict)

# вложени речници създаване:
students = {1: {'name': 'Peter', 'age': 22}, 2: {'name': 'Alex', 'age': 21}}

# достъпване на елементите:
first_student_name = students[1]['name']
print(first_student_name)

# добавяне на елемент:
students[3] = {}  # {3: {}}
students[3]['name'] = 'Amy'  # {3: {'name': 'Amy'}}
students[3]['age'] = 25   # {3: {'name': 'Amy', 'age': 25}}

# за итериране през вложени речници се ползва вложен for loop:
shopping_list = {
    "foods": {"nuts": "almonds"},
    "drinks": {"soft": "lemonade", "wine": "merlot"}
}

for key, value in shopping_list.items():
    for nested_key, nested_value in value.items():
        print(f'{nested_value} bought')
        shopping_list[key][nested_key] = 'bought'
