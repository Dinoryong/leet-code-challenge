class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        original = []
        for i in mat:
            for j in i:
                original.append(j)
        if r*c != len(original):
            return mat
        lst = []
        for i in range(0,len(original),c):
            lst.append(original[i:i+c])
        return lst