# Type Casting

**`Type Casting:`** The process of converting a value of one data type to another;
(string, integer, float, boolean)

`Explicit` vs `Implicit`

**Explicit:**

```python
# Example of four data types
name = "ali"        # String
age = 26            # Integer
gpa = 1.4           # Float
student = True      # Boolean
```

If you need the type of a variable you can use **`type()`** function to get the data type.

```python
type(name)    
type(age)
type(gpa)
type(student)
```

However if you run this you can't see any thing !

You should place it in **`print()`** function. 

```python
print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(gpa))        # <class 'float'>
print(type(student))    # <class 'bool'>
```

For example if we want to convert `age` to `floating point number` we can Explicitly do this:

```python
age = float(age)
print(age)         # 26.0
print(type(age))   # <class 'float'>
```

We can call it float because it has decimal portion.

And if we print the type of the `age` it would be float.

Let's convert `gpa` to integer :

```python
gpa = int(gpa)
print(gpa)         # 1
print(type(gpa))   # <class 'int'>
```

And it will be whole number without decimal portion .

For converting value to string place it in `str()` function .

```python
student = int(student)
print(student)         # 'True'
print(type(student))   # <class 'str'>
```

And it will convert to the `String` .

That is `Expilicit Type Casting`, **converting data type to another manually .**


**Implicit:**

**It happends when one data type converts to anothe automaticlly.**

```python
x = 2
y = 2.0
# let's say :
x = x / y
print(x)          # 1.0
print(type(x))    # <class 'float'>
```

However `x` was integer it converted to the float automaticlly .