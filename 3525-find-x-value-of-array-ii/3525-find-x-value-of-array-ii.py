class Node:
    def __init__(self):
        self.remain = [0] * 5
        self.prod = 1


class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree = [Node() for _ in range(4 * self.n)]
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, cur, left, right):
        if left == right:
            self.tree[cur].remain[nums[left]] = 1
            self.tree[cur].prod = nums[left]
            return

        mid = (left + right) // 2

        self.build(nums, 2 * cur + 1, left, mid)
        self.build(nums, 2 * cur + 2, mid + 1, right)

        self.tree[cur] = self.merge(
            self.tree[2 * cur + 1],
            self.tree[2 * cur + 2]
        )

    def update(self, i, val):
        self._update(0, 0, self.n - 1, i, val)

    def _update(self, tree_index, lo, hi, i, val):
        if lo == hi:
            self.tree[tree_index] = Node()
            self.tree[tree_index].remain[val] = 1
            self.tree[tree_index].prod = val
            return

        mid = (lo + hi) // 2

        if i <= mid:
            self._update(
                2 * tree_index + 1,
                lo,
                mid,
                i,
                val
            )
        else:
            self._update(
                2 * tree_index + 2,
                mid + 1,
                hi,
                i,
                val
            )

        self.tree[tree_index] = self.merge(
            self.tree[2 * tree_index + 1],
            self.tree[2 * tree_index + 2]
        )

    def query(self, i, j):
        return self._query(0, 0, self.n - 1, i, j)

    def _query(self, tree_index, lo, hi, i, j):
        # Completely inside
        if i <= lo and hi <= j:
            return self.tree[tree_index]

        # Completely outside
        if j < lo or hi < i:
            return Node()

        mid = (lo + hi) // 2

        left = self._query(
            2 * tree_index + 1,
            lo,
            mid,
            i,
            j
        )

        right = self._query(
            2 * tree_index + 2,
            mid + 1,
            hi,
            i,
            j
        )

        return self.merge(left, right)

    def merge(self, left, right):
        node = Node()

        node.prod = (left.prod * right.prod) % self.k

        for i in range(self.k):
            node.remain[i] = left.remain[i]

        for i in range(self.k):
            node.remain[(i * left.prod) % self.k] += right.remain[i]

        return node


class Solution:
    def resultArray(self, nums, k, queries):
        # Take all values modulo k
        for i in range(len(nums)):
            nums[i] %= k

        # query[1] is also a value
        for query in queries:
            query[1] %= k

        n = len(nums)

        tree = SegmentTree(nums, k)

        ans = []

        for query in queries:
            index = query[0]
            value = query[1]
            start = query[2]
            x = query[3]

            tree.update(index, value)

            result = tree.query(start, n - 1)

            ans.append(result.remain[x])

        return ans