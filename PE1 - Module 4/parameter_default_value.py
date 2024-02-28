def introduction(first_name, last_name = "Perez"):
    print("Hello, my name is", first_name, last_name)

# Passing both parameters
introduction("James", "Doe")

# Positional argument, just sending the first_name, not the last name
# introduction function specifies a default for last_name in case this
# argument will not be specified.
introduction("Juan")
introduction(first_name = "Pedro")

#  Both parameters have their default values
def introduction(first_name = "Juan", last_name = "Perez"):
    print("Hello, my name is", first_name, last_name)

# invoking introduction with the two parameters with default values
introduction()

# If at the invocation time we use one of the argument, the remaining one
#   will take the default value
introduction(last_name = "García")

introduction("Paco")
