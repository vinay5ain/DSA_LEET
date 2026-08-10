class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] = True if the current player can win with i stones
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                # Removing j^2 stones makes the opponent lose
                if not dp[i - j * j]:
                    dp[i] = True
                    break
                j += 1

        return dp[n]