"""
Create a Rock Paper Scissors game where the player inputs their choice
and plays  against a computer that randomly selects its move, 
with the game showing who won each round.
Add a score counter that tracks player and computer wins, 
and allow the game to continue until the player types “quit”.
"""
import random
import sys
import time
import os
from colorama import Fore, Style, init
init(autoreset=True)
from pyfiglet import Figlet
from termcolor import colored
# from playsound import playsound
from tqdm import tqdm
from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.prompt import Prompt
from rich.progress import track
from rich.theme import Theme
from rich.layout import Layout
from rich.live import Live
from rich.markdown import Markdown
from rich.rule import Rule
from rich.syntax import Syntax
from rich.traceback import install
install()
console = Console()
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red"
})
console = Console(theme=custom_theme)
figlet = Figlet(font='slant')
os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.CYAN + figlet.renderText('Rock Paper Scissors'))
print(Fore.YELLOW + Style.BRIGHT + "Welcome to Rock Paper Scissors!")
print(Fore.GREEN + "Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")
time.sleep(1)
player_score = 0
computer_score = 0
choices = ['rock', 'paper', 'scissors']
while True:
    player_choice = console.input("[bold green]Your choice (rock/paper/scissors/quit): [/]").lower()
    if player_choice == 'quit':
        print(Fore.MAGENTA + Style.BRIGHT + "Thanks for playing! Final Scores:")
        print(Fore.CYAN + f"Player: {player_score} | Computer: {computer_score}")
        break
    if player_choice not in choices:
        print(Fore.RED + "Invalid choice. Please try again.")
        continue
    computer_choice = random.choice(choices)
    print(Fore.YELLOW + f"Computer chose: {computer_choice}")
    if player_choice == computer_choice:
        print(Fore.BLUE + "It's a tie!")
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print(Fore.GREEN + "You win this round!")
        player_score += 1
    else:
        print(Fore.RED + "Computer wins this round!")
        computer_score += 1
    print(Fore.CYAN + f"Scores => Player: {player_score} | Computer: {computer_score}")
    time.sleep(1)
    print(Fore.YELLOW + "-"*40)
    time.sleep(1)
# End of the game loop  
print(Fore.MAGENTA + Style.BRIGHT + "Thanks for playing! Final Scores:")
print(Fore.CYAN + f"Player: {player_score} | Computer: {computer_score}")
# playsound('game_over.mp3')