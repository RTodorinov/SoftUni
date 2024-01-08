try:
    text_file = open('text.txt', 'r')
    print('File found')
    text_file.close()
except FileNotFoundError:
    print('File not found')


