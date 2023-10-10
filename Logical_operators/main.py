# Logical Operators in Python

# and :
temp = 25

if temp > 0 and temp < 30:
    print("the temperature is good")
else:
    print("the temperature is bad")

# > the temprature is good

temp = -10

if temp > 0 and temp < 30:
    print("the temperature is good")
else:
    print("the temperature is bad")

# > the temperature is bad

temp = 40

if temp > 0 and temp < 30:
    print("the temperature is good")
else:
    print("the temperature is bad")

# > the temperature is bad

# or :

temp = 40

if temp > 0 or temp < 30:
    print("the temperature is good")
else:
    print("the temperature is bad")

# > the temperature is good

temp = 40

if temp <= 0 and temp >= 30:
    print("the temperature is bad")
else:
    print("the temperature is good")

# > the temperature is bad

# not :

temp = 20
sunny = False # today is sunny outside :)

if temp <= 0 and temp >= 30:
    print("the temperature is bad")
else:
    print("the temperature is good")

if not sunny == True: # or if sunny:
    print("it is cloudy outside")
else:
    print("it is sunny outside")
# > the temperature is bad
# > it is sunny outside