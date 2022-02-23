nested_list = ["this", "item", ["is", "a", ["a", "mess"], "needs", "to", ["be", "unwrapped"]], ["into", "a"], "single", ["item"]]
#For loop
def nest_list(nested_list):

    flat_list = []
    # Iterate over all the elements in given list
    for i in nested_list:
        # Check if type of element is list(all the elements)
        if isinstance(i, list):
            # Extend the flat list by adding contents of this element (list)
            flat_list.extend(nest_list(i))
        else:
            # Append/add the elemengt to the list
            flat_list.append(i)    
    return flat_list

print(nest_list(nested_list))

#While loop
def nest_list2(nested_list):
    
    flat_list2 = []
    z = 0
    
    while z < len(nested_list):
        
        if isinstance(nested_list[z], list):

            flat_list2.extend(nest_list2(nested_list[z]))
            
        else:

            flat_list2.append(nested_list[z])
    
        z += 1
    return flat_list2

print(nest_list2(nested_list))
