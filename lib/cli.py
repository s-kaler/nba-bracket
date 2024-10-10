# lib/cli.py

from helpers import (
    exit_program,
    greeting,
    list_team_all,
    find_team_by_name,
    find_team_by_location,
    create_team,
    update_team,
    delete_team,
    update_starting_roster,
    list_players_by_league,
    list_players_by_team,
    find_player_by_name,
    find_players_by_height,
    find_players_by_position,
    create_player,
    update_player,
    delete_player,
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

            #find_team_by_id()
            #find_team_by_name()
            #find_team_by_location()
            #list_all_players()
            #find_players_by_name()
            #find_players_by_height()
            #find_players_by_position()
            #find_players_by_team()
            #find_players_by_height_range()

def menu():
    print("0. Exit")
    print("1. Team Management")
    print("2. Player Management")

def teams_menu():
    while True:
        print("0. Back")
        print("1. List all teams by league")
        print("2. Find team by name")
        print("3. Find team by location")
        print("4. Create a new team")
        print("5. Update a team's information")
        print("6. Update a team's starting roster")
        print("7. Delete a team")

        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_team_all()
        elif choice == "2":
            find_team_by_name()
        elif choice == "3":
            find_team_by_location()
        elif choice == "4":
            create_team()
        elif choice == "5":
            update_team()
        elif choice == "6":
            update_starting_roster()
        elif choice == "7":
            delete_team()
        else:
            print("Invalid choice.")
        


def players_menu():
    while True:
        print("0. Back")
        print("1. List all players by league")
        print("2. List all players by team")
        print("3. Find players by name")
        print("4. Find players by height")
        print("5. Find players by position")
        print("6. Create a new player")
        print("7. Update a player's information")
        print("8. Delete a player")
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_players_by_league()
        elif choice == "2":
            list_players_by_team()
        elif choice == "3":
            find_player_by_name()
        elif choice == "4":
            find_players_by_height()
        elif choice == "5":
            find_players_by_position()
        elif choice == "6":
            create_player()
        elif choice == "7":
            update_player()
        elif choice == "8":
            delete_player()

if __name__ == "__main__":
    main()

