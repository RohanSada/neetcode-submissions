class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        rows, cols = len(grid), len(grid[0])

        queue = deque([])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
        step = 1
        while len(queue)>0:
            n = len(queue)
            for _ in range(n):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = step
                        queue.append((nr, nc))
            step+=1
        


        








        