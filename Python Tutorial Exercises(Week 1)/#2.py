#2
s = "Tianchi Ma"
ss = ""
for i in s:
    if i.islower():
        x = i.upper()
    elif i.isupper():
        x = i.lower()
    elif i.isspace():
        x = " "

    ss += x
print(ss)
