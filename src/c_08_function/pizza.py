def make_pizza(*topping):

    for topping in topping:
        print(f' - {topping}')


# make_pizza('mushroom')
# make_pizza(('bacon', 'mushroom', 'tomato'))


def make_pizza_size(size, *topping):
    print(f'Pizza size: {size}')
    for topping in topping:
        print(f' - {topping}')

# make_pizza_size(12, 'mushroom')
# make_pizza_size(20, 'mushroom', 'bacon', 'tomato')