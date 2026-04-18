class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r):
            while l<r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        l, r = 0, len(s)-1
        if l == r == 0:
            return True
        while l<r:
            if s[l] != s[r]:
                left_drop = isPalindrome(l+1, r)
                right_drop = isPalindrome(l, r-1)
                return left_drop or right_drop
            l+=1
            r-=1
        return True



        


        