# Empty list
my_list = []

# Filling the empty list through a for loop
for i in range(5):
    my_list.append(i + 1)

print(my_list)

# Other empty list
other_list = []

# Filling the other list
for i in range(5):
    other_list.insert(0, i + 1)

print(other_list)
