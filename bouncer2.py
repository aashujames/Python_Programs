print("How old are you?")
age = input()
if age != "":
    age = int(age)
    if age>=18 and age<21:
        print("You can enter but need a wristband.")
    elif age>=21:
        print("You are good to go and can drink.")
    else:
        print("You are not allowed kid!")
else:
    print("Enter an age please!")