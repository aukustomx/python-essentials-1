def affect_global():
    global var_a
    var_a = 5
    return var_a

var_a = 1
print(var_a)
print(affect_global())
print(var_a)
