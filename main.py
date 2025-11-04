from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import art

maker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

should_stop = False
while not should_stop:
    print(art.logo)
    # 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        # a. Check the user’s input to decide what to do next.
        # b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer
    valid_option = False

    while not valid_option:
        option = input(f"What would you like? {menu.get_items()}: ").lower()
        # 2. Turn off the Coffee Machine by entering “off” to the prompt. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.
        if option == "off":
            valid_option = True
            should_stop = True
            print("Good Bye!")
        elif option == "report":
            valid_option = True
            maker.report()
            money.report()
        elif menu.find_drink(option):
            valid_option = True
            if maker.is_resource_sufficient(menu.find_drink(option)):
                if money.make_payment(menu.find_drink(option).cost):
                    maker.make_coffee(menu.find_drink(option))
        else:
            print("You typed an invalid option. Please choose again.")
