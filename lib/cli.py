# lib/cli.py

from helpers import (
    exit_program,
    list_artists,
    find_artist_by_name,
    find_artist_by_id,
    create_artist,
    update_artist,
    delete_artist,
    list_albums,
    find_album_by_title,
    find_album_by_id,
    create_album,
    update_album,
    delete_album,
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
        elif choice == "7":
            list_albums()
        elif choice == "8":
            find_album_by_title()
        elif choice == "9":
            find_album_by_id()
        elif choice == "10":
            create_album()
        elif choice == "11":
            update_album()
        elif choice == "12":
            delete_album()
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
    #print("Search for artist by genre")
    print("7. List all albums")
    print("8. Find album by title")
    print("9. Find album by id")
    print("10. Create new album")
    print("11. Update existing album")
    print("12. Delete existing album")
    #print("13. ")
    #print("14. ")
    #print("15. ")


if __name__ == "__main__":
    main()
