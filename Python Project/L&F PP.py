Movies = ["The purge" , "Cruella" , "The Conjouring"]

ThePurgeShowtimes = ["The Purge Showtimes:" , "12:45","3:00","5:30","6:15","7:45","8:25"]

CruellaShowtimes = ["Cruella Showtimes:" , "12:45","3:00","5:30","6:15","7:45","8:25"]

TheConjouringShowtimes = ["The Conjouring Showtimes:","12:45","3:00","5:30","6:15","7:45","8:25" ]

seats = ["A1","A2","A3","A4","A5" , "B1","B2","B3","B4","B5" , "C1","C2","C3","C4","C5" , "D1","D2","D3","D4","D5"]

FoodandDrinks = ["FOOD:" , "Butter Popcorn" , "Caramel Popcorn" , "Cheese Popcorn" , "Nachos" , "Hotdog" , "Fries" , "DRINKS:" , "Slushy" , "Water" , "Coca Cola" , "Sprite"]

ThePurgeAG = ["The Purge Age requirements:","18+"]
CruellaAG = ["Cruella Age requirements:","No age requirements"]
TheConjouringAG = ["The Conjouring Age requirements:","18+"]

CSeat = []
CMovie = []
CShowtime = []
ChosenFoodandDrink = []

movies_18 = ["The purge","The Conjouring"]

name = input("Welcome to S&G's Cinema, what's your name? ")

command = input(f"Hello {name}, How may we assist you? \n(type 'help' to see the possible services!) ")

while command!="exit":
    if command == "Movies":
        for movie in Movies:
            print(movie)

    elif command == "V":
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

    elif command == "AG":
        for Purge in ThePurgeAG:
            print(Purge)
        for Cruella in CruellaAG:
            print(Cruella)
        for Conj in TheConjouringAG:
            print(Conj)

    elif command == "Seats":
        for seat in seats:
            print(seat)

    elif command == "FD":
        for fooddrink in FD:
            print(fooddrink)

    elif command == "FDel":
        confirm = input("Do you want the food delivered to your seat or do you want to pick it up? ")
        if confirm == "seat delivery":
            print("Your food will be delivered to your seat!")
        if confirm == "pickup":
            print("Your food is ready for pickup!")

    elif command == "Cmovie":
        chose=input("Which Movie did you decide on? ")
        if chose in Movies:
            if chose in movies_18:
                age=input("This movie is +18, How old are you? ")
                if int (age) >= 18 :
                  CMovie.append(chose)
                else :
                  print("Sorry, you are not allowed in")

    elif command == "Cseat":
        chose=input("Which seat did you decide on? ")
        if chose in seats:
            CSeat.append(chose)
            seats.remove(chose)

    elif command == "Cfood":
        choice=input("What would you like to eat? ")
        if choice in FoodandDrinks:
            ChosenFoodandDrink.append(choice)

    elif command == "Cdrink":
        choice=input("What would you like to drink? ")
        if choice in FoodandDrinks:
            ChosenFoodandDrink.append(choice)

    elif command == "Cshowtime":
        choice=input("Which showtime is the most suitable for you? ")
        if choice in ThePurgeShowtimes:
            CShowtime.append(choice)
        elif choice in CruellaShowtimes:
            CShowtime.append(choice)
        elif choice in TheConjouringShowtimes:
            CShowtime.append(choice)


    elif command == "Ticket":
        print("Ticket:")
        print(CMovie)
        print(CSeat)
        print(ChosenFoodandDrink)
        print(CShowtime)


    elif command == "help":
        print("Movies: Prints the list of movies \nV: Asks if you are vaccinated or not \nAG: Shows the age requirement for each movie \nShowtimes: Prints movie showtimes \nSeats: Prints all seats available \nFD: Prints the list of food and drinks available \nFDel: Allows you to choose to either pickup or get your food delivered to your seat  \nCmovie: Choose a movie \nCseat: Allows you to choose a seat \nCfood: Allows you to choose your food \nCdrink: Allows you to choose your drink\nCshowtime: Allows you to choose a showtime \nTicket: Prints your chosen movie, movieshowtime, seat and food \nexit: You Exit the program.")

    command = input("Okay, what Next? ")

    if command =="exit":
        print("Thank you, Enjoy your movie!")