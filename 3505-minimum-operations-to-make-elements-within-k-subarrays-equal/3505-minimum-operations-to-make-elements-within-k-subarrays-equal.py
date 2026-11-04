from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:

        minOps = self.getMinOps(nums, x)

        n = len(nums)
        mem = [[-1] * (k + 1) for _ in range(n + 1)]

        return self.solve(nums, x, 0, k, minOps, mem)

    def solve(self, nums, x, i, k, minOps, mem):

        if k == 0:
            return 0

        if i == len(nums):
            return float('inf')

        if mem[i][k] != -1:
            return mem[i][k]

        skip = self.solve(nums, x, i + 1, k, minOps, mem)

        pick = float('inf')

        if i + x <= len(nums):
            pick = minOps[i] + self.solve(
                nums, x, i + x, k - 1, minOps, mem
            )

        mem[i][k] = min(skip, pick)

        return mem[i][k]

    def getMinOps(self, nums, x):

        lower = SortedList()
        upper = SortedList()

        lowerSum = 0
        upperSum = 0

        minOps = []

        for i in range(len(nums)):

            if not lower or nums[i] <= lower[-1]:
                lower.add(nums[i])
                lowerSum += nums[i]
            else:
                upper.add(nums[i])
                upperSum += nums[i]

            if i >= x:
                outNum = nums[i - x]

                if outNum in lower:
                    lower.remove(outNum)
                    lowerSum -= outNum
                else:
                    upper.remove(outNum)
                    upperSum -= outNum

            # Balance both sets
            if len(lower) < len(upper):
                val = upper.pop(0)
                lower.add(val)

                upperSum -= val
                lowerSum += val

            elif len(lower) - len(upper) > 1:
                val = lower.pop(-1)
                upper.add(val)

                lowerSum -= val
                upperSum += val

            # Calculate operations
            if i >= x - 1:

                median = lower[-1]

                ops = (
                    median * len(lower) - lowerSum
                    + upperSum - median * len(upper)
                )

                minOps.append(ops)

        return minOps