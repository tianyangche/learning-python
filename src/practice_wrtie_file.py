file_name = 'programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write('I love programming!\n')

# append to an existing file
with open(file_name, 'a') as file_object:
    file_object.write('This is another line.\n')
