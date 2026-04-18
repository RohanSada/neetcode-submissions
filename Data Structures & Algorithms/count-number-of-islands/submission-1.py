class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque

        queue = deque([])
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '0' or (row, col) in visited:
                    continue
                islands+=1
                queue.append((row, col))
                while len(queue)>0:
                    n = len(queue)
                    for _ in range(n):
                        r, c = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = r+dr, c+dc
                            if 0<=nr<rows and 0<=nc<cols:
                                if grid[nr][nc] == '1' and (nr, nc) not in visited:
                                    visited.add((nr, nc))
                                    queue.append((nr, nc))
        return islands


                

        
                                


                
                

                
                
        