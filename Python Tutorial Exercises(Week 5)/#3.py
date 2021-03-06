'''
Extract all numbers from a string text and print the sum of it using list comprehension. 
use for loop and .split() to split the string.
use if s.rstrip(",.") to remove the remove commas and full stops from the string and find all the number that is in the string by using .isdigit().
use sum to add the Number list:[2018, 1000000, 2019, 5, 2020, 2] all together 
then print the total number out.
'''

my_string = "Back in the early 2010s, Andrew has always had a keen interest in cars. So much that in 2018, he spent over 1000000 in cash just to buy his favorite car. In 2019, he sold that car just to buy 5 other cars. However, when covid-19 hit NZ in 2020, he had to sell all but 2 of his cars."

print(sum([int(s.rstrip(",.")) for s in my_string.split() if s.rstrip(",.").isdigit()]))
