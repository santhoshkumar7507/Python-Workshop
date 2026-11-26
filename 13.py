# Write a Python program to check whether a given array contains at least 3 consecutive odd numbers. If it contains 3 consecutive odd numbers, print True; otherwise, print False.

n = [1,2,3,4,5,7,9,12]

count = 0
result = False

for i in n:
    if i % 2 != 0:
        count += 1
    else:
        count = 0
    
    if count == 3:
        result = True
        break
print(result)
