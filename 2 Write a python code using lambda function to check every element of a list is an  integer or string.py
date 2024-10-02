"""
Name: Kiran G
Program: Write a python code using lambda function to check every element of a list is an  integer or string?

"""
# Sample list
data = [10, 'hello', 3.14, 'world', 42, True, None, 'Python']

# Using map and lambda to check types
result = list(map(lambda x: (x, 'Integer' if isinstance(x, int) else 'String' if isinstance(x, str) else 'Other'), data))

# Print the results
for value, type_of in result:
    print(f"{value}: {type_of}")
