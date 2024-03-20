def fib(n):
    a, b = 0, 1
    for i in range(n+1):
        if i == 0:
            yield b 
        else:
            a, b = b, a+b
            yield b
        
print(sum(fib(5)) * 4)
print(sum(fib(7)) * 4)
print(sum(fib(20)) * 4)
print(sum(fib(30)) * 4)
print(sum(fib(100)) * 4)
print(sum(fib(500)) * 4)
