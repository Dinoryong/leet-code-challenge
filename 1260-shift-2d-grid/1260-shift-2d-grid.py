class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        num_rows, num_cols = len(grid), len(grid[0])

        for _ in range(k):
            # Create a new grid to copy into.
            new_grid = [[0] * num_cols for _ in range(num_rows)]

            # Case 1: Move everything not in the last column.
            for row in range(num_rows):
                for col in range(num_cols - 1):
                    new_grid[row][col + 1] = grid[row][col]

            # Case 2: Move everything in last column, but not last row.
            for row in range(num_rows - 1):
                 new_grid[row + 1][0] = grid[row][num_cols - 1]

            # Case 3: Move the bottom right.
            new_grid[0][0] = grid[num_rows - 1][num_cols - 1]

            grid = new_grid

        return grid