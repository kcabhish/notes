"""
Create a function that takes in3 parameters(firstname, lastname, age) and retrns a dictionary based on those values
"""

def Customers(firstName, lastName, age):
    return {
        "firstName" : firstName,
        "lastName" : lastName,
        "age": age
    }

customers_data = []
# Adding single items into the list
customers_data.append(Customers("John", "Doe", 19))
customers_data.append(Customers("Jane", "Dane", 18))

# Adding multiple items into the list
customers_data.extend([Customers("Tom", "Cat", 3), Customers("Jerry", "Mouse", 1)])
print(customers_data)
