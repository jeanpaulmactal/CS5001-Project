import csv
from function_location_counters import location_continent
from function_location_counters import location_country
from function_location_counters import location_province
from function_location_counters import location_city

def search_continent():
    list_continent = location_continent()
    print("There are", len(list_continent), "continents, specifically: \n")
    for i in range(len(list_continent)):
        print(i + 1, list_continent[i])
    print()


def search_country():
    list_country = location_country()
    print("There are", len(list_country), "countries, specifically: \n")
    for i in range(len(list_country)):
        print(i + 1, list_country[i])
    print()


def search_province():
    list_province = location_province()
    print("There are", len(list_province), "provinces or states, specifically: \n")
    for i in range(len(list_province)):
        print(i + 1, list_province[i])
    print()


def search_city():
    list_city = location_city()
    print("There are", len(list_city), "cities, specifically: \n")
    for i in range(len(list_city)):
        print(i + 1, list_city[i])
    print()


def secondary_search():

    continuation = input("Would you like to search for a different category? Please indicate 'Yes' or 'No': ") 
    continuation = continuation.lower().strip()
    print()
    
    while continuation  == "" or continuation.isnumeric() == True:
        continuation = input("Only 'Yes' or 'No' are valid entries - please indicate 'Yes' or 'No': ")
        continuation = continuation.lower().strip()
        print()
 
    if continuation == "yes" or continuation == "y":
        selection = input("Please specify - continent, country, province or state, or city: ")
        selection = selection.lower().strip()

        if selection == "continent" or selection == "continents":
            search_continent()

        elif selection == "country" or selection == "countries":
            search_country()
        
        elif selection == "province" or selection == "provinces" or selection == "state" or selection == "states":
            search_province()
        
        elif selection == "city" or selection == "cities":
            search_city()
    
        else:
            choice = input("You did not enter a valid selection. If you want to continue, type 'Continue', otherwise, the program will terminate. ")
            choice = choice.lower().strip()

            if choice == "continue":
                print()
                secondary_search()
        
            else:
                print("Thank you for searching out list. \n")
        
        secondary_search()

    elif continuation == "no" or continuation == "n":
        print("\nHopefully, you got some helpful information. \n")
    
    else:
        print("\nThat was not a valid entry. Thank you for visiting. \n")
        quit()


def location_search():

    print("Where shall we go today? You can search the database by entering a continent, country, state or province, or city.\n")
    print("Only the cities will have a detailed description and highlights or recommendation. \n")
    selection = input("Where should we start your journey? Please indiciate continent, country, province or state, or city: ")
    selection = selection.lower().strip()
    print()
    
    while selection  == "" or selection.isnumeric() == True:
        selection = input("Enter a starting point - continent, country, province or state, or city: ")
        selection = selection.lower().strip()
        print()

    if selection == "continent" or selection == "continents":
        search_continent()
        secondary_search()

    elif selection == "country" or selection == "countries":
        search_country()
        secondary_search()
        
    elif selection == "province" or selection == "provinces" or selection == "state" or selection == "states":
        search_province()
        secondary_search()

    elif selection == "city" or selection == "cities":
        search_city()
        secondary_search()
    
    else:
        continuation = input("You did not enter a valid selection. If you want to continue, type 'Continue', otherwise, the program will terminate. ")
        continuation = continuation.lower().strip()

        if continuation == "continue" or continuation == "c":
            print()
            location_search()
        
        else:
            print("\nThank you for stopping by today. We hope to see you again in the near future. \n")
            quit()