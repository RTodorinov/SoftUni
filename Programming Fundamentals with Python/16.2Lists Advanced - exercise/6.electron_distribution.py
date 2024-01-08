
# number_of_electrons = int(input())
# shells = []
#
# while number_of_electrons > 0:
#     filling = len(shells) + 1
#     shell_filling = 2 * (filling**2)  # min(2 * (filling**2), number_of_electrons)
#     if shell_filling > number_of_electrons:
#         shells.append(number_of_electrons)
#         break
#     else:
#         shells.append(shell_filling)
#     number_of_electrons -= shell_filling
#
# print(shells)

number_of_electrons = int(input())
shells = []

while number_of_electrons > 0:
    filling = len(shells) + 1
    shell_filling = min(2 * (filling ** 2), number_of_electrons)
    shells.append(shell_filling)
    number_of_electrons -= shell_filling

print(shells)
