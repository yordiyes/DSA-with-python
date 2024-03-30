def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i
        while(arr[j-1] > arr[j]) and j > 0:
            # Swap operation
            # arr[j-1], arr[j] = arr[j], arr[j-1]
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp
            j -= 1
            
array = [2,6,5,3,1,4]
insertionSort(array)
print(array)

for i in range(1, len(array)):
    key = i
    while key > 0 and array[key] > array[key - 1]:
        array[key], array[key-1] = array[key - 1], array[key]
        key -= 1
print(array)

