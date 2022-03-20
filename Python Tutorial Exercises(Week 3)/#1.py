'''
This script takes in an argument n and prints the factorial output, 
without using any math libraries. A factorial of a number is represented by n!, 
for example, 3! = 3 x 2 x 1 = 6. 
This script includes a while loop and a for loop.
'''
n = 5
factorial = 1
#1 for loop
for i in range(1, n+1):
    factorial=factorial*i
print(factorial)

#1 while loop

while n > 0:
    factorial = factorial * n
    n = n - 1
print(factorial)
