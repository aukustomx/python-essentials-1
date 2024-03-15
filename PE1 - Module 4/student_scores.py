VALID_SCORE_RANGE = range(0, 11)
school_class = {}

while True:

    name = input("Enter a student name: ")
    if '' == name:
        break

    score = int(input("Enter the score (0-10) for " + name + ": "))
    if score not in VALID_SCORE_RANGE:
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    print(name, "-> scores:", school_class[name])
    print(name, ":", sum(school_class[name]) / len(school_class[name]))
