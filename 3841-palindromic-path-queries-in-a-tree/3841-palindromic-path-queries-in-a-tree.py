
class LazyPropagationSegmentTree:
    def __init__(self, arr, baseFn, combineFn, applyLazyToValue, combineLazies, tupleNametags=None):
        self.n = len(arr)
        self.arr = arr
        self.tree = [None] * (4 * self.n)
        self.lazy = [None] * (4 * self.n)
        self._combine = combineFn
        self._baseFn = baseFn
        self._applyAggregate = applyLazyToValue
        self._compose = combineLazies
        self.tupleNametags = tupleNametags
        self._build(1, 0, self.n - 1)

    def _build(self, i, tl, tr):
        if tl == tr:
            self.tree[i] = self._baseFn(self.arr[tl])
            return
        tm = (tr + tl) // 2
        self._build(2 * i, tl, tm)
        self._build(2 * i + 1, tm + 1, tr)
        self.tree[i] = self._combine(self.tree[2 * i], self.tree[2 * i + 1])

    def _push(self, i, tl, tr):
        if self.lazy[i] is not None:
            left_child = 2 * i
            right_child = 2 * i + 1
            self.tree[i] = self._applyAggregate(self.lazy[i], self.tree[i])
            if tl != tr:
                if self.lazy[left_child] is None:
                    self.lazy[left_child] = self.lazy[i]
                else:
                    self.lazy[left_child] = self._compose(self.lazy[left_child], self.lazy[i])

                if self.lazy[right_child] is None:
                    self.lazy[right_child] = self.lazy[i]
                else:
                    self.lazy[right_child] = self._compose(self.lazy[right_child], self.lazy[i])

            self.lazy[i] = None

    def _updateRange(self, i, tl, tr, l, r, lazyValue):
        self._push(i, tl, tr)
        if l > tr or r < tl:
            return  # No overlap
        if l <= tl and tr <= r:
            self.lazy[i] = lazyValue
            self._push(i, tl, tr)
            return
        tm = (tl + tr) // 2
        self._updateRange(2 * i, tl, tm, l, r, lazyValue)
        self._updateRange(2 * i + 1, tm + 1, tr, l, r, lazyValue)
        self.tree[i] = self._combine(self.tree[2 * i], self.tree[2 * i + 1])

    def _queryRecurse(self, i, tl, tr, l, r):
        self._push(i, tl, tr)
        if l > tr or r < tl:
            return None  # No overlap
        if l <= tl and tr <= r:
            return self.tree[i]
        tm = (tl + tr) // 2
        if l > tm:
            return self._queryRecurse(2 * i + 1, tm + 1, tr, l, r)
        elif r < tm + 1:
            return self._queryRecurse(2 * i, tl, tm, l, r)

        leftResult = self._queryRecurse(2 * i, tl, tm, l, r)
        rightResult = self._queryRecurse(2 * i + 1, tm + 1, tr, l, r)
        combinedResult = self._combine(leftResult, rightResult)
        return combinedResult

    def updateRange(self, l, r, lazyValue):
        self._updateRange(1, 0, self.n - 1, l, r, lazyValue)

    def query(self, l, r):
        return self._queryRecurse(1, 0, self.n - 1, l, r)

class Lift:
    def __init__(self, root, numNodes, g):
        # g[node] = list of adjacent nodes
        self.root = root
        self.numNodes = numNodes
        self.LOG = max(1, numNodes.bit_length())
        self.depths = [0] * numNodes
        self.up = [[0] * numNodes for _ in range(self.LOG)]

        # O(n log n) - build depths and ancestor table via iterative DFS
        stack = [(root, root, False)]
        while stack:
            node, parent, visited = stack.pop()
            if visited:
                continue
            self.depths[node] = 0 if node == root else self.depths[parent] + 1
            self.up[0][node] = parent
            for k in range(1, self.LOG):
                self.up[k][node] = self.up[k - 1][self.up[k - 1][node]]
            stack.append((node, parent, True))
            for child in g[node]:
                if child != parent:
                    stack.append((child, node, False))

    # O(log n) - get kth ancestor of a, or root if overshooting
    def kthAncestor(self, a, kth):
        for k in range(self.LOG):
            if (kth >> k) & 1:
                a = self.up[k][a]
        return a

    # O(log n) - lowest common ancestor of a and b
    def lca(self, a, b):
        if self.depths[a] < self.depths[b]:
            a, b = b, a
        diff = self.depths[a] - self.depths[b]
        for k in range(self.LOG):
            if (diff >> k) & 1:
                a = self.up[k][a]
        if a == b:
            return a
        for k in range(self.LOG - 1, -1, -1):
            if self.up[k][a] != self.up[k][b]:
                a = self.up[k][a]
                b = self.up[k][b]
        return self.up[0][a]

    # O(log n) - edge distance between a and b
    def pathDist(self, a, b):
        ab = self.lca(a, b)
        return self.depths[a] + self.depths[b] - 2 * self.depths[ab]

    # O(log n) - unique node on all three pairwise paths between a, b, c
    def geodesic(self, a, b, c):
        return self.lca(a, b) ^ self.lca(a, c) ^ self.lca(b, c)

    # O(log n) - kth node on path a->b (1-indexed, a is 1st). returns -1 if out of range
    def kthOnPath(self, a, b, kth):
        ab = self.lca(a, b)
        distA = self.depths[a] - self.depths[ab]
        distB = self.depths[b] - self.depths[ab]
        totalLen = distA + distB + 1
        if kth < 1 or kth > totalLen:
            return -1
        if kth <= distA + 1:
            return self.kthAncestor(a, kth - 1)
        return self.kthAncestor(b, distB - (kth - distA - 1))

    # O(log n) - shortest distance from x to the path a<->b
    def distToPath(self, a, b, x):
        return self.pathDist(self.geodesic(a, b, x), x)

    # O(log n) - checks if x lies on the path a<->b
    def inPath(self, a, b, x):
        return self.geodesic(a, b, x) == x

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        g = [[] for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        lifter = Lift(0, n, g)
        
        label = [0] * n
        timer = 0
        def makeLabel(node, parent):
            nonlocal timer
            label[node] = timer
            timer += 1
            for adjN in g[node]:
                if adjN == parent:
                    continue
                makeLabel(adjN, node)
        makeLabel(0, -1)


        toRoot = [0] * n # toRoot[label] 

        def make(letter):
            return 1 << (ord(letter) - ord('a'))

        def makeXor(node, parent, aboveMask):
            nmask = aboveMask ^ make(s[node])
            toRoot[label[node]] = nmask
            for adjN in g[node]:
                if adjN != parent:
                    makeXor(adjN, node, nmask)
        
        makeXor(0, -1, 0)

        size = [0] * n # size[node]

        
        def dfs(node, parent):
            sizeHere = 1
            for adjN in g[node]:
                if adjN != parent:
                    dfs(adjN, node)
                    sizeHere += size[adjN]
            size[node] = sizeHere
        dfs(0, -1)

        def basefn(mask):
            return mask
        
        def combine(a, b):
            return a ^ b
        
        def applyLazyToValue(lazy, value):
            return lazy ^ value
        
        def combineLazies(l1, l2):
            return l1 ^ l2

        
        arr = [x for x in s]

        st = LazyPropagationSegmentTree(toRoot, basefn, combine, applyLazyToValue, combineLazies)

        res = []

        for q in queries:
            term, a, b = q.split()
            if term == 'update':
                node = int(a)
                old = arr[node]
                l = label[node]
                r = label[node] + size[node] - 1
                st.updateRange(l, r, make(b) ^ make(old))
                arr[node] = b
            else:
                a = int(a)
                b = int(b)
                lca = lifter.lca(a, b)
                l1 = st.query(label[a], label[a])
                l2 = st.query(label[b], label[b])
                l3 = make(arr[lca])
                answer = l1 ^ l2 ^ l3
                res.append(answer.bit_count() <= 1)
        
        return res