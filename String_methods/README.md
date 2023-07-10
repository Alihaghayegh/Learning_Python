# Strings

Strings in `python` are surrounded by either single qoutation marks, or double qoutation marks.

`'hello'` is same as `"hello"`

You can display a string literal with the `print()` function:
```python
print("hello")
print('hello')
```

**Assign String to a Variable**:

Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
```python
a = "Hello"
print(a)
```

**Multiline Strings**:

You can assign a multiline string to a variable by using three quotes:

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

Or three single qoutes:
```python
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
```

**String Length**:
To get the length of a string, use the `len()` function, it will returns the length as a string:
```python
a = "Hello, World!"
print(len(a))
```

**Check String**:

To check if a certain phrase or character is present in a string, we can use the keyword `in`.

```python
txt = "The best things in life are free!"
print("free" in txt)
```

To check if a certain phrase or character is NOT present in a string, we can use the keyword `not in`.
```python
txt = "The best things in life are free!"
print("expensive" not in txt)
```

**Modify String**:

Python has a set of built-in methods that you can use on strings.

The `upper()` method returns the string in upper case:
```python
a = "Hello, World!"
print(a.upper())
```

The `lower()` method returns the string in lower case:

```python
a = "Hello, World!"
print(a.lower())
```

The `strip()` method removes any whitespace from the beginning or the end:
```python
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!
```

The `replace()` method replaces a string with another string:

```python
a = "Hello, World!"
print(a.replace("H", "J"))
```

The `split()` method returns a list where the text between the specified separator becomes the list items, The `split()` method splits the string into substrings if it finds instances of the separator:

```python
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
```
