# Format Specifiers in Python

`format specifiers` : {value:flags} format a value based on that flags are intered when you use an "f"string

**.(number)f** = round to that many decimal point (fixed point)

**:(number)** = allocate that many spaces

**:03** = allocate and zero pads that many spaces

**:<** = left justify

**:>** = right justify

**:^** = center align

**:+** = use a plus sign to indicate positive value

**:=** = place sign to leftmost position

**:** = insert space before positive numbers

**:,** = comma seperator

let's say :
```python
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is ${price1:.2f}")  # price 1 is $3.14
print(f"price 2 is ${price2:.2f}")  # price 2 is $-987.65
print(f"price 3 is ${price3:.2f}")  # price 3 is $12.34
```
for spaces :
```python
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is ${price1:10}")  # price 1 is $      3.14
print(f"price 2 is ${price2:10}")  # price 2 is $   -987.65
print(f"price 3 is ${price3:10}")  # price 3 is $     12.34
```
if you want zero padded number :
```python
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is ${price1:010}")  # price 1 is $000003.14
print(f"price 2 is ${price2:010}")  # price 2 is $00-987.65
print(f"price 3 is ${price3:010}")  # price 3 is $000012.34
```
to left justify :
```python
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is ${price1:<10}")  # price 1 is $3.14159
print(f"price 2 is ${price2:<10}")  # price 2 is $-987.65
print(f"price 3 is ${price3:<10}")  # price 3 is $12.34
```
* The values are left justified and all rest of them are spaces till 10 character

and for right justify:
```python
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is ${price1:>10}")  # price 1 is $      3.14159
print(f"price 2 is ${price2:>10}")  # price 2 is $   -987.65
print(f"price 3 is ${price3:>10}")  # price 3 is $     12.34
```
for center align :
```python
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is ${price1:^10}")  # price 1 is $ 3.14159
print(f"price 2 is ${price2:^10}")  # price 2 is $ -987.65
print(f"price 3 is ${price3:^10}")  # price 3 is $  12.34
```
if you have any positive value and you want to show plus sign :
```python
price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is ${price1:+}")  # price 1 is $+3.14159
print(f"price 2 is ${price2:+}")  # price 2 is $-987.65
print(f"price 3 is ${price3:+}")  # price 3 is $+12.34
```
* Every positive number is shown by plus sign

for comma seperation :
```python
price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"price 1 is ${price1:,}")  # price 1 is $3,000.14159
print(f"price 2 is ${price2:,}")  # price 2 is $-9,870.65
print(f"price 3 is ${price3:,}")  # price 3 is $1,200.34
```