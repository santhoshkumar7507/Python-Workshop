# Given a positive integer, find the second-largest distinct digit without converting the number into a string and without using sort() or max().

n = 231589

largest = -1
second = -1

while n>0:
    digit = n % 10
    if digit > largest:
        largest = second
        second = digit
    
    elif digit > second and digit != largest:
        second = digit
     
    n = n // 10

print(second)
