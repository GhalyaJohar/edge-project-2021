Movies = ["The purge" , "Cruella" , "The Conjouring"]

ThePurgeShowtimes = ["The Purge Showtimes:" , "12:45","3:00","5:30","6:15","7:45","8:25"]

CruellaShowtimes = ["Cruella Showtimes:" , "12:45","3:00","5:30","6:15","7:45","8:25"]

TheConjouringShowtimes = ["The Conjouring Showtimes:","12:45","3:00","5:30","6:15","7:45","8:25" ]

seats = ["A1","A2","A3","A4","A5" , "B1","B2","B3","B4","B5" , "C1","C2","C3","C4","C5" , "D1","D2","D3","D4","D5"]

FoodandDrinks = ["FOOD:" , "Butter Popcorn" , "Caramel Popcorn" , "Cheese Popcorn" , "Nachos" , "Hotdog" , "Fries" , "DRINKS:" , "Slushy" , "Water" , "Coca Cola" , "Sprite"]

# ThePurgeAG = ("18+")
# CruellaAG = ("PG13")
# TheConjouringAG = ("18+")

ChosenSeat = []
ChosenMovie = []
ChosenShowtime = []
ChosenFoodandDrink = []

name = input("Welcome to S&G's Cenima, what's your name? ")

command = input(f"Hello {name}, How may we assist you? \n(type 'help' to see the possible services!) ")

while command!="exit":
    if command =="exit":
        print("Thank you, Enjoy your movie!")

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
        for showtime in ThePurgeShowtimes:
            print(showtime)
        for showtime in CruellaShowtimes:
            print(showtime)
        for showtime in TheConjouringShowtimes:
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

    elif command == "ChosenShowtime":
        choice=input("Which showtime is the most suitable for you? ")
        if choice in ThePurgeShowtimes:
            ChosenShowtime.append(choice)
        elif choice in CruellaShowtimes:
            ChosenShowtime.append(choice)
        elif choice in TheConjouringShowtimes:
            ChosenShowtime.append(choice)

    elif command == "Ticket":
        print("Ticket:")
        print(ChosenMovie)
        print(ChosenSeat)
        print(ChosenFoodandDrink)
        print(ChosenShowtime)

    # elif command == "AgeRequirements":

    elif command == "help":
        print("Movies: Prints the list of movies \nEHTERAZ: Asks if you are vaccinated or not \nShowtimes: Prints movie showtimes \nSeats: Prints all seats available \nFood.Drinks: Prints the list of food and drinks available \nFoodDelivery: Allows you to choose to either pickup or get your food delivered to your seat  \nMovieChosen: Choose a movie \nSeatChosen: Allows you to choose a seat \nChosenFoodandDrink: Allows you to choose your food and drink \nChosenShowtimes: Allows you to choose a showtime \nTicket: Prints your chosen movie, movieshowtime, seat and food \nexit: You Exit the program.")


    command = input("Okay, what Next? ")
