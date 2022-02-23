#4
first_names  = ["Tianchi", "Ariel", "Patrick", "Andrew"]
last_names = ["Jane", "Savill", "Yap", "Ma"]
x = len(last_names)
#for loop 1
for v,b in zip(first_names,last_names[::-1]):
    print(v,b)
#for loop 2  
for i in range(int(x/2)):
    n = last_names[i]
    last_names[i] = last_names[x - i - 1]
    last_names[x - i - 1] = n
#print(last_names)
for v,b in zip(first_names,last_names):
    print(v,b)

#Wile Loop
first_names  = ["Tianchi", "Ariel", "Patrick", "Andrew"]
last_names = ["Jane", "Savill", "Yap", "Ma"]
 # Point x to the last element in list
x = len(last_names) - 1
y = len(first_names)
z = 0

# Iterate till 1st element and keep on decrementing i
while z < y:

    while x >= 0:
        print(first_names[z],last_names[x])
        x -= 1

        z += 1