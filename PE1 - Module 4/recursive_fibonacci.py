import sys

def fibonacci(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(sys.argv)
number = int(sys.argv[1])
print(number, fibonacci(number))
