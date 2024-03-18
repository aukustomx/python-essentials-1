def zeros(n):
    number = n
    zeros = 0
    while number >= 5:
        number //= 5
        zeros += number
    
    return zeros
