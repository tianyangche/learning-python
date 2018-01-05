class Car(object):
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def get_mileage(self):
        print 'Current mileage is ' + str(self.mileage)

    def update_mileage(self, mileage):
        if (mileage > 0):
            self.mileage += mileage

if __name__ == '__main__':
    my_car = Car("honda", "prius", "2015")
    print my_car.get_descriptive_name()
    my_car.get_mileage()
    my_car.update_mileage(100)
    my_car.get_mileage()
