class CoffeeMachine:
    # norms for coffee
    # 1 - espresso
    # 2 - latte
    # 3 - cappuccino
    coffee_norms = [0, [4, 250, 16, 0, 1],
                    [7, 350, 20, 75, 1],
                    [6, 200, 12, 100, 1]]

    def __init__(self):
        self.money = 550  # $ at the moment
        self.water = 400  # ml of water at the moment
        self.milk = 540  # ml of milk at the moment
        self.beans = 120  # g of coffee beans at the moment
        self.cups = 9  # disposable cups at the moment
        self.action = None

    def check_remaining(self, kind):
        state_remaining = {True}
        if self.water - self.coffee_norms[kind][1] < 0:
            state_remaining.add(False)
            print('Sorry, not enough water!')
        if self.milk - self.coffee_norms[kind][3] < 0:
            state_remaining.add(False)
            print('Sorry, not enough milk!')
        if self.beans - self.coffee_norms[kind][2] < 0:
            state_remaining.add(False)
            print('Sorry, not enough coffee beans!')
        if self.cups - self.coffee_norms[kind][4] < 0:
            state_remaining.add(False)
            print('Sorry, not enough disposable cups!')
        if False in state_remaining:
            return False
        else:
            return True

    def state_of_machine(self):
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.beans, 'of coffee beans')
        print(self.cups, 'of disposable cups')
        if self.money > 0:
            print(f'${self.money} of money')
        else:
            print(f'{self.money} of money')
        print()

    def action_buy(self):
        # print(coffee_norms)
        kind_of_coffee = input(
            'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n')
        if kind_of_coffee == 'back':
            return
        elif 1 <= int(kind_of_coffee) <= 3:
            if my_coffee_machine.check_remaining(int(kind_of_coffee)):
                self.money += self.coffee_norms[int(kind_of_coffee)][0]
                self.water -= self.coffee_norms[int(kind_of_coffee)][1]
                self.beans -= self.coffee_norms[int(kind_of_coffee)][2]
                self.milk -= self.coffee_norms[int(kind_of_coffee)][3]
                self.cups -= self.coffee_norms[int(kind_of_coffee)][4]
                print('I have enough resources, making you a coffee!')
        else:
            print('Incorrect kind of coffee, try again...')
        print()
        # state_of_machine()

    def action_fill(self):
        print('Write how many ml of water do you want to add:')
        self.water += int(input())
        print('Write how many ml of milk do you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.beans += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.cups += int(input())
        print()
        # state_of_machine()

    def action_take(self):
        print(f'I gave you ${self.money}')
        self.money = 0
        print()
        # state_of_machine()

    def start_work(self):
        self.action = input('Write action (buy, fill, take, remaining, exit):\n')
        print()


# state_of_machine()
my_coffee_machine = CoffeeMachine()
my_coffee_machine.start_work()

while True:
    if my_coffee_machine.action == 'buy':
        my_coffee_machine.action_buy()
    elif my_coffee_machine.action == 'fill':
        my_coffee_machine.action_fill()
    elif my_coffee_machine.action == 'take':
        my_coffee_machine.action_take()
    elif my_coffee_machine.action == 'remaining':
        my_coffee_machine.state_of_machine()
    elif my_coffee_machine.action == 'exit':
        break
    else:
        print('Incorrect action, try again...')
    my_coffee_machine.start_work()
