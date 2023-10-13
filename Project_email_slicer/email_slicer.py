# Python email slicer

email = input("Enter your email: ")

# There is a built in method called string.index[c]
# that find the character and returns the instance of it
index = email.index("@") # it returns a number

username = email[:index]

domain = email[index + 1:]

print(f"Your username is {username} and the Domain is {domain}")
