# Given a number, check whether its digits are arranged in ascending order from left to right, without converting the number into a string.

n = 123457

previous = n % 10
n = n // 10

result = True

while n > 0:
    digit = n % 10
    if digit > previous:
        result = False
        break
    else:
        previous = digit
    
    n = n // 10
if result:
    print("Ascending")
else:
    print("discending")