class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        from collections import deque
        queue = deque([])
        max_area = 0

        directions = [(-1,0), (1,0), (0,1), (0,-1)]
        rows, cols = len(grid), len(grid[0])

        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 or (row,col) in visited:
                    continue
                visited.add((row, col))
                queue.append((row, col))
                area = 0
                while len(queue)>0:
                    n = len(queue)
                    for _ in range(n):
                        r, c = queue.popleft()
                        area+=1
                        for dr, dc in directions:
                            nr, nc = r+dr, c+dc
                            if 0<=nr<rows and 0<=nc<cols:
                                if grid[nr][nc] == 1 and (nr, nc) not in visited:
                                    #area+=1
                                    visited.add((nr, nc))
                                    queue.append((nr, nc))
                max_area = max(max_area, area)
        return max_area


        