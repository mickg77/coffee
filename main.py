from menu import Menu, MenuItem
import math
from coffee_maker import CoffeeMaker

from money_machine import MoneyMachine

money_machine = MoneyMachine() #creates instance of the class MoneyMachine
coffee_maker = CoffeeMaker() #creates instance of the class CoffeeMaker

menu = Menu()

is_on=True
while is_on:
    options = menu.get_items()
    print(options)
    choice ="test"
    while choice not in options:
        choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
           coffee_maker.make_coffee(drink)



