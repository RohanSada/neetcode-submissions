class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}
        for i, n in enumerate(nums):
            complement = target - n
            if n in prev_map:
                return [prev_map[n], i]
            prev_map[complement] = i
            


        