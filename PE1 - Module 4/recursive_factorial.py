# Fibn = Fibn-1 + Fibn-2
def factorial(n):
    if n < 0:
        return None
    
    if n < 2:
        return 1

    return n * factorial(n - 1)

# Testing
for n in range(1, 6):
    print(n, factorial(n))
