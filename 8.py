# Given a positive integer n and a digit target, remove all occurrences of the target digit from the number without converting it into a string.

n = 1223
target = 2

result = 0
place = 1

while n > 0:
    digit = n % 10
       
    if digit != target:
        result = digit * place + result
        place = place * 10    

    n = n // 10

print(result)
