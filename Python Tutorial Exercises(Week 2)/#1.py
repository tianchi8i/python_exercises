'''
Print all individual items stored in the nested list x by using two nested for loops.
'''
x = [["this", "is", "a", "nested"], ["list", "that"], ["will", "be", "printed", "out"]]
for i in x:
    for z in i:
        print(z)
