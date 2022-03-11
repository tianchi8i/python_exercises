'''
This script consolidates two dictionaries into a single dictionary and 
prints the output sorted by the highest paying to lowest.

Use the set() constructor to make a set.

Create a new dictionary called 'result_list'.

Use a for loop to find all the keys and values and add the keys and 
the values to the new dictionary called 'result_list'. 

Print the output sorted by the highest paying to lowest 
by using the sorted() and reverse method.
'''
pay_part_one = {"john": 1000, "kevin": 60, "ben": 300, "janet": 500, "jean": 30}
pay_part_two = {"jean": 50, "ben": 300, "kevin": 700, "janet": 40, "jack": 1230}

z = set(pay_part_one)
x = set(pay_part_two)
result_list = {}

for i in z | x:
    c = pay_part_one.get(i, 0) + pay_part_two.get(i, 0)
    result_list[i] = c
result = sorted(result_list.items(),key=lambda item: item[1], reverse=True)
print(result)
