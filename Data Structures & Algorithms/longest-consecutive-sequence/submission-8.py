class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        if len(nums)==1:
            return 1
        nums = sorted(set(nums))
        prev_value = nums[0]
        max_count = 1
        max_count_list = [1]
        for i in range(1, len(nums)):
            if nums[i] - prev_value == 1:
                max_count += 1
                prev_value = nums[i]
                max_count_list.append(max_count)
            else:
                max_count_list.append(max_count)
                prev_value = nums[i]
                max_count = 1
        print(max_count_list)
        return max(max_count_list)


                


        