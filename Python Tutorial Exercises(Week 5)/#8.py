#week 1.1
n = 5
print("\n".join([str(v * v) for v in range(n + 1) if v != 4]))
# def pw(w):
#     print(w)
#     return True
# print([v for v in range(n + 1) if v != 4 and pw(v*v)])

#week 1.2
s = "Tianchi!@&%#Ma"
ss = ""
print("".join([i.upper() if i.islower() else i.lower() if i.isupper() else i for i in s]))

#week 1.3
a = "harry had a little lamb"
b = "ha"
count = 0
c = len(b)
print(len([i for i in range(len(a)) if a[i:i + c] == b]))

#week 1.4
store_products = ["fruit", "water", "bread", "toilet paper", "soap"]
shopping_list = ["eggs", "tooth paste", "toilet paper", "ice cream", "water"]
print([i for i in shopping_list if i in store_products][0])

#week 1.5
x = 8
y = 30
print([i for i in range(x,y) if i % 7 == 0][0])

# week 2.1
x = [["this", "is", "a", "nested"], ["list", "that"], ["will", "be", "printed", "out"]]
print("\n".join([val for sublist in x for val in sublist]))

# week2.2
c = 6
print("\n".join([i * "6" for i in range(1, c + 1)]))

# week2.3
b = 4

print("\n".join([((b - i) * "* " + str(i) + ((i - 1) * f" {i}")) for i in range(b,0,-1)][::-1]))

# week2.4
y = [4, 8, 2, 12, 7, 10]
word1 = "List has an odd number"
word2 = "List does not have an odd number"

odd_number = [i if i % 2 != 0 else word1 for i in y]
print("\n".join([i if i == word1 else word2 for i in odd_number]))


# week 2.5
Ingredient_list = ["rice", "cheese", "pasta", "tomato sauce", "broccoli"]

i = [str(f"{Ingredient_list[i]} and {Ingredient_list[n]}") for i in range(0, len(Ingredient_list)) for n in range(i, len(Ingredient_list)) if i != n]
print("\n".join(i))

# week 3.1
n = 5
factorial = 1
factorial_list=[]
print([factorial_list[-1] for x in range(1, n+1) if not factorial_list.append(x*factorial_list[-1] if factorial_list else 1)][-1])

#week 3.2
x = 20
y = 47
every_number = set([i for i in range(x, y + 1) for a in range(2, i) if i % a != 0])
non_prime_numbers = set([i for i in range(x, y + 1) for a in range(2, i) if i % a == 0])
prime_numbers = list(every_number - non_prime_numbers)
prime_numbers.sort(reverse=False)
print(prime_numbers)
# week3.3
#can't use while loop in list comprehension

# week 3.4
first_names  = ["Tianchi", "Ariel", "Patrick", "Andrew"]
last_names = ["Jane", "Savill", "Yap", "Ma"]
print("\n".join([' '.join(x) for x in zip(first_names,last_names[::-1])]))

