''' Tuples and Sets '''

''' Tuples:
Read only collection 
Tuples are part of the standard language
Tuples are immutable* objects ...but the objects, inside the tuples, are mutable
Tuples are sequences, just like lists
Tuples cannot be changed unlike lists
Tuples use parentheses {}, whereas lists use square brackets []
'''

''' Creating a Tuple '''
# To create a tuple, place values within brackets
t = (1, 2, 3)
print(t[0])

# You can also use commas
t = 1, 2, 3
print(t)

# Creating tuple with a single element
t = (1, )

''' Tuple Methods '''
# There are only two available tuple methods:
# count – returns the number of times a specified value occurs
numbers = (1, 2, 1, 3, 1)
numbers.count(1)

# index - returns the index of a particular element
names = ("Pesho", "Gosho", "Gosho")
names.index("Gosho")

# Tuple unpacking allows to extract tuple elements and assign them to elements
data = (1, 2, 3)
x, y, z = data
print(x)
print(y)
print(z)

''' Sets:
Unique Sequence 
Set is an unordered collection of items
Every element of a set is unique and do not allow duplicate values.
Set items are unchangeable, meaning that we cannot change the items after the set has been created.
Sets are mutable, so we can add or remove items from it
Sets can be used to perform mathematical set operations 
(union, intersection, symmetric difference, etc.)
'''
#  Sets are written with curly brackets. {}
#  Using the set() constructor to make a set:
this_set = {"apple", "banana", "cherry"}  # note the double round-brackets
print(type(this_set))
#  The values True and 1 are considered the same value in sets, and are treated as duplicates
#  To determine how many items a set has, we can use the len() function.
#  A set can contain different data types: strings, integers and boolean values
''' Operators used to perform mathematical set operations '''
empty_set = set()

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

union = a | b                 # Union -> {1, 2, 3, 4, 5, 6}
intersection = a & b          # Intersection -> {3, 4}
subset = a < b                # Subset -> False
difference = a - b            # Difference -> {1, 2}
symmetric_difference = a ^ b  # Symmetric Difference -> {1, 2, 5, 6}

'''  
You can also use methods instead of symbols
Each operator is associated to a symbol and a method name '''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.union(b)			       # Equivalent to a | b
a.intersection(b)          # Equivalent to a & b
a.issubset(b)              # Equivalent to a <= b
a.issuperset(b)            # Equivalent to a >= b
a.difference(b)            # Equivalent to a - b
a.symmetric_difference(b)  # Equivalent to a ^ b

''' Set Comprehension 
Set comprehensions are pretty similar to list comprehensions
The only difference is that set comprehensions use curly brackets { }
'''
nums = [1, 2, 3, 4, 4, 5, 6, 2, 1]
unique = {num for num in nums}  # {1, 2, 3, 4, 5, 6}

''' Other Set Methods '''

''' 
add()                  Adds an element to the set 
clear()                Removes all the elements from the set
copy()	               Returns a copy of the set
difference_update()	   Removes the items in this set that are also included 
                       in another, specified set
discard()              Remove the specified item
intersection_update()  Removes the items in this set that are not 
                       in present other, specified set
isdisjoint()           Returns whether two sets have a intersection or not
pop()	               Removes an element from the set
remove()	           Removes the specified element
update()	           Update the set with another set, or any other iterable
symmetric_difference_update()  inserts the symmetric differences from
                               this set and another
'''
