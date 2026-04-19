class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # DFS

        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        islands = 0

        def dfs(row, col):
            if row < 0 or row >=rows or col < 0 or col >=cols or grid[row][col] == '0':
                return
            visited.add((row, col))
            for dr, dc in directions:
                nr, nc = row+dr, col+dc
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == '1':
                    if (nr, nc) in visited:
                        continue
                    dfs(nr, nc)
            return

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row, col) not in visited:
                    dfs(row, col)
                    islands+=1
        
        return islands


        # BFS
        '''
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
    '''

                
                

                
                
        