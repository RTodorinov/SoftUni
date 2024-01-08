''' Python File Object
Built-In Functions to Create and Manipulate Files '''

''' io module is the default module for accessing files - Don't need to import it
open() returns a file object whose type depends on:
The mode
File operations such as reading and writing
Files in a text mode ('w', 'r', 'wt', 'rt', etc.) returns a TextIOWrapper '''

''' Opening a File '''
#  open() Function
''' open() function in Python opens a file and returns a file object '''
# file = open('text.txt', 'r')
# file.close()

'''The arguments are file name and the mode (reading and etc.)
All arguments except file are optional and have default values
If the file is not in the current directory, the full path to the file can be provided '''
# file = open('D:\\text.txt', 'r')

'''If the file does not exist, FileNotFoundError is thrown '''
# file = open('invalid.txt', 'r')  # FileNotFoundError

'''It can be caught a try-finally block'''
# try:
#     file = open('invalid.txt', 'r')  # FileNotFoundError
# except FileNotFoundError:
#     print("File not found or path is incorrect")
# finally:
#     print("exit")

''' File Modes 
The mode argument is optional and specifies the mode for manipulating the file
Its default value is 'r' - open for reading in text mode

File modes in Python
w - open for writing, truncating the file first
x - create a new file and open it for writing
a - open for writing, appending to the end of the file if it exists
t - text mode (default)
b -  binary mode
+ - open a disk file for updating (reading and writing) '''

# primer
email = input()


file = open("users.txt", "a")
file.write(email + "\n")

file.close()
print(email)


