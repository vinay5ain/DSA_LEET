
class LazySegmentTree:
    def __init__(self, n, kMod):
        self.n = n
        self.kMod = kMod
        self.lazy = [0] * (4 * n)
        self.sums = [0] * (4 * n)
        self.squaredSums = [0] * (4 * n)

    def updateRange(self, l, r):
        self._updateRange(0, 0, self.n - 1, l, r)

    def propagate(self, i, l, r):
        gap = r - l + 1
        mod = self.kMod
        lazy = self.lazy[i]

        self.squaredSums[i] = (
            self.squaredSums[i]
            + 2 * lazy * self.sums[i]
            + lazy * lazy * gap
        ) % mod

        self.sums[i] = (self.sums[i] + lazy * gap) % mod

        if l < r:
            self.lazy[2 * i + 1] += lazy
            self.lazy[2 * i + 2] += lazy

        self.lazy[i] = 0

    def getTreeSquaredSums(self):
        return self.squaredSums[0]

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

        self._updateRange(2 * i + 1, start, mid, l, r)
        self._updateRange(2 * i + 2, mid + 1, end, l, r)

        self.sums[i] = (
            self.sums[2 * i + 1] + self.sums[2 * i + 2]
        ) % self.kMod

        self.squaredSums[i] = (
            self.squaredSums[2 * i + 1]
            + self.squaredSums[2 * i + 2]
        ) % self.kMod


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        n = len(nums)

        ans = 0
        lastSeen = {}
        tree = LazySegmentTree(n, MOD)

        for r, num in enumerate(nums):
            l = lastSeen[num] + 1 if num in lastSeen else 0

            tree.updateRange(l, r)
            lastSeen[num] = r

            ans = (ans + tree.getTreeSquaredSums()) % MOD

        return ans