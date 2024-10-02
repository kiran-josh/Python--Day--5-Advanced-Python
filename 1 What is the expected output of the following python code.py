"""
Name: Kiran G
Program: What is the expected output of the following python code given below:

"""
#data is defined as:
data = [10, 501, 22, 37,100, 999, 87, 351]

#The filter function is called with a lambda function:
result = filter (lambda x:x > 4, data) #This lambda function checks if each element x in the data list is greater than 4.

#The filtered result is converted to a list:
print (list(result))