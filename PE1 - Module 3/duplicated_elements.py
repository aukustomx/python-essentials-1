my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_list = []

for i in my_list:
    if i not in unique_list:
        unique_list.append(i)

print("Original list elements:", my_list)
print("List with unique elements:", unique_list)
