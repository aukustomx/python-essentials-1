def my_function_with_parameters(number):
    print("As the invocation of this function happen",
          "without the needed parameters, this code will never be executed")

my_function_with_parameters()

# A message like this will be thrown
# TypeError: my_function_with_parameters() missing 1 required
#   positional argument: 'number'
