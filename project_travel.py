from function_banner import banner
from function_welcome_menu import welcome_menu
from function_location_search import location_search
from function_selected_city_list import selected_city_list
from function_city_info import city_info

def main():
    '''The program launches the Travel recommendation application. The user is first required to enter personal information, which
       creates/initializes a Traveller class and includes it in the "username.txt" database - to ensure that there is a unique user
       in the application.
    '''
    owner = "Jean Paul"
    
    #launches the banner function with the owner specified in the initial variable
    banner(owner)
    print()
    
    #launches the welcome menu function and prompts the user to make a selection in order to progress in the program
    welcome_menu()
    print()
    
    #launches the database search function and prompts the user to navigate through the list of items in the database
    location_search()
    
    list_input = selected_city_list()
    city_info(list_input)

    print("Thank you for using the program. We will see you soon. Safe travels!")


main()