from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create our objects
menu = Menu()
my_maker = CoffeeMaker()
my_money = MoneyMachine()

# The program
on = True

while on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == "off":
        on = False
    elif menu.find_drink(choice).name == choice:
        drink = menu.find_drink(choice)

        if  my_maker.is_resource_sufficient(drink) and my_money.make_payment(drink.cost):
            my_maker.make_coffee(drink)
    elif choice == "report":
        my_maker.report()
        my_money.report()
    else:
        print("Not a valid option!\n")