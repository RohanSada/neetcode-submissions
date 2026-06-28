class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True

        l, r = 0, len(s)-1
        while l<=r:
            if s[l] != s[r]:
                left_check = isPalindrome(l+1, r)
                right_check = isPalindrome(l, r-1)
                if left_check or right_check:
                    return True
                else:
                    return False
            l+=1
            r-=1
        return True
        