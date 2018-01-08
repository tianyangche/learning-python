# read the entire content
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print contents

# read line by line
with open('pi_digits.txt') as file_object:
    for line in file_object:
        print line

# store content in a list
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

print len(lines)

# read large file
with open('pi_million_digits.txt') as file_object:
    digits = file_object.read()
print len(digits)
