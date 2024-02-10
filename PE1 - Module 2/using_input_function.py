#print("Tell me anything")
#anything = input()
#print("Hmm...", anything, "... Really?")

# Input with a message
#anything = input('Tell me anything...')
#print("Hmm...", anything, "... Really?")

# Input is a string, nothing else
#anything = input("Enter a number: ")
#operation = anything ** 2.0
#print(anything, "to the power of 2 is", operation)
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'

## Input is a string, nothing else
#anything = input("Enter a number: ")
#operation = anything ** 2.0
#print(anything, "to the power of 2 is", operation)
## TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'float'

## Conver string Input to int
#anything = input("Enter a number: ")
#number = float(anything)
#operation = number ** 2.0
#print(anything, "to the power of 2 is", operation)

## Direct input conversion
#number = float(input("Enter a number: "))
#operation = number ** 2.0
#print(number, "to the power of 2 is", operation)

## Calculating the hypotenuse
#leg_a = float(input('Input side a: '))
#leg_b = float(input('Input side b: '))
#hypo = (leg_a ** 2 + leg_b ** 2) ** .5
#print("Hypotenuse length is: ", hypo)

## + as a concatenation operator
#fnam = input("May I have your first name, please? ")
#lnam = input("May I have your last name, please? ")
#print("Thank you.")
#print("\nYour name is " + fnam + " " + lnam + ".")

## Concatenation (+) and replication operators (*)
#print("+" + 10 * "-" + "+")
#print(("|" + " " * 10 + "|\n") * 5, end="")
#print("+" + 10 * "-" + "+")

## Artwork using concatenation and repliction operators
#print(" "*4 + "*"*1 + " "*4)
#print(" "*3 + "*" + " "*2 + "*" + " "*3)
#print(" "*2 + "*" + " "*4 + "*" + " "*2)
#print(" "*1 + "*" + " "*6 + "*" + " "*1)
#print("*"*10)
#print((("*" + " "*8 + "*\n")*5), end="")
#print("*"*10)

## Lab of input and string operations
## input a float value for variable a here
#a = float(input("Enter a float value for variable a here: "))
## input a float value for variable b here
#b = float(input("Enter a float value for variable b here: "))
## output the result of addition here
#print(a, "added to", b, "is equal to", (a+b))
## output the result of subtraction here
#print(a, "substract to", b, "is equal to", str(a-b))
## output the result of multiplication here
#print("The result of multiply " + str(a) + " times " + str(b) + " is equal to " + str(a*b))
## output the result of division here
#print(str(a) + " / " + str(b) + " = " + str(a/b))
#print("\nThat's all, folks!")

## Lab operators precedence or priority
#x = float(input("Enter value for x: "))
## Write your code here.
#y = 1. /((x + (1. / (x + (1. / (x + (1. / x)) )))))
#print("y =", y)

## Lab adding minutes to a given hour, what time result
## Your task is to prepare a simple code able to evaluate
## the end time of a period of time, given as a number of
## minutes (it could be arbitrarily large). The start time
## is given as a pair of hours (0..23) and minutes (0..59). 
## The result has to be printed to the console.
## For example, if an event starts at 12:17 and lasts 59 minutes,
## it will end at 13:16.
## Write your code here.
print("-----------")
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

dura_hour = dura // 60
hour = hour + dura_hour
print("Duracion horas:", dura_hour, ", Horas totales: ", hour)

dura_mins = dura % 60
mins = mins + dura_mins
print("Restante mins duracion:", dura_mins, ", Minutos totales: ", mins)

hour = (hour + (mins // 60)) % 24
mins = mins % 60

print(hour, ":", mins)
