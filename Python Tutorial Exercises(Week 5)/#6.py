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

name_list = {i : len(i) for i in names if len(i) < 7}
print(name_list)
