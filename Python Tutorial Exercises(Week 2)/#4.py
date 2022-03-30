'''
Check if a given list y contains an odd number. 
Iterate each element in the list using for loop and 
check if num % 2 != 0. If the condition satisfies, 
then print "List has an odd number" 
otherwise print "List does not have an odd number".
'''
y = [4, 8, 2, 12, 7, 10]

for p in y:
   if p % 2 != 0:
      print("List has an odd number")
      break
else:
   print("List does not have an odd number")