# Given an integer n and a digit target, count how many times the target digit appears in the number.

n = 122522
k = 2
count = 0

while n>0:
    digit = n % 10

    if digit  == k:
        count += 1
    n = n // 10
print(count)