my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 10
found = False

for i in range(len(my_list)):
    if my_list[i] == to_find:
        found = True
        break

if found:
    print("Element found at index", i)
else:
    print("absent")


        
