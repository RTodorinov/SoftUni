# list_of_integers = [int(x) for x in input().split()]
# command = input().split()
#
# while command[0] != "end":
#
#     even = [i for i in list_of_integers if i % 2 == 0]
#     odd = [i for i in list_of_integers if i % 2 != 0]
#
#     if command[0] == "exchange":
#         if 0 <= int(command[1]) < len(list_of_integers):
#             list_of_integers = list_of_integers[int(command[1]) + 1:] + list_of_integers[:int(command[1]) + 1]
#         else:
#             print(f'Invalid index')
#
#     elif command[0] == "max":
#         if command[1] == "even" and even:
#             print((len(list_of_integers) - list_of_integers[::-1].index(max(even)) - 1))
#         elif command[1] == "odd" and odd:
#             print((len(list_of_integers) - list_of_integers[::-1].index(max(odd)) - 1))
#         else:
#             print('No matches')
#
#     elif command[0] == "min":
#         if command[1] == "even" and even:
#             print((len(list_of_integers) - list_of_integers[::-1].index(min(even)) - 1))
#         elif command[1] == "odd" and odd:
#             print((len(list_of_integers) - list_of_integers[::-1].index(min(odd)) - 1))
#         else:
#             print('No matches')
#
#     elif command[0] == "first":
#         if 0 < int(command[1]) <= len(list_of_integers):
#             if command[2] == "even":
#                 print(even[0:int(command[1])])
#             else:
#                 print(odd[0:int(command[1])])
#         else:
#             print(f"Invalid count")
#
#     elif command[0] == "last":
#         if 0 < int(command[1]) <= len(list_of_integers):
#             if command[2] == "even":
#                 print(even[-int(command[1]):])
#             else:
#                 print(odd[-int(command[1]):])
#         else:
#             print(f"Invalid count")
#
#     command = input().split()
#
# print(list_of_integers)

def exchange_list(lst, index):
    ''' Here, we define a function called exchange_list that takes a list (lst) and an index (index)
    as arguments. If the index is within valid bounds (0 to len(lst)-1), the function returns a new
    list that swaps the portions before and after the specified index.
    Otherwise, it prints an error message and returns the original list unchanged. '''
    if 0 <= index < len(lst):
        return lst[index + 1:] + lst[:index + 1]
    else:
        print("Invalid index")
        return lst


def process_commands(list_of_integers, command):
    ''' The process_commands function takes the list of integers (list_of_integers) and a command (command)
    as arguments. It initializes two lists, even and odd, which contain even and odd elements respectively
    from the list_of_integers. '''
    even = [i for i in list_of_integers if i % 2 == 0]
    odd = [i for i in list_of_integers if i % 2 != 0]
    ''' If the first command word is "exchange", the function calls the exchange_list function with the given
    list_of_integers and the index specified in command[1]. It returns the modified list.'''
    if command[0] == "exchange":
        return exchange_list(list_of_integers, int(command[1]))

    elif command[0] == "max":
        ''' If the command is "max", it checks whether the maximum element should be even or odd (command[1]).
            If such elements exist (even or odd lists are not empty), it finds the index of the rightmost maximum
            element and prints it. If there are no matches, it prints "No matches".'''
        if command[1] == "even" and even:
            print(len(list_of_integers) - list_of_integers[::-1].index(max(even)) - 1)
        elif command[1] == "odd" and odd:
            print(len(list_of_integers) - list_of_integers[::-1].index(max(odd)) - 1)
        else:
            print('No matches')

    elif command[0] == "min":
        ''' Similarly, for the "min" command, it checks whether the minimum element should be even or odd. 
        It finds the index of the rightmost minimum element and prints it. If there are no matches, 
        it prints "No matches".'''
        if command[1] == "even" and even:
            print(len(list_of_integers) - list_of_integers[::-1].index(min(even)) - 1)
        elif command[1] == "odd" and odd:
            print(len(list_of_integers) - list_of_integers[::-1].index(min(odd)) - 1)
        else:
            print('No matches')

    elif command[0] == "first":
        ''' For the "first" command, it checks the count of elements to print (count). If it's within valid bounds,
        it prints the first count even or odd elements as requested. If the count is invalid, 
        it prints "Invalid count".'''
        count = int(command[1])
        if 0 < count <= len(list_of_integers):
            if command[2] == "even":
                print(even[:count])
            else:
                print(odd[:count])
        else:
            print("Invalid count")

    elif command[0] == "last":
        ''' For the "last" command, it's similar to "first" but prints the last count elements instead.'''
        count = int(command[1])
        if 0 < count <= len(list_of_integers):
            if command[2] == "even":
                print(even[-count:])
            else:
                print(odd[-count:])
        else:
            print("Invalid count")
    ''' Finally, the function returns the updated list_of_integers after processing the command.'''
    return list_of_integers


''' Here, the main part of the program initializes list_of_integers with the provided input and enters a loop 
that continues until the command is "end". Within the loop, the process_commands function is called with the current
list_of_integers and command. The function updates the list as needed. After processing, the loop takes a new input 
command and continues. Finally, when the loop exits, the list_of_integers is printed, 
showing the result of the operations.'''
list_of_integers = [int(x) for x in input().split()]
command = input().split()

while command[0] != "end":
    list_of_integers = process_commands(list_of_integers, command)
    command = input().split()

print(list_of_integers)
