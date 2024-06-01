#!/usr/bin/python

# Generate 3 Passwords, then prompts again.
# Developed for Coding Club - OHC.

import random
import string

# Could automate from online dictionary?
adjectives = ['sleepy', 'slow', 'smelly', 'wet', 'green', 'orange', 'yellow', 'purple']

nouns = ['apple', 'dinosaur', 'ball', 'goat', 'dragon', 'duck', 'panda', 'hammer']

print("Welcome to Password Picker")

# Creates infinite loop
while True:
	# Sets range for only 3 passwords
	for num in range(3):
		# Randomly gets item from adjectives
		adjectives = random.choice(adjectives)
		# Randomly gets item from nouns
		noun = random.choice(nouns)
		# Randomly get number between 0 and 100
		number = random.randrange(0, 100)
		# Get random special character 
		special_char = random.choice(string.punctuation)

		password = adjectives + noun + str(number) + special_char
		print("Your new password is: %s " % password)
		
	response = input("Wouold you like another set of passwords? (Y/N): ")
	if response == "n":
		break