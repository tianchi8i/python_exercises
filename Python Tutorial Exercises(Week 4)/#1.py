'''
This script uses the dictionary john_smith from the tutorial example, 
loop through the list of his children and convert all of them into dictionaries as well. 
Use the function .update() to add the children's attributes to john_smith's dictionary.
The final output prints the john_smith dictionary and his list of children with 
their attributes by print(john_smith) and using a for loop.

'''
john_smith = {
    "firstname": "john",
    "lastname": "smith",
    "age": 99,
    "company": "Google",
    "children": ["john jr", "jane", "bob"],
}

john_smith.update(
        {'children': 
            [{'firstname': 'john jr', 'lastname': john_smith['lastname'], 'age': 9, 'favourite_fruit': 'apple'}, 
            {'firstname': 'jane', 'lastname': john_smith['lastname'], 'age': 6, 'favourite_fruit': 'orange'},
            {'firstname': 'bob', 'lastname': john_smith['lastname'], 'age': 1, 'favourite_fruit': 'banana'}]
        }
    )

print(john_smith)
for i in john_smith["children"]:
    print(i)
    