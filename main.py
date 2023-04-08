from storage import MENU,resources, commands, bank
from art import logo


machine_on = True

def get_item_and_price():
    for item in MENU:
        cost = MENU[item]["cost"]
        print(f"{item} - ${cost} ")


def check_resource(order):
    missing_resources = {}
    order_resource = MENU[order]["ingredients"]
    available_resource = resources
    for keys in available_resource:
        if available_resource[keys] > order_resource[keys]:
            resources[keys] -= order_resource[keys]
        else:
            missing_resources[keys] = available_resource[keys] - order_resource[keys]

    if missing_resources == {}:
        return True
    else:
        print("Unable to Proceed - Machine storage not available")
        for items in missing_resources:
            print(f"{items} status {missing_resources[items]}")
        print("refill storage")
        return False


def get_payment():
    """ prints cost of order and receive, validate payments """
    cost = MENU[order]["cost"]
    print(f"Pay ${cost}")
    denominations = ""
    for notes in bank:
        denominations += notes +", "

    print(f"Acceptable denominations are {denominations}")
    paid = 0
    while paid < cost:
        for notes in bank:
            received = input(f"How many {notes}RS ?: ")
            while not received.isdigit():
                print("Invalid input retry")
                received = input(f"How many {notes}RS ?: ")
            received = int(received)
            bank[notes] += received
            paid += received * int(notes)
            print(f"paid {paid}RS")
            if paid > cost:
                print(f"Collect your balance{paid - cost}RS")
                break
    print("Payment successful")
    return True





while machine_on:

    print(logo)

    get_item_and_price()

    order = input("what would you like?").lower()

    while order not in commands:
        print("Invalid input, try again")
        order = input("what would you like?").lower()

    if order == "off":
        machine_on = False

    if order == "report":
        total_cash = 0
        print("\n//Available in Storage")
        for key in resources:
            print(f"{key} - {resources[key]}ml")

        print("\n//Available Cash in Machine")
        for key in bank:
            print(f"{key} notes - {bank[key]}Nos = {bank[key]* int(key)}RS")
            total_cash += bank[key]* int(key)
        print(f"Total {total_cash}RS")

    if order in MENU:
        can_make = check_resource(order)
        if can_make:
            get_payment()
            print(f"Enjoy your {order}, Have a nice day")



