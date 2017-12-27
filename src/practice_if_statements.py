cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw' or car == 'subaru':
        print car.upper()
    else:
        print car.title()

print "=========="

if 'audi' in cars:
    print 'Exist.'
else:
    print 'Not exist.'

if 'honda' not in cars:
    print 'Not exist.'

# if - elif - else

age = 10

if age < 4:
    print 'Less than 4.'
elif age < 11:
    print 'Less than 11.'
else:
    print 'Larger than or equal to 11.'

# check if list is empty
print "=========="
names = []
if names:
    print 'List \'names\' is not empty.'
else:
    print 'List \'names\' is empty.'
