'''
Use nested for loop and range to find the different food combinations.
The outer loop tells us the first item we needed and the inner loop tells us the second item we needed. 
If the outer loop and the inner loop have the same value/item skip it by using if m == u: continue.
'''
Ingredient_list = ["rice","cheese", "pasta", "tomato sauce", "broccoli"]
for m in range(0, len(Ingredient_list)):
    for u in range(m, len(Ingredient_list)):
        if m == u:
            continue
        print(Ingredient_list[m], "and", Ingredient_list[u])
