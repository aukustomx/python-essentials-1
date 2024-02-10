my_list = [10, 8, 6, 4, 2]

# It will produce a slice from index 0 to 3.
# The element in the index 4 is not included.
slice_omiting_start = my_list[:4]
print(slice_omiting_start)

# It will create a slice starting with the
# element in index 2 and ends in the last element
slice_omiting_end = my_list[2:]
print(slice_omiting_end)

# If we omit both start and end, it will
# make a copy of the whole list.
slice_omiting_start_end = my_list[:]
print(slice_omiting_start_end)
