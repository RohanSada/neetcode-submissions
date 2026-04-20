class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        from collections import deque
        queue = deque([])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row, col))
        visited = set()
        step = 1
        while len(queue)>0:
            n = len(queue)
            for _ in range(n):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] != -1 and grid[nr][nc] == 2147483647:
                        queue.append((nr, nc))
                        grid[nr][nc] = step
            step+=1
        








        