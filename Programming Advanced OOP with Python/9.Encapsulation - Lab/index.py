class Person:
    kind = "mammal"

    def __init__(self, name: str, age: int):
        self._name = name
        self.age = age

    def say_hi(self):
        return "Hello"


class Student(Person):
    def __init__(self, name, age):
        self._name = f"Student {name}"


p = Person("Test", 30)
print(p._name)
print(p.age)
print(p.say_hi())
p._name = "Hello"
print(p._name)


