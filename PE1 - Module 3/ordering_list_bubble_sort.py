#lst = [8, 10, 6, 2, 4, 1, 25, 3, 9]
#lst = [1, 2, 3, 4, 5]
lst = [8, 10, 6, 2, 4]
print("Original list:", lst)

length = len(lst)
cycles = 0
comparisons = 0
swaps = 0


for i in range(length - 1):
    
    cycles += 1
    
    for j in range(length - i - 1):
        
        comparisons += 1
        
        if lst[j] > lst[j + 1]:

            swaps += 1
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            
print("Ordered list:", lst)
print("Cycles:", cycles)
print("Comparisons:", comparisons)
print("Swaps:", swaps)
