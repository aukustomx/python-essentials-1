print("           *")
print("          * *")
print("         *   *")
print("        *     *")
print("       *       *")
print("      *         *")
print("     *           *")
print("    *             *")
print("   *               *")
print("  ******       ******")
print("       *       *")
print("       *       *")
print("       *       *")
print("       *       *")
print("       *********")

print()

print("    *     " * 2)
print("   * *    " * 2)
print("  *   *   " * 2)
print(" *     *  " * 2)
print("***   *** " * 2)
print("  *   *   " * 2)
print("  *   *   " * 2)
print("  *****   " * 2)

print()
print('"I\'m"\n""learning""\n"""Python"""')

print(14 % 4)
print(12 % 4.5)
print(12 // 4.5)

#print(2 / 0)
#print(2 // 0)
print(2 % 0)

print(-4 + 4)
print(-4. + 8)
print(4 + 4)

print(-1.1)
print(+2)

print(9 % 6 % 2)
print(9 / 6 / 2)

print(2 ** 2 ** 3)

print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
print((2 % -4), (2 % 4), (2 ** 3 ** 2))

#Variables
var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

#  Pythagorean theorem. The square of the hypotenuse is equal
# to the sum of the squares of the other two sides.
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("c =", c)

# Experimenting with variables

# Apples
john = 3
mary = 5
adam = 6
print(john, mary, adam)

total_apples = john + mary + adam
print(total_apples)
print('Total apples', total_apples)

# Median
value1 = 10
value2 = 9
value3 = 11
value4 = 10
value5 = 8
median = (value1 + value2 + value3 + value4 + value5) / 5
print(median)

# Miles to kilometers and viceversa
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61 

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# Value of a function for x = 0, 1 -1
x =  -1
x = float(x)
y = (3 *(x ** 3)) - (2 * (x ** 2)) + (3 * x) - 1
print("y =", y)

x = 1
y = 2
# y = y + x
print(x + y)
