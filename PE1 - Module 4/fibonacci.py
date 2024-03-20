def fibonacci(n):
    if n < 1:
        return None

    if n < 3:
        return 1

    result = 0
    item1 = 1
    item2 = 1
    
    for i in range(3, n + 1):
        result = item1 + item2
        item1, item2 = item2, result

    return result

# Testing
#for i in range(1, 10):
#    print(i, fibonacci(i))

number = int(input("Enter the number to calculate its Fibonacci: "))
print("Fibonacci of", number, "is", fibonacci(number))
