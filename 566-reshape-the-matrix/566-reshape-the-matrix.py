class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp = []
        matrix = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                temp.append(mat[i][j])
        # print(temp)
        if r*c == len(temp):
            for i in range(0,len(temp),c):
                matrix.append(temp[i:i+c])
            return matrix
        
        # otherwise return the original matrix
        else:
            return mat
 