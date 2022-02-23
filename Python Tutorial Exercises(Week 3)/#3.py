g = 1000
week_number = 0
total_number = 0
s = input()
while s != g:
    #print(s)
    s = input("Enter a number: ")
    #Add one to the week_number list/container, every time Andrew enter a number
    week_number += 1
    #Add the input number to the total list/container
    total_number += int(s)
#Once the 'total number' is greater then 'g'($1000),print the message and break the loop
    if int(total_number) > g: 
        print(f"He has saved enough at week {week_number} with a total of $ {total_number}.")
        break