#  Class Objects
''' Classes support two kinds of operations:
attribute references – access them using the "." operator
instantiation - uses function notations
'''


class Example:
    text = 'Hello'

    def print_text(self):
        return 'SoftUni'


Example.text	    # attribute reference
Example.print_text  # attribute reference
x = Example()	     # instantiation

#  Instantiation
''' It is known as "calling" the class
Creates an empty object - new instance of the class
Assigns the object to a local variable
'''


class Person:
    name = "George"
    age = 25


person = Person()
print(person.name)  # George
print(person.age)   # 25

#  __init__()
''' Creates objects with instances, customized to a specific initial state
Automatically invoked for the newly created class instance
'''


class Laptop:
    def __init__(self, name, model):
        self.name = name
        self.model = model


my_laptop = Laptop("Inspiron 15", "Dell")

#  self Parameter
''' self is used to represent the instance of the class
It binds the attributes with the given arguments
It is not a keyword, but using it increases the readability of code
'''


class Laptop:
    def __init__(self, name, model):
        self.name = name
        self.model = model


my_laptop = Laptop("Inspiron 15", "Dell")

#  Instance Objects
''' Instances support only one kind of operations:
attribute references - access them using the "." operator 
'''


class Laptop:
    def __init__(self, name, model):
        self.name = name
        self.model = model


my_laptop = Laptop("Inspiron 15", "Dell")
print(laptop.name)  # Inspiron 15
print(laptop.model)  # Dell

