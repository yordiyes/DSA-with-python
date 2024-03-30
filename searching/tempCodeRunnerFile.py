def binSearch(A,left,right,key):
    while left <= right:
        mid = (left+right)//2
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            left = mid + 1
        else:
            #key , A[mid]
            right = mid - 1
    return -1

A = [11,23,33,45,65,100,222,344]
key = 45
print(binSearch(A,0,len(A)-1),key)