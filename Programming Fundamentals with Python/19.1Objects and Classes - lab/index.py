''' функцията вътре в класа се нарича метод
- клса е топ левъл а обектите са инстанции на класа
- атрибутите на обектите се присвояват с конструктор __init__
- атрибутите са еднакви за всички инстанции на класа
- методите винаги започват със self
'''

# class Automobile:
#
#     name = ""
#
#     def drive_to_repair(self):
#         print(f"Car is driven to repair by {self.name}")
#
#
# class Car(Automobile):  # това е под клас на Automobile
#
#     def __init__(self, mark, model, year, color):  # инициализатора __init__ към него се закачат атрибутите на обектите
#         self.mark = mark
#         self.model = model
#         self.year = year
#         self.color = color
#
#     def start_engine(self):  # това е метод който се ползва от обектите
#         print(f"The {self.mark} {self.model}\'s engine is starting")
#
#     def drive(self, distance):
#         print(f"The {self.mark} {self.model} is driving {distance} kilometers")
#
#     def stop_engine(self):
#         print(f"The {self.mark} {self.model}\'s engine is stopping")
#
#     def display_info(self, plate_number):
#         print(f"mark: {self.mark} \nmodel: {self.model} \nyear: {self.year} \ncolor: {self.color} \nnumber: "
#               f"{plate_number} \nowner: {self.name}")
#
#
# car1 = Car("Toyota", "Corolla", 2020, "Red")  # това е обект car1
# car2 = Car("Mercedes", "S500", 2021, "Black")  # това е обект car2
#
#
# car1.start_engine()
# car1.drive(200)  # този параметър се подава извън класа
# car1.stop_engine()
# car1.name = "Ivan Petrov"
# car1.display_info("CA2346MM")  # този параметър се подава извън класа
# car1.drive_to_repair()
#

# class Person:
#     def __init__(self, first_name, last_name, age=0):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#
# person = Person("Ivan", "Petrov", 45)
# print(person.first_name)
# print(person.last_name)
# print(person.age)

# 1
# class Comment:
#     def __init__(self, username, content, likes=0):
#         self.username = username
#         self.content = content
#         self.likes = likes
#
#
# comment = Comment("user1", "I like this book")
# print(comment.username)
# print(comment.content)
# print(comment.likes)

# 2

# class Party:
#     def __init__(self):
#         self.people = []
#
#
# party = Party()
# name = input()
# while name != "End":
#     party.people.append(name)
#     name = input()
#
# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")

# class Party:
#     def __init__(self):
#         self.people = []
#
#
# party = Party()
# while True:
#     name = input()
#     if name == "End":
#         break
#
#     party.people.append(name)
#
# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")

# class Party:
#     def __init__(self):
#         self.people = []
#
#     def add_person(self, name):
#         self.people.append(name)
#
#     def get_party_info(self):
#         party_info = {
#             "going": ', '.join(self.people),
#             "total": len(party.people)
#         }
#         result = f"Going: {party_info['going']}\nTotal: {party_info['total']}"
#
#         return result
#
#
# party = Party()
# while True:
#     name = input()
#     if name == "End":
#         break
#     party.add_person(name)
#
# print(party.get_party_info())

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def calculate_area(self):
#         return self.length * self.width
#
#     def resize(self, new_length, new_width):
#         self.length = new_length
#         self.width = new_width
#
#
# rect = Rectangle(4, 5)
# area = rect.calculate_area()
# print(area)
# rect.resize(6, 7)
# print(rect.calculate_area())

# 3
# class Email:
#
#     def __init__(self, sender, receiver, content):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False
#
#     def send(self):
#         self.is_sent = True
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
#
#
# emails = []
#
# # line = input()
# # while line != "Stop":
# #     tokens = line.split(" ")
# #     sender = tokens[0]
# #     receiver = tokens[1]
# #     content = tokens[2]
# #     email = Email(sender, receiver, content)
# #     emails.append(email)
# #     line = input()
# #
# # send_emails = list(map(lambda x: int(x), input().split(", ")))
# #
# # for x in send_emails:
# #     emails[x].send()
# #
# # for email in emails:
# #     print(email.get_info())
#
#
# while True:
#     tokens = input().split(" ")
#     if tokens[0] == "Stop":
#         break
#     sender, receiver, content = tokens
#     email = Email(sender, receiver, content)
#     emails.append(email)
#
# send_emails = [int(i) for i in input().split(", ")]  # взимам индексите след "Stop"
#
# for idx in send_emails:
#     if 0 <= idx < len(emails):  # проверка за валидност на индекса
#         emails[idx].send()
#
# for email in emails:
#     print(email.get_info())

# 5
# class Circle:
#     __pi = 3.14  # защитен параметър
#
#     def __init__(self, diameter):
#         self.diameter = diameter
#         self.radius = diameter / 2
#
#     def calculate_circumference(self):
#         return Circle.__pi * self.diameter
#
#     def calculate_area(self):
#         return Circle.__pi * self.radius * self.radius
#
#     def calculate_area_of_sector(self, angle):
#         return (angle / 360) * Circle.__pi * self.radius * self.radius
#
#
# circle = Circle(10)
# angle = 5
#
# print(f"{circle.calculate_circumference():.2f}")
# print(f"{circle.calculate_area():.2f}")
# print(f"{circle.calculate_area_of_sector(angle):.2f}")

# 4
# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == "mammal":
#             self.mammals.append(name)
#         elif species == "fish":
#             self.fishes.append(name)
#         elif species == "bird":
#             self.birds.append(name)
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         result = ""
#         if species == "mammal":
#             result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
#         elif species == "fish":
#             result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
#         elif species == "bird":
#             result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
#
#         result += f"Total animals: {Zoo.__animals}"
#         return result
#
#
# zoo_name = input()
# zoo = Zoo(zoo_name)
# count = int(input())
#
# for el in range(count):
#     animal = input().split()
#     species = animal[0]
#     name = animal[1]
#     zoo.add_animal(species, name)
#
# info = input()
# print(zoo.get_info(info))
