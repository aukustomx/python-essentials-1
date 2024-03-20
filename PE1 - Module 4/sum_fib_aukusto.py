def perimeter(n):
    squares_sum = 0
    prev_1 = 0
    prev_2 = 1
    for i in range(n + 1):
        squares_sum += prev_2
        prev_1, prev_2 = prev_2, prev_1 + prev_2    
    return squares_sum * 4
        
print(perimeter(5) * 4)
print(perimeter(7) * 4)
print(perimeter(20) * 4)
print(perimeter(30) * 4)
print(perimeter(100) * 4)
print(perimeter(500) * 4)
