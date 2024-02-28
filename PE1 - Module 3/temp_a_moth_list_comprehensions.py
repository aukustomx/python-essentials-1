import random

def fill_temperatures(temperatures):
    for day in range(31):
        for hour in range(24):
            temperatures[day][hour] = round(random.uniform(-5.0, 38.0), 2)


temperatures = [[0.0 for hour in range(24)] for day in range(31)]
fill_temperatures(temperatures)

print(temperatures)

