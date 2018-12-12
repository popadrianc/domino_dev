check = ["X", "admin", "Q"]
def data():
    input("This is a registration form. Press Enter to continue")
    username = str(input("Set a Username: "))
    if (username in check) == True:
         print("Invalid username")
         data()
    else:
        password = input("Set a Passowrd: ")
        input("Press enter to login...")
        previoususername = str(input("Enter your username: "))
        previouspassword = input("Enter your Password: ")
    if (previoususername == username and previouspassword == password):
        print("Login successfully")
        check.append(username)
        data()
    elif (previoususername != username and previouspassword == password):
        print ("The username you have entered is incorrect. Please check again and write it correctly!")
        data()
    elif (previoususername == username and previouspassword != password):
        print("The password that you have entered is not correct. Please check again and write it correctly! ")
        data()
    else:
        print("Authentification has failed. An Administrator will be announced about this!")
        data()
data()