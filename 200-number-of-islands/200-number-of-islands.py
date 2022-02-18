class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        LAND = '1'
        WATER = '0'
        VISITED = '#'
        rows = len(grid)
        cols = len(grid[0])
        pointer = {
            'row': 0,
            'col': 0
        }
        landsFound = 0
        
        def visitWholeIsland(row, col):
            # find all adjacent land
            # mark them as visited as we go
            grid[row][col] = VISITED
            
            # above
            if row > 0 and grid[row-1][col] == LAND:
                visitWholeIsland(row-1, col)
			  
            # under
            if row < rows-1 and grid[row+1][col] == LAND:
                visitWholeIsland(row+1, col)
                    
            # left
            if col > 0 and grid[row][col-1] == LAND:
                visitWholeIsland(row, col-1)
            
            # right
            if col < cols-1 and grid[row][col+1] == LAND:
                visitWholeIsland(row, col+1)
        
        while pointer['row'] < rows and pointer['col'] < cols:
            row = pointer['row']
            col = pointer['col']
            frame = grid[row][col]
            
            if frame == LAND:
                # when hit land
                # mark as Nth land
                landsFound += 1
                visitWholeIsland(row, col)
            # move it down right
            if col == cols-1:
                pointer['col'] = 0
                pointer['row'] += 1
            else:
                pointer['col'] += 1        
        
        return landsFound