'''
This script takes a given input number x, using the reverse for loop and a nested for loop 
to print the downward triangle pattern with stars and a number triangle pattern together. 

The outer loop tells us the number of rows, and the inner loop tells us 
the column needed to print the pattern.

Downward triangle pattern
Where numbers get reduced in each iteration, and on the last row, 
it shows only one number. We use stars to replace the numbers here. 

number triangle pattern
In this number pattern, we display a single digit on the first row, 
the next two digits of the second row, And the following three numbers 
on the third row and this process will repeat till the number of rows is reached.
'''
b = 4
for i in range(1, b+1):
    
    for j in range(b, 0, -1):
        num = i
        if j > i:
            print("*", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print()
    