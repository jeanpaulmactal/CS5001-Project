from function_new_user import create_user
from function_validate import valid_user
from function_validate import valid_password
from function_update_user_list import update_user_list

def welcome_menu():

    MAX_PASSWORD_ATTEMPTS = 5

    user = input("Select an option: \n" + 
                 "\n1 Registered user (r)" + 
                 "\n2 New user (n)" + 
                 "\n3 Guest (g) \n" + 
                 "\nSelection: ")
    user = user.lower()

    #if the user enters anything else other than "r" or "n", the program will continue to prompt the user for
    #the correct by repeating the same question using a WHILE loop.  
    while user != "r" and user != "n" and user!= "g":
        user = input("\nAre you a registered user (r), a new user (n), or a guest (g)? ")
        user = user.lower()

    if user == "g":
        #a guest using the program will be welcomed to the platform
        print("\nWelcome guest! \n")

    elif user == "n":
        #a new user profile is created for the user
        new_user = create_user()
        update_user_list(new_user)
        print("\nWelcome", new_user.get_fullname(), "\n")
    
    else:
        #the conditional tests for a valid username registered in the active user dictionary - if the username is valid, the user is prompted to 
        #the correct passowrd in order to proceed
        registered = input("\nPlease enter your username: ")
        if valid_user(registered)== True:
            print("\nWelcome back", registered, "\n")
            password = input("Please enter your password: ")
            if valid_password(password) == False:
                attempts = MAX_PASSWORD_ATTEMPTS
                #if the user enters the incorrect password, the conditional loop will prompt the user to re-enter the password up to the MAXIMUM
                #number of attempts (defined above). If the maximum number of attempts is reached, the program terminates.
                while valid_password(password) == False:
                    if attempts > 0:
                        password = input("\nPassword incorrect. You have " + str(attempts) + " attempts remaining. Please enter your password: ")
                        attempts -= 1
                    else:
                        print("\nMaximum attempts reached. Please contact administrator for immediate access or return after 24 hours. Goodbye for now. \n")
                        break
        
        else:
            new_choice = input("\nThe username entered is invalid - would you like to restart (r) or quit (q)? ")
            print()
            while new_choice != "r" and new_choice!= "q":
                new_choice = input("Would you like to restart (r) or quit (q)? ")
                new_choice = new_choice.lower()
                print()

            if new_choice == "r":
                welcome_menu()

            else:
                print("\nThank you for visiting. Hope to see you again in the future. \n")
                quit()