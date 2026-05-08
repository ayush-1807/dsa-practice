num = 12
factors = []

for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        factors.append(i)
        factors.append(num // i)

# duplicate remove + sort
factors = list(set(factors))
factors.sort()

print(*factors)