# While Loops in python

**`while loop`** : execute some code WHILE some condition remains true

let's say : 
```python
name = input("Enter your name: ")

if name == "" :
    print("You did not enter your name")
else:
    print(f"Hello {name}")
```

what if we want to continuously prompt user for name...???

then here is a while loop:
```python
name = input("Enter your name: ")

while name == "" :
    print("You did not enter your name")
    name = input("Enter your name: ")

print(f"Hello {name}")
```