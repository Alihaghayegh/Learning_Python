# variables and data types
### variables:

`variable` = a reusable container for storing a value; a `variable` behavesas if it were value it contains.

```python
age = 27
```
for printing a `variable` you should do this:
```python
print(age)
```
and for printing `variable` with other texts you have different options:
```python
print("I have " + str(age) + " years old")
print("I have", age, "years old")
print(f"I have {age} years old")
```
- **Tip:** Pay attention to spacing.
- **Tip:** The str() is for type casting and concatenation strings (we will talk about type casting in next chapter).

***
### 4 Basic data types:
- `INTEGER`: Just whole numbers
```python
age = 27
players = 2
quantity = 5

print(f"I have {age} years old")
print(f"There are {players} players online")
print(f"You would like tp buy {quantity} items")
```

- `FLOAT`: The number that contains a decimal. even a decimal part was a Zero 
```python
gpa = 3.2
dictance = 2.5
price = 10.99

print(f"Your gpa is {gpa}")
print(f"You ran {dictance}km")
print(f"the price is ${price}")
```
- `STRING`: Series of text (characters) within quotes or double quotes
```python
name = "ali"
food = "pizza"
email = "haghayeghali95@gmail.com"

print(f"Hello {name}")
print(f"You like {food}")
print(f"Your email is: {email}")
```
- **Tip:** Strings can contain numbers
- `BOOLEAN`: either True or False
- **Tip:** Remember a light switch or 0 and 1
- **Tip:** booleans are usually used internally in programs

```python
online = True
for_sale = False
running = True

print(f"Are you online? {online}")
print(f"Is this item for sale? {for_sale}")
print(f"Is game running? {running}")
```
- **Tip:** The first letter of True and False is capital
- **Tip:** Do not put them in quotes in this case it will become string

