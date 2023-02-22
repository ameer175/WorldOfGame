from Live import load_game,welcome
username = input("enter your UserName: ")
print(welcome(username))
Difficulty,Yourgame = load_game()
if(Yourgame == 1):
    from MemoryGame import play
    from Score import add_score
    if(play((Difficulty))):
        print("You win")
        add_score(Difficulty)
    else:
        print("You lose")
elif(Yourgame == 2):
    from GuessGame import play
    from Score import add_score
    if (play((Difficulty))):
        print("You win")
        add_score(Difficulty)
    else:
        print("You lose")
elif(Yourgame == 3):
    from CurrencyRouletteGame import play
    from Score import add_score
    if (play((Difficulty))):
        print("You win")
        add_score(Difficulty)
    else:
        print("You lose")
