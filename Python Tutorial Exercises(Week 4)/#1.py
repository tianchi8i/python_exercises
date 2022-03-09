john_smith = {
    "firstname": "john",
    "lastname": "smith",
    "age": 99,
    "company": "Google",
    "children": ["john jr", "jane", "bob"],
}

john_smith.update(
        {'children': 
            [{'firstname': 'john jr', 'lastname': 'smith', 'age': 9, 'favourite_fruit': 'apple'}, 
            {'firstname': 'jane', 'lastname': 'smith', 'age': 6, 'favourite_fruit': 'orange'},
            {'firstname': 'bob', 'lastname': 'smith', 'age': 1, 'favourite_fruit': 'banana'}]
        }
    )

print(john_smith)
for i in john_smith["children"]:
    print(i)
    