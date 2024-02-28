row = ['A' for i in range(10)]
print(row)

row_2 = ["A" + str(i) for i in range(10)]
print(row_2)

# Squares of numbers from 0 to 9
squares = [x ** 2 for x in range(10)]
print(squares)

# Even numbers from 2 to 14
even_numbers = [n * 2 for n in range(1, 8)]
print(even_numbers)

# Powers of 2
powers_of_2 = [2 ** p for p in range(8)]
print(powers_of_2)

# Create a list containing odd numbers from
# the previous squares list
odds = [sq for sq in squares if sq % 2 != 0]
print(odds)
