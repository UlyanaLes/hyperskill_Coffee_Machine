money = 550  # $ at the moment
water = 400  # ml of water at the moment
milk = 540  # ml of milk at the moment
beans = 120  # g of coffee beans at the moment
cups = 9  # disposable cups at the moment

# espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4
ESP1_MONEY = 4
ESP1_WATER = 250
ESP1_BEANS = 16

# latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7
LAT2_MONEY = 7
LAT2_WATER = 350
LAT2_MILK = 75
LAT2_BEANS = 20

# cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6
CAP3_MONEY = 6
CAP3_WATER = 200
CAP3_MILK = 100
CAP3_BEANS = 12

coffee_norms = [0, [ESP1_MONEY, ESP1_WATER, ESP1_BEANS, 0, 1],
                [LAT2_MONEY, LAT2_WATER, LAT2_BEANS, LAT2_MILK, 1],
                [CAP3_MONEY, CAP3_WATER, CAP3_BEANS, CAP3_MILK, 1]]


def check_remaining(kind):
    state_remaining = {True}
    if water - coffee_norms[kind][1] < 0:
        state_remaining.add(False)
        print('Sorry, not enough water!')
    if milk - coffee_norms[kind][3] < 0:
        state_remaining.add(False)
        print('Sorry, not enough milk!')
    if beans - coffee_norms[kind][2] < 0:
        state_remaining.add(False)
        print('Sorry, not enough coffee beans!')
    if cups - coffee_norms[kind][4] < 0:
        state_remaining.add(False)
        print('Sorry, not enough disposable cups!')
    if False in state_remaining:
        return False
    else:
        return True


def state_of_machine():
    print('The coffee machine has:')
    print(water, 'of water')
    print(milk, 'of milk')
    print(beans, 'of coffee beans')
    print(cups, 'of disposable cups')
    if money > 0:
        print(f'${money} of money')
    else:
        print(f'{money} of money')


def action_buy():
    # print(coffee_norms)
    global money, water, beans, milk, cups, coffee_norms
    kind_of_coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ')
    if kind_of_coffee == 'back':
        return
    elif 1 <= int(kind_of_coffee) <= 3:
        if check_remaining(int(kind_of_coffee)):
            money += coffee_norms[int(kind_of_coffee)][0]
            water -= coffee_norms[int(kind_of_coffee)][1]
            beans -= coffee_norms[int(kind_of_coffee)][2]
            milk -= coffee_norms[int(kind_of_coffee)][3]
            cups -= coffee_norms[int(kind_of_coffee)][4]
            print('I have enough resources, making you a coffee!')
    else:
        print('Incorrect kind of coffee, try again...')
    # print()
    # state_of_machine()


def action_fill():
    global water, beans, milk, cups
    print('Write how many ml of water do you want to add:')
    water += int(input('>'))
    print('Write how many ml of milk do you want to add:')
    milk += int(input('>'))
    print('Write how many grams of coffee beans do you want to add:')
    beans += int(input('>'))
    print('Write how many disposable cups of coffee do you want to add:')
    cups += int(input('>'))
    # print()
    # state_of_machine()


def action_take():
    global money
    print(f'I gave you ${money}')
    money = 0
    # print()
    # state_of_machine()


# state_of_machine()
action = input('Write action (buy, fill, take, remaining, exit):\n> ')
print()
while True:
    if action == 'buy':
        action_buy()
        print()
    elif action == 'fill':
        action_fill()
        print()
    elif action == 'take':
        action_take()
        print()
    elif action == 'remaining':
        state_of_machine()
        print()
    elif action == 'exit':
        break
    else:
        print('Incorrect action, try again...')
    action = input('Write action (buy, fill, take, remaining, exit):\n> ')
    print()
