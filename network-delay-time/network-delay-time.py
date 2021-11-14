'''sketch
1번 따로 넣기
2번 같이 넣기


'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # graph[u] = [(v, t)] 만들어서 입력값 정리
        graph = [[] for x in range(n+1)]
        
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 거리 리스트 만들기
        # 0x3f3f3f : 10억
        dist = [0x3f3f3f3f for node in range(n+1)]
        dist[0] = 0
        
        # node를 시작노드 u로 하는 dfs
        def dfs(node, arrived):
            # 시작노드 거리가 돌아가
            if dist[node] <= arrived:
                # print(dist)
                return
            
            dist[node] = arrived
                            
            # 시간 누적시키고, 인접노드로 이동해서 dfs 돌려
            for v, w in graph[node]:
                dfs(v, arrived+w)
            
        dfs(k, 0)
        print(dist)
        result = max(dist)
        
        return result if result < 0x3f3f3f else -1
        