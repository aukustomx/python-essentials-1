def is_prime(num):
    if num <= 1:
        return False
    
    half = num // 2
    for div in range(2, half + 1):
        if num % div == 0:
            return False
    
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
