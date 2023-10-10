# String indexing

# usage : [start : end : step]

credit_number = "1234-5678-9012-3456"

# one_element:
print(credit_number[0]) # 1
print(credit_number[1]) # 2
print(credit_number[2]) # 3
print(credit_number[3]) # 4
print(credit_number[4]) # -

# 4 elements:
print(credit_number[0:4]) # 1234
print(credit_number[:4]) # 1234
print(credit_number[5:9]) # 5678

# 12 next elements:
print(credit_number[5:]) # 5678-9012-3456

# negative index:
print(credit_number[-1]) # 6

# step:
print(credit_number[::2]) # 13-6891-46
print(credit_number[::3]) # 146-136

# examples:
# last 4 digits:
last_digits = credit_number[-4:]
print(f"XXX-XXXX-XXXX-{last_digits}") # XXXX-XXXX-XXXX-3456

# revesing:
credit_number = credit_number[::-1]
print(credit_number) # 6543-2109-8765-4321
