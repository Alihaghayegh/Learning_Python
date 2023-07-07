import math
# Arithmetic Operators:

friends = 0

# name of variable = name of variable + 1
friends = friends + 1
print(friends)     # 1

# friends = friends + 1
friends += 1
print(friends)


# name of variable = name of variable - 1
friends = friends - 1

# And for shorten:
friends -= 1
print(friends)  # -1



friends = 5

# name of variable = name of variable * 3
friends = friends * 3

# And for shorten:
friends *= 3
print(friends)  # 15



friends = 5

# name of variable = name of variable / 2
friends = friends / 2

# And for shorten:
friends /= 2
print(friends)  # 2.5
# Somebody was cutten half :))) we have half of friend



friends = 5

# name of variable = name of variable ** 2
friends = friends ** 2

# And for shorten:
friends **= 2
print(friends)  # 25



friends = 10

# name of variable = name of variable % 3
remainder = friends % 3

print(remainder)  # 1


# built in math functions:

x = 3.14
y = -4
z = 5

result = round(x)
print(result) # 3


result = abs(y)
print(result) # 4


result = pow(4, 3)
print(result) # 64


result = max(x, y, z)
print(result) # 5


result = min(x, y, z)
print(result) # -4


# the math class:

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
