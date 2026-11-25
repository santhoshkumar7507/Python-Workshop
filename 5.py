# Given a positive integer n, find the largest digit present in the number without converting the number into a string.

n = 12154410
largest = 0

while n > 0:
    digit = n % 10

    if digit > largest:
        largest = digit
    
    n = n // 10
print(largest)