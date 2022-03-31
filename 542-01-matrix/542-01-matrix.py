class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        output = [[math.inf if mat[i][j] != 0 else 0 for j in range(n)] for i in range(m)]

        queue = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))

        distance = 0

        while len(queue) > 0:
            size = len(queue)

            while size > 0:
                size -= 1

                i, j = queue.popleft()

                if mat[i][j] != 0:
                    output[i][j] = distance

                for i, j in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= i < m and 0 <= j < n and (i, j) not in visited:
                        visited.add((i, j))
                        queue.append((i, j))

            distance += 1

        return output