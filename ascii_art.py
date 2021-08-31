import pyfiglet
from termcolor import colored

colors = ('red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white')
msg = input("what would you to print?")

color = input("what color?")

if color not in colors:
  color = 'red'


  

ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color=color)
print(colored_ascii)