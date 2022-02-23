#2
x = 20
y = 47
z = []
u = x

# for loop
for i in range(x,y+1):
    #20 to 47
    for a in range(2,i):
        if i%a == 0:
            break
    else:
        z.append(i)
print(z)

#while loop
while u >= x and u <= y:
    count = 0
    q = 2
    while q <= u//2:

        if u%q == 0:
            count += 1
            break
        q += 1
        
    if count == 0:
        z.append(u)
    u += 1
print(z)