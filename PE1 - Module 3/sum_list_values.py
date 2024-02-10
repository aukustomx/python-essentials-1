my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print("Total is:", total)

# Now, hiding all the actions connected to the list's indexing
total2 = 0

for i in my_list:
    total2 += i

print("Total2: ", total2)
