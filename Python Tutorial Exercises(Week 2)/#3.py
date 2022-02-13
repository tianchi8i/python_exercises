b = 4
for i in range(1, b+1):
    
    for j in range(b, 0, -1):
        num = i
        if j > i:
            print("*", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print()