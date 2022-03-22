'''
This script prints a list of all prime numbers found between a given range of x and y inclusively. 
This script includes a while loop and a for loop.
The outer loop tells us all the numbers in the given range and 
the inner loop helps us find all prime numbers.
Create a new list 'z' to store the values we find from the inner loop.
'''
x = 20
y = 47
prime_number_list = []
u = x

# for loop
for i in range(x,y+1):
    for a in range(2,i):
        if i%a == 0:
            break
    else:
        prime_number_list.append(i)
print(prime_number_list)

Min = 20
Max = 47
i = Min
prime_numbers = []

while i >= Min and i <= Max:
    j = 2
    while j < i:
        if i % j == 0:
            break
        else:
            if j+1 == i:
                prime_numbers.append(i)
        j += 1
    i += 1
print(prime_numbers)