class Solution:
    def __init__(self):
        self.ans = []
        
    def dfs(self, tree, toKill):
        for nxt in tree[toKill]:
            self.dfs(tree, nxt)
            
        self.ans.append(toKill)
        tree[toKill] = []
    
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        p2c = collections.defaultdict(list)
        N = len(pid)
        for i in range(N):
            parent = ppid[i]
            child = pid[i]
            p2c[parent].append(child)
            
        self.dfs(p2c, kill)
        return self.ans