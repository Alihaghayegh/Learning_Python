# User input

input()                             # Without any prompt
input("What's your name...???")     # With prompt


name = input("What's your name...???")

print(name)

# Let's beautify our response
print(f"Hello {name}")


# Let's go for somebodys age
age = input("Enter your age: ")

print(f"You are {age} years old.")

# Error on type of output
age = input("Enter your age: ")
age = age + 1  
print(f"You are {age} years old.")  # It will get Type Error


# casting the type of input
age = input("Enter your age: ")
age = int(age)
age = age + 1  
print(f"You are {age} years old.")


# one liner type casting
age = int(input("Enter your age: "))
age = age + 1  
print(f"You are {age} years old.")
