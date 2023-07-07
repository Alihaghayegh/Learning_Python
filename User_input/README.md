# User Input

**`Input`**: in this topic we gonna learn how we except some user input; it shows in the console and then the user can enter some input.

To get the user input we use `input()` function and within the parantheses we can type our prompt to show to the user :

```python
input()                             # Without any prompt
input("What's your name...???")     # With prompt
```

When you run this with input, the program will pause in the console window until we type some input and hit enter.

when you use the `input()` lonely, after you hit enter you see nothing happened. maybe we should store the input somewhere. how about inside a variable...???

```python
name = input("What's your name...???")

print(name)

# Let's beautify our response
print(f"Hello {name}")


# Let's go for somebodys age
age = input("Enter your age: ")

print(f"You are {age} years old.")
```

Note that the output of `input()` function is always `string data type`. so we can not do this:
```python
age = input("Enter your age: ")
age = age + 1  
print(f"You are {age} years old.")  # It will get Type Error
```
To solve this, we can cast the output to what ever we want:
```python
age = input("Enter your age: ")
age = int(age)
age = age + 1  
print(f"You are {age} years old.")
```

Let's do it in one line of code:
```python
age = int(input("Enter your age: "))
age = age + 1  
print(f"You are {age} years old.")
```

and that's how we except the user input.