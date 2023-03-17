#Introduction to *args and **kwargs

def pizza_machine(size,*toppings):
    print("Pizza oven is switching on.")
    print('Your', size.upper(), 'size pizza is getting ready!')
    print('These are the toppings you selected:')
    
    for topping in toppings:
        print(topping.upper())
        current = topping.upper()
        delivery.append(current)

delivery = []
pizza_machine('small', 'cheese')
pizza_machine('medium', 'pepperoni','jalapeno', 'roquefort','cherry tomatoes','swiss cheese', 'mozzarella')
print(delivery)

def cake_oven(size,*flavours):
    print('Welcome to the Bakery')
    print('Your size',size.upper(),'cake is being baked')
    print('These are the flavours you chose:')
    for flavour in flavours:
        current = flavour.upper()
        baking.append(current)
    print(baking)

baking = []
cake_oven('small', 'cheesecake')
cake_oven('medium', 'raspberries', 'carrot cake')
