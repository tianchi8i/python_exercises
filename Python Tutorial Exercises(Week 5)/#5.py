'''
First use dictionary comprehension to recreate the dictionary below, then 
use dictionary comprehension to swap the key values using dictionary comprehension.
Use key and val and .items() to find the keys and the values first.
Create a new list then place the value first then the key second then 
convert the list to a dictionary by using .dict().
'''
x = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4', 'key5': 'value5', 'key6': 'value6'}

invert_dict = dict([val, key] for key, val in x.items())
print(invert_dict)

# List comprehension in one line code
print(dict([val, key] for key, val in x.items()))