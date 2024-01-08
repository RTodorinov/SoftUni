
from math import ceil
persons = int(input())
capacity_of_elevator = int(input())

courses = ceil(persons / capacity_of_elevator)
print(courses)
