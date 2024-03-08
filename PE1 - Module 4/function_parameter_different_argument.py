def my_function(n):
    print("Recibo n =", n)

    # This operation affects only to n parameter, a copy of the
    # argument, not the original n outside the function
    n += 1
    print("Ahora n = ", n)

n = 1

# After function invocation, n is not affected
print(my_function(n))
print(n)
