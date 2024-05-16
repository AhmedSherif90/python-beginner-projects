from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def game(chance):
	"""Function that plays the game and check the user input against the chance"""
	num = random.randint(1, 100)
	print(f"You have {chance} chances left.")
	done = True
	while done:
		guess = int(input("input ur guess \n"))
		chance -= 1
		if chance == 0:
			print(f"You Lose ! {chance} chances left number was {num} .")
			done = False
		else:
			if guess == num:
				print(f"You got it right! with  {chance} chances left .")
				if chance >= 5:
					print("OMG!!!!!!", chance, "chances left")
				else:
					print("Not Bad", chance, "chances left")
				done = False
			elif guess > num:
				print(f"Too high! You have {chance} chances left.")
			elif guess < num:
				print(f"Too low! You have {chance} chances left.")


def set_difficulty():
	"""Function that sets the difficulty of the game"""
	level = input("Choose a difficulty. Type 'easy' or 'hard': ")
	if level == "easy":
		return EASY_LEVEL_TURNS
	else:
		return HARD_LEVEL_TURNS


def start():
	"""Function that starts the game"""
	print(logo)
	print("Welcome to the guessing game")
	chance = set_difficulty()
	game(chance)
	print("Want to play again? (Type 'yes' or 'no')")
	choice = input()
	if choice == "yes":
		start()


start()
