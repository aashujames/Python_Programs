# import random
# #print("rock\npaper\nscissor")

# player = input("Player make your move:")
# rand_num = random.randint(0,2)
# if rand_num == 0:
#     computer = 'rock'
# elif rand_num == 1:
#     computer = 'paper'
# else:
#     computer = 'scissor'    

# print(f"computer plays {computer}")

# if player == computer:
#     print("Tie!")
# elif player == "rock":
#     if computer == "paper":
#         print("computer wins!")
#     else:
#         print("player wins!")
# elif player == "paper":
#     if computer == "scissor":
#         print("computer wins!")
#     else:
#         print("player wins!")
# elif players == "scissor":
#     if computer == "rock":
#         print("computer wins!")
#     else:
#         print("player wins!")
# else:
#     print("something wrong!!")
    



#looping version
import random

player_w = 0
comp_w=0
winsc=3   #best of 3
while player_w<winsc and comp_w<winsc:
    print(f"Player Score: {player_w}  Computer Score: {comp_w}")
    print("rock..\npaper..\nscissor..")
    player = input("Player make your move:")
    rand_num = random.randint(0,2)
    if rand_num == 0:
        computer = 'rock'
    elif rand_num == 1:
        computer = 'paper'
    else:
        computer = 'scissor'    

    print(f"computer plays {computer}")

    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer wins!")
            comp_w += 1
        else:
            print("player wins!")
            player_w += 1
    elif player == "paper":
        if computer == "scissor":
            print("computer wins!")
            comp_w += 1
        else:
            print("player wins!")
            player_w += 1
    elif player == "scissor":
        if computer == "rock":
            print("computer wins!")
            comp_w += 1
        else:
            print("player wins!")
            player_w += 1
    else:
        print("something wrong!!")
if player_w > comp_w:
    print("Congo You Win")
else:
    print("Lol Computer Wins")
print(f"Final scores.... Player:{player_w} Computer:{comp_w}")
    