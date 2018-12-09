import sys  # this allows you to use the sys.exit command to quit/logout of the application


def main():
    login()
    register()


def login():
    username = "formtutor"
    password = "teacherypass"
    print("Enter username : ")
    answer1 = input()
    print("Enter password : ")
    answer2 = input()
    if answer1 == username and answer2 == password:
        print("Welcome - Access Granted")
        menu()

#def register():
    #create_user = raw_input("Enter your username")
    #type(create_user)

def menu()

def menu2():
    print("************MAIN MENU**************")
    # time.sleep(1)
    print()

    choice = input("""
                      1. Enter Student details
                      2. View Student details
                      3. Search by ID number
                      4. Produce Reports
                      5. Quit/Log Out

                      Please enter your choice: """)

    if choice == "1":
        enterstudentdetails()
    elif choice == "2":
        viewstudentdetails()
    elif choice == "3":
        searchbyid()
    elif choice == "4":
        producereports()
    elif choice == "5":
        exit()
    else:
        print("You must only select either A,B,C, or D.")
        print("Please try again")
        menu()


def enterstudentdetails():
    pass
    # Teacher will enter student details manually
    # These will be appended to the csv file


def viewstudentdetails():
    pass


# Teacher can press a button to view all students at a glance

def searchbyid():
    pass
    # Teacher can input an ID number and display the relevant student's details


def producereports():
    pass
    # Teacher can produce clever reports such as:
    # a) list of names of males and email addresses (to email a reminder about boys football club)
    # b) list of names of females in specific postcode (to remind them of a girls coding club in the area)
    # c) list of all names, birthdays and addresses (to send out birthday cards!)


# the program is initiated, so to speak, here
main()
