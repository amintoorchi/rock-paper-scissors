import random
import questionary
from rich.console import Console
from rich.panel import Panel

console = Console()

def main():
    while True:
        choice = questionary.select("Welcome to the best game in the world :))",choices=["Play Game", "Exit Game"],).ask()

        if choice == "Exit Game":
            print("Bye :)))")
            break
        if choice == "Play Game":
            game_logic()
            

def game_logic():
    items = ["Rock", "Paper", "Scissors"]
    sys_selection = random.choice(items)

    user_selection = questionary.select("choose your move", choices=[*items, "Back To Main Menu"],).ask()

    if user_selection == "Back To Main Menu":
        return
    
    if user_selection == sys_selection:
        console.print("Its a draw :)", style="bold red")
    elif (
        (user_selection == "Rock" and sys_selection == "Scissors")
        or (user_selection == "Paper" and sys_selection == "Rock")
        or (user_selection == "Scissors" and sys_selection == "Paper")
    ):
        console.print("Your Winnnnnnn :))", style="bold red")
    else:
        console.print("Your Loseeeeee :((", style="bold red")
    

#TODO research about this part in python ...
if __name__ == "__main__":
    main()