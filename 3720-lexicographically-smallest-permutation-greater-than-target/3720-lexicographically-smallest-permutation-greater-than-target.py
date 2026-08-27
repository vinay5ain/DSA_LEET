class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        sb = []

        if self.dfs(0, freq, sb, target, False):
            return ''.join(sb)

        return ""

    def dfs(self, i: int, freq: list[int], sb: list[str],
            target: str, check: bool) -> bool:

        if i == len(target):
            return check

        for j in range(26):
            if freq[j] == 0:
                continue

            can = chr(ord('a') + j)

            if not check and can < target[i]:
                continue

            freq[j] -= 1
            sb.append(can)

            next_check = check or can > target[i]

            if self.dfs(i + 1, freq, sb, target, next_check):
                return True

            sb.pop()
            freq[j] += 1

        return False