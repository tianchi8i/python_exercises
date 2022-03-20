'''
Extract all numbers from a string text and print the sum of it using list comprehension. 
Ignore punctuation (commas) by use for loop and if i !="," after find them then use .join()
///if want to remove commas and full stops you can use: if i !="," and i != ".".///
joins them into a single string. Now you get a string without commas.
use .isdigit() to find all the numbers in the string then 
use sum to add the Number list:[2018, 1000000, 2019, 5, 2020, 2] all together 
then print the total number out.
'''
my_string = "Back in the early 2010s, Andrew has always had a keen interest in cars. So much that in 2018, he spent over 1000000 in cash just to buy his favorite car. In 2019, he sold that car just to buy 5 other cars. However, when covid-19 hit NZ in 2020, he had to sell all but 2 of his cars."
#Find and remove all the commas
commas = "".join([i for i in my_string if i != ","])
#Number list:[2018, 1000000, 2019, 5, 2020, 2]
#total number
print(sum([int(s) for s in commas.split() if s.isdigit()]))

#  # List comprehension in one line code
print(sum([int(s) for s in ("".join([i for i in my_string if i != ","])).split() if s.isdigit()]))