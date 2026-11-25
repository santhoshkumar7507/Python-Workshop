# Write a Python program to reverse a number without converting it into a string.

n = 123
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n//10
print(rev)