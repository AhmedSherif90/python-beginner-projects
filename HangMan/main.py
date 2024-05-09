import random
import re
from ad import logo , stages

def check():
	index = []
	for i in range(len(Current_Word)):
		if Current_Word[i] == guess:
			index.append(i)
	return index




print(logo)

words = ["Ahmed", "Sherif", "Abdelfatah"]

Current_Word = random.choice(words).lower()
label_name = re.sub('[^0-9]', '_', Current_Word)
label_name2 = list(label_name)
print(label_name)
tries = 6
end = False
while not end:
	guess = input("Guess a letter:").lower()

	if len(check()) != 0:
		for i in check():
			label_name2[i] = guess
		print("".join(label_name2))
		if "_" not in label_name2:
			print("You Win!!")
			end = True

	else:
		tries -= 1
		print(f"you have{tries} tries left")
		print(stages[tries])
		if tries == 0:
			print("You Lose!!")
			end = True




