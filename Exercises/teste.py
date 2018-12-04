import random

menu_actions = {}



def main_menu():

    print("\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("||||>>The World Of Evernothing<<||||")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("++++++++++++++++++++++++++++++++++++")
    print("++just an other hack and slash RPG++")
    print("++++++++++++++++++++++++++++++++++++")
    print(" ")
    print(" ")
    print("1. New Game")
    print("2. How to")
    print("3. Social stuff")
    print("0. Exit")
    print(" ")
    print(" ")
    choice = input("Choose your way NooB! : ")
    exec_menu(choice)

    return


def exec_menu(choice):
    ch = choice.lower()
    if ch == '':
        menu_actions[ch]()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Wrong option NOOB. Are you trying to cheat?\n")
            menu_actions['main_menu']()
    return



def menu1():
    print("What the hec are you looking for?")
    print("9. Back")
    print("0. Exit")
    choice = input(">>  ")
    exec_menu(choice)
    return



def menu2():
    print("Not yet implemented")
    print("9. Back")
    print("0. Exit")
    choice = input(">>  ")
    exec_menu(choice)
    return



def menu3():
    print("Not yet implemented")
    print("9. Back")
    print("0. Exit")
    choice = input(">>  ")
    exec_menu(choice)
    return

def back():
    menu_actions['main_menu']()



#def exit():
    #sys.exit()



menu_actions = {
    'main_menu': main_menu,
    '1': menu1,
    '2': menu2,
    '3': menu3,
    '9': back,
    '0': exit,
}


if __name__ == "__main__":
    main_menu()
