class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            mid_idx = l + ((r-l)//2)
            mid_val = nums[mid_idx]
            if target > mid_val:
                l = mid_idx + 1
            elif target < mid_val:
                r = mid_idx - 1
            else:
                return mid_idx
        return -1 