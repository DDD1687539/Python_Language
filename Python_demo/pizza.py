# Coder: Lee
# Time:  2022/11/7 21:45

def make_pizza(size, *toppings):
    print('Making a ' + str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print("- " + topping)
    print()
