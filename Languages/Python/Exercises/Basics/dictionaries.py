"""
Dictionaries
"""

user_dictionary = {
    'username': 'JohnCena',
    'name': 'John',
    'age': 32
}
# addes new entry to the dictionary
user_dictionary["married"] = True
# prints the full dictionary
print (user_dictionary)

# prints the first item from the list
for x in user_dictionary:
    print(x)

# removing property 
user_dictionary.pop("age")
for x, y in user_dictionary.items():
    print(x, y)

# when items are assinged they are passed by reference
user_dictionary2 = user_dictionary
# this is passed by value
user_dictionary3= user_dictionary.copy()
