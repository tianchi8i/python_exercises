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

for i in pay_part_two:
    if i in pay_part_one:
        pay_part_one[i] += pay_part_two[i]
    else:
        pay_part_one[i] = pay_part_two[i]

sorted_result = sorted(pay_part_one.items(),key=lambda item: item[1], reverse=True)
result = dict(sorted_result)
print(result)
