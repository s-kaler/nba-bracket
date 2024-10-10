# lib/cli.py

from helpers import (
    exit_program,
    greeting,
    teams_menu,
    players_menu
)

def main():
    greeting()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            teams_menu()
        elif choice == "2":
            players_menu()


def menu():
    print("0. Exit")
    print("1. Team Management")
    print("2. Player Management")

if __name__ == "__main__":
    main()

