'''
    Find all overlapping matches
    This script takes a given input string a and substring b, 
    made a 'count' container to store the number of times 
    the substring appears in the string.
    as c is the length of the substring b
    It add one a number to 'count' every time the computer find c in a, 
    print 'count' value at the end of the for loop.
'''
a = "harry had a little lamb"
b = "ha" 
count = 0
c = len(b)
for i in range(len(a)):
    if a[i:i+c] == b:
        count += 1
print(count)
