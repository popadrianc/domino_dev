from mods.g1 import battle_tags



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
          "4. Log in\n"
          "5. Register\n\n"
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
            print("Let's roll the dice!")
            battle_tags()
        if choice_menu1 == 0:
            main_menu()

    if choice == 2:
        print("This feature is not implemented")
        print("0. Go back")

        try:
            choice_menu2 = int(input(">>>"))
        except KeyError:
            print("\n\nWrong option NOOB!\n"
                  "Are you trying to cheat?\n\n")
            main_menu()
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
        print("This feature is not implemented")
        print("0. Go back")

        try:
            choice_menu4 = int(input())
        except KeyError:
            print("\n\nWrong option NOOB!\n"
                  "Are you trying to cheat?\n\n")
            main_menu()
        if choice_menu4 == 0:
            main_menu()

    if choice == 5:
        print("This feature is not implemented")
        print("0. Go back")

        try:
            choice_menu5 = int(input())
        except KeyError:
            print("\n\nWrong option NOOB!\n"
                  "Are you trying to cheat?\n\n")
            main_menu()
        if choice_menu5 == 0:
            main_menu()

    if choice == 0:
        print("Shuuuutingggg doooown!")
        exit(0)

#def login


if __name__ == "__main__":
    main_menu()
