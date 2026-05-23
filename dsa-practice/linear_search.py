arr = [1, 2, 3, 4]
x = 3

n = len(arr)

found = False

for i in range(n):

    if arr[i] == x:
        print(i)
        found = True
        break

if found == False:
    print(-1)