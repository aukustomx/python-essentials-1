dictionary = {"book": "libro", "chair": "silla", "box": "caja"}
totals_by_status = {"backlog": 45, "in progress": 12, "done": 40}
empty_dict = {}

print(dictionary)
print(totals_by_status)
print(empty_dict)

# To get a value, we deliver a valid key
# We can use single or double quotes to specify the key
print("Book in spanish is:", dictionary['book'])
print("Chair in spanish is:", dictionary["chair"])
print("The total tasks in done status are: ", totals_by_status["done"])

# If we use an invalid key, we get the error:
# print("Mouse in spanish is:", dictionary['mouse'])
# KeyError: 'mouse'

# Every dictionary have a key(method)
print("Dictionary keys:", dictionary.keys())
print("Status:", totals_by_status.keys())

animals = {
    "cat": "chat",
    "dog": "chien",
    "horse": "cheval"
    }


for key in animals.keys():
    print(key, "->", animals[key])

# If we want to navigate the keys in an ordered way, we can enrich the for loop
for key in sorted(animals.keys()):
    print(key, "->", animals[key])

# We can extract key value pairs using the method items() from each dictionary
for status, total in totals_by_status.items():
    print("Status:", status, "->", "Total:", total)

# Assigning a new value for an existing key
totals_by_status["backlog"] = 35
totals_by_status["in progress"] = 10
totals_by_status["done"] = 52
print(totals_by_status)

# Adding a non existing key (and value)}
totals_by_status["on hold"] = 5
print(totals_by_status)

