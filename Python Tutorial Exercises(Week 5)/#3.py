
my_string = "Back in the early 2010s, Andrew has always had a keen interest in cars. So much that in 2018, he spent over 1000000 in cash just to buy his favorite car. In 2019, he sold that car just to buy 5 other cars. However, when covid-19 hit NZ in 2020, he had to sell all but 2 of his cars."
#Find and remove all the commas
for i in my_string:
    if i == ",":
        my_string = my_string.replace(i, "")
#Number list:[2018, 1000000, 2019, 5, 2020, 2]
number_list = [int(s) for s in my_string.split() if s.isdigit()]
#Total number
print(sum(number_list))
