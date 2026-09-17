class Solution:
    def minSumOfLengths(self, arr, target):
        ans = float('inf')
        leftLength = float('inf')
        prefix = 0

        prefixToIndex = {0: -1}

        # Store prefix sum -> index
        for i in range(len(arr)):
            prefix += arr[i]
            prefixToIndex[prefix] = i

        prefix = 0

        for i in range(len(arr)):
            prefix += arr[i]

            # Check subarray ending at i
            if prefix - target in prefixToIndex:
                leftLength = min(
                    leftLength,
                    i - prefixToIndex[prefix - target]
                )

            # Check another subarray starting after i
            if leftLength < float('inf'):
                if prefix + target in prefixToIndex:
                    ans = min(
                        ans,
                        leftLength + prefixToIndex[prefix + target] - i
                    )

        return -1 if ans == float('inf') else ans