# lib/cli.py

from helpers import (
    exit_program,
    list_pokemon_all,
    find_pokemon_by_name,
    find_pokemon_by_id,
    create_pokemon,
    update_pokemon,
    delete_pokemon,
    list_pokemon_by_type,
    add_starter,
    greeting,
    list_all_in_team,
    list_current_party,
)
from models.team import Team

money = 1000

def main():
    Team.drop_table()
    Team.create_table()
    starter_is_chosen = False
    print("Welcome to the Pokemon World!")
    while True:
        #start with asking user to pick one starter pokemon
        #starter will be added to the team and party automatically
        #print 3 options of pokemon, Bulbasaur, Charmander, Squirtle

        #afterwards, show menu of new options
        #user has a certain amount of pokeballs (5)
        #user can choose to catch new pokemon
        #   user will get a random battle encounter
        #   can run away from battle
        #   chance of success will be random
        #   new pokemon will be random
        #user can choose to release existing pokemon
        #user can change around pokemon in party
        #user can ask to view current party
        
        #user has a certain amount of money
        #can get more money by releasing pokemon, higher level pokemon are worth more
        #can spend money on pokeballs for better chances
        #if they choose to catch new pokemon, show a list of available pokemon
        #if they choose to release existing pokemon, show a list of their current team

        #as a bonus, users can create their own new pokemon
        if not starter_is_chosen:
            greeting()
            starter_choice = input("> ")
            if starter_choice == "1" or starter_choice == "2" or starter_choice == "3":
                add_starter(starter_choice)
                starter_is_chosen = True
            else:
                print("Invalid choice")
        else:
            menu()
            choice = input("> ")
        
            if choice == "0":
                exit_program()
        
def menu():
    print(f"You currently have ${money}")
    list_current_party()



if __name__ == "__main__":
    main()