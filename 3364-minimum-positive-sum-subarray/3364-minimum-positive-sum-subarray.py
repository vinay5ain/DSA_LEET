class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        min_sum = float('inf') 
        for start in range(n):
            current_sum = 0
          
            for end in range(start, n):
                current_sum += nums[end]
                subarray_length = end - start + 1
                if l <= subarray_length <= r and current_sum > 0:
                    min_sum = min(min_sum, current_sum)
        return -1 if min_sum == float('inf') else min_sum
