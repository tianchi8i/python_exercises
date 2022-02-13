Ingredient_list = ["rice","cheese", "pasta", "tomato sauce", "broccoli"]
for m in range(0, len(Ingredient_list)):

    for u in range(m, len(Ingredient_list)):
        if m == u:
            continue
        print(Ingredient_list[m], "and", Ingredient_list[u])