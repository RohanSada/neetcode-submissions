class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        algorithm:
        lets first make a copy of nums1 and call is nums1_copy. 
        Now that we have a copy, we create a loop with 3 pointers. i, j and idx.
        i iterates through nums1_copy and j iterates through nums2. 
        we compare i and j and compare the min value of these with the idx value. 
        If its lesser than the idx value, add it at idx and iterate idx. 
        '''
        i, j, idx = 0, 0, 0
        nums1_copy = nums1[:m]
        while idx < m+n:
            if j>=n or (i<m and nums1_copy[i]<=nums2[j]):
                nums1[idx] = nums1_copy[i]
                i+=1
            else:
                nums1[idx] = nums2[j]
                j+=1
            idx+=1
        

