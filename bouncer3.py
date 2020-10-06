print("How old are you?")
age = input()
if age:
    age = int(age)
    if age>=21:
        print("You are good to go and can drink.")
    elif age>=18:
        print("You can enter but need a wristband.")
    else:
        print("You are not allowed kid!")
else:
    print("Enter an age please!")