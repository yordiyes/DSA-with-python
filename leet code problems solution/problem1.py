a = [3,4,5,1,2]
b = []
i=0
while  i < 5:
    b[i]=a[(i+3) % len(a)]
    print(b)