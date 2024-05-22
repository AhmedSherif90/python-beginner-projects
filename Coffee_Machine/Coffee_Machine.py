logo: str = '''

________._________
|      | \   -   /
|  ||  |  \  -  /
|  ||  |___\___/
|  ||  |     X
|      |    ___
|      |  [] - []
|______| []  -  []
| ____ |[]_______[]
||7:30||__________
||____|           |
|_________________|
'''

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
	"water": 500,
	"milk": 500,
	"coffee": 100,
}


def paid():
	"""Returns the total calculated from coins inserted."""
	print("Please insert coins.")
	total = int(input("how many quarters?: ")) * 0.25
	total += int(input("how many dimes?: ")) * 0.1
	total += int(input("how many nickles?: ")) * 0.05
	total += int(input("how many pennies?: ")) * 0.01
	return total


def check_resources(choice):
	items = MENU[choice]["ingredients"]
	for item in items:
		if resources[item] < items[item]:
			print(f"Sorry there is not enough {item}.")
			return False
		else:
			resources[item] -= items[item]
	return True


def report():
	print(f"Water: {resources['water']}ml")
	print(f"Milk: {resources['milk']}ml")
	print(f"Coffee: {resources['coffee']}g")
	print(f"Money: ${profit}")


is_on = True

while is_on:
	print(logo)
	choice = input("What would you like? (espresso/latte/cappuccino): ")
	if choice in MENU or choice == "off" or choice == "report":
		if choice == "off":
			is_on = False
		elif choice == "report":
			report()
		elif check_resources(choice):
			total = paid()
			if total >= MENU[choice]["cost"]:
				print(f"take your exchange{round(total - MENU[choice]["cost"], 2)}")
				profit += MENU[choice]["cost"]
				print(f"Here is your {choice} ☕️. Enjoy!")
			elif total < MENU[choice]["cost"]:
				print(f"Sorry there is not enough Money you paid {total} and cost is {MENU[choice]['cost']} .")

	else:
		print("invalid input.")
