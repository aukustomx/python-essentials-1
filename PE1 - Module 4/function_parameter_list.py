print("------ Not affecting the list argument value nor its content")
def my_function(list_1):
    print("Print #1:", list_1)
    print("Print #2:", list_2)
    list_1 = [0, 1]
    print("Print #3:", list_1)
    print("Print #4:", list_2)

# list_2 will be used as the my_function's argument
list_2 = [2, 3]

# Calling my_function
my_function(list_2)
print("Print #5:", list_2)

print()
print()

print("------- Affecting the list argument value nor its content")
def my_function(list_a):
    print("Print #1:", list_a)
    print("Print #2:", list_b)
    del list_a[0] # This will affect list content
    print("Print #3:", list_a)
    print("Print #4:", list_b)

list_b = [2, 3]
my_function(list_b)
print("Print #5:", list_b)
