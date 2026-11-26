# Write a Python program to repeatedly calculate the sum of digits until you get a single-digit number.

n = 38
total = 0
sum = 0

while n > 0:
    digit = n % 10
    total += digit
    n = n // 10
print(total)

while total > 0:
    digit = total % 10
    sum = sum + digit
    total = total // 10
print(sum)