# Coffee Machine

This project simulates how a basic coffee vending machine works. Users can order drinks from a menu, insert money, and receive their coffee if there are enough resources available. The machine keeps track of remaining ingredients and total earnings throughout the session.

**Technologies Used**

+ ```Python```
+ ```sys``` module for program control
+ External data module for menu and resources
+ Dictionaries for structured data handling

**Features**

+ Menu-based coffee ordering system
+ Resource checking before making a drink
+ Payment processing with change calculation
+ Ingredient deduction after each successful order
+ Report feature to display remaining resources and earnings
+ Option to shut down the machine

**What Users Can Do**

+ Order espresso, latte, or cappuccino
+ View a report of remaining ingredients and earnings
+ Insert money and receive change when applicable
+ Get refunded if resources or payment are insufficient
+ Turn off the machine using a command

**The Process / How It’s Built**

+ The program displays a menu and waits for user input.
+ Users can order a drink, request a report, or turn off the machine.
+ Before processing an order, the machine checks if enough resources are available.
+ If payment is sufficient and resources are available, the drink is made and resources are deducted.
+ Earnings are tracked throughout the program’s runtime.

