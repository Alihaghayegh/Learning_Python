# Python temprature converter

unit = input("Is this temprature in Celsius or Fahrenheit? (C/F)")
temp = float(input("Enter the temprature: "))

if unit == 'C':
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temprature in Fahrenheit is: {temp}° F")
elif unit == 'F':
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The temprature in Celsius is: {temp}° C")
else:
    print(f"{unit} is an invalid unit of measurment!")

# For ° :
# On Windows : Alt + 0176 and space
# On linux : hold ctrl + shift + u and release and type 00b0 and press space
# On Mac : shift + option + 8
