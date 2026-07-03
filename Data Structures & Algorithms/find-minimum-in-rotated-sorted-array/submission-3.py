class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if nums[l] < nums[r]:
            return nums[l]
        while l<r:
            if r-l == 1:
                break
            mid = (l + r)//2
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        return nums[r]
        

            