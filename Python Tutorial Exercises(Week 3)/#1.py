'''
This script takes in an argument n and prints the factorial output, 
without using any math libraries. A factorial of a number is represented by n!, 
for example, 3! = 3 x 2 x 1 = 6. 
This script includes a while loop and a for loop.
'''
n = 5
x = 1
#1 for loop
for i in range(1, n+1):
    x=x*i
print(x)

#1 while loop

while n > 0:
    x = x * n
    n = n - 1
print(x)
