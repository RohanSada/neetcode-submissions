class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        output_list = []
        zero_count = 0
        for i, n in enumerate(nums):
            if n == 0:
                zero_count +=1
            else:
                total_product *= n 
        for i, n in enumerate(nums):
            if n != 0 and zero_count > 0:
                output_list.append(0)
            elif n!=0 and zero_count == 0:
                output_list.append(int(total_product/n))
            elif n == 0 and zero_count == 1:
                output_list.append(int(total_product))
            elif n == 0 and zero_count > 1:
                output_list.append(0)

        return output_list
