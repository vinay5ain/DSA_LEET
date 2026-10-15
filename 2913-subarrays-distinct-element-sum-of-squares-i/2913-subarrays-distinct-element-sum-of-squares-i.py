class LazySegmentTree:
    def __init__(self, n, kMod):
        self.n = n
        self.kMod = kMod
        self.lazy = [0] * (4 * n)
        self.sums = [0] * (4 * n)
        self.squaredSums = [0] * (4 * n)

    def propagate(self, i, l, r):
        gap = r - l + 1
        mod = self.kMod

        self.squaredSums[i] = (
            self.squaredSums[i]
            + 2 * self.lazy[i] * self.sums[i]
            + self.lazy[i] * self.lazy[i] * gap
        ) % mod

        self.sums[i] = (
            self.sums[i] + self.lazy[i] * gap
        ) % mod

        if l < r:
            self.lazy[i * 2 + 1] += self.lazy[i]
            self.lazy[i * 2 + 2] += self.lazy[i]

        self.lazy[i] = 0

    def updateRange(self, l, r):
        self._updateRange(0, 0, self.n - 1, l, r)

    def _updateRange(self, i, start, end, l, r):
        if self.lazy[i] > 0:
            self.propagate(i, start, end)

        if end < l or start > r:
            return

        if start >= l and end <= r:
            self.lazy[i] = 1
            self.propagate(i, start, end)
            return

        mid = (start + end) // 2

        self._updateRange(i * 2 + 1, start, mid, l, r)
        self._updateRange(i * 2 + 2, mid + 1, end, l, r)

        self.sums[i] = (
            self.sums[i * 2 + 1] + self.sums[i * 2 + 2]
        ) % self.kMod

        self.squaredSums[i] = (
            self.squaredSums[i * 2 + 1]
            + self.squaredSums[i * 2 + 2]
        ) % self.kMod

    def getTreeSquaredSums(self):
        return self.squaredSums[0]


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        ans = 0
        lastSeen = {}

        tree = LazySegmentTree(n, MOD)

        for r in range(n):
            l = lastSeen[nums[r]] + 1 if nums[r] in lastSeen else 0

            tree.updateRange(l, r)

            lastSeen[nums[r]] = r

            ans = (ans + tree.getTreeSquaredSums()) % MOD

        return ans