a_list = []
for i in range(100):
    a_list.append(i + 1)

print(a_list)

# reverse the list by swapping elements
length = len(a_list)
for i in range(len(a_list) // 2):
    a_list[i], a_list[length - i - 1] = a_list[length - i - 1], a_list[i]

print(a_list)
