class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        t=[[0 for i in range(amount+1)] for j in range(n+1)]
        for i in range(1,amount+1):
            t[0][i]=float(inf)-1
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    t[i][j]=min(t[i][j-coins[i-1]]+1,t[i-1][j])
                else:
                    t[i][j]=t[i-1][j]
        # print(t)
        if t[n][amount]==float(inf)-1:
            return -1
        return t[n][amount]