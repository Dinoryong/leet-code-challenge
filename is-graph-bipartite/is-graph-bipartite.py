class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        
        def dfs(node):
            for i in graph[node]:
                if i not in color:
                    color[i] = -color[node]
                    
                else:
                    if (color[i] == color[node]):
                        return False
                    # 둘의 노드의 색깔이 다르다
                    else:
                        continue
                if not dfs(i):
                    return False
                
            return True
        
        for j in range(len(graph)):
            # 노드 색깔이 없으면 default 1로 채워
            if j not in color:
                color[j] = 1
            
            # dfs 
            if not dfs(j):
                return False
            
        return True
                    
      