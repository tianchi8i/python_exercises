'''
this script uses both for loop and while loop to add the name “TROLL” to words that are 5 characters or less, in the given list 'list_of_names'. 
Create a new list 'z' to store the words that satisfy the condition. 

Use the for/while loop and 'i'/'x' to list all the items in the given list 'list_of_names'.

 If len(i) <= 5, add the name "TROLL" after the words that meet the condition and 
 store the old name list and "TROLL" to the new list "z" by the new order.
'''

list_of_names = ["John", "Emmanuel", "Addie", "Karen", "Rickey", "Nadine"]
z =[]
for i in list_of_names:
    if len(i)<=5:

        x = [i,'TROLL']   
    else:
        x = [i]
    z.extend(x)
print(z)

#while loop 
list_of_names = ["John", "Emmanuel", "Addie", "Karen", "Rickey", "Nadine"]
x = 0
z = []

while x < len(list_of_names):

    #get character numbers for each name
    if len(list_of_names[x]) <= 5:
        #print out the number that's less and smaller than 5 characters
        y = [list_of_names[x], 'TROLL']
    else:
        y = [list_of_names[x]]
    z.extend(y)
    x += 1

print(z)
