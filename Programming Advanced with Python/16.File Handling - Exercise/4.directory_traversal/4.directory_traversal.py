import os

files = {}  # {'py': ['file1.py', 'file2.py'...], 'txt': ['text1.txt', 'text2.txt'...]}
directory = '../'


for element in os.listdir(directory):
    f = os.path.join(directory, element)
    if os.path.isfile(f):
        ext = element.split('.')[-1]
        if ext not in files:
            files[ext] = []
        files[ext].append(element)
    else:
        for el in os.listdir(f):
            filename = os.path.join(f, el)
            if os.path.isfile(filename):
                ext = el.split('.')[-1]
                if ext not in files:
                    files[ext] = []
                files[ext].append(el)

with open(os.path.join(directory, 'report.txt'), 'w') as output_file:
    for ext, f_names in sorted(files.items()):
        output_file.write(f'.{ext}\n')
        for f_name in sorted(f_names):
            output_file.write(f'- - - {f_name}\n')

# variant 2 with recursion
# import os
#
# files = {}
# directory = input()
#
#
# def get_files(folder, level):
#     if level < 0:
#         return
#     for element in os.listdir(folder):
#         f = os.path.join(folder, element)
#         if os.path.isfile(f):
#             extension = element.split('.')[-1]
#             if extension not in files:
#                 files[extension] = []
#             files[extension].append(element)
#         else:
#             get_files(f, level - 1)
#
#
# get_files(directory, 1)
#
# with open(os.path.join(directory, 'report.txt'), 'w') as output_file:
#     for ext, f_names in sorted(files.items()):
#         output_file.write(f'.{ext}\n')
#         for f_name in sorted(f_names):
#             output_file.write(f'- - - {f_name}\n')
