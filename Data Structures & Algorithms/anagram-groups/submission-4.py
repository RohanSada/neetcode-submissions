class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = {}
        for i in strs:
            s_i = ''.join(sorted(i))
            freq_dict[s_i] = freq_dict.get(s_i, [])
            freq_dict[s_i].append(i)
        return list(freq_dict.values())




        