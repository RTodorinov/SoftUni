''' Comprehensions provide us with a short way to construct new sequences
They allow sequences to be built from other sequences
They require less memory
They have shorter syntax and better performance
'''

my_list = [5, 2, 8, 1, 3]
sorted_list = my_list[:]  # Create a copy of the list
for j in range(len(sorted_list) - 1, 0, -1):
    for i in range(j):
        sorted_list.insert(i, sorted_list.pop(i + 1))
print(sorted_list)
''' горното да се напише с компрехеншън? '''
test = [sorted_list.insert(i, sorted_list.pop(i+1)) for j in range(len(sorted_list)-1, 0, -1) for i in range(j)]
print(test)

''' Creating a list using the range function'''

'''create a list from 1 to 4 '''
x = [num for num in range(5)]
print(x)

''' Getting the square values of numbers in a list '''
# new_list = [1, 2, 3, 4]
# squares = []
# for x in new_list:
#     squares.append(x**2)
# print(squares)

new_list = [1, 2, 3, 4]
squares = [x**2 for x in new_list]
print(squares)

''' Using if statement in a list comprehension '''
''' get evens from list '''
new_list = [1, 2, 3, 4, 5, 6]
evens = [num for num in new_list if num % 2 == 0]
print(evens)

''' using if and else goes all from left side and result to True or False '''
nums = [1, 2, 3, 4, 5, 6]
filtered = [True if x % 2 == 0 else False for x in nums]
print(filtered)

nums = ["even" if num % 2 == 0 else "odd" for num in range(1, 11)]

''' List Methods '''

''' Using the append() method : Add single element at the end '''
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

''' Using the extend() method : Add multiple elements at the end '''
fruits = ["apple", "banana", "cherry"]
additional_fruits = ["lemon", "strawberry"]
fruits.extend(additional_fruits)
print(fruits)

''' Using the insert() method: Add single element at a specific index '''
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
fruits.insert(3, "strawberry")
print(fruits)

''' Using the index() method: Finds the index of the first occurrence '''
fruits = ["apple", "banana", "cherry", "apple", "lemon", "apple"]
index = fruits.index("apple", 4)
print(index)

my_list = [1, 2, 3, 2, 2]
last = my_list.index(2)


''' Using the clear() method: Removes all elements '''
my_list = [1, 2, 3]
my_list.clear()
print(my_list)

''' Using the pop() method: Removes element by index and returns it '''
my_list = [1, 2, 3]
number = my_list.pop(0)
print(my_list)

''' Using the remove() method: Removes by value (first occurrence) '''
my_list = [1, 2, 3]
my_list.remove(1)
print(my_list)

''' Generate list with same values '''

train_length = int(input())
train = [0] * train_length

''' Creating list with 10 zeros '''
notes = [0] * 10

''' Using the count() method: Finds all occurrences in a list '''
my_list = [1, 2, 3, 2, 2]
my_list.count(2)

''' Using the reverse() method: Reverses the elements '''
my_list = [1, 2, 3]
my_list.reverse()


''' Advanced Functions '''
''' sorted() Function '''

''' Sorts the elements of a list in ascending order '''
fruits = ["apple", "banana", "cherry", "strawberry"]
sorted_fruits = sorted(fruits)
print(fruits)

number_list = [6, 2, 1, 4, 3, 5]
sorted_numbers = sorted(number_list)
print(number_list)
print(sorted_numbers)

''' Sorts the elements of a list in descending order '''
number_list = [6, 2, 1, 4, 3, 5]
sorted_numbers = sorted(number_list, key=lambda x: -x)
print(number_list)
print(sorted_numbers)

# fruits = ["apple", "banana", "cherry", "strawberry"]
# sorted_fruits = sorted(fruits, key=len)
# print(fruits[::-1])

''' map() Function 
Use it to convert list of strings to list of integers '''
strings_list = ["1", "2", "3", "4"]
numbers_list = list(map(int, strings_list))  # Returns int(x) for each element x in the list

''' It applies function to every item of an iterable '''
numbers_list = [1, 2, 3, 4]
doubled_list = list(map(lambda x: x*2, numbers_list))

# numbers = [1, 2, 3, 4, 5]
# square_numbers = map(lambda x: x**2, numbers)
# print(list(square_numbers))
# It returns an iterator object, so you need to convert it into a list

names = ["john", "emma", "gosho", "alex"]
capitalized_names = map(str.capitalize, names)
print(list(capitalized_names))

# words = ["hello", "world", "python"]
# reversed_words = map(lambda x: x[::-1], words)
# print(list(reversed_words))

''' filter() Function '''
''' Use it to filter elements that fulfill a given condition '''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter(lambda x: x % 2 != 0, numbers)  # Filter all the odd numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)  # Filter all the even numbers
''' The lambda should return either True or False '''
''' It returns an iterator object, so you need to convert it into a list '''
print(list(odd_numbers))
print(list(even_numbers))

''' Additional List Manipulations '''
''' Swapping List Elements '''
nums = [1, 2, 3]
nums[0], nums[1], nums[2] = nums[2], nums[0], nums[1]
print(nums)
''' The first element on the left swaps with the first on the right etc. '''

''' Concatenating Lists '''
''' You can use the "+" operator to join two lists '''
nums_list_1 = [1, 2, 3]
nums_list_2 = [4, 5, 6]
final_list = nums_list_1 + nums_list_2
print(final_list)
''' Always the second list is added at the end of the first '''

''' The Set Function '''
''' You can use the set() function to extract only the unique elements from a list '''
numbers = [1, 2, 2, 3, 1, 4, 5, 4]
unique_numbers = list(set(numbers))
''' The set() function returns a set with the unique values '''

''' generator '''
numbers = (map(int, input().split()))
