class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l, r = 0, max(piles)-1
        final_k = r+1
        while l<=r:
            mid_val = ((l + r)//2)+1
            h_c = 0
            for i in piles:
                if mid_val <= i:
                    h_c += math.ceil(i/mid_val)
                else: 
                    h_c += 1
            if h_c > h:
                l = mid_val
            elif h_c <= h:
                final_k = min(final_k, mid_val)
                r = mid_val - 2
        return final_k






        
        