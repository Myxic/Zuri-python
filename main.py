def rPs_game(your_name="Player 2"):
    global h1
    import random
    print("Game Time", "R is Rock", "S is Scissor", "P is Paper", "Have fun", sep="\n", end='\n')
    j = ["R", "P", "S", "ROCK", "PAPER", "SCISSOR"]
    t = ["Rock", "Paper", "Scissor"]
    while True:
        h = input("Rock, Paper, Scissor(choose one or just their first letter)>: ")
        if h[0].upper() == "R":
            h1 = "Rock"

        elif h[0].upper() == "S":
            h1 = "Scissor"

        elif h[0].upper() == "P":
            h1 = "Paper"

        if h.upper() in j:
            c = random.choice(t)

            print(f"{your_name}(you): {h1}")
            print(f"Player 1: {c}")

            if h1 == "Rock" and c == "Scissor" or h1 == "Scissor" and c == "Paper" or h1 == "Paper" and c == "Rock":
                return "you win"

            elif c == "Rock" and h1 == "Scissor" or c == "Scissor" and h1 == "Paper" or c == "Paper" and h1 == "Rock":
                print("you lose")
                # for sore losers :) who don't like losing lol
                tie = input("Do you want to continue Y OR N >: ")
        # we need some protection for the code so if not y (letter casing don't matter) the code will break or stop
                if tie.upper() == "Y":
                    print("Okay")

                else:
                    return "Nice game"

            else:
                print("Tie")
                # a game should be win or lose :)
                tie = input("Do you want to continue Y OR N >: ")
                # same code as that in lose
                if tie.upper() == "Y":
                    print("Okay")

                else:
                    return "Nice game"

        else:
            print("Enter Either R or P or S")


# Remember to add your name although it doesn't matter since a default was already placed
print(rPs_game("Ben"))
