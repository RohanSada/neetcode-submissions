class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows-1
        while top<=bottom:
            mid_row = top + ((bottom-top)//2)
            if target < matrix[mid_row][0]:
                bottom = mid_row-1
            elif target > matrix[mid_row][-1]:
                top = mid_row+1
            else:
                break
        mid_row = top + ((bottom-top)//2)
        left, right = 0, cols-1
        while left<=right:
            mid_idx = left + ((right-left)//2)
            if target < matrix[mid_row][mid_idx]:
                right = mid_idx-1
            elif target > matrix[mid_row][mid_idx]:
                left = mid_idx+1
            else:
                return True
        return False