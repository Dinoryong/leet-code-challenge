class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        l, r = 0, len(mat[0]) - 1

        while l <= r:
            # Select a mid column from n columns. O(logn) operation, n is the number of lements in the row
            m = l + (r - l) // 2
            maxLoc, maxVal = [0, m] ,mat[0][m]
            # find the global max in the mid column - O(m) operation, m is the number of elements in the column
            for val in range(1, len(mat)):
                if mat[val][m] > maxVal:
                    maxLoc, maxVal = [val, m], mat[val][m]
            
            row, col = maxLoc
            maxColumnVal = mat[row][col]
            
            # check left cell and compare the value to maxColumnVal
            if col in range(1, len(mat[0])) and mat[row][col - 1] > maxColumnVal:
                # we need to go left
                r = m - 1
            # check right cell and compare the value to maxColumnVal
            elif col in range(0, len(mat[0]) - 1) and mat[row][col + 1] > maxColumnVal:
                # we need to go right
                l = m + 1
            else:
                return maxLoc