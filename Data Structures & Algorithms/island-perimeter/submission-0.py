class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        directions = [(1,0), (-1,0), (0,1), (0, -1)]
        visits = set()
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    continue
                if (row, col) in visits:
                    continue
                visits.add((row, col))
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if not 0<=nr<rows or not 0<=nc<cols:
                        perimeter+=1
                    elif grid[nr][nc]==0:
                        perimeter+=1
        return perimeter
        




                
                
        