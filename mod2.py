from pyfiglet import figlet_format
from termcolor import colored

def print_art(msg,color):
	valid_colors = ("red","white","blue","orange","green","cyan")

	if color not in valid_colors:
		color = "white"

	ascii_art = figlet_format(msg)
	colored_ascii = colored(ascii_art,color=color)
	print(colored_ascii)

msg = input("what would you like to print?")
color = input("what color?")
print_art(msg,color)