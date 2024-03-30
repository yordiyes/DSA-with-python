def countSwaps(a):
    # Write your code here
    Sorted = False
    swap = 0
    
    while not Sorted:
        Sorted = True
        for i in range(0, len(a) - 1):
            if a[i] > a[i +1]:
                swap += 1
                Sorted = False
                a[i], a[i+1] = a[i+1], a[i] 
                
    print(f'Array is sorted in {swap} swaps.')     
    print("First Element: ", a[0])
    print("Last Element: ", a[-1])
    print(a)

countSwaps([5,3,2,4,1])