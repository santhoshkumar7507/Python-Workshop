s = "(3(4+6)-2+(5+7))"

num = 0
total = 0
sign = 1

for n in s:
    if n.isdigit():
        num = num * 10 + int(n)

    elif n == "+":
        total += num * sign
        num = 0
        sign = 1
    
    elif n == "-":
        total += num * sign
        num = 0
        sign = -1
    
    elif n == ")":
        total += num * sign
        num = 0

print(total)
    

