'''
This script takes an inputs number 's' and stores the number to the 'total_number' list 
and adds a number to the 'week_number' list to count the weeks. When the 'total_number' 
is greater than the goal then print the number of weeks that have passed and 
the final amount he has saved once the goal has been reached.
'''

g = 1000
week_number = 0
total_number = 0
s = input()
while s != g:   

    s = input("Enter a number: ")
    #Add one to the week_number list/container, every time Andrew enter a number
    week_number += 1
    #Add the input number to the total list/container
    total_number += int(s)
    #Once the 'total number' is greater then 'g'($1000),print the message and break the loop
    if int(total_number) > g: 
        print(f"He has saved enough at week {week_number} with a total of $ {total_number}.")
        break
