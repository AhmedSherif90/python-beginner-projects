import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
choice = (int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n0/1/2:")))
computers_choice = random.randint(0, 2)

if choice < 0 or choice > 2:
	print("You've entered an invalid value, try again and choose a number between 0-2.")
else:
	print(game_images[choice])
	print("Computer chose:")
	print(game_images[computers_choice])
	if choice == computers_choice:
		print("It's a draw!")
	elif choice == 0 and computers_choice == 1 or (choice == 1 and computers_choice == 2):
		print("Computer wins!")
	else:
		print("You wins!")
