nums = [8,1,2,2,3]
count = 0
a = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if  nums[j] < nums[i]:
            count += 1
    a.append(count)
    count = 0
    
print(a)