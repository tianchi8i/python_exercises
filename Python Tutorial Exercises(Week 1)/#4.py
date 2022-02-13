#4
store_products = ["fruit", "water", "bread", "toilet paper", "soap"]
shopping_list = ["eggs", "tooth paste", "toilet paper", "ice cream", "water"]

for x in shopping_list:
    if x in store_products:
        print(x)
        #toilet paper,water
        break