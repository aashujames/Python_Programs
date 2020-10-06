# import random

# random_no = random.randint(1,10)
# guess = ''

# while guess != random_no:
#     guess=input("Pick a number from 1 to 10:")
#     guess=int(guess)
#     if guess == random_no:
#         print("You got it!")
#     elif guess < random_no:
#         print("Too low")
#     else:
#         print("too high")
# print(random_no)


# my advance version
import random

random_no = random.randint(1,10)
guess = ''
while guess != random_no:
    guess=input("Pick a number from 1 to 10:")
    guess=int(guess)
    if guess == random_no:
        print("You got it!")
    elif guess < random_no:
        print("Too low")
    else:
        print("too high")
print(random_no)
while True:
    random_no = random.randint(1,10)
    play= input("wanna play again? Y/N: ")
    if play == "Y":
        
        guess= ''
        while guess != random_no:
            guess=input("Pick a number from 1 to 10:")
            guess=int(guess)
            if guess == random_no:
                print("You got it!")
            elif guess < random_no:
                print("Too low")
            else:
                print("too high")
    else:
        print("Ok bye!!")
        break

# alternative version

# import random

# random_no = random.randint(1,10)

# while True:
#     guess=input("Pick a number from 1 to 10:")
#     guess=int(guess)
#     if guess > random_no:
#         print("Too high")
#     elif guess < random_no:
#         print("Too low")
#     else:
#         print("You Win!!")
#         print(random_no)
#         play = input("Do you wanna play again? (y/n):")
#         if play == 'y':
#             random_no = random.randint(1,10)
#             guess=None
#         else:
#             print("Ok bye!")
#             break

    