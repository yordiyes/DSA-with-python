class Solution:
    def check(self, nums: list[int]):
        unsorted = nums[:]  
        unsorted.sort()
        sorted_list = unsorted[:] 
        A = []
        for i in range(len(unsorted)):
            if len(unsorted) <= 3 or len(unsorted) == 4: 
                rotated_index = (i + 3) % len(unsorted)  
            else:
                rotated_index = (i + 2) % len(unsorted)
            A.append(sorted_list[rotated_index]) 
        print(A)
        return A == nums 
soln = Solution()
result = soln.check([3,4,5,1,2])
print(result)