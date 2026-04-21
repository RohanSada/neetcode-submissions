class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        # BFS

        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        islands = 0

        def bfs(row, col):
            queue = deque([(row, col)])
            while len(queue)>0:
                n = len(queue)
                for _ in range(n):
                    r, c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == '1':
                            queue.append((nr, nc))
                            grid[nr][nc] = '0'

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    grid[row][col] == '0'
                    bfs(row, col)
                    islands+=1

        return islands
