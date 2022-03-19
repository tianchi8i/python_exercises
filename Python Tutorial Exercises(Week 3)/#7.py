'''
Solve Week 2 exercises using while loops instead of for loops
'''
#1
x = [["this", "is", "a", "nested"], ["list", "that"], ["will", "be", "printed", "out"]]
#                0                         1                         2
nested_list_one = 0
nested_list_two = 0
#len(x)=3 and nested_list_one will never greater than 3 becuse there only 3 list in the x list[0,1,2]. So we use '<' in here.
while nested_list_one < len(x):
    #nested_list_two = [ [0,1,2,3], [0,1], [0,1,2,3]  ] . 
    #len(x[nested_list_one]) = 4444(nested list 1 have 4 items and so on),22,4444.
    #nested_list_two will never greater than nested_list_one, so use '<' in here.
    while nested_list_two < len(x[nested_list_one]):
        print(x[nested_list_one][nested_list_two])
        nested_list_two += 1
        #reset loop [1,2,3,4] &[4,4,4,4] if 4 == 4 reset list two and break.
        if nested_list_two == len(x[nested_list_one]):
            nested_list_two = 0
            break
    nested_list_one += 1

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
