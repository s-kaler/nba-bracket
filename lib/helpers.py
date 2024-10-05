# lib/helpers.py
import random

from models.pokemon import Pokemon
from models.team import Team

def exit_program():
    print("Goodbye! Thanks for playing!")
    exit()

#pokemon functions 
def list_pokemon_all():
    pokemon_all = Pokemon.get_all()
    for pokemon in pokemon_all:
        print(pokemon)

def find_pokemon_by_name():
    name = input("Enter the pokemon's name: ")
    pokemon = Pokemon.find_by_name(name)
    print(pokemon) if pokemon else print(
        f'Pokemon {name} not found')

def find_pokemon_by_id():
    id_ = input("Enter the pokemon's id: ")
    pokemon = Pokemon.find_by_id(id_)
    print(pokemon) if pokemon else print(f'Pokemon {id_} not found')


def create_pokemon():
    name = input("Enter the pokemon's name: ")
    genre = input("Enter the pokemon's genre: ")
    try:
        pokemon = Pokemon.create(name, genre)
        print(f'Success: {pokemon}')
    except Exception as exc:
        print("Error creating pokemon: ", exc)

def update_pokemon():
    id_ = input("Enter the pokemon's id: ")
    if pokemon := Pokemon.find_by_id(id_):
        try:
            name = input("Enter the pokemon's new name: ")
            pokemon.name = name
            genre = input("Enter the pokemon's new genre: ")
            pokemon.genre = genre

            pokemon.update()
            print(f'Success: {pokemon}')
        except Exception as exc:
            print("Error updating pokemon: ", exc)
    else:
        print(f'Pokemon {id_} not found')

def delete_pokemon():
    id_ = input("Enter the pokemon's id: ")
    if pokemon := Pokemon.find_by_id(id_):
        pokemon.delete()
        print(f'Pokemon {id_} deleted')
    else:
        print(f'Pokemon {id_} not found')

def list_pokemon_by_type():
    find_type = input("Enter the pokemon's type: ")
    if pokemon_all := Pokemon.find_by_type(find_type):
        for pokemon in pokemon_all:
            print(pokemon)
    else:
        print(f'No pokemon_all with {find_type} found')

def greeting():
    print("Please choose one of the three starter Pokemon.")
    bulbasaur = Pokemon.find_by_name("Bulbasaur")
    charmander = Pokemon.find_by_name("Charmander")
    squirtle = Pokemon.find_by_name("Squirtle")
    print(f"1. {bulbasaur}")
    print(f"2. {charmander}")
    print(f"3. {squirtle}")

def add_starter():
    pokemon_name = ""
    while True:
        starter_choice = input("> ")
        if starter_choice == "1" or starter_choice == "2" or starter_choice == "3":
            if starter_choice == "1":
                pokemon_name = "Bulbasaur"
            elif starter_choice == "2":
                pokemon_name = "Charmander"
            elif starter_choice == "3":
                pokemon_name = "Squirtle"
            break
        else:
            print("Invalid choice")
    print(f"You've chosen {pokemon_name}! Give your pokemon a nickname: ")
    while True:
        nickname = input("> ")
        if nickname:
            pokemon = Pokemon.find_by_name(pokemon_name)
            new_team = Team.create(nickname, pokemon.id, True)
            print(f'Success: {nickname} has been added to the team!')
            return True
        else:
            print("Please enter a nickname.")

def list_all_in_team():
    team_all = Team.get_all()
    for team in team_all:
        print(team)

def list_current_party():
    party = Team.list_all_party()
    print("Current Party: ")
    for team in party:
        print(team)
    print(f'Party Level: {party_level()}')
    
def party_level():
    party = Team.list_all_party()
    total_level = 0
    for team in party:
        total_level += Pokemon.find_by_id(team.pokemon_id).level
    return total_level

def change_nickname():
    print("Choose a pokemon to change the nickname of: ")
    old_nickname = input("> ")
    team = Team.find_by_nickname(old_nickname)
    if team:
        print("What would you like to change it to?")
        new_nickname = input("> ")
        team.nickname = new_nickname
        team.update()
        print(f'Success: {old_nickname} has been changed to {new_nickname}.')
    else:
        print(f'Team member {old_nickname} not found.')

def remove_pokemon_from_party():
    party = Team.list_all_party()
    if len(party) == 1:
        print("You cannot remove the last member from the party.")
        return
    else:
        print("Which party member do you want to remove?")
        nickname = input("> ")
        party_member = Team.find_by_nickname(nickname)
        if party_member:
            if party_member.in_party == 1:
                party_member.in_party = 0
                party_member.update()
                print(f'Success: {nickname} has been removed from the party.')
            else:
                print(f'{nickname} is not currently in the party.')
        else:
            print(f'Party member {nickname} not found.')


def add_pokemon_to_party():
    all_team = Team.get_all()
    party = Team.list_all_party()
    
    if len(party) == 6:
        print("You cannot add more than 6 members to the party.")
        return
    else:
        if len(party) == len(all_team):
            print("You do not have any pokemon to add to the party")
            return
        else:
            print("Which party member do you want to add?")
            nickname = input("> ")
            new_party_member = Team.find_by_nickname(nickname)
            if new_party_member:
                if new_party_member.in_party == 0:
                    new_party_member.in_party = 1
                    new_party_member.update()
                    print(f'Success: {nickname} has been removed from the party.')
                else:
                    print(f'{nickname} is already in the party.')
            else:
                print(f'Party member {nickname} not found.')


#for catching pokemon, if the wild pokemon is between certain levels, it will be harder to catch
#1 to 10 is easy
#10 to 30 is medium
#30 to 50 is hard
#50+ is very hard
#add up level of all pokemon in party to increase chances of catching

def catch_pokemon():
    random_id = random.randint(1, 151)
    wild_pokemon = Pokemon.find_by_id(random_id)
    wild_level =  wild_pokemon.level
    difficulty = 0
    difficulty_pct = 0
    if wild_level >= 1 and wild_level < 10:
        difficulty = "Easy"
        difficulty_pct = 75
    elif wild_level >= 10 and wild_level < 30:
        difficulty = "Medium"
        difficulty_pct = 50
    elif wild_level >= 30 and wild_level < 50:
        difficulty = "Hard"
        difficulty_pct = 25
    else:
        difficulty = "Very Hard"
        difficulty_pct = 10

    party = Team.list_all_party()
    party_lvl = party_level()
    chance_boost = party_lvl / 5
    chance_to_catch = random.randint(0, 100) + chance_boost
    will_be_caught = False
    if chance_to_catch <= difficulty_pct:
        will_be_caught = True
    
    print("")
    print(f"A wild {wild_pokemon.name} appeared!")
    print(f"Difficulty: {difficulty}")
    print(wild_pokemon)
    print("What would like to do?")
    print("1. Catch pokemon")
    print("2. Run away")
    while True:
        choice = input("> ")
        if choice == "1":
            if(will_be_caught):
                print(f"Success! You caught a {wild_pokemon.name}!")
                print("Give it a nickname: ")
                while True:
                    nickname = input("> ")
                    if team := Team.find_by_nickname(nickname):
                        print("You already have a team member with that nickname!")
                    else:
                        break  # Exit the loop if the nickname is unique
                if len(party) == 6:
                    new_team = Team.create(nickname, wild_pokemon.id, False)
                else:
                    new_team = Team.create(nickname, wild_pokemon.id, True)
                print(f'Success: {nickname} has been added to the team!')
                return True
            else:
                print(f"The pokeball broke and the pokemon got away.")
                return True
        elif choice == "2":
            print("The wild pokemon got away.")
            return False
        else:
            print("Invalid choice. Please try again.")

def release_team():
    party = Team.list_all_party()
    team_all = Team.get_all()
    if len(team_all) == 1:
        print("You cannot release the last pokemon from the team!")
        return 0
    print("Choose a pokemon to release:")
    nickname = input("> ")
    team_member = Team.find_by_nickname(nickname)
    
    if team_member:
        released_money = Pokemon.find_by_id(team_member.pokemon_id).level * 3
        if team_member.in_party == 1 and len(party) == 1:
            print(f'You cannot release your last pokemon in the party!')
            return 0
        if team_member.id == 1:
            print("You cannot release your starter pokemon from the team!")
            return 0
        else:
            print(f'Are you sure you want to release {nickname}?')
            are_you_sure = input("> y/n? ")
            if are_you_sure == "y":
                team_member.delete()
                print(f'Success: {nickname} has been released from the team.')
                print(f'You gained ${released_money}')
                return released_money
            else:
                return 0
    else:
        print(f'Team member {nickname} not found.')
        return 0