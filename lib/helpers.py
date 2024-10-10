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
    print("")

def teams_menu():
    while True:
        print("Teams Menu")
        print(" 0. Back")
        print(" 1. List all teams by league")
        print(" 2. Find team by name")
        print(" 3. Find team by location")
        print(" 4. Create a new team")
        print(" 5. Update a team's information")
        print(" 6. Update a team's starting roster")
        print(" 7. Delete a team")

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
        print("Players Menu")
        print(" 0. Back")
        print(" 1. List all players by league")
        print(" 2. List all players by team")
        print(" 3. Find players by name")
        print(" 4. Find players by height")
        print(" 5. Find players by position")
        print(" 6. Create a new player")
        print(" 7. Update a player's information")
        print(" 8. Delete a player")
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


def list_team_all():
    print("Which league do you want to list?")
    print("1. NBA")
    print("2. NCAA")
    while True:
        league_input = input("> ")
        if league_input.isdigit() and (league_input == '1' or league_input == '2'):
            if league_input == '1':
                league = 'NBA' 
            else:
                league = 'NCAA'
            team_all = Team.find_by_league(league)
            print(f"Teams in {league} league:")
            for team in team_all:
                print("  ", team)
            break
        else:
            print("Please select a valid league.")

#id will go unused in user interface
def find_team_by_id():
    id_ = input("Enter the team's id:\n> ")
    team = Team.find_by_id(id_)
    print(team) if team else print(f'Team {id_} not found.')

def find_team_by_name():
    print("Enter the team's name:")
    while True:
        name = input("> ")
        if isinstance(name, str) and name:
            break
        else:
            print("Name must be a non-empty string.")
    if team := Team.find_by_name(name):
        print(team)
    else:
        print(f'Team {name} not found.')

def find_team_by_location():
    print("Enter the team's location:")
    while True:
        location = input("> ")
        if isinstance(location, str) and location:
            break
        else:
            print("Location must be a non-empty string.")
    if teams := Team.find_by_location(location):
        for team in teams:
            print(team)
    else:
        print(f'Team in {location} not found.')
    

def create_team():
    print("Enter the team's location:")
    while True:
        location = input("> ")
        if isinstance(location, str) and location:
            break
        else:
            print("Location must be a non-empty string.")
    print("Enter the team's name:")
    while True:
        name = input("> ")
        if isinstance(name, str) and name:
            if Team.find_by_name(name):
                print("Team name already exists. Please choose a different name.")
            else:
                break
        else:
            print("Team name must be a non-empty string.")
    print("Enter the team's league: ")
    print("1. NBA")
    print("2. NCAA")
    league = ''
    while True:
        league_input = input("> ")
        if league_input.isnumeric() and (league_input == '1' or league_input == '2'):
            league = 'NBA' if league_input == '1' else 'NCAA'
            team = Team.create(name, location, league)
            print(f'Success: {team} created!')
            break
        else:
            print("Please select a valid league.")
    
def update_team():
    name = input("Enter the team's name:\n> ")
    if team := Team.find_by_name(name):
        try: 
            print("Enter the team's new name:")
            while True:
                new_name = input("> ")
                if isinstance(new_name, str) and new_name:
                    if new_name != name and Team.find_by_name(new_name):
                        print("Team name already exists. Please choose a different name.")
                    else:
                        team.name = name
                        break
                else:
                    print("Team name must be a non-empty string.")
            print("Enter the team's new location:")
            while True:
                location = input("> ")
                if isinstance(location, str) and location:
                    team.location = location
                    break
                else:
                    print("Location must be a non-empty string.")

            print("Enter the team's league: ")
            print("1. NBA")
            print("2. NCAA")
            while True:
                league_input = input("> ")
                if league_input.isnumeric() and (league_input == '1' or league_input == '2'):
                    team.league = 'NBA' if league_input == '1' else 'NCAA'
                    break
                else:
                    print("Please select a valid league.")
            team.update()
            print(f'Success: {team}')
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
        print(player)

def list_players_by_team():
    team_name = input("Please enter the team you want to see the roster for:\n> ")
    if team := Team.find_by_name(team_name):
        team_roster = Player.find_by_team_id(team.id)
        print("-----Starting Roster-----")
        for player in team_roster:
            if player.starter == 1:
                print(player)
        print("-----Bench-----")
        for player in team_roster:
            if player.starter == 0:
                print(player)
    else:
        print(f"No team {team_name} found.")

def list_players_by_league():
    print("Enter the team's league:")
    print("1. NBA")
    print("2. NCAA")
    print("3. Free Agents")
    while True:
        league = input("> ")
        if league.isdigit() and (league == '1' or league == '2' or league == '3'):
            if league == '1':
                league = 'NBA'
            elif league == '2':
                league = 'NCAA'
            else:
                league = None
            break
        else:
            print("Please select a valid league.")
    if league == '1' or league == '2':
        team_all = Team.find_by_league(league)
        if team_all:
            for team in team_all:
                team_roster = Player.find_by_team_id(team.id)
                if team_roster:
                    print(f"{team}\nRoster: ")
                    for player in team_roster:
                        print("   ", player)
                else:
                    print(f"{team}\nRoster: No players found.")
                print("")
        else:
            print("No active players found.")
    else:
        free_agents = Player.find_by_team_id(None)
        if free_agents:
            print("Free Agents:")
            for player in free_agents:
                print("  ", player)
        else:
            print("No active free agents found.")

def find_player_by_name():
    print("Enter the player's name:")
    while True:
        name = input("> ")
        if isinstance(name, str) and name:
            break
        else:
            print("Name must be a non-empty string.")
    player = Player.find_by_name(name)
    if player:
        if player.team_id:
            team = Team.find_by_id(player.team_id)
            print(f"{player} | {team.name}")
        else:
            print(f"{player} | Free Agent")
    else:
        print(f'Player {name} not found.')

def find_players_by_height():
    print("Enter the player's height (in inches): ")
    while True:
        height_input = input("> ")
        if height.isdigit():
            break
        else:
            print("Please enter a valid height (in inches).")
    height = int(height_input)
    players = Player.find_by_height(height)
    for player in players:
        if player.team_id:
            team = Team.find_by_id(player.team_id)
            print(f"{player} | {team.name}")
        else:
            print(f"{player} | Free Agent")
    else:
        print("No players found with that height.")

def find_players_by_position():
    print("Enter the player's position: ")
    while True:
        position = input("> ")
        if isinstance(position, str) and position:
            break
        else:
            print("Position must be a non-empty string.")
    players = Player.find_by_position(position)
    if players:
        for player in players:
            if player.team_id:
                team = Team.find_by_id(player.team_id)
                print(f"{player} | {team.name}")
            else:
                print(f"{player} | Free Agent") 
    else:
        print("No players found with that position.")

def create_player():
    print("Enter the player's name: ")
    while True:
        name = input("> ")
        if isinstance(name, str) and name:
            break
        else:
            print("Name must be a non-empty string.")
    print("Enter the player's height (in inches): ")
    while True:
        height_input = input("> ")
        if height_input.isdigit() and int(height_input) > 0:
            height = int(height_input)
            break
        else:
            print("Please enter a valid height (in inches).")
    print("Enter the player's position: ")
    while True:
        position = input("> ")
        if isinstance(position, str) and position:
            break
        else:
            print("Name must be a non-empty string.")
    starter = 0
    print("What team does this player belong to? Choose None if Free Agent")
    all_teams = Team.get_all()
    print("0. None")
    for index, team in enumerate(all_teams):
        print(f"{index+1}. {team}")
    while True:
        team_input = input("> ")
        if team_input == '0':
            team_id = None
            break
        elif team_input.isdigit and int(team_input) <= len(all_teams):
            team_id = int(team_input)
            team = Team.find_by_id(team_id)
            if len(Player.find_by_starter_and_team(1, team_id)) < 5:
                starter = 1
            
            break
        else:
            print("Invalid team selection.")
    player = Player.create(name, height, position, starter, team_id)
    if player.team_id == None:
        print(f'{player} has joined as a free agent!')
    else:
        if starter == 1:
            print(f'{player} has joined the {team.location} {team.name} as a starter!')
        else:
            print(f'{player} has joined the {team.location} {team.name}!')


def update_player():
    print("Choose a player to change the information of: ")
    old_name = input("> ")
    player = Player.find_by_name(old_name)
    if player:
        print("Enter the player's new name:")
        while True:
            new_name = input("> ")
            if isinstance(new_name, str) and new_name:
                player.name = new_name
                break
            else:
                print("Name must be a non-empty string.")

        print("Enter the player's new height:")
        while True:
            new_height = input("> ")
            if new_height.isdigit() and int(new_height) > 0:
                player.height = int(new_height)
                break
            else:
                print("Please enter a valid height (in inches).")
            
        print("Enter the player's new position:")
        while True:
            new_position = input("> ")
            if isinstance(new_position, str) and new_position:
                player.position = new_position
                break
            else:
                print("Name must be a non-empty string.")
        
        player.update()
        print(f'Success: {new_name} has been changed.')
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
                print(f'Player must be in {team}')
        else:
            print(f'Player {name} not found.')
    else:
        print(f'Team {team_name} not found.')

