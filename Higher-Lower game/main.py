from art import logo, vs
import random
from Game_Data import data


def get_random_accounts():
	"""Function to get random Instagram accounts."""
	return random.sample(data, 2)


def format_account(account):
	"""Format account into printable format: name, description, and country."""
	name = account["name"]
	description = account["description"]
	country = account["country"]
	followers = account["follower_count"]
	return f"{name}, a {description}, from {country}, {followers} followers."


def check_guess(account_a, account_b, guess):
	"""Check if the user's guess is correct."""
	followers_a = account_a["follower_count"]
	followers_b = account_b["follower_count"]
	return followers_a > followers_b if guess == "a" else followers_b > followers_a


def display_accounts(accounts):
	"""Display the two Instagram accounts."""
	account_a, account_b = accounts
	print(f"Compare A: {format_account(account_a)}")
	print(vs)
	print(f"Against B: {format_account(account_b)}")


def game():
	"""Function to start the higher-lower game."""
	print(logo)
	print("Welcome to the Higher-Lower game!")

	score = 0
	accounts = get_random_accounts()

	while True:
		display_accounts(accounts)
		guess = input("Who has more followers? Type 'A' or 'B': ").lower()
		if guess not in ["a", "b"]:
			print("Invalid input. Please enter 'A' or 'B'.")
			continue

		if check_guess(accounts[0],accounts[1], guess):
			score += 1
			accounts[0] = accounts[1]
			print(f"Correct! Your current score is: {score}")
		else:
			print(f"Wrong answer! Game over. Your final score is: {score}")
			break

		accounts[1] = get_random_accounts()[1]


game()
