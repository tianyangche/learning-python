class Dog(object):
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command."""
        print self.name.title() + " is now sitting."

    def roll_over(self):
        """simulate rolling over in response to a command."""
        print self.name.title() + " rolled over!"


my_dog = Dog('Baby', 6)
print 'My dog\'s name is ' + my_dog.name.title() + '.'
print 'My dog is ' + str(my_dog.age) + ' years old.'
