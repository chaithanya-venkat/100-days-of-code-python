from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myMenu = Menu()
myCoffeeMaker = CoffeeMaker()
myMoneyMachine = MoneyMachine()


is_on = True
while is_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        myCoffeeMaker.report()
        myMoneyMachine.report()
    else:
        drink = myMenu.find_drink(user_choice)
        if myCoffeeMaker.is_resource_sufficient(drink) and myMoneyMachine.make_payment(drink.cost):
            myCoffeeMaker.make_coffee(drink)