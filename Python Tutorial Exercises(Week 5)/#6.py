'''
Take a list of names and convert it to a dictionary with the key 
being the name and the value being the length of the name, 
removing any name that has 7 characters or more.
Use for loop to find the name that is less than 7 characters, 
if len(i) < 7 add them to the list called name_list.
Same as above, but we use len(i) to get the name's characters thsi time
Use zip to make those two list into one list then use dict convert the list to a dictionary.
'''

names = ["Raphael", "Tanya", "Miriam", "Leonard", "Owen", "Julie", "Haleema", "Mabel", "Stanley"]
#find the name that is less than 7 characters 
name_list = [i for i in names if len(i) < 7]
#find the name characters that is less than 7
number_list = [len(i) for i in names if len(i) < 7]
# zip 2 lists together then convert then to a dictionary
print(dict(zip(name_list, number_list)))

# List comprehension in one line code
print(dict(zip([i for i in names if len(i) < 7], [len(i) for i in names if len(i) < 7])))
