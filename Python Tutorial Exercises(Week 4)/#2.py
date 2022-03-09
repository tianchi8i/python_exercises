john_smith = {
    "firstname": "john",
    "lastname": "smith",
    "age": 99,
    "company": "Google",
    "children": ["john jr", "jane", "bob"],
}
#john's info
print(list(john_smith.items())[:4])

# wife's info
john_smith["wife"] = {'firstname': 'jane sr', 'lastname': 'smith', 'age': 90}
print(john_smith["wife"])

#mary's info
john_smith['wife']['children'] = [{'firstname': 'mary', 'lastname': 'smith', 'age': 12, 'parent': 'jane sr smith'}]
for i in john_smith['wife']['children']:
    print(i)

#children’s info
john_smith.update(
        {'children': 
            [{'firstname': 'john jr', 'lastname': 'smith', 'age': 9, 'favourite_fruit': 'apple', 'parent': 'john smith and jane sr smith'}, 
            {'firstname': 'jane', 'lastname': 'smith', 'age': 6, 'favourite_fruit': 'orange', 'parent': 'john smith and jane sr smith'},
            {'firstname': 'bob', 'lastname': 'smith', 'age': 1, 'favourite_fruit': 'banana', 'parent': 'john smith'}]
        }
    )

for i in john_smith["children"]:
    print(i)
    