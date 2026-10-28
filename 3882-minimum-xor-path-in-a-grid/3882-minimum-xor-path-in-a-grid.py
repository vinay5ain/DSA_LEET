class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        ans = float('inf')
        m, n = len(grid), len(grid[0])
        memo = [[[False] * 1024 for _ in range(n)] for _ in range(m)]

        def dfs(i, j, xor):
            nonlocal ans

            xor ^= grid[i][j]

            if ans == 0:
                return

            if memo[i][j][xor]:
                return

            memo[i][j][xor] = True

            if i == m - 1 and j == n - 1:
                ans = min(ans, xor)
                return

            if i + 1 < m:
                dfs(i + 1, j, xor)

            if j + 1 < n:
                dfs(i, j + 1, xor)

        dfs(0, 0, 0)
        return ans