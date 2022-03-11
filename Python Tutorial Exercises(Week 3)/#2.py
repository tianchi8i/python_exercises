'''
This script prints a list of all prime numbers found between a given range of x and y inclusively. 
This script includes a while loop and a for loop.
The outer loop tells us all the numbers in the given range and 
the inner loop helps us find all prime numbers.
Create a new list 'z' to store the values we find from the inner loop.
'''
x = 20
y = 47
z = []
u = x

# for loop
for i in range(x,y+1):
    for a in range(2,i):
        if i%a == 0:
            break
    else:
        z.append(i)
print(z)

#while loop
while u >= x and u <= y:
    count = 0
    q = 2
    while q <= u//2:
        if u%q == 0:
            count += 1
            break
        q += 1
        
    if count == 0:
        z.append(u)
    u += 1
print(z)
