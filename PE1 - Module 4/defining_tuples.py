# The preferred way to declare a tuple is using parentheses
tuple_1 = (1, 2, 3, 4, 5)

# It's also posibble to create a tuple just from a set of values
# sepatated by commas
tuple_2 = 1, 2, 3, 4, 5

# If we print out both tuples, this is the result
# (1, 2, 3, 4, 5) (1, 2, 3, 4, 5)
print(tuple_1, tuple_2)

# We are able to create an empty tuple. In this case, parentheses are necessary
tuple_3 = ()
print("Tuple 3:", tuple_3)

# If we want to create a tuple with a single element, we need to end
# the unique value with a comma. If we don't do so, we will get a single
# variable instead of a tuple
tuple_4 = (1,)
tuple_5 = 1,
print("Tuple 4 type is:", type(tuple_4))
print("Tuple 5 type is:", type(tuple_5))

# Without the comma at the end, they are simple variable and values
tuple_6 = (1)
print("Tuple 6 type is:", type(tuple_6))

# Don't modify a tuple element
# tuple_1[0] = 0
# TypeError: 'tuple' object does not support item assignment

# If we try to delete an element of the tuple
# del my_tuple[0]
# TypeError: 'tuple' object doesn't support item deletion

