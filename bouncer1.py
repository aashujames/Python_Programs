print("How old are you?")
age = input()
if age == "":
    print("Enter an age please!")
elif int(age)>=18 and int(age)<21:
    print("You can enter but need a wristband.")
elif int(age)>=21:
    print("You are good to go and can drink.")
else:
    print("You are not allowed kid!")