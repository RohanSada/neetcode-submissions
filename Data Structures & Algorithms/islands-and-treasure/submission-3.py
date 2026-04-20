class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def bfs(row, col):
            visited = set()
            from collections import deque
            queue = deque([(row, col)])
            steps = 0
            while len(queue)>0:
                n = len(queue)
                for _ in range(n):
                    r, c = queue.popleft()
                    if grid[r][c] == 0:
                        return steps
                    visited.add((r, c))
                    for dr, dc in directions:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] != -1 and (nr, nc) not in visited:
                            queue.append((nr, nc))
                steps+=1
            return None


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == -1 or grid[row][col] == 0:
                    continue
                else:
                    val = bfs(row, col)
                    if val:
                        grid[row][col] = val


        