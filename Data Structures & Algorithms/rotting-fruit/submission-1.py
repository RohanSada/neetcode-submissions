class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1, 0), (0,1), (0,-1)]

        queue = deque([])
        len_fresh = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    len_fresh+=1
        if len_fresh == 0:
            return 0
            
        minute = -1
        while len(queue)>0:
            n = len(queue)
            for _ in range(n):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        grid[nr][nc] = 2
                        len_fresh-=1
            minute+=1
        return minute if len_fresh == 0 else -1
        
                
        
        