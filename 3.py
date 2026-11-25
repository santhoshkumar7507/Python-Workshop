# Write a Python program to count the number of digits in a given integer without using len() or converting it into a string.

n = 1211
count = 0

while n > 0:
    digit = n % 10
    count =count + 1
    n = n // 10
print(count) 