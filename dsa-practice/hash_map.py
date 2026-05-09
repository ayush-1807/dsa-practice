n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

freq = {}

# count frequency
for num in n:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# queries
for num in m:
    print(freq.get(num, 0))