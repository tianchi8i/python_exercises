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
list_one = 6
list_two = 1

while list_two<list_one+1:
    number = 1
    while number <= list_two:
        print(list_one, end="")
        number += 1
    list_two += 1
    print(" ")

#3
range1 = 4
range2 = 1
while range2 <= range1:
    
    number1 = 0
    while number1 < range1 - range2:
        print("*",end=' ')
        number1 += 1
        
    number2 = 0
    while number2 < range2:
        print(range2, end=' ')
        number2 += 1
    range2 += 1
    print()

#4
list1 = [4, 8, 2, 12, 7, 10]
item = 0

while(item < len(list1)):

    if list1[item] % 2 != 0:
        print("List has an odd number")
    else:
        print("List does not have an odd number")
        
    item += 1
