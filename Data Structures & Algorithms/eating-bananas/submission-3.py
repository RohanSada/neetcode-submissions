class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            res = 0
            for i in piles:
                res += math.ceil(i / k)
                if res > h:
                    return False
            return True

        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = l + ((r-l)//2)
            if check(mid):
                r = mid - 1
                res = min(mid, res)
            else:
                l = mid + 1
        return res

