x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x = float(input("Enter x: "))
y = float(input("Enter y: "))

if x == x1 or x == x2:
    if y >= y1 and y <= y2:
        print("The point is on one of the sides of the rectangle")
elif y == y1 or y == y2:
    if x >= x1 and x <= x2:
        print("The point is on one of the sides of the rectangle")
else:
    print("The point is not on any of the sides of the rectangle")
#This program takes 6 inputs (x1, y1, x2, y2, x, and y) and checks if the point (x, y) is located on any of the sides
#of the rectangle defined by (x1, y1) and (x2, y2).
#The program outputs a message indicating whether the point is on one of the sides of the rectangle or not.

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x = float(input("Enter x: "))
y = float(input("Enter y: "))

if (x == x1 or x == x2) and (y1 <= y <= y2):
    print("Point is on the side of the rectangle")
elif (y == y1 or y == y2) and (x1 <= x <= x2):
    print("Point is on the side of the rectangle")
else:
    print("Point is not on the side of the rectangle")
