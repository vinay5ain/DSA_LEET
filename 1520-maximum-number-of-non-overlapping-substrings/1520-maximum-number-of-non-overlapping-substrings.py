class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)

        # First and last occurrence of each character
        left = [n] * 26
        right = [-1] * 26

        for i in range(n):
            idx = ord(s[i]) - ord('a')
            left[idx] = min(left[idx], i)
            right[idx] = i

        intervals = []

        # Find all valid intervals
        for i in range(n):
            idx = ord(s[i]) - ord('a')

            # Only start from the first occurrence
            if i != left[idx]:
                continue

            end = right[idx]
            valid = True

            j = i
            while j <= end:
                char_idx = ord(s[j]) - ord('a')

                # Character occurs before i -> invalid
                if left[char_idx] < i:
                    valid = False
                    break

                # Extend interval if necessary
                end = max(end, right[char_idx])
                j += 1

            if valid:
                intervals.append((i, end))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        last_end = -1

        # Greedily select non-overlapping intervals
        for start, end in intervals:
            if start > last_end:
                result.append(s[start:end + 1])
                last_end = end

        return result