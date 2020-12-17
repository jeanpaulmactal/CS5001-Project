def create_city_list():

    city_list = []
    MAXIMUM_NUMBER_OF_CITIES = 5

    print("\nYou can look up information for up to 5 cities. If you enter more than 5 cities the last entry will be discarded from your list. \n")
    store = input("Would you like to add a city in your list? Please indicate 'Yes' or 'No': ")
    store = store.lower().strip()
    print()

    while store  == "" or store.isnumeric() == True:
        store = input("Only 'Yes' or 'No' are valid entries - please indicate 'Yes' or 'No': ")
        store = store.lower().strip()
        print()

    while store == "yes" or store == "y":
        if len(city_list) < MAXIMUM_NUMBER_OF_CITIES:
            selected_city = input("Please enter the city you would like additional information on: ")
            selected_city = selected_city.capitalize().strip()
            print()
            
            while selected_city  == "" or selected_city.isnumeric() == True:
                selected_city = input("Please enter a valid city: ")
                selected_city = selected_city.capitalize().strip()
                print()
            city_list.append(selected_city)

            
        elif len(city_list) >= MAXIMUM_NUMBER_OF_CITIES:
            print("You have reached the maximum number of cities. Adding another will remove your last choice. \n")
            remove = input("Add another city anyway. Please indicate 'Yes' or 'No': ")
            print()
            
            if remove  == "" or remove.isnumeric() == True:
                remove = input("Please enter either 'Yes' or 'No': ")
                remove = remove.lower().strip()
                print()
            
            elif remove == "Yes" or remove == "yes" or remove == "Y" or remove == "y":
                city_list.pop(4)
                selected_city = input("Please enter the city you would like additional information on: ")
                print()
                
                while selected_city  == "" or selected_city.isnumeric() == True:
                    selected_city = input("Please enter a valid city: ")
                    selected_city = selected_city.capitalize().strip()
                    print()
                city_list.append(selected_city)
        
        store = input("Would you like to add another city in your list? Please indicate 'Yes' or 'No': ")
        store = store.lower().strip()
        print()
        
        while store  == "" or store.isnumeric() == True:
            store = input("Only 'Yes' or 'No' are valid entries - please indicate 'Yes' or 'No': ")
            store = store.lower().strip()
            print()
    
    if store == "no" or store == "n" and len(city_list) == 0:
        print("Thank you for using the program and come visit again in the future. \n")
    
    else:
        print("That was not a valid city. Thank you for visiting. \n")
    
    return city_list