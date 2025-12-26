import data
import sys

machine_money = 0

print("-----MENU-----")
print("1. Espresso - ₱20.50")
print("2. Latte - ₱40.50")
print("3. Cappuccino - ₱50")
print("\nPlease type in your order.")

def print_report():
    """Prints the remaining resources and the earnings."""
    for resource in data.resources:
        print(f"{resource}: {data.resources[resource]}")
    print(f"Earnings: ₱{machine_money}\n")

# can be improved by having it specify the ingredients that aren't enough
def check_resources(order):
    """Checks if the machine resources are enough to make the order"""
    for resource in data.MENU[order]["ingredients"]:
        if data.resources[resource] < data.MENU[order]["ingredients"][resource]:
            return False
    return True

# needs to fix where the order should only be the ones on the menu to avoid breaking it.
while True:
    order = input("What is your order: ").lower()

    if order == "off":
        sys.exit()

    if order == "report":
        print_report()
        continue

    user_money = float(input("Please insert your money: "))
    coffee_cost = data.MENU[order]["cost"]
    is_resource_enough = check_resources(order)

    if user_money > coffee_cost and is_resource_enough == True:
        print(f"\nHere is your ☕ {order}.\nHere is your change: ₱{user_money - coffee_cost}\n")
        machine_money += coffee_cost
        
        # for deducting machine resources based on coffee ingredient
        for resource in data.MENU[order]["ingredients"]:
            data.resources[resource] -= data.MENU[order]["ingredients"][resource]
    elif is_resource_enough == False:
        print("\nSorry, the machine doesn't have enough ingredients to make your coffee.\nMoney refunded.")
    elif user_money < coffee_cost:
        print(f"\nYour money is not enough.\nMoney refunded.")



