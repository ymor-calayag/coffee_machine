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

# print("-----MENU-----")
# print("1. Espresso - ₱20.50")
# print("2. Latte - ₱40.50")
# print("3. Cappuccino - ₱50")
# print("\nPlease type in your order.")

order = input("What is your order: ").lower()
# user_money = float(input("Please insert your money: "))

# # print(data.MENU[order])
# print(data.resources)
# print(data.MENU[order]["ingredients"]["water"])
# coffee_cost = data.MENU[order]["cost"]

# if user_money > coffee_cost:
#     print(f"\nHere is your ☕ {order}.\nHere is your change: ₱{user_money - coffee_cost}")
#     machine_money += coffee_cost
#     data.resources["water"] -= data.MENU[order]["ingredients"]["water"]
# elif user_money < coffee_cost:
#     print(f"\nYour money is not enough.\nMoney refunded.")

# print(data.resources)
    # "espresso": {
    #     "ingredients": {
    #         "water": 50,
    #         "coffee": 18,
    #     },
    #     "cost": 20.50,
    # },

# for machine_resource in data.resources:
#     machine_resource -= 50
#     print(machine_resource)
print(data.MENU[order])
print(data.resources)

# for deducting machine resources based on coffee ingredient
for i in data.MENU[order]["ingredients"]:
    data.resources[i] -= data.MENU[order]["ingredients"][i]

print(data.MENU[order])
print(data.resources)