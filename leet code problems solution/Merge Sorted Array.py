def merge( nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        result = []
        for i in range(m):
            for j in range(n):
                if nums1[i] <= nums2[j]:
                    result.append(nums1[i])
                else:
                    result.append(nums2[j])
                    
        return result
                    
print(merge([1,2,3,0,0,0], 6,[2,5,6],3))