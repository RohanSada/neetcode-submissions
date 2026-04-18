class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = {}

        for i in range(len(nums)):
            if nums[i] in complement_map:
                return [min(i, complement_map[nums[i]]), max(i, complement_map[nums[i]])]
            complement = target - nums[i]
            complement_map[complement] = i

            


        