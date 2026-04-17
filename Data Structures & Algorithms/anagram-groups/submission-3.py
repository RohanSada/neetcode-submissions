class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        prev_dict = {}
        for i, n in enumerate(strs):
            sorted_n = tuple(sorted(n))
            if sorted_n in prev_dict:
                prev_dict[sorted_n].append(n)
            else:
                prev_dict[sorted_n] = [n]
        return list(prev_dict.values())

        