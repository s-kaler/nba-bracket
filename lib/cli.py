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
    list_all_in_team,
    change_nickname,
    remove_pokemon_from_party,
    add_pokemon_to_party,
    catch_pokemon,
    release_team,
    party_level,
)
from models.team import Team



def main():
    money = 1000
    pokeballs = 5
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
        #   cannot release first pokemon
        #   cannot release all pokemon
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
            menu(money, pokeballs)
            choice = input("> ")
        
            if choice == "0":
                exit_program()
            elif choice == "1":
                list_all_in_team()
                print("1. Change nickname of pokemon")    
                print("2. Remove pokemon from current party")
                print("3. Add pokemon to current party")
                print("4. Release an existing Pokemon")
                choice2 = input("> ")
                if choice2 == "1":
                    change_nickname()
                elif choice2 == "2":
                    remove_pokemon_from_party()
                elif choice2 == "3":
                    add_pokemon_to_party()
                elif choice2 == "4":
                    release_team()
            elif choice == "2":
                if pokeballs >  0:
                    caught = catch_pokemon()
                    if caught:
                        pokeballs += -1
                else:
                    print("You don't have enough pokeballs.")
            elif choice == "3":
                list_pokemon_all()
            elif choice == "4":
                buy_pokeballs()

        
def menu(money, pokeballs):
    print("")
    print(f"You currently have ${money}.")
    print(f"You have {pokeballs} pokeballs.")
    list_current_party()
    print("1. View full team configuration")
    print("2. Catch a new Pokemon")
    print("3. View the Pokedex")
    print("4. Buy more pokeballs")


#for catching pokemon, if the wild pokemon is between certain levels, it will be harder to catch
#1 to 10 is easy
#10 to 30 is medium
#30 to 50 is hard
#50+ is very hard
#add up level of all pokemon in party to increase chances of catching

def buy_pokeballs():
    pass


if __name__ == "__main__":
    main()