class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        pre_sum = list(accumulate(stones))
        f = pre_sum[len(stones) - 1]
        for i in range(len(stones) - 2, 0, -1):
            f = max(f, pre_sum[i] - f)
        return f

############

# 1872. Stone Game VIII
# https://leetcode.com/problems/stone-game-viii/

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        for i in range(1, n):
            stones[i] += stones[i-1]
            
        dp = stones[-1]

        for i in range(n - 2, 0, -1):
            dp = max(dp, stones[i] - dp)
            
        return dp