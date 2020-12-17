import csv

def location_total():

    user_info = csv.DictReader(open("locations.csv"))
    count = 0

    for row in user_info:
        count += 1

    return count

def location_continent():
    
    user_info = csv.DictReader(open("locations.csv"))
    list_continent = []

    for row in user_info:
        unique_location = row["Continent"]
        if unique_location not in list_continent:
            list_continent.append(unique_location)
    
    return list_continent


def location_country():
    
    user_info = csv.DictReader(open("locations.csv"))
    list_country = []

    for row in user_info:
        unique_location = row["Country"]
        if unique_location not in list_country:
            list_country.append(unique_location)
    
    return list_country


def location_province():
    
    user_info = csv.DictReader(open("locations.csv"))
    list_province = []

    for row in user_info:
        unique_location = row["Province"]
        if unique_location not in list_province:
            list_province.append(unique_location)
    
    return list_province


def location_city():
    
    user_info = csv.DictReader(open("locations.csv"))
    list_city = []

    for row in user_info:
        unique_location = row["City"]
        if unique_location not in list_city:
            list_city.append(unique_location)
    
    return list_city
