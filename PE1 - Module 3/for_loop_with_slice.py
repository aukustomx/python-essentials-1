# Find the largest element in a list.

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for current_element in my_list[1:]:
    if current_element > largest:
        largest = current_element

print(largest)
