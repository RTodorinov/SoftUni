class Person:
    # атрибути на класа

    def __init__(self, name: str, age: int):  # атрибути на инстанцията
        self.name = name
        self.age = age

    def has_birthday(self):  # метод на класа
        self.age += 1

    def change_name(self, new_name):
        self.name = new_name


ivan = Person('Ivan', 30)  # подаване на информация за инстанцията на класа
pesho = Person('Petar', 25)
print(ivan.age)
print(ivan.name)
ivan.has_birthday()
print(ivan.age)
print(pesho.age)
ivan.change_name('Gosho')
print(ivan.name)
