# Given a positive integer n, find the sum of digits present at odd positions, counting positions from the right side (rightmost digit is position 1).


n = 12345
total = 0
position = 1

while n > 0:
    digit = n % 10

    if digit % 2 != 0:
        total = position + total
    position = position + 1
    n = n // 10
print(total)