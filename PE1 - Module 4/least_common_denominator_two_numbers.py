def least_common_denominator(a, b):
    multiples = {a: {}, b: {}}

    # Calculate multiples, starting from 1
    mult = 1
    while True:

        # a times multiple in turn
        a_times_mult = a * mult

        # Inspecting if a times mult is inside multiples of b.
        # If so, we return a times mult.
        if a_times_mult in multiples[b].keys():
            return a_times_mult

        # If not, we add a times mult in the multiples of a dictionary.
        multiples[a].update({a_times_mult: mult})
        
        # It's b's turn. Calculate b times mult in turn.
        b_times_mult = b * mult

        # Inspecting if b times mult is inside multiples of a.
        # If so, we return b times mult.
        if b_times_mult in multiples[a].keys():
            return b_times_mult

        # If not, we add b times in the multiple of b dictionary.
        multiples[b].update({b_times_mult: mult})

        # Increment out multiplier by one.
        mult += 1
             
