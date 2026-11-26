# Given a positive integer, calculate the sum of digits present at even positions, counting positions from the right side (rightmost digit is position 1)

n = 12345
total = 0
postion = 1

while n > 0:
    digit = n % 10

    if digit % 2 == 0:
        total = postion + total
    
    postion = postion + 1
    n = n // 10
print(total)