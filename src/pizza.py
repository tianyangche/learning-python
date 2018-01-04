def make_pizza(size, *topping):
    print 'A pizza whose size is ' + str(size) + ' will be made.'
    for t in topping:
        print 'Topping ' + t + ' will be added.'
