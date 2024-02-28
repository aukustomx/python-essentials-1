def message(number):
    # This "number" parameter is not the same as the "number" variable
    print("Enter a number:", number)

# This number variable is not related to the "number" parameter of message
#   function defined above.
number = 1234

# "1" is the argument send to the message function. When the
#   function has been reached, this 1 value will be called number inside
#   the function, but this won't the same as "number = 1234"
message(1)

# This print will print 1234, the value of our variable name, not
#   the value of number parameter of message function.
print(number)
