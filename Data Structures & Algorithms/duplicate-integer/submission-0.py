class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_list = set(nums)
        if len(set_list) != len(nums):
            return True
        return False
        