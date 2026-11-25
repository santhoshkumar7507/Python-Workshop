# Given a positive integer n, find the smallest digit present in the number without converting it into a string and without using min().

n = 84989
smallest = 9
while n > 0:
    digit = n % 10
    if digit < smallest:
        smallest = digit
    n= n // 10
print(smallest)