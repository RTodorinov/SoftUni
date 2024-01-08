# a = [int(el) for el in input().split()]
#
# try:
#     index = int(input())
#     print(a[index])
# except ValueError:
#     print(f"Invalid index type, please enter integer")
# except IndexError:
#     print(f"Invalid index for list with length {len(a)}")
# else:
#     print("print from else")
# finally:
#     print("from finally")


test_dict = {'a': 1, 'b': 2, 'c': 3}
test_list = ['a', 'b', 'c']

letter = input()

try:
    print(test_list[8])
    print(test_dict[letter])

except KeyError:
    print('Error')
except IndexError:
    print('Index error')
else:
    print('No errors')
finally:
    print('Program finished')
