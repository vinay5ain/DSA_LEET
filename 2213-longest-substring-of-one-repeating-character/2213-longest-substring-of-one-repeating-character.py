class SegmentTreeNode:
    def __init__(
        self,
        lo,
        hi,
        max_letter,
        prefix_letter,
        suffix_letter,
        max_length,
        prefix_length,
        suffix_length,
        left=None,
        right=None
    ):
        self.lo = lo
        self.hi = hi
        self.max_letter = max_letter
        self.prefix_letter = prefix_letter
        self.suffix_letter = suffix_letter
        self.max_length = max_length
        self.prefix_length = prefix_length
        self.suffix_length = suffix_length
        self.left = left
        self.right = right


class SegmentTree:
    def __init__(self, s):
        self.root = self.build(s, 0, len(s) - 1)

    def build(self, s, lo, hi):
        if lo == hi:
            return SegmentTreeNode(
                lo, hi,
                s[lo], s[lo], s[lo],
                1, 1, 1
            )

        mid = (lo + hi) // 2

        left = self.build(s, lo, mid)
        right = self.build(s, mid + 1, hi)

        return self.merge(left, right)

    def merge(self, left, right):
        # Find maximum length
        if left.max_length > right.max_length:
            max_letter = left.max_letter
            max_length = left.max_length
        else:
            max_letter = right.max_letter
            max_length = right.max_length

        # Check if suffix of left + prefix of right can be combined
        if (
            left.suffix_letter == right.prefix_letter
            and left.suffix_length + right.prefix_length > max_length
        ):
            max_letter = left.suffix_letter
            max_length = left.suffix_length + right.prefix_length

        # Find prefix
        prefix_letter = left.prefix_letter
        prefix_length = left.prefix_length

        if (
            left.lo + prefix_length == right.lo
            and left.prefix_letter == right.prefix_letter
        ):
            prefix_length += right.prefix_length

        # Find suffix
        suffix_letter = right.suffix_letter
        suffix_length = right.suffix_length

        if (
            right.hi - suffix_length == left.hi
            and right.suffix_letter == left.suffix_letter
        ):
            suffix_length += left.suffix_length

        return SegmentTreeNode(
            left.lo,
            right.hi,
            max_letter,
            prefix_letter,
            suffix_letter,
            max_length,
            prefix_length,
            suffix_length,
            left,
            right
        )

    def update(self, node, i, c):
        # Leaf node
        if node.lo == i and node.hi == i:
            node.max_letter = c
            node.prefix_letter = c
            node.suffix_letter = c

            return node

        mid = (node.lo + node.hi) // 2

        if i <= mid:
            updated_left = self.update(node.left, i, c)
            return self.merge(updated_left, node.right)

        else:
            updated_right = self.update(node.right, i, c)
            return self.merge(node.left, updated_right)

    def update_value(self, i, c):
        self.root = self.update(self.root, i, c)

    def get_max_length(self):
        return self.root.max_length


class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        ans = []

        tree = SegmentTree(s)

        for i in range(len(queryIndices)):
            tree.update_value(
                queryIndices[i],
                queryCharacters[i]
            )

            ans.append(tree.get_max_length())

        return ans