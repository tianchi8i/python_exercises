
'''
This script uses both while loops and for loops to print everyone's full name correctly 
without using list methods like reverse().  
This script uses [::-1] to reverse the' last_names' list and 
uses zip() to merge two lists to one list then print the list out at the end. 

The While loop is pretty much the same. Convert the list first and 
reverse the list by using len(last_names) - 1, then print both values 
by using a nested while loop.
'''
first_names  = ["Tianchi", "Ariel", "Patrick", "Andrew"]
last_names = ["Jane", "Savill", "Yap", "Ma"]
len_last_names = len(last_names)

# for loop
for first_name,last_name in zip(first_names,last_names[::-1]):
    print(first_name,last_name)

#Wile Loop
first_names  = ["Tianchi", "Ariel", "Patrick", "Andrew"]
last_names = ["Jane", "Savill", "Yap", "Ma"]

reversed_last_names = list(reversed(last_names))
number = 0
while number != len(first_names):
        print(first_names[number], reversed_last_names[number])
        number += 1
