import csv

def city_info(list_input):
    '''The function returns the 'Description' and 'Highlights' values from the csv file Dictionary based on the list of cities
       Parameter: A list of cities to be compared against the Disctionary
       Return: Prints the information stored in the csv file
    '''
    
    field1 = "Description"
    field2 = "Highlights"

    user_info = csv.DictReader(open("locations.csv"))

    for row in user_info:
        for i in range(len(list_input)):
            if row["City"] == list_input[i]:
                print(list_input[i])
                print(field1)  
                print(row[field1] + "\n") 
                print(field2) 
                print(row[field2] + "\n\n")
#            elif list_input[i] not in user_info:
#                print(list_input[i], "is not included in the database. Please send in a request to have it added for future searches.")

