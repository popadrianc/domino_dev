import time
from mods.registration import data
from mods.g1 import game_tags




print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n" 
      "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
      "||||>>The World Of Evernothing<<||||\n"
      "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
      "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
      "  just an other hack and slash RPG  \n")


def main_menu():
    print("1. New Game\n"
          "2. Help\n"
          "3. Social Stuff\n"
          "4. Register or Login\n\n"          
          "0. Exit application.")

    try:
        choice = int(input(">>>"))
    except KeyError:
        print("\n\nWrong option NOOB!\n"
              "Are you trying to cheat?\n\n")
        main_menu()

    if choice == 1:
        print("What the hec are you looking for?")
        print("1. Create your char")
        print("0. Go back")

        try:
            choice_menu1 = int(input(">>>"))
        except KeyError:
            print("\n\nWrong option NOOB!\n"
                  "Are you trying to cheat?\n\n")
            main_menu()
        if choice_menu1 == 1:
            print("Write your char name: ")
            char_name = input(">>>")
            print("Howdy", char_name)
            print("\n")
            print("And the adventure will start!")
            print("\n")
            time.sleep(2)
            print(game_tags())
        if choice_menu1 == 0:
            main_menu()

    if choice == 2:
        print("1. Open help doc")
        print("0. Go back")

        try:
            choice_menu2 = int(input(">>>"))
        except KeyError:
            print("\n\nWrong option NOOB!\n"
                  "Are you trying to cheat?\n\n")
            main_menu()
        if choice_menu2 == 1:
            with open("mods/help.txt", 'r') as f:
                file = f.read()
            print(file)
            running_total = 0
            for line in file:
                if line.isnumeric():
                    running_total += int(line)
            print(running_total)
        if choice_menu2 == 0:
            main_menu()

    if choice == 3:
        print("This feature is not implemented")
        print("0. Go back")

        try:
            choice_menu3 = int(input())
        except KeyError:
            print("\n\nWrong option NOOB!\n"
                  "Are you trying to cheat?\n\n")
            main_menu()
        if choice_menu3 == 0:
            main_menu()

    if choice == 4:
        print("1. Register or Login")
        print("0. Go back")

        try:
            choice_menu4 = int(input())
        except KeyError:
            print("\n\nWrong option NOOB!\n"
                  "Are you trying to cheat?\n\n")
            main_menu()
        if choice_menu4 == 1:
            print(data())
            main_menu()
        if choice_menu4 == 0:
            main_menu()

    if choice == 0:
        print("Shuuuutingggg doooown!")
        exit(0)

if __name__ == "__main__":
    main_menu()

