num = print(int(input()))
sign = -1 if num < 0 else 1
num = sign(abs)

reverse = 0
while num > 0:
    ld = num % 10
    reverse = reverse*10 + ld
    num = num//10

reverse = reverse * sign
if reverse < -2**31 or reverse > 2**31-1:
    print(0)
print(reverse)        

