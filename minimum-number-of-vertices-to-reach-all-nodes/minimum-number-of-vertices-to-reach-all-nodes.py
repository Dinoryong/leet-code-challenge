class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        fr = []
        to = []
        for node in edges:
            fr.append(node[0])
            to.append(node[1])
        
        fr=set(fr)
        to=set(to)
        
        result = fr - to
        result = list(result)
        return result