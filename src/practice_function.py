def greet_user():
    """
    Display a simple greeting.
    """
    print 'hello!'


greet_user()

# multiple parameters
def greet_user(first, last='Che'):
    print last
    print first

# positional arguments
greet_user('Terry', 'Che')

# keyword arguments
greet_user(last='Che', first='Terry')

# default value
greet_user('Terry')

# Exercise 8-3

def make_shirt(size='L', message='I love python'):
    print 'Your T-shirt with the message \'' + message + '\' will be made. The size is ' + size

make_shirt()
make_shirt(size='M')

# return a value
def format_name(first, last):
    print 'function 1'
    return (first + ' ' + last).title()

# make an argument optional
def format_name(first, last, middle=''):
    print 'function 2'
    print first

print format_name('tianyang', 'test')


# pass a list to a function
def modify_list(list):
    list.append(3)

my_list = list(range(3))
modify_list(my_list)
print my_list

# prevent function from modifying a list
def not_modify_list(list):
    list.append('100')

print 'Before calling function...'
print my_list
not_modify_list(my_list[:])
print 'After calling function...'
print my_list

# arbitrary number of arguments
def make_football_club(*soccer_players):
    for player in soccer_players:
        print player.title() + ' is in Real Madrid team.'

make_football_club('cristiano ronaldo')
make_football_club('cristiano ronaldo', 'gareth bale', 'karim benzema')

def make_football_club(money, *soccer_players):
    for player in soccer_players:
        print player.title() + ' is in Real Madrid team.'
    print 'Our club has money : $' + str(money)

make_football_club(11111, 'cristiano ronaldo', 'gareth bale', 'karim benzema')

# arbitrary key word arguments
def build_profile(first_name, last_name, **arguments):
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in arguments.items():
        profile[key] = value

    print 'The user profile is:'
    print profile

build_profile('Tianyang', 'Che', age=28, salary=0)
