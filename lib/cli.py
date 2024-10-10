# lib/cli.py

from helpers import (
    exit_program,
    greeting,
)

def main():
    greeting()
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            # Create a new team
            pass
        elif choice == "2":
            # View a team's roster
            pass
        elif choice == "3":
            # Update a team's information
            pass
        elif choice == "4":
            # Delete a team
            pass
        elif choice == "5":
            # List all teams by league
            pass
        elif choice == "6":
            # List all players in team
            pass
        elif choice == "7":
            # List all players by league
            pass
        elif choice == "8":
            # Create a new player
            pass
        elif choice == "9":
            # Update a player's information
            pass
        elif choice == "10":
            # Delete a player
            pass

def menu():
    
    print("0. Exit")
    print("1. Create a new team")
    print("2. View a team's roster")
    print("3. Update a team's information")
    print("4. Delete a team")
    print("5. List all teams by league")
    print("6. List all players in team")
    print("7. List all players by league")
    print("8. Create a new player")
    print("9. Update a player's information")
    print("10. Delete a player")


if __name__ == "__main__":
    main()
