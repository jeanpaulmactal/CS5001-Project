from function_create_city_list import create_city_list

def selected_city_list():

    print("\nAre you interested on descriptions and highlights and recommendations in any of the cities listed?") 
    print("As a reminder, only the cities will have descriptions and highlights and recommendations.\n")
    create_list = input("Please indicate 'Yes' or 'No': ")
    create_list = create_list.lower().strip()

    while create_list == "" or create_list.isnumeric() == True:
        create_list = input("\nOnly 'Yes' or 'No' are valid entries. Please indicate either 'Yes' or 'No': ")
        create_list = create_list.lower().strip()

    if create_list == "yes" or create_list == "y":
        selected_city_list = create_city_list()

    elif create_list == "no" or create_list == "n":
        print("\nThank you for using the program and we will see you in the near future. Bon voyage! \n")
        quit()
    
    else:
        print("\nYou entered an invalid entry - only 'Yes' or 'No' can be entered.\n")
        continuation = input("If you want to start over - enter 'Continue' otherwise, the program will terminate: ")
        continuation = continuation.lower().strip()

        if continuation == "continue" or continuation == "yes" or continuation == "y":
            selected_city_list()
        
        else:
            print("\nBon voyage!!! A bientot!!!\n")
            quit()

    return selected_city_list
