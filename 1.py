# Write a Python program to find the sum of all digits
#  in a number without converting the number into a string.

n = 12345
total = 0

while n > 0:
    digit = n % 10

    total += digit

    n = n//10
print(total)

