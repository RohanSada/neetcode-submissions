class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_dict = {}
        for i in range(len(nums)):
            if nums[i] in complement_dict:
                return [complement_dict[nums[i]], i]
            complement = target - nums[i]
            complement_dict[complement] = i
