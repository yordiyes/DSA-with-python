# def moveZeroes( nums: list[int]) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     sort = sorted(nums)
#     # print(sort)
#     for i in range(1, len(nums)):
#         j=i
#         while sort[j-1] < sort[j] and sort[j-1]==0:
#             sort[j], sort[j-1] = sort[j-1] , sort[j]
#             j-=1
#     print(sort)
        
# nums = [0,1,0,3,12]
# moveZeroes(nums)
array = [0,1,0,3,12]
# Sort the array with zeros moved to the end
sorted_array = sorted(array, key=lambda x: (x == 0, x))
print(sorted_array)