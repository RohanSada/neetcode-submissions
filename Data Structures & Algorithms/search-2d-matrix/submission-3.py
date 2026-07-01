class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        t, b = 0, rows-1
        while t<=b:
            mid = t + ((b-t)//2)
            if target < matrix[mid][0]:
                b = mid - 1
            elif target > matrix[mid][-1]:
                t = mid + 1
            elif matrix[mid][0]<=target<=matrix[mid][-1]:
                l, r = 0, cols-1
                while l <= r:
                    mid_c = l + ((r-l)//2)
                    if matrix[mid][mid_c] < target:
                        l = mid_c + 1
                    elif matrix[mid][mid_c] > target:
                        r = mid_c - 1
                    else:
                        return True
                return False
        return False

        