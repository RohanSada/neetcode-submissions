class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        fourSum with 4 loops. This solution uses 4 loops and not a generic solution. 
        For a generic solution we need to use recursion instead of calling multiple loops. 
        steps: 
        1. First loop fixes a specific index
        2. Second loop fixes a specific index
        3. The thrid loop does 2 sum to get the other two values. 
        '''
        result = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, n):
                if j>i+1 and nums[j-1] == nums[j]:
                    continue
                l, r = j+1, n-1
                while l < r:
                    fsum = nums[i] + nums[j] + nums[l] + nums[r]
                    if fsum > target:
                        r-=1
                    elif fsum < target:
                        l+=1
                    else:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        l+=1
                        while l < r and nums[l] == nums[l-1]:
                            l+=1
                        r-=1
        return result



