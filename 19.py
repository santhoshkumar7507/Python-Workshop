# Given a number, check whether its digits are arranged in descending order without converting it into a string.

n = 54321
previos = n % 10
n = n // 10

result = True

while n > 0:
    digit = n % 10 

    if digit < previos:
        result = False
        break

    else:
        digit = previos
    
    n = n // 10
if result:
    print("discending ")
else:
    print("not discenting")