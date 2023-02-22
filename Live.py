def welcome(name):
    str = "Hello" + " " + name + " " + "and welcome to the World of Games (WoG), Here you can find many cool games to play."
    return str

def load_game():
    print("Please choose a game to play:  ")
    print("1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back  ")
    print("2.Guess Game - guess a number and see if you chose like the computer  ")
    print("3.Currency Roulette - try and guess the value of a random amount of USD in ILS  ")
    try:
        your_game = int(input("chose your game please:"))
        Level_Of_Difficulty = int(input("Please choose game difficulty from 1 to 5: "))

        if(your_game >= 1 and your_game <=3):
            if(Level_Of_Difficulty >= 1 and Level_Of_Difficulty <= 5):
                print("----------------------------------")
                print("your game is: ", your_game)
                print("your level is: ",Level_Of_Difficulty)
                print("----------------------------------")
            else:
                print("try again!!, your input incorrect!, chose difficulty from 1 to 5")
        else:
            print("try again!!, your input incorrect!, chose game from 1 to 3")
    except Exception as inst:
        print("----------------------------------\n", "the Type Error is: ", type(inst), "try again\n","----------------------------------")
        load_game()




    return Level_Of_Difficulty,your_game


