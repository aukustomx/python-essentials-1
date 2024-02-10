drawn = [5, 11, 9, 42, 3, 49]
bets = [9, 42, 5]
hits = 0

for bet in bets:
    if bet in drawn:
        hits += 1

print(hits)
