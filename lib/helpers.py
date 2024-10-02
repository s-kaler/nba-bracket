# lib/helpers.py

from models.pokemon import Pokemon
from models.team import Team

def exit_program():
    print("Goodbye!")
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
    print("Please choose on the three starter Pokemon")
    bulbasaur = Pokemon.find_by_name("Bulbasaur")
    charmander = Pokemon.find_by_name("Charmander")
    squirtle = Pokemon.find_by_name("Squirtle")
    print(f"1. {bulbasaur}")
    print(f"2. {charmander}")
    print(f"3. {squirtle}")

def add_starter(starter_choice):
    pokemon_name = ""
    if starter_choice == "1":
        pokemon_name = "Bulbasaur"
    elif starter_choice == "2":
        pokemon_name = "Charmander"
    elif starter_choice == "3":
        pokemon_name = "Squirtle"
    print(f"You've chosen {pokemon_name}! Give your pokemon a nickname: ")
    nickname = input("> ")
    pokemon = Pokemon.find_by_name(pokemon_name)
    new_team = Team.create(nickname, pokemon.id, True)
    print(f'Success: {nickname} has been added to the team!')

def list_all_in_team():
    team_all = Team.get_all()
    for team in team_all:
        print(team)

def list_current_party():
    party = Team.find_by_party()
    print("Current Party: ")
    for team in party:
        print(team)

