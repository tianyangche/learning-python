class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print 'This is ' + self.restaurant_name + ' whose flavor is ' + self.cuisine_type + '.'

    def open_restuarant(self):
        print self.restaurant_name + ' is currently open.'

rest1 = Restaurant("Miah's Kitchen", "Chinese")
rest2 = Restaurant("Famous Chicken", "Fast food")
rest3 = Restaurant("Spice Up", "Chinese")

rest1.describe_restaurant()
rest2.describe_restaurant()
rest3.describe_restaurant()
