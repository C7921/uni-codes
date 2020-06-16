from pyfiglet import figlet_format
from termcolor import colored

valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

def print_art(msg, color):
	if color not in valid_colors:
		color = "magenta"
	ascii_art = figlet_format(msg)
	colored_ascii = colored(ascii_art, color=color)
	print(colored_ascii)

msg = input("What would you like to print? ")
color = input("What colour? ")
print_art(msg, color)

