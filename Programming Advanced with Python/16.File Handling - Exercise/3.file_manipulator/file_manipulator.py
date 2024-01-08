import os

while True:
    line = input()
    if line == "End":
        break

    command, filename, *args = line.split('-')

    if command == 'Create':
        open(filename, 'w').close()

    elif command == 'Add':
        with open(filename, 'a') as f:
            f.write(f'{args[0]}\n')

    elif command == 'Replace':
        try:
            with open(filename, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print('An error occurred')
        else:
            with open(filename, 'w') as f:
                content.replace(args[0], args[1])
                f.write(content)

    elif command == 'Delete':
        if os.path.exists(filename):
            os.remove(filename)
        else:
            print('An error occurred')


# version 2
# import os
#
# while True:
#     line = input()
#     if line == "End":
#         break
#
#     command, filename, *args = line.split('-')
#
#     if command == 'Create':
#         open(filename, 'w').close()
#
#     elif command == 'Add':
#         with open(filename, 'a') as f:
#             f.write(f'{args[0]}\n')
#
#     elif command == 'Replace':
#         try:
#             with open(filename, 'r+') as f:
#                 content = f.read()
#                 content = content.replace(args[0], args[1])
#                 f.truncate(0)
#                 f.seek(0)
#                 f.write(content)
#         except FileNotFoundError:
#             print('An error occurred')
#
#     elif command == 'Delete':
#         if os.path.exists(filename):
#             os.remove(filename)
#         else:
#             print('An error occurred')
