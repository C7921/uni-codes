#!/usr/bin/python

# Generate 3 Passwords, then prompts again.
# Developed for Coding Club - OHC.

import random
import string

# Could automate from online dictionary?
adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'green', 'orange', 'yellow', 'purple']

nouns = ['apple', 'dinosaur', 'ball', 'goat', 'dragon', 'duck', 'panda', 'hammer']

print("Welcome to Password Picker")

while True:
	for num in range(3):
		adjectives = random.choice(adjectives)
		noun = random.choice(nouns)
		number = random.randrange(0, 100)
		special_char = random.choice(string.punctuation)

		password = adjectives + noun + str(number) + special_char
		print("Your new password is: %s " % password)

	response = input("Wouold you like another set of passwords? (Y/N): ")
	if response == "n":
		break