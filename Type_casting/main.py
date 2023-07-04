# Example of four data types
name = "ali"        # String
age = 26            # Integer
gpa = 1.4           # Float
student = True      # Boolean


# type() function
type(name)    
type(age)
type(gpa)
type(student)

print(type(name))       # <class 'str'>
print(type(age))        # <class 'int'>
print(type(gpa))        # <class 'float'>
print(type(student))    # <class 'bool'>


# Explicit:

age = float(age)
print(age)         # 26.0
print(type(age))   # <class 'float'>


gpa = int(gpa)
print(gpa)         # 1
print(type(gpa))   # <class 'int'>


student = int(student)
print(student)         # 'True'
print(type(student))   # <class 'str'>



# Implicit :

x = 2
y = 2.0
# let's say :
x = x / y
print(x)          # 1.0
print(type(x))    # <class 'float'>
