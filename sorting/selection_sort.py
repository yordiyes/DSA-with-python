def selectionSort(array):
    for i in range(0, len(array) - 1):
        currenMinIndex = i
        for j in range(i+1, len(array)):
            if array[currenMinIndex] > array[j]:
                currenMinIndex = j
        array[i], array[currenMinIndex] = array[currenMinIndex], array[i]
        
numbers = [3,6,1,5,2,4]
selectionSort(numbers)
print(numbers)
