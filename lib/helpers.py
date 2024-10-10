# lib/helpers.py
import random

from models.team import Team
from models.player import Player

def exit_program():
    print("Goodbye! Thanks for playing!")
    exit()
    
def greeting():
    print("Welcome to the NBA and NCAA Brackets!")
    print("Here, you will be able to manage teams for each league.")
    print("You will be able to create new teams for each league and draft new players as well.")
    
def teams_menu():
    while True:
        print("")
        print("Teams Menu")
        print(" 0. Back")
        print(" 1. List all teams by league")
        print(" 2. Find team by name")
        print(" 3. Find team by location")
        print(" 4. Create a new team")
        print(" 5. Update a team's information")
        print(" 6. Delete a team")

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
            delete_team()
        else:
            print("Invalid choice.")
        

def players_menu():
    while True:
        print("")
        print("Players Menu")
        print(" 0. Back")
        print(" 1. List all players by league")
        print(" 2. List all players by team")
        print(" 3. Find players by name")
        print(" 4. Find players by height")
        print(" 5. Find players by position")
        print(" 6. Update a starting roster")
        print(" 7. Create a new player")
        print(" 8. Update a player's information")
        print(" 9. Change a player's team")
        print(" 10. Delete a player")
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
            update_starting_roster()
        elif choice == "7":
            create_player()
        elif choice == "8":
            update_player()
        elif choice == "9":
            change_player_team()
        elif choice == "10":
            delete_player()
        else:
            print("Invalid choice.")


def list_team_all():
    print("Which league do you want to list?")
    print("1. NBA")
    print("2. NCAA")
    is_not_found = True
    while is_not_found:
        league_input = input("> ")
        if league_input.isdigit() and (league_input == '1' or league_input == '2'):
            if league_input == '1':
                league = 'NBA' 
            else:
                league = 'NCAA'
            team_all = Team.find_by_league(league)
            print(f"Teams in {league} league:")
            for team in team_all:
                print(f"  {team.location} {team.name}")
            is_not_found = False
        else:
            print("Please select a valid league.")

#id will go unused in user interface
def find_team_by_id():
    id_ = input("Enter the team's id:\n> ")
    team = Team.find_by_id(id_)
    print(f"{team.location} {team.name} | League: {team.league}") if team else print(f'Team {id_} not found.')

def find_team_by_name():
    print("Enter the team's name:")
    is_not_found = True
    while is_not_found:
        name = input("> ")
        if isinstance(name, str) and name:
            is_not_found = False
        else:
            print("Name must be a non-empty string.")
    if team := Team.find_by_name(name):
        print(f"{team.location} {team.name} | League: {team.league}")
    else:
        print(f'Team {name} not found.')

def find_team_by_location():
    print("Enter the team's location:")
    is_not_found = True
    while is_not_found:
        location = input("> ")
        if isinstance(location, str) and location:
            if teams := Team.find_by_location(location):
                for team in teams:
                    print(f"{team.location} {team.name} | League: {team.league}")
            else:
                print(f'Team in {location} not found.')
            is_not_found = False
        else:
            print("Location must be a non-empty string.")
    
    

def create_team():
    print("Enter the team's location:")
    location_not_found = True
    while location_not_found:
        location = input("> ")
        if isinstance(location, str) and location:
            location_not_found = False
        else:
            print("Location must be a non-empty string.")
    print("Enter the team's name:")
    name_not_found = True
    while name_not_found:
        name = input("> ")
        if isinstance(name, str) and name:
            if Team.find_by_name(name):
                print("Team name already exists. Please choose a different name.")
            else:
                name_not_found = False
        else:
            print("Team name must be a non-empty string.")
    print("Enter the team's league: ")
    print("1. NBA")
    print("2. NCAA")
    league = ''
    is_not_created = True
    while is_not_created:
        league_input = input("> ")
        if league_input.isnumeric() and (league_input == '1' or league_input == '2'):
            league = 'NBA' if league_input == '1' else 'NCAA'
            team = Team.create(name, location, league)
            print(f'Success: {team.location} {team.name} created!')
            is_not_created = False
        else:
            print("Please select a valid league.")
    
def update_team():
    name = input("Enter the team's name:\n> ")
    if team := Team.find_by_name(name):
        try: 
            print("Enter the team's new name:")
            name_not_created = True
            while name_not_created:
                new_name = input("> ")
                if isinstance(new_name, str) and new_name:
                    if new_name != name and Team.find_by_name(new_name):
                        print("Team name already exists. Please choose a different name.")
                    else:
                        team.name = name
                        name_not_created = False
                else:
                    print("Team name must be a non-empty string.")
            print("Enter the team's new location:")
            location_not_created = True
            while location_not_created:
                location = input("> ")
                if isinstance(location, str) and location:
                    team.location = location
                    location_not_created = False
                else:
                    print("Location must be a non-empty string.")

            print("Enter the team's league: ")
            print("1. NBA")
            print("2. NCAA")
            league_not_created = True
            while league_not_created:
                league_input = input("> ")
                if league_input.isnumeric() and (league_input == '1' or league_input == '2'):
                    team.league = 'NBA' if league_input == '1' else 'NCAA'
                    league_not_created = False
                else:
                    print("Please select a valid league.")
            team.update()
            print(f'Success: {team.location} {team.name} updated.')
        except Exception as exc:
            print("Error updating team: ", exc)
    else:
        print(f'Team {name} not found.')

def delete_team():
    print("Warning: Deleting a team will mean all players will become free agents.")
    name = input("Enter the team's name:\n> ")
    if team := Team.find_by_name(name):
        confirmation = input(f"Are you sure you want to delete team {team.name}? (y/n)\n> ")
        if confirmation.lower() == 'y':
            team_id = team.id
            players_in_team = Player.find_by_team_id(team_id)
            for player in players_in_team:
                player.starter = 0
                player.team_id = None
                player.update()
            team.delete()
            print(f'Team {name} deleted. Any players have become free agents.')
        else:
            print(f"Team {name} not deleted.")
            return
    else:
        print(f'Team {name} not found.')

def list_all_players():
    player_all = Player.get_all()
    for player in player_all:
        print(display_player(player))

def list_players_by_team():
    team_name = input("Please enter the team you want to see the roster for:\n> ")
    if team := Team.find_by_name(team_name):
        team_roster = Player.find_by_team_id(team.id)
        print("-----Starting Roster-----")
        for player in team_roster:
            if player.starter == 1:
                print(display_player(player))
        print("-----Bench-----")
        for player in team_roster:
            if player.starter == 0:
                print(display_player(player))
    else:
        print(f"No team {team_name} found.")

def list_players_by_league():
    print("Enter the team's league:")
    print("1. NBA")
    print("2. NCAA")
    print("3. Free Agents")
    is_not_league = True
    while is_not_league:
        league_input = input("> ")
        if league_input.isdigit() and (league_input == '1' or league_input == '2' or league_input == '3'):
            if league_input == '1':
                league = 'NBA'
            elif league_input == '2':
                league = 'NCAA'
            else:
                league = None
            is_not_league = False
        else:
            print("Please select a valid league.")
    if league == 'NBA' or league == 'NCAA':
        team_all = Team.find_by_league(league)
        if team_all:
            for team in team_all:
                team_roster = Player.find_by_team_id(team.id)
                if team_roster:
                    print(f"{team.location} {team.name}\nRoster: ")
                    for player in team_roster:
                        print("   ", display_player(player))
                else:
                    print(f"{team.location} {team.name}\nRoster: No players found.")
                print("")
        else:
            print("No active players found.")
    else:
        free_agents = Player.find_by_team_id(None)
        if free_agents:
            print("Free Agents:")
            for player in free_agents:
                print("  ", display_player(player))
        else:
            print("No active free agents found.")

def find_player_by_name():
    print("Enter the player's name:")
    is_not_found = True
    while is_not_found:
        name = input("> ")
        if isinstance(name, str) and name:
            player = Player.find_by_name(name)
            if player:
                if player.team_id:
                    team = Team.find_by_id(player.team_id)
                    print(f"{display_player(player)} | {team.location} {team.name}")
                else:
                    print(f"{display_player(player)} | Free Agent")
            else:
                print(f'Player {name} not found.')
            is_not_found = False
        else:
            print("Name must be a non-empty string.")
    

def find_players_by_height():
    print("Enter the player's height (in inches): ")
    is_not_found = True
    while is_not_found:
        height_input = input("> ")
        if height_input.isdigit():
            height = int(height_input)
            players = Player.find_by_height(height)
            if players:
                for player in players:
                    if player.team_id:
                        team = Team.find_by_id(player.team_id)
                        print(f"{display_player(player)}| {team.location} {team.name}")
                    else:
                        print(f"{display_player(player)} | Free Agent")
            else:
                print("No players found with that height.")
            is_not_found = False
        else:
            print("Please enter a valid height (in inches).")
    

def find_players_by_position():
    print("Enter the player's position: ")
    is_not_found = True
    while is_not_found:
        position = input("> ")
        if isinstance(position, str) and position:
            players = Player.find_by_position(position)
            if players:
                for player in players:
                    if player.team_id:
                        team = Team.find_by_id(player.team_id)
                        print(f"{display_player(player)} | {team.name}")
                    else:
                        print(f"{display_player(player)} | Free Agent") 
            else:
                print("No players found with that position.")
            is_not_found = False
        else:
            print("Position must be a non-empty string.")
    

def create_player():
    print("Enter the player's name: ")
    name_not_valid = True
    while name_not_valid:
        name = input("> ")
        if isinstance(name, str) and name:
            name_not_valid = False
        else:
            print("Name must be a non-empty string.")
    print("Enter the player's height (in inches): ")
    height_not_valid = True
    while height_not_valid:
        height_input = input("> ")
        if height_input.isdigit() and int(height_input) > 0:
            height = int(height_input)
            height_not_valid = False
        else:
            print("Please enter a valid height (in inches).")
    print("Enter the player's position: ")
    position_not_valid = True
    while position_not_valid:
        position = input("> ")
        if isinstance(position, str) and position:
            position_not_valid = False
        else:
            print("Name must be a non-empty string.")
    starter = 0
    print("What team does this player belong to? Choose None if Free Agent")
    all_teams = Team.get_all()
    print("0. None")
    for index, team in enumerate(all_teams):
        print(f"{index+1}. {team.location} {team.name}")
    team_not_found = True
    while team_not_found:
        team_input = input("> ")
        if team_input == '0':
            team_id = None
            team_not_found = False
        elif team_input.isdigit and int(team_input) <= len(all_teams):
            team = all_teams[int(team_input) - 1]
            team_id = team.id
            if len(Player.find_by_starter_and_team(1, team_id)) < 5:
                starter = 1
            team_not_found = False
        else:
            print("Invalid team selection.")
    player = Player.create(name, height, position, starter, team_id)
    if player.team_id == None:
        print(f'{display_player(player)} has joined as a free agent!')
    else:
        if starter == 1:
            print(f'{display_player(player)} has joined the {team.location} {team.name} as a starter!')
        else:
            print(f'{display_player(player)} has joined the {team.location} {team.name}!')


def update_player():
    print("Choose a player to change the information of: ")
    old_name = input("> ")
    player = Player.find_by_name(old_name)
    if player:
        print("Enter the player's new name:")
        name_not_valid = True
        while name_not_valid:
            new_name = input("> ")
            if isinstance(new_name, str) and new_name:
                player.name = new_name
                name_not_valid = False
            else:
                print("Name must be a non-empty string.")

        print("Enter the player's new height:")
        height_not_valid = True
        while height_not_valid:
            new_height = input("> ")
            if new_height.isdigit() and int(new_height) > 0:
                player.height = int(new_height)
                height_not_valid = False
            else:
                print("Please enter a valid height (in inches).")
            
        print("Enter the player's new position:")
        position_not_valid = True
        while position_not_valid:
            new_position = input("> ")
            if isinstance(new_position, str) and new_position:
                player.position = new_position
                position_not_valid = False
            else:
                print("Name must be a non-empty string.")
        
        player.update()
        print(f'Success: {new_name} has been updated.')
    else:
        print(f'Player member {old_name} not found.')

def delete_player():
    print("Choose a player to delete: ")
    name = input("> ")
    player = Player.find_by_name(name)
    if player:
        print(f"Are you sure you want to delete {name}? (y/n)")
        choice = input("> ")
        if choice.lower() == 'y':
            player.delete()
            print(f'Success: {name} has retired.')
        else:
            print(f'Player {name} not deleted.')
    else:
        print(f'Player member {name} not found.')

def update_starting_roster():
    team_name = input("Which team's roster would you like to update?\n> ")
    
    team = Team.find_by_name(team_name)
    if team:
        team_roster = Player.find_by_team_id(team.id)
        team_starting_size = len(Player.find_by_starter_and_team(1, team.id))
        print("-----Starting Roster-----")
        for player in team_roster:
            if player.starter == 1:
                print("  ", player)
        print("-----Bench-----")
        for player in team_roster:
            if player.starter == 0:
                print("  ", player)
        print("Which player's status do you want to change?")
        name = input("> ")
        player = Player.find_by_name(name)
        if player:
            if player in team_roster:
                if player.starter == 1:
                    choice = input(f"Do you want to bench {name}?\ny/n? ")
                    if choice.lower() == 'y':
                        player.starter = 0
                        player.update()
                        print(f'Success: {name} has been removed from the starting roster.')
                    else:
                        return
                else:
                    if team_starting_size < 5:
                        choice = input(f"Do you want to start with {name}?\ny/n? ")
                        if choice.lower() == 'y':
                            player.starter = 1
                            player.update()
                            print(f'Success: {name} has been added to the starting roster.')
                        else:
                            return
                    else:
                        print("You cannot start with more than 5 players.")
                        return
            else:
                print(f'Player must be in {team.location} {team.name}')
        else:
            print(f'Player {name} not found.')
    else:
        print(f'Team {team_name} not found.')


def change_player_team():
    print("Choose a player to change the team of: ")
    is_not_found = True
    team = None
    while is_not_found:
        name = input("> ")
        if isinstance(name, str) and name:
            player = Player.find_by_name(name)
            if player:
                if player.team_id:
                    team = Team.find_by_id(player.team_id)
                    print(f"{name} is on the {team.location} {team.name}.")
                else:
                    print(f"{name} is a Free Agent.")
            else:
                print(f'Player {name} not found.')
                return
            is_not_found = False
        else:
            print("Name must be a non-empty string.")
    starter = 0
    team_id = None
    print("What team would you like to change them to? Choose None if Free Agent")
    all_teams = Team.get_all()
    print("0. None")
    for index, team in enumerate(all_teams):
        print(f"{index+1}. {team.location} {team.name}")
    team_not_found = True
    while team_not_found:
        team_input = input("> ")
        if team_input == '0':
            team_not_found = False
        elif team_input.isdigit and int(team_input) <= len(all_teams):
            team = all_teams[int(team_input) - 1]
            team_id = team.id
            if len(Player.find_by_starter_and_team(1, team_id)) < 5:
                starter = 1
            team_not_found = False
        else:
            print("Invalid team selection.")
    player.starter = starter
    player.team_id = team_id
    player.update()
    if player.team_id == None:
        print(f'{display_player(player)} has joined as a free agent!')
    else:
        if starter == 1:
            print(f'{display_player(player)} has joined the {team.location} {team.name} as a starter!')
        else:
            print(f'{display_player(player)} has joined the {team.location} {team.name}!')

def display_player(player):
    return f"{player.name}: {int(player.height / 12)}\'{player.height % 12}\", {player.position}"