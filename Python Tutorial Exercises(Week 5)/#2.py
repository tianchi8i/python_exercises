'''
Take an input string from the command line/terminal, 
and remove all vowels (a, e, i, o, u) from that string using list comprehension. 
Use.lower() to convert the uppercase to lowercase
Then see if the list vowels is in the inputs or not, if can find them in inputs list remove all.
'''
inputs = input("Enter: ")
vowels = ('a', 'e', 'i', 'o', 'u')

outputs = [i for i in inputs if i.lower() not in vowels]
print(''.join(outputs))
