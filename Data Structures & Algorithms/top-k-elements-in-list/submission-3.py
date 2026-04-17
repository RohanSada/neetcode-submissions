class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        output_list = []
        for i, n in enumerate(nums):
            mydict[n] = 1 + mydict.get(n, 0)
        output_list = []
        for i in mydict:
            output_list.append([mydict[i], i])
        output_list.sort()
        res = []
        while len(res) < k:
            res.append(output_list.pop()[1])
        return res
        

        

            
        