my_list = [10, 8, 6, 4, 2]

# [1:-1] indicates the the slice will contain the elements from index 1
# and ends in the last index of the list, using -1 reference.
new_list = my_list[1:-1]
print(new_list)

list_2 = my_list[-3:-1]
print(list_2)

# From the list's beginning point of view, if the start specifies
# an element further than the one describe by the end, the slice
# will be empty
list_3 = my_list[2:1]
list_4 = my_list[-1:2]
print(list_3)
print(list_4)
