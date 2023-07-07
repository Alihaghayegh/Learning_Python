# Math In Python

**`Arithmetic Operators`** :

let's say we have a variable called friends:
```python
friends = 0
```
But if we want to increment friend to 1 we do this:
```python
# name of variable = name of variable + 1
friends = friends + 1
```
And if we print the friend it will print the new variable:

```python
friends = friends + 1
print(friends)     # 1
```
You could also shorten that line of code, you could say:
```python
# friends = friends + 1
friends += 1
print(friends)
```
That is known as `augmented assignment operator` and does the same thing.

Now we have a subtraction :
```python
# name of variable = name of variable - 1
friends = friends - 1

# And for shorten:
friends -= 1
print(friends)  # -1
```

For multiplication :
```python
friends = 5

# name of variable = name of variable * 3
friends = friends * 3

# And for shorten:
friends *= 3
print(friends)  # 15
```

For division :
```python
friends = 5

# name of variable = name of variable / 2
friends = friends / 2

# And for shorten:
friends /= 2
print(friends)  # 2.5
# Somebody was cutten half :))) we have half of friend
```
For exponent :
```python
friends = 5

# name of variable = name of variable ** 2
friends = friends ** 2

# And for shorten:
friends **= 2
print(friends)  # 25
```
For modulus :

it also known as remaider of the division
```python
friends = 10

# name of variable = name of variable % 3
remainder = friends % 3

print(remainder)  # 1
```

Now let's cover some **`built in math functions`**:
```python
x = 3.14
y = -4
z = 5
```
`round()` function rounds the floating point number to the nearest integer number:
```python
result = round(x)
print(result) # 3
```
with the `abs()` function we can take the absolute value of the number:
```python
result = abs(y)
print(result) # 4
```
There is a built in power function:
```python
result = pow(4, 3)
print(result) # 64
```
With the `max()` function we can find the maximium value of various values:
```python
result = max(x, y, z)
print(result) # 5
```
Otherwise there is `min()`:
```python
result = min(x, y, z)
print(result) # -4
```

The **`Math`** class:

For using the math class we need to import it first:
```python
import math

# if you need the value of pi:
print(math.pi)  # 3.14

# if working with (e) number :
print(math.e)   # 2.71

# for squere root of something:
x = 9
result = math.sqrt(x)
print(result)   # 3.0

# there is a ceiling function that always rounds floating point number up:
y = 9.1
result = math.ceil(y)
print(result)  # 10

# otherwise there is floor that rounds number down:
z = 9.9
result = math.floor(z)
print(z)      # 9
```

