num = 153
original = num
cube = 0 
result = 0
nod = len(str(num))

while num>0:
    ld = num%10
    cube = ld**nod
    result = cube + result
    num = num//10
print(result)

if original == result:
    print("No. is Armstrong ")
else:
    print("Not Armstrong")    
