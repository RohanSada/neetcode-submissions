class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_length = 0
        freq_counter = {}
        for r in range(len(s)):
            freq_counter[s[r]] = freq_counter.get(s[r], 0) + 1
            while freq_counter[s[r]] > 1:
                freq_counter[s[l]]-=1
                if freq_counter[s[l]] == 0:
                    del freq_counter[s[l]]
                l+=1
            max_length = max(max_length, r-l+1)
        return max_length
            
            
            