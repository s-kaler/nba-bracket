# lib/cli.py

from helpers import (
    exit_program,
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        choice2 =  None

        if choice == "0":
            exit_program()

        elif choice == "1":
            pass
        else:
            print("Invalid choice")



if __name__ == "__main__":
    main()