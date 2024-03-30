def bubbleSort(array):
    sorted = False
    while not sorted:
        sorted = True 
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
            
    return array
two = [3,2,1,0,5,4]
print(bubbleSort(two))
 
# Below code is another way of implementing the buble sort
"""array = [2,5,3,1,4]
condition = True
while condition:
    condition = False
    for i in range(0, len(array)-1):
        if array[i] > array[i+1]:
            array[i], array[i+1] = array[i+1], array[i]
            condition = True
            
print(array)"""