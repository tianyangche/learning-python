person = {'first_name': 'Tianyang', 'last_name': 'Che', 'age': 5}
print person['first_name']

# add a new key-value pair
person['title'] = 'Software Development Engineer'
print person

# remove a key-value pair
del person['title']
print person

# better format dict
employee = {
    'org': 'Alexa',
    'level': 5
}

for key, value in person.items():
    print 'key = ' + key + ', value = ' + str(value)


print '=========='
print 'Printing key only...'
for key in person.keys():
    print 'key = ' + key
