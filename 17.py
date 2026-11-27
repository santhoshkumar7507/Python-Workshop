# Given a number, find the difference between the sum of its even digits and the sum of its odd digits.

n = 12345678
even = 0
odd = 0

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        even = even + digit
    else:
        odd = odd + digit
    
    n = n // 10

    difference = even - odd
print(difference)