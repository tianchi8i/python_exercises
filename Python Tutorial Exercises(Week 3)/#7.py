'''
Solve Week 2 exercises using while loops instead of for loops
'''
#1
x = [["this", "is", "a", "nested"], ["list", "that"], ["will", "be", "printed", "out"]]
def nest_list(x):
    
    new_list = []
    z = 0
    
    while z < len(x):
        if isinstance(x[z], list):
            new_list.extend(nest_list(x[z])) 

        else:
            new_list.append(x[z])
        z += 1

    return new_list

i = 0
while i < len(nest_list(x)):
    print(nest_list(x)[i])
    i += 1

#2
c = 6
d = 1

while d<c+1:
    q=1
    while q <= d:
        print(c, end="")
        q+=1
    d+=1
    print(" ")

#3
x = 4
z = 1
while z <= x:
    
    j = 0
    while j < x-z:
        print("*",end=' ')
        j += 1
        
    k = 0
    while k < z:
        print(z, end=' ')
        k += 1
    z += 1
    print()

#4
y = [4, 8, 2, 12, 7, 10]
i = 0

while(i < len(y)):

    if y[i] % 2 != 0:
        print("List has an odd number")
    else:
        print("List does not have an odd number")
        
    i += 1
