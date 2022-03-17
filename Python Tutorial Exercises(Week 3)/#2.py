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
# set range
while u >= x and u <= y:
    count = 0
    #q = 2 is used for checking the factor of the number
    # we start dividing by 2. 
    # This is because divide 0 is invalid and any number can be divided by 1.
    # So we will make a variable with the starting value of 2.
    q = 2
    
    #use a while loop to calculate the prime number. 
    # The smallest prime number is 2. the largest factor for q must be 
    # smaller and equal to u/2, and check all integers smaller or equal 
    # or smaller and equal to u/2. 
    while q <= u/2:
        #We are dividing the number by all the numbers using u%q == 0
        if u%q == 0:
            count += 1      
            #The break statement is used to come out of 
            #the loop as soon we get any positive divisor then no further check is required.
            break
        q += 1
    #check the count number
    if count == 0:
        z.append(u)
    u += 1
#printing the prime numbers between x and y
print(z)

Min = 20
Max = 47
prime_numbers = []
i = Min

while i >= Min and i <= Max:
    q = 2

    isPrime = False # for integer = 1
    if i > 1: 
        isPrime = True
    
    while q <= int(i/2):

        if i%q == 0: 
            isPrime = False 
            break
        q += 1
    else:
        if isPrime:
            prime_numbers.append(i)
            if not isPrime:
                print(i)
    i += 1

print(prime_numbers)

