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
    list_artist_albums,
    list_songs,
    find_song_by_title,
    find_song_by_id,
    create_song,
    update_song,
    delete_song,
    list_album_songs,
    list_artists_by_genre,
    list_artist_songs,
    list_artist_singles
)


def main():
    while True:
        menu()
        choice = input("> ")
        choice2 =  None

        if choice == "0":
            exit_program()

        elif choice == "1":
            #artist functions
            artist_menu()
            choice2 = input("> ")
            if choice2 == "0":
                pass
            elif choice2 == "1":
                list_artists()
            elif choice2 == "2":
                find_artist_by_name()
            elif choice2 == "3":
                find_artist_by_id()
            elif choice2 == "4":
                create_artist()
            elif choice2 == "5":
                update_artist()
            elif choice2 == "6":
                delete_artist()
            elif choice2 == "7":
                list_artists_by_genre()

        elif choice == "2":
            #album functions
            album_menu()
            choice2 = input("> ")
            if choice2 == "0":
                pass
            elif choice2 == "1":
                list_albums()
            elif choice2 == "2":
                find_album_by_title()
            elif choice2 == "3":
                find_album_by_id()
            elif choice2 == "4":
                create_album()
            elif choice2 == "5":
                update_album()
            elif choice2 == "6":
                delete_album()
            elif choice2 == "7":
                list_artist_albums()

        elif choice == "3":
            #song functions
            song_menu()
            choice2 = input("> ")
            if choice2 == "0":
                pass
            elif choice2 == "1":
                list_songs()
            elif choice2 == "2":
                find_song_by_title()
            elif choice2 == "3":
                find_song_by_id()
            elif choice2 == "4":
                create_song()
            elif choice2 == "5":
                update_song()
            elif choice2 == "6":
                delete_song()
            elif choice2 == "7":
                list_album_songs()
            elif choice2 == "8":
                list_artist_songs()
            elif choice2 == "9":
                list_artist_singles()

        
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Artist options")
    print("2. Album options")
    print("3. Song options")
    
def artist_menu():
    print("0. Back")
    print("1. List all artists")
    print("2. Find artist by name")
    print("3. Find artist by id")
    print("4. Create new artist")
    print("5. Update existing artist")
    print("6. Delete existing artist")
    print("7. List all artists by genre")

def album_menu():
    print("0. Back")
    print("1. List all albums")
    print("2. Find album by title")
    print("3. Find album by id")
    print("4. Create new album")
    print("5. Update existing album")
    print("6. Delete existing album")
    print("7. List all albums by artist")

def song_menu():
    print("0. Back")
    print("1. List all songs")
    print("2. Find song by title")
    print("3. Find song by id")
    print("4. Create new song")
    print("5. Update existing song")
    print("6. Delete existing song")
    print("7. List all songs in album")
    print("8. List all songs by artist")
    print("9. List all singles by artist")


if __name__ == "__main__":
    main()