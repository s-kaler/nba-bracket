# lib/helpers.py
import random

from models.team import Team
from models.player import Player

def exit_program():
    print("Goodbye! Thanks for playing!")
    exit()

#team functions 
def list_team_all():
    team_all = Team.get_all()
    for team in team_all:
        print(team)

def find_team_by_id():
    id_ = input("Enter the team's id:\n> ")
    team = Team.find_by_id(id_)
    print(team) if team else print(f'Team {id_} not found.')

def find_team_by_name():
    name = input("Enter the team's name:\n> ")
    team = Team.find_by_name(name)
    print(team) if team else print(f'Team {name} not found.')

def find_team_by_city():
    city = input("Enter the team's city: ")
    team = Team.find_by_city(city)
    print(team) if team else print(f'Team in {city} not found.')

def find_team_by_league():
    print("Enter the team's league:")
    print("1. NBA")
    print("2. NCAA")
    while True:
        league = input("> ")
        if league.isdigit() and (league == '1' or league == '0'):
            league = 'NBA' if league == '1' else 'NCAA'
            team = Team.find_by_league(league)
            print(team) if team else print(f'Team in {league} not found.')
            break
        else:
            print("Please select a valid league.")
    

def create_team():
    name = input("Enter the team's name:\n> ")
    print("Enter the team's city: ")
    city = input("Enter the team's city:\n> ")
    print("Enter the team's league: ")
    print("1. NBA")
    print("2. NCAA")
    while True:
        league = input("> ")
        if league.isdigit() and (league == '1' or league == '0'):
            league = 'NBA' if league == '1' else 'NCAA'
            break
        else:
            print("Please select a valid league.")
    try:
        team = Team.create(name, city, league)
        print(f'Success: {team} created!')
    except Exception as exc:
        print("Error creating team: ", exc)

def update_team():
    id_ = input("Enter the team's id:\n> ")
    if team := Team.find_by_id(id_):
        try:
            name = input("Enter the team's new name:\n> ")
            team.name = name
            city = input("Enter the team's new city:\n> ")
            team.city = city
            print("Enter the team's league: ")
            print("1. NBA")
            print("2. NCAA")
            while True:
                league = input("> ")
                if league.isdigit() and (league == '1' or league == '0'):
                    league = 'NBA' if league == '1' else 'NCAA'
                    break
                else:
                    print("Please select a valid league.")
            team.update()
            print(f'Success: {team}')
        except Exception as exc:
            print("Error updating team: ", exc)
    else:
        print(f'Team {id_} not found.')

def delete_team():
    id_ = input("Enter the team's id:\n> ")
    if team := Team.find_by_id(id_):
        team.delete()
        print(f'Team {id_} deleted.')
    else:
        print(f'Team {id_} not found.')

def list_team_by_city():
    find_city = input("Enter the team's city:\n> ")
    if team_all := Team.find_by_city(find_city):
        for team in team_all:
            print(team)
    else:
        print(f'No team in {find_city} found.')

def list_team_by_league():
    print("Enter the team's league:")
    print("1. NBA")
    print("2. NCAA")
    while True:
        league = input("> ")
        if league.isdigit() and (league == '1' or league == '0'):
            league = 'NBA' if league == '1' else 'NCAA'
            if team_all := Team.find_by_league(league):
                for team in team_all:
                    print(team)
            else:
                print(f'No team in {league} found.')
            break
        else:
            print("Please select a valid league.")

def greeting():
    print("Please choose one of the three starter Team.")
    bulbasaur = Team.find_by_name("Bulbasaur")
    charmander = Team.find_by_name("Charmander")
    squirtle = Team.find_by_name("Squirtle")
    print(f"1. {bulbasaur}")
    print(f"2. {charmander}")
    print(f"3. {squirtle}")


def list_all_players():
    player_all = Player.get_all()
    for player in player_all:
        print(player)

def list_players_in_team():
    team_name = input("Please enter the team you want to see the roster for:\n> ")
    team = Team.find_by_name(team_name)
    team_roster = Player.find_by_team_id(team.id)
    print("Current Party: ")
    for player in team_roster:
        if player.active == 1:
            print(player)
    for player in team_roster:
        if player.active == 0:
            print(player)


def change_name():
    print("Choose a player to change the name of: ")
    old_name = input("> ")
    player = Player.find_by_name(old_name)
    if player:
        print("What would you like to change it to?")
        new_name = input("> ")
        player.name = new_name
        player.update()
        print(f'Success: {old_name} has been changed to {new_name}.')
    else:
        print(f'Player member {old_name} not found.')

def remove_team_from_active():
    print("Which player do you want to remove?")
    name = input("> ")
    party_member = Player.find_by_name(name)
    if party_member:
        if party_member.active == 1:
            party_member.active = 0
            party_member.update()
            print(f'Success: {name} has been removed from the active roster.')
        else:
            print(f'{name} is not currently in the active roster.')
    else:
        print(f'Party member {name} not found.')


def add_player_to_active():
    roster = Player.find_by_active(1)
    if len(roster) == 5:
        print("You cannot add more than 5 members to the active roster.")
        return
    else:
        print("Which player do you want to add?")
        name = input("> ")
        new_party_member = Player.find_by_name(name)
        if new_party_member:
            if new_party_member.active == 0:
                new_party_member.name = 1
                new_party_member.name()
                print(f'Success: {name} has been removed from the active roster.')
            else:
                print(f'{name} is already in the active roster.')
        else:
            print(f'Player member {name} not found.')

