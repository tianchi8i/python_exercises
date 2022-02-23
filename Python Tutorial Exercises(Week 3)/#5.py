list_of_names = ["John", "Emmanuel", "Addie", "Karen", "Rickey", "Nadine"]
z =[]
for i in list_of_names:
    if len(i)<=5:
        #print(list_of_names.index(i))
        #0,2,3
        #x = ['TROLL', i]
        x = [i,'TROLL']   
    else:
        x = [i]
    #print(x) ['John', 'TROLL'] ['Emmanuel'] ['Addie', 'TROLL'] ['Karen', 'TROLL'] ['Rickey'] ['Nadine']
    z.extend(x)
print(z)

#while loop 
list_of_names = ["John", "Emmanuel", "Addie", "Karen", "Rickey", "Nadine"]
x = 0
z = []

while x < len(list_of_names):
    #print(list_of_names[x])
    #get all the name
    
    #print(len(list_of_names[x]))
    #get character numbers for each name
    if len(list_of_names[x]) <= 5:
        #print(len(list_of_names[x]))
        #print out the number that's less and smaller than 5 characters
        y = [list_of_names[x], 'TROLL']
    else:
        y = [list_of_names[x]]
    z.extend(y)
    x += 1

print(z)
