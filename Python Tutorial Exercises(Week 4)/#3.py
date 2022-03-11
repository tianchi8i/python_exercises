'''
This script uses for loop to find the youngest and oldest employees 
in the dictionary of 'company' by setting minimum & min_key and maximum & max_key values.
'''
company = {"john": 99, "ben": 34, "kevin": 45, "janet": 20, "jack": 50, "jean": 87}

minimum = 100
min_key = None 
for z in company:
    if company[z] < minimum:
        minimum = company[z]
        min_key = z
print(f"Youngest employee award goes to {min_key} at age {minimum}.")

maximum = 0
max_key = None
for k in company:
    if company[k] > maximum:
        maximum = company[k]
        max_key = k
print(f"Oldest employee award goes to {max_key} at age {maximum}.")
