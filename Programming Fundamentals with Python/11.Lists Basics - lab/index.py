''' A list is a collection which is index supported and
changeable (mutable)/ листовете са (списък)колекция която може да бъде индексирана и променяна
лист е вид колекция като променлива която съдържа много типове стойности от различен вид
It allows duplicate members/ позволява съдържането на еднакви стойности(дубликати)
In Python lists are written with square brackets / в Python листове се пишат с [] скоби '''

# example :
list_example = ["apple", "banana", "cherry"]
my_list = list()
my_list1 = []

# print(dir(list_example))
# print(help(list_example))  # дава помощ като и подробна информация за методите
# print(len(list_example))  # дава бройката елементи в листа

''' Usage in Programming / Използване в програмирането:

Lists are very useful for storing multiple elements / полезни са за съдържането на много типове елементи (променливи)
They can expand and shrink/ могат да нарастват или да намаляват
In Python a single list can store elements with 
different data types/ в един лист може да се добавят елементи от различни дата типове
Lists are the basis for the other abstract data types 
like queues, stacks and their variations/ те са основата на останалите типове от данни - опашки, стакове '''

# example :
some_text = "a     b  c d"
my_list = some_text.split()
spaces = some_text.split(" ")
print(my_list)
print(spaces)

# example :
text = "Hello"
print(f"[{'-*'.join(['a','b','c','d'])}]")

# example :
list_of_numbers = [1, 2, 3, 4, 5]
print(f"{sum(list_of_numbers)}")

''' accessing elements by INDEX '''

# example :
my_list = ["banana", "tomato", "apple", "mango"]
just_some_list_item = my_list[2]
print(just_some_list_item)
# example :
my_list = ["banana", ["test", 123], "apple", 0.35]
just_some_list_item = my_list[1][1]
print(just_some_list_item)

''' We can use the negative sign to access an element
 The negative sign will start counting from the end of the list '''

# example :
my_pets = ["cat", "dog", "parrot"]
print(my_pets[-1])
print(my_pets[-2])
print(my_pets[-3])


''' методът .split() връща резултат, който е лист с елементите, които сме разделили, затова се ползва с нова променлива
която да приеме листа тъй като той не променя основния стринг '''

# example :
my_list = "This is just a test string"
x = my_list.split()
print(x)
print(x[2])
print(my_list)

''' join работи с листове обратно на сплит и от елементите на лист прави стинг '''

# example :
my_list = ["a", "b", "c", "d"]
just_some_string = "-".join(my_list)
print(just_some_string)

# example :
my_list = ["dog", "cat", "fish"]
while my_list:
    print(my_list[0], end=" ")
    current_element = my_list[0]
    my_list.remove(current_element)
print(f"\n{my_list}")

''' lists manipulation '''

''' Use the append method to add a new element at the end of the list
добавя/модифицира директно елемент към колекцията '''

# example :
empty_list = list()
# empty_list = []

empty_list.append(2)
empty_list.append("b")
empty_list.append([1, 2, "c"])
print(empty_list)

''' Use the remove method to remove a particular element / директно модифицира/премахва елемент от колекцията '''

# example :
list_of_numbers = [1, 2, 3, 4, 5]
list_of_numbers.remove(3)
list_of_numbers.remove(1)
print(list_of_numbers)

''' Use the sum() function to addition elements in the list: '''

# example :
list_of_numbers = [1, 2, 3, 4, 5]
print(f"{sum(list_of_numbers)}")

''' using clear() removes all the elements from the list '''

# example :
fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()
print(fruits)

''' using copy() returns a copy of the list '''

# example :
fruits = ['apple', 'banana', 'cherry', 'orange']

x = fruits.copy()
print(x, fruits)
# now if you change x fruits will not be affected

''' using count() returns the number of elements with the specified value '''

# example :
fruits = ['cherry', 'apple', 'banana', 'cherry']

x = fruits.count("cherry")
print(x)

''' using extend() add the elements of a list (or any iterable), to the end of the current list '''

# example :
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)

''' using index() returns the index of the first element with the specified value '''

# example :
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")
print(x)

''' using insert() adds an element at the specified position '''

# example :
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")
print(fruits)

''' using pop() removes the element at the specified position '''

# example :
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)
print(fruits)
# using pop method can save poped item to other variable
fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)
print(fruits)
print(x)

''' using reverse() reverses the order of the list '''

# example :
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()
print(fruits)

''' using sort() sorts the list ascending by default '''
# example :
cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)  # can be False
print(cars)

# example :
# A function that returns the length of the value:


def my_Func(e):
    return len(e)


cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=False, key=my_Func)
print(cars)

# example :
# A function that returns the 'year' value:


def myFunc(e):
    return e['year']


cars = [
{'car': 'Ford', 'year': 2005},
{'car': 'Mitsubishi', 'year': 2000},
{'car': 'BMW', 'year': 2019},
{'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)

''' There are two ways you can loop through a list using for loops
Iterating over the elements
 '''
# examples :
my_list = ["dog", "cat", "fish"]
for element in my_list:
    print(element, end=" ")

# using generated list with range

my_list = ["dog", "cat", "fish"]
for index in range(len(my_list)):
    print(index, end=" ")
    print(my_list[index], end=" ")

''' Using While Loop:
Най удобно се ползва while цикъл при вадене на елементи от лист
You can also use while loops to iterate through a list
In the first example, we iterate until we reach the end of the list
In the second example, we iterate until there are no more elements in the list
'''

# first example:
my_list = ["dog", "cat", "fish"]
idx = 0
while idx < len(my_list):
    print(my_list[idx], end=" ")
    idx += 1

# second example:
my_list = ["dog", "cat", "fish"]
while my_list:
    print(my_list[0], end=" ")
    current_element = my_list[0]
    my_list.remove(current_element)

''' Searching for Elements:
Use the keyword "in" to check if an element is in a list '''

my_list = [1, 2, 3, 4]
if 3 in my_list:
    print("The number 3 is in the list")

''' Usually the "in" keyword is used with if-else statements

The "not in" keywords are used to check if an element is NOT in a list
'''

my_list = [1, 2, 3, 4]
if 5 not in my_list:
    print("The number 5 is not in the list")

''' The "not in" keywords are also mainly used with 
if-else statements
'''

