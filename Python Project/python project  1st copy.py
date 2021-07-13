# DONE s#Hello, Welcome to S&G's cenima! Type Hey to see the available services!
# DONE s# 1-List of movies + Age requirement
# DONE s# 2-Ehtraz if vaccinated y if not vaccinated print "sorry you cannot access the cenima"
# DONE s# 3-List of movie showtime (each movie printed with it's showtime)
# g# 4-if age >13 not allowed without parent quardian if age 18=< print please choose seat
# DONE s# 5-list = available seats, row a n/ row n/
# DONE s# 6-print the seat chosen (seat A3) (it will be deleted from the og list)
# DONE g# 7-available food (butter popcorn caramel popcorn, cheese popcorn, nachos, hotdog, fries, slush, water, coca cola, sprite )
# DONE g# 8-do you want the food delivered to your seat or pickup.
# DONE g# Thank you, enjoy your movie

# Movie names: The purge | Cruella | The Conjouring
# Seat list: A1-A5 | B1-B5 | C1-C5 | D1-D5

Movies = ["The purge" , "\nCruella" , "\nThe Conjouring"]

showtimes = ["The purge showtimes: \n-12:45 \n-3:00 \n-5:30 \nCruella showtimes: \n-6:15 \n-7:45 \n-8:25 \nThe Conjouring showtimes: \n-5:15 \n-13:45 \n-20:30"]

seats = ["A1" , "A2" , "A3" , "A4" , "A5" , "\nB1" , "B2" , "B3" , "B4" , "B5" , "\nC1" , "C2" , "C3" , "C4" , "C5" , "\nD1" , "D2" , "D3" , "D4" , "D5"]


FoodandDrinks = ["FOOD: \nButter Popcorn" , "Caramel Popcorn" , "Cheese Popcorn" , "Nachos" , "Hotdog" , "Fries" , "\nDRINKS: \nSlushy" , "Water" , "Coca Cola" , "Sprite"]

ChosenSeat = []

ChosenMovie = []

ChosenFoodandDrink = []

name = input("Welcome to S&G's Cenima, what's your name? ")

command = input(f"Hello {name}, How may we assist you? \n(type 'help' to see the possible services!) ")

while command!="exit":

    if command == "Movies":
        for movie in Movies:
            print(movie)

    elif command == "EHTERAZ":
        confirm = input("Are you vaccinated? Y/N? ")
        if confirm == "Y":
            print("Great, Welcome!")
        if confirm == "N":
            print("Sorry :( , You are not allowed in the cenima.")

    elif command == "Showtimes":
        for showtime in showtimes:
            print(showtime)

    elif command == "Seats":
        for seat in seats:
            print(seat)

    elif command == "Food.Drinks":
        for fooddrink in FoodandDrinks:
            print(fooddrink)

    elif command == "FoodDelivery":
        confirm = input("Do you want the food delivered to your seat or do you want to pick it up?")
        if confirm == "seat delivery":
            print("Your food will be delivered to your seat!")
        if confirm == "pickup":
            print("Your food is ready for pickup!")

    elif command == "MovieChosen":
        chose=input("Which Movie did you decide on? ")
        if chose in Movies:
            ChosenMovie.append(chose)

    elif command == "SeatChosen":
        chose=input("Which seat did you decide on? ")
        if chose in seats:
            ChosenSeat.append(chose)
            seats.remove(chose)

    elif command == "ChosenFoodandDrink":
        choice=input("What would you like to eat and drink? ")
        if choice in FoodandDrinks:
            ChosenFoodandDrink.append(choice)

    elif command == "Ticket":
        print(ChosenMovie)
        print(ChosenSeat)
        print(ChosenFoodandDrink)


    elif command == "help":
        print("Movies: Prints the list of movies \nMovieChosen: Choose a movie \nEHTERAZ: Asks if you are vaccinated or not \nShowtimes: Prints movie showtimes \nSeats: Prints all seats available \nSeatChosen: Allows you to choose a seat \nFood.Drinks: Prints the list of food and drinks available \nChosenFoodandDrink: Allows you to choose your food and drink \nFoodDelivery: Allows you to choose to either pickup or get your food delivered to your seat \nTicket: Prints your chosen movie, seat and food \nExit: You Exit the program.")


    elif command == "exit":
        print("Thank you, Enjoy your movie!")

    command = input("Okay, what Next? ")

