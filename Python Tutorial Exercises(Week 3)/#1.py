#1
n = 5
x = 1

#1 for loop
#1-5
for i in range(1, n+1):
    x=x*i
print(x)

#1 while loop
while n > 0:
    #1x5,2x5,3x5,4x5,5x5
    x = x * n
    #4,3,2,1
    n = n - 1
print(x)