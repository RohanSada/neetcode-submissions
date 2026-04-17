class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        output_list = []
        for i, n in enumerate(nums):
            mydict[n] = 1 + mydict.get(n, 0)
        output_list = []
        for i in mydict:
            output_list.append([mydict[i], i])
        output_list.sort(reverse=True)
        top_k = output_list[:k]
        final_output = []
        for i in top_k:
            final_output.append(i[1])
        return final_output


        

            
        