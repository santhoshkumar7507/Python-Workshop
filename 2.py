# Find the product of all digits in a number.

n = 123
total = 1

while n > 0:
    digit = n%10
    total = digit * total 
    n = n//10
print(total)
