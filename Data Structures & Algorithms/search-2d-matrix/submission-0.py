class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        1. keep two pointers for the first row and the last row. 
        2. Take the first element of the middle row (first + ((last-first)//2))
        3. Check if the element is greater or lesser than this. 
        4. If its greater than, check the middle row 
        '''
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows-1
        while top <= bottom:
            mid = ((bottom + top)//2)
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][cols-1]:
                top = mid + 1
            else:
                break
        row = (top + bottom)//2
        l, r = 0, cols-1
        while l<=r:
            m = (l+r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else: 
                return True
        return False



        




        