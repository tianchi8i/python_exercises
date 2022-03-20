'''
Take an input string from the command line/terminal, 
and remove all vowels (a, e, i, o, u) from that string using list comprehension. 
Use.lower() to convert the uppercase to lowercase
Then see if the list vowels is in the inputs or not, if can find them in inputs list remove all.
'''
inputs = 'This is some input string'
vowels = ('A', 'E', 'I', 'O', 'U')

vowels = ''.join(vowels).lower()
outputs = [i for i in inputs if i not in vowels]
print(''.join(outputs))

# List comprehension in one line code
print(''.join([i for i in inputs if i not in ''.join(vowels).lower()]))
