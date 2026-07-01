class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people)-1
        boats = 0
        while l<=r:
            if l==r:
                boats+=1
                l+=1
                r-=1
                continue
            if people[r] + people[l] > limit:
                boats+=1
                r-=1
            elif people[r] + people[l] <= limit:
                boats+=1
                l+=1
                r-=1
        return boats


            