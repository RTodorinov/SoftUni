# n = int(input())
# row = 0
# for row in range(1, n + 1):
#     if row == 1:
#         print((n - row) * " " + row * "*")
#     else:
#         print((n - row) * " " + row * "* ")
# for rows in range(0, n - 1):
#     if rows == 0:
#         print((n - (row - 1)) * " " + (n - 1) * "* ")
#     else:
#         print((rows + 1) * " " + (n - rows - 1) * "* ")


# n = int(input())
#
# for row in range(1, n + 1):
#     print(' ' * (n - row), end="")
#     print(*['*'] * row)
# for row in range(n - 1, 0, -1):
#     print(' ' * (n - row), end="")
#     print(*['*'] * row)


# def print_row(size_, star_count_):
#     for row in range(size_ - star_count_):
#         print(" ", end="")
#     for row in range(1, star_count_):
#         print("*", end=" ")
#     print("*")
#
#
# size = int(input())
# for star_count in range(1, size):
#     print_row(size, star_count)
# for star_count in range(size, 0, -1):
#     print_row(size, star_count)


def print_row(n, row):
    print(' ' * (n - row), end="")
    print(*['*'] * row)


def print_triangle(n):
    for row in range(1, n + 1):
        print_row(n, row)


def print_reverse_triangle(n):
    for row in range(n - 1, 0, -1):
        print_row(n, row)


def create_rhombus(n):
    print_triangle(n)
    print_reverse_triangle(n)


create_rhombus(int(input()))
