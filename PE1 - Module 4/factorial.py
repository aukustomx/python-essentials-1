def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    producto = 1
    
    for i in range(2, n + 1):
        producto *= i

    return producto

# Testing factorial function
for i in range(1, 6):
    print(i, factorial(i))
