# number_of_elements = int(input())
#
# unique_elements = set()
#
# for _ in range(number_of_elements):
#     elements = input().split()
#     for el in elements:
#         unique_elements.add(el)
#
# print('\n'.join(unique_elements))

number_of_elements = int(input())

unique_elements = set()

for _ in range(number_of_elements):
    [unique_elements.add(el) for el in input().split()]

print(*unique_elements, sep='\n')
