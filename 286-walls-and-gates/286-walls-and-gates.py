class Solution:
    def wallsAndGates(self, rooms):
        n, m, gates = len(rooms), len(rooms[0]), []

        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    gates.append((i,j))


        while gates:
            x, y = gates.pop(0)

            for nx, ny in [[x+1,y],[x-1,y],[x,y-1],[x,y+1]]:
                if nx < 0 or nx >= n or ny < 0 or ny >= m or rooms[nx][ny] != 2**31 - 1:
                    continue
                else:
                    rooms[nx][ny] = rooms[x][y] + 1
                    gates.append((nx,ny))