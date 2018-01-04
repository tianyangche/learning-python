# 1. test importing entire module
# import pizza
# pizza.make_pizza(16, 'green peppers', 'mushroom', 'cheese')

# 2. test importing specific functions
# from pizza import make_pizza
# make_pizza(16, 'green peppers', 'mushroom', 'cheese')

# 3. test aliasing.
from pizza import make_pizza as mk
mk(16, 'green peppers', 'mushroom', 'cheese')
