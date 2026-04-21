class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        queue = deque([])

        fresh_fruit = 0
        minute = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh_fruit +=1

        while len(queue)>0 and fresh_fruit > 0:
            n = len(queue)
            for _ in range(n):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh_fruit-=1
            minute+=1
        if fresh_fruit == 0:
            return minute
        return -1
        
