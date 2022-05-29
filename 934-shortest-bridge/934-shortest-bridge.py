class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def change(i, j):
            if min(i, j) < 0 or max(i, j) >= n or grid[i][j] != 1:
                return
            grid[i][j] = 2
            q.append((i, j, 0))
            for dx, dy in moves:
                change(i+dx, j+dy)
        
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        n = len(grid)
        q = []
        found = False
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    change(i, j)
                    found = True
                    break
            if found: break
        
        while q:
            sz = len(q)
            for _ in range(sz):
                i, j, ans = q.pop(0)
                for dx, dy in moves:
                    x, y = i + dx, j + dy
                    if 0 <= x < n and 0 <= y < n:
                        if grid[x][y] == 1:
                            return ans 
                        if grid[x][y] == 0:
                            grid[x][y] = 2
                            q.append((x, y, ans+1))
        return 0