class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # replace every 0 in nums1 with element from nums2 and then sort the entire array. 
        # By doing this, its going to be O(nlogn).
        nums1[m:] = nums2[:n]
        nums1.sort() 
        