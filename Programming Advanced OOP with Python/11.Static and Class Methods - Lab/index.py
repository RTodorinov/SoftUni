# class Person:
#     kind = "genius"
#
#     def __init__(self, name: str):
#         self.name = name
#
#     def introduce(self):
#         self.name = "Rosen"
#         return f"Hi. My name is {self.name}. I am a {self.kind}"
#
#     @staticmethod
#     def is_adult(age: int):
#         return age >= 18
#
#
# Man = Person("Test")
# print(Man.introduce())
# print(Man.is_adult(44))
# print(Man.is_adult(15))


# class Pizza:
#     def __init__(self, ingredients):
#         self.ingredients = ingredients
#
#     @classmethod  # standard already made pizza type
#     def quattro_formaggi(cls):
#         return cls(["mozzarella", "gorgonzola", "fontina", "parmigiana"])
#
#     @classmethod  # standard already made pizza type
#     def pepperoni(cls):
#         return cls(["tomato sauce", "parmesan", "pepperoni"])
#
#
# custom_pizza = Pizza(["tomato", "cheese", "beacon", "ananas"])  # custom pizza
# first_pizza = Pizza.quattro_formaggi()
# second_pizza = Pizza.pepperoni()

