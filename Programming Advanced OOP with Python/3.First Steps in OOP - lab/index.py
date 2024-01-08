def print_list(my_list_):
    for el in my_list_:
        if el:
            print(el)


my_list = [1, 2, None, 3]
print(my_list)

my_list2 = [3, 4, 5]
print(my_list2)

''' Splitting Code into Functions
Improves code readability
Allows for easier debugging
A single function should complete a single task
'''

# Scope and Namespace
''' What is Namespace?
A mapping from names to objects
Built-in names, for example the abs() function
Global names in a module
Local names on a function invocation
There is no relation between names in different namespaces
Namespaces Order -> Built-in namespace -> Modul: Global namespace -> Function: Local namespace
'''

''' What is a Scope?
A region in a program where a namespace is directly accessible
In most of the cases there are at least three nested scopes:
--The innermost is checked first
--The scopes of any enclosing functions
--The next-to-last scope (module's global names)
--The outermost (built-in names)
'''

# pravilen nachin za promqna na globalna promenliva
a = 5


def f1(a):
    a = 10
    return a


a = f1(a)
print(a)
# # primer za immutable state
a = 5


def f1():
    a = 10  # immutable state
    print(a)


f1()
print(a)
#  What is an Object-Oriented Programming?
''' 
It is the most popular programming paradigm 
It relies on the concept of classes and objects
A class is used to create individual instance of object
'''

#  Advantages of OOP
''' 
Provides a clear program structure and a clean code
Reduces complexity
Make it easy to write a reusable code
Could test each behavior of an object separately
Facilitates easy maintenance and modification of existing code
'''

#  Objects in Python
''' 
Everything in Python is an object and has a type
We could create as many objects as we like, manipulate them, or remove them
'''
#  What is a Class?
''' 
The class is a blueprint that defines the nature of a future object
In Python a class is created by the keyword class
'''
#  What is an Instance?
'''
Specific realization of an object of a certain class 
The creation of an instance is called instantiation
using self.atribute from __init__
'''
#  Method
''' 
We define the behavior of the object using methods
It is like a function, that works only within a class
'''
# Using a Class
''' Using a class means creating new instances of object and executing operation on the instances
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return 'eating..'


person = Person
print(person.eat)  # instance
