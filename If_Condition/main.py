# if condition

age = int(input("Enter your age: "))


if age >= 18:
    print("You are now signed up")


if age >= 18:
    print("You are now signed up")
else:
    print("You most be 18+ to sign up")


if age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You most be 18+ to sign up")


if age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet!")
elif age >= 100:
    print("You are too old to sign up")
else:
    print("You most be 18+ to sign up")


if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You most be 18+ to sign up")


# Another example:

response = input("Would you like food?: (Y/N)")

if response == "Y":
    print("Have some food")
else:
    print("No food for you")


# for booleans

for_sale = True

if for_sale:
    print("This iten is for sale")
else:
    print("This item is NOT for sale")