# If Condition

`if` : do some code only `if` some condition is True, Else do something else.

`It's a basic form of decision making.`

let's say:
```python
age = int(input("Enter your age: "))
```

let's pretend that the user wants to sign up for credit card, for that our user should have as leats 18 years old at this situation we have to make decision depends on what user entered in age input:

```python
if age >= 18:
    print("You are now signed up")
```
* Note: any code in `if` statement block should be indented (4 spaces or one tab)

the print function in if block only runs when `if` is True if you we want to add another action we use `else`:
```python
if age >= 18:
    print("You are now signed up")
else:
    print("You most be 18+ to sign up")
```

we can check more than one condition if we need before reaching else using `elif` keyword (header for else if):

```python
if age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You most be 18+ to sign up")
```
you can add as many elif statements as you want:

```python
if age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet!")
elif age >= 100:
    print("You are too old to sign up")
else:
    print("You most be 18+ to sign up")
```

if we run this code it says `You are now signed up` because the first `if `statement is technically True you need to pay attention to order of statements if we want to run this code right maybe we should move second `elif` to the top:
```python
if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You most be 18+ to sign up")
```
Another example:
```python
response = input("Would you like food?: (Y/N)")

if response == "Y":
    print("Have some food")
else:
    print("No food for you")
```
* Note: to check and see two values are equal we use double equals `(==)`

for booleans and add action to them we could do that:
```python
for_sale = True

if for_sale:
    print("This iten is for sale")
else:
    print("This item is NOT for sale")
```

the if statement just validates that it is true or not