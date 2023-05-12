MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def insert_coins():
    inserting = True
    inserted_value = 0
    coin_values = {"quarter": .25, "dime": .10, "nickel": .05, "penny": .01}
    while inserting:
        coin = input("Please feed in a coin (Quarter, Dime, Nickel, Penny, or done if finished): ").lower()
        if coin.lower() == "done":
            inserting = False
            return inserted_value
        try:
            inserted_value += coin_values[coin]
        except:
            print("Sorry, not a valid coin input")


def check_resources(drink_type):
    if resources["water"] - MENU[drink_type]["ingredients"]["water"] >= 0:
        if resources["coffee"] - MENU[drink_type]["ingredients"]["coffee"] >= 0:
            if resources["milk"] - MENU[drink_type]["ingredients"]["milk"] >= 0:
                 return True
            else:
                print("Sorry but there is not enough milk.")
        else:
            print("Sorry but there is not enough coffee.")
    else:
        print("Sorry but there is not enough water.")
    return False


def make_transaction(drink_type, payment):
    global profit
    resources["coffee"] -= MENU[drink_type]["ingredients"]["coffee"]
    resources["water"] -= MENU[drink_type]["ingredients"]["water"]
    if drink_type != "espresso":
                    resources["milk"] -= MENU[drink_type]["ingredients"]["milk"]
    profit += MENU[drink_type]["cost"]
    change = payment - MENU[drink_type]["cost"]
    return change


on = True

while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        on = False
    elif choice in ["espresso", "latte", "cappuccino"]:
        inserted_money = insert_coins()
        if inserted_money >= MENU[choice]["cost"] and check_resources(choice):
            make_transaction(choice, inserted_money)
            print(f"Here is your {choice}. Enjoy!")
        elif inserted_money < MENU[choice]["cost"]:
            print("Sorry, that's not enough money. Money refunded.")
    elif choice == "report":
        print(f"\n Water: {resources.get('water')}\n",
              f"Milk: {resources.get('milk')}\n",
              f"Coffee: {resources.get('coffee')}\n",
              f"Money: ${profit}\n")
    else:
        print("Not a valid option!\n")