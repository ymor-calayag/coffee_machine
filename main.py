import data

# TODO 1: print coffee options (espresso, latte, cappuccino)
# each coffee has its own ingredients and cost
# ingredients - machine resources
# machine money += cost of coffee
# if the machine has insufficient resources, it will tell the user (Sorry, not enough {resource})
# user will input money, deduct money by coffee cost
    # if the users money is insufficient, refund money
    # if money is more than enough give back change (print)
    # if just enough, no change

# TODO 2: print report
# if the user instead inputs "report" it will list the current resources of the machine
# remaining water, milk, coffee, and the money accumulated.

machine_money = 0

print("-----MENU-----")
print("1. Espresso - ₱20.50")
print("2. Latte - ₱40.50")
print("3. Cappuccino - ₱50")
print("\nPlease type in your order.")

def print_report():
    for resource in data.resources:
        print(f"{resource}: {data.resources[resource]}")
    print(f"Earnings: ₱{machine_money}")

def check_resources(order):
    for resource in data.MENU[order]["ingredients"]:
        if data.resources[resource] < data.MENU[order]["ingredients"][resource]:
            return False
    return True

order = input("What is your order: ").lower()

# if order == "report":
#     print_report()

user_money = float(input("Please insert your money: "))
coffee_cost = data.MENU[order]["cost"]
is_resource_enough = check_resources(order)

if user_money > coffee_cost and is_resource_enough == True:
    print(f"\nHere is your ☕ {order}.\nHere is your change: ₱{user_money - coffee_cost}")
    machine_money += coffee_cost
    
    # for deducting machine resources based on coffee ingredient
    for resource in data.MENU[order]["ingredients"]:
        data.resources[resource] -= data.MENU[order]["ingredients"][resource]
elif is_resource_enough == False:
    print("Sorry, the machine doesn't have enough ingredients to make your coffee.")
elif user_money < coffee_cost:
    print(f"\nYour money is not enough.\nMoney refunded.")

print(data.resources)


