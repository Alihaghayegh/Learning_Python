# Logical Operators in `Python`

- **logical operators** : used on conditional statements
- **`and`** : checks two or more condition if True
- **`or`** : checks at least one condition is True
- **`not`** : True if condition is False, and vice versa

```python
temp = 25

if temp > 0 and temp < 30:
    print("the temperature is good")
else:
    print("the temperature is bad")

# > the temprature is good
```
- our temp is **25** so it means both of our conditions are True and the block of if statement will execute.

But what if it was **-10** ...???
```python
temp = -10

if temp > 0 and temp < 30:
    print("the temperature is good")
else:
    print("the temperature is bad")

# > the temperature is bad
```

What is it was over than **30** ...???
```python
temp = 40

if temp > 0 and temp < 30:
    print("the temperature is good")
else:
    print("the temperature is bad")

# > the temperature is bad
```
- one of confitions became False and it will execute else statement.

- Let's replace **and** with **or** :

```python
temp = 40

if temp > 0 or temp < 30:
    print("the temperature is good")
else:
    print("the temperature is bad")

# > the temperature is good
```
- If at least one statement is True then the entire statement is True and if statement will execute.

What if it was like this :
```python
temp = 40

if temp <= 0 and temp >= 30:
    print("the temperature is bad")
else:
    print("the temperature is good")

# > the temperature is bad
```
- Well **the temperature is bad**.
- First condition is True but second is False, using **`or`** operator needs only one True to whole condition become True.

- Let's say we have a boolean statement :
```python
temp = 20
sunny = True # today is sunny outside :)

if temp <= 0 and temp >= 30:
    print("the temperature is bad")
else:
    print("the temperature is good")

if sunny == True: # or if sunny:
    print("it is sunny outside")
else:
    print("it is cloudy outside")
# > the temperature is bad
# > it is sunny outside
```
- using **`not`** operator flips the result :
```python
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
```
- The **`not`** logical operator changes something True to False and vice versa.