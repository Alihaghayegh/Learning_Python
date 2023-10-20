# Format specifiers in python

price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f"price 1 is ${price1:.2f}")  # price 1 is $3.14
print(f"price 2 is ${price2:.2f}")  # price 2 is $-987.65
print(f"price 3 is ${price3:.2f}")  # price 3 is $12.34


print(f"price 1 is ${price1:10}")  # price 1 is $      3.14
print(f"price 2 is ${price2:10}")  # price 2 is $   -987.65
print(f"price 3 is ${price3:10}")  # price 3 is $     12.34


print(f"price 1 is ${price1:010}")  # price 1 is $000003.14
print(f"price 2 is ${price2:010}")  # price 2 is $00-987.65
print(f"price 3 is ${price3:010}")  # price 3 is $000012.34


print(f"price 1 is ${price1:<10}")  # price 1 is $3.14159
print(f"price 2 is ${price2:<10}")  # price 2 is $-987.65
print(f"price 3 is ${price3:<10}")  # price 3 is $12.34


print(f"price 1 is ${price1:>10}")  # price 1 is $      3.14159
print(f"price 2 is ${price2:>10}")  # price 2 is $   -987.65
print(f"price 3 is ${price3:>10}")  # price 3 is $     12.34


print(f"price 1 is ${price1:^10}")  # price 1 is $ 3.14159
print(f"price 2 is ${price2:^10}")  # price 2 is $ -987.65
print(f"price 3 is ${price3:^10}")  # price 3 is $  12.34


print(f"price 1 is ${price1:+}")  # price 1 is $+3.14159
print(f"price 2 is ${price2:+}")  # price 2 is $-987.65
print(f"price 3 is ${price3:+}")  # price 3 is $+12.34


print(f"price 1 is ${price1:,}")  # price 1 is $3,000.14159
print(f"price 2 is ${price2:,}")  # price 2 is $-9,870.65
print(f"price 3 is ${price3:,}")  # price 3 is $1,200.34
