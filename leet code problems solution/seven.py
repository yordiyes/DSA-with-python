def find_x(nums, k):
    nums.sort()  # Sort the sequence
    
    # If k is 0, any x greater than the maximum element satisfies the condition
    if k == 0:
        return nums[-1] + 1
    
    # If k equals n, the maximum element in the sequence is the desired x
    if k == len(nums):
        return nums[-1]
    
    # Otherwise, return the kth element in the sorted sequence
    return nums[k - 1]

# Read input
n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Find x
x = find_x(nums, k)

# Print result
print(x)
