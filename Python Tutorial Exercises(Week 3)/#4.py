
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
x = len(last_names)
#for loop
for v,b in zip(first_names,last_names[::-1]):
    print(v,b)

#Wile Loop
first_names  = ["Tianchi", "Ariel", "Patrick", "Andrew"]
last_names = ["Jane", "Savill", "Yap", "Ma"]

x = len(last_names) - 1
y = len(first_names)
z = 0

while z < y:

    while x >= 0:
        print(first_names[z],last_names[x])
        
        x -= 1
        z += 1
