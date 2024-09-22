# lib/cli.py

from helpers import (
    exit_program,
    list_artists,
    find_artist_by_name,
    find_artist_by_id,
    create_artist,
    update_artist,
    delete_artist
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_artists()
        elif choice == "2":
            find_artist_by_name()
        elif choice == "3":
            find_artist_by_id()
        elif choice == "4":
            create_artist()
        elif choice == "5":
            update_artist()
        elif choice == "6":
            delete_artist()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all artists")
    print("2. Find artist by name")
    print("3. Find artist by id")
    print("4. Create new artist")
    print("5. Update existing artist")
    print("6. Delete existing artist")
    #print("7. ")
    #print("8. ")
    #print("9. ")
    #print("10. ")
    #print("11. ")
    #print("12. ")
    #print("13. ")
    #print("14. ")
    #print("15. ")


if __name__ == "__main__":
    main()
