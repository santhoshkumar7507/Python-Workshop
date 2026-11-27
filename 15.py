# Given a positive integer, swap its first and last digits without converting the number into a string.


n = 12345

temp = n
last = n % 10

div = 1
while temp >= 10:
    temp = temp // 10
    div = div * 10

first = temp
middle = (n % div) // 10

result = last * div + middle * 10 + first

print(result)