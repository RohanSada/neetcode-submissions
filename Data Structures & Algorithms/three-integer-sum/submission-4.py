class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Threesum can be thought of as iterative two sum approach. 
        steps: 
        1. we first sort the array
        2. Once we have a sorted array, we then have 3 pointers. 
        3. One loop iterates over all elements and there is another loop which does two sum from the next element of the parent loop. 
        '''
        result = []
        nums.sort()
        for i, a in enumerate(nums):
            l, r = i+1, len(nums)-1
            if i>0 and a==nums[i-1]:
                continue
            while l<r :
                if a + nums[l] + nums[r] < 0:
                    l+=1
                elif a + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    result.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return result
        