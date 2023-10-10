# String indexing

**`indexing`** : accessing elements of a sequence using [] AKA: (indexing operator)

**usage** : [start : end : step]

```python
credit_number = "1234-5678-9012-3456"
```
- If i need first character of this number i can type the variable name followed by square brackets and index of character which is zero (computers always start with zero)

```python
credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # 1
print(credit_number[1]) # 2
print(credit_number[2]) # 3
print(credit_number[3]) # 4
print(credit_number[4]) # -
```
Then 4st character of `credit_number` is dash (-).

- with indexing operator there is up to three fields we can fill in: `start`, `end` and `step`

Now what if we want first 4 digits of string :
```python
credit_number = "1234-5678-9012-3456"

print(credit_number[0:4]) # 1234
```
The staring index is always inculsive and ending index is always exclusive.

- Well you can omit the `0` and python will automatically starts with first index :
```python
credit_number = "1234-5678-9012-3456"

print(credit_number[:4]) # 1234
```

- let's get the next set of digits :

```python
credit_number = "1234-5678-9012-3456"

print(credit_number[5:9]) # 5678
```
- Maybe we need the next 12 digits, well in that case we can type like this :

```python
credit_number = "1234-5678-9012-3456"

print(credit_number[5:]) # 5678-9012-3456
```

- You could also use a negative index :
```python
credit_number = "1234-5678-9012-3456"

print(credit_number[-1]) # 6
```
- it will print the last digit of index.

- Let's talk about `step` :
- using the `step` field we can access the characters of string by given step :

- If we don't need start and end but we only need step, we can type :
```python
credit_number = "1234-5678-9012-3456"

print(credit_number[::2]) # 13-6891-46
print(credit_number[::3]) # 146-136
```
- Here is a practical example, let's create a program that shows the last 4 digit of number:

```python
credit_number = "1234-5678-9012-3456"

last_digits = credit_number[-4:]

print(f"XXX-XXXX-XXXX-{last_digits}") # XXXX-XXXX-XXXX-3456
```

- Now let's reverse the characters of the string :
```python
credit_number = "1234-5678-9012-3456"

credit_number = credit_number[::-1]

print(credit_number) # 6543-2109-8765-4321
```