"""Restaurant rating lister."""

def sorted_ratings(file_name):

    ratings = {}
    open_file = open(file_name)

    see_ratings = input("Would you like to see all the ratings?")
    if see_ratings == "yes" or see_ratings == "Yes" or see_ratings == "y" or see_ratings == "Y":
        return(see_all(file_name))

    add_restaurant = input("Would you like to add a new restaurant?")
    if add_restaurant == "yes" or add_restaurant == "Yes" or add_restaurant == "y" or add_restaurant == "Y":
        return(add_rest(file_name))

    if_quit = input("Would you like to quit?")
    if if_quit == "yes" or if_quit == "Yes" or if_quit == "y" or if_quit == "Y":
        return


def see_all(file_name):
    ratings = {}
    open_file = open(file_name)

    for line in open_file:
        line = line.strip()
        list_restaurant = line.split(":")
        ratings[list_restaurant[0]] = list_restaurant[1]

    for restaurant, rating in sorted(ratings.items()):
        print(f"{restaurant} is rated at {rating}.")
        

def add_rest(file_name):
    ratings = {}
    open_file = open(file_name)

    customer_restaurant = input("What is the restaurant name?")
    customer_score = input("What is the restaurant score?")

    try:
        if int(customer_score):
            customer_score = input("Please input score between 1 through 5")
    except: 
        customer_score = input("Please input numeric value for restaurant score.")
    
    if int(customer_score) < 1 or int(customer_score) > 5:
            customer_score = input("Please input score between 1 through 5")

    for line in open_file:
        line = line.strip()
        list_restaurant = line.split(":")
        ratings[list_restaurant[0]] = list_restaurant[1]
        
    ratings[customer_restaurant] = int(customer_score)

    for restaurant, rating in sorted(ratings.items()):
        print(f"{restaurant} is rated at {rating}.")

print(sorted_ratings("scores.txt"))


