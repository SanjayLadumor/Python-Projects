ingredients = {
    "milk": 3000,
    "coffee": 2000,
    "water": 5000,
    "sugar": 1000
}


menu = {
    "Latte": {
        "price": 150,
        "ingredients": {
            "milk": 250,
            "coffee": 20,
            "water": 80,
            "sugar": 10
        }
    },

    "Espresso": {
        "price": 180,
        "ingredients": {
            "milk": 200,
            "coffee": 40,
            "water": 60,
            "sugar": 20
        }
    },

    "Cappuccino": {
        "price": 200,
        "ingredients": {
            "milk": 200,
            "coffee": 40,
            "water": 60,
            "sugar": 30
        }
    }
}


total_sales = 0
total_orders = 0


def show_menu():
    print("\n========== COFFEE MENU ==========")

    for coffee in menu:
        print(f"{coffee:<15} Rs.{menu[coffee]['price']}")

    print("\nReport")
    print("Exit")


def show_report():
    print("\n========== REPORT ==========")

    for item in ingredients:
        print(f"{item.capitalize():<10}: {ingredients[item]}")

    print(f"\nTotal Orders : {total_orders}")
    print(f"Total Sales  : Rs.{total_sales}")


def take_order():
    return input("\nEnter your order: ").title()


def check_ingredients(coffee):

    required = menu[coffee]["ingredients"]

    for item in required:
        if ingredients[item] < required[item]:
            print(f"Sorry! Not enough {item}.")
            return False

    return True


def calculate_bill(coffee):
    return menu[coffee]["price"]


def take_payment(amount):

    paid = int(input(f"Please pay Rs.{amount}: "))

    if paid >= amount:
        change = paid - amount
        print(f"Payment Successful!")
        print(f"Change Returned : Rs.{change}")
        return True

    print("Insufficient Payment.")
    return False


def deduct_ingredients(coffee):

    required = menu[coffee]["ingredients"]

    for item in required:
        ingredients[item] -= required[item]


def make_coffee(coffee):

    global total_sales
    global total_orders

    deduct_ingredients(coffee)

    total_sales += menu[coffee]["price"]
    total_orders += 1

    print(f"\n☕ Here is your {coffee}. Enjoy!\n")


def vending_machine():

    running = True

    while running:

        show_menu()

        choice = take_order()

        if choice == "Exit":
            print("\nThank you for visiting!")
            running = False

        elif choice == "Report":
            show_report()

        elif choice in menu:

            if check_ingredients(choice):

                amount = calculate_bill(choice)

                print(f"\nBill Amount : Rs.{amount}")

                payment = take_payment(amount)

                if payment:
                    make_coffee(choice)

                else:

                    retry = input(
                        "Would you like to try payment again? (Y/N): "
                    ).upper()

                    if retry == "Y":

                        payment = take_payment(amount)

                        if payment:
                            make_coffee(choice)
                        else:
                            print("Payment Failed.\n")

            else:
                print("Please choose another coffee.\n")

        else:
            print("Invalid Choice! Please select from the menu.")

vending_machine()