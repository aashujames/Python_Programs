print("rock\npaper\nscissor")

player1 = input("P1 make your move:")
print("**No Cheating**\n\n"*20)
player2 = input("P2 make your move:")

if player1 == player2:
    print("Tie!")
elif player1 == "rock":
    if player2 == "paper":
        print("player 2 wins!")
    elif player2 == "scissor":
        print("player 1 wins!")
elif player1 == "paper":
    if player2 == "scissor":
        print("player 2 wins!")
    elif player2 == "rock":
        print("player 1 wins!")
elif player1 == "scissor":
    if player2 == "rock":
        print("player 2 wins!")
    elif player1 == "paper":
        print("player 1 wins!")
else:
    print("something wrong!!")
    