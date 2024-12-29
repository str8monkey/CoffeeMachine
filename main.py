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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def report():
    """Prints a report of the current resources."""
    # Prints the current resources.
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}ml")
    print(f"Money: ${resources["money"]}")

def can_make_coffee(order):
    """Checks resources to see if coffee can be made.  Returns True if it can, False if not.
        Also subtracts resources if coffee can be made."""
    # Checks if there are enough resources to make the coffee.
    # Check if there are enough resources
    for item in MENU[order]["ingredients"]:
        if resources[item] < MENU[order]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False

    # If there are enough resources, subtract them
    for item in MENU[order]["ingredients"]:
        resources[item] -= MENU[order]["ingredients"][item]

    return True

def payment(order):
    """Returns True if payment is successful, False if not.  Also updates resources to add money."""
    print(f"The cost of {order} is ${MENU[order]["cost"]}.")
    print("Please insert payment.")
    # Takes user input for payment.
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    # If payment is successful, will return True and update resources.
    if total >= MENU[order]["cost"]:
        # Calculates change.
        # how do I limit change to 2 decimal places?
        change = total - MENU[order]["cost"]
        print(f"Here is ${change:.2f} in change.")
        # Adds money to resources.
        if order == "espresso":
            resources["money"] += MENU["espresso"]["cost"]
        elif order == "latte":
            resources["money"] += MENU["latte"]["cost"]
        elif order == "cappuccino":
            resources["money"] += MENU["cappuccino"]["cost"]
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")

def coffee_machine():
    """Main function to run the coffee machine."""
    # Takes user input for order.  Will continue to take orders until user types "off".
    # Will also print a report if user types "report".
    machine_on = True

    while machine_on:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if order == "off":
            machine_on = False
        elif order == "report":
            report()
        # Checks if the order is in the MENU.  If not, will ask for another order.
        elif order == "espresso" or order == "latte" or order == "cappuccino":
            # Will check if the coffee can be made.
            if can_make_coffee(order):
                # Will check if payment is successful.
                if payment(order):
                    print(f"Here is your {order} ☕️. Enjoy!")


coffee_machine()


