# Strings

print("hello")
print('hello')

# Assign String to a Variable:

a = "Hello"
print(a)

# Multiline Strings:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# len():

a = "Hello, World!"
print(len(a))

# Check String:

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

# upper():
a = "Hello, World!"
print(a.upper())

# lower():
a = "Hello, World!"
print(a.lower())

# strip():
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!


# replace():
a = "Hello, World!"
print(a.replace("H", "J"))

# split():
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

