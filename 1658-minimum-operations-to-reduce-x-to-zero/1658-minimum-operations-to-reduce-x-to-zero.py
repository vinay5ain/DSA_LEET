class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # Calculate target sum for the middle subarray
        # We want to find the longest subarray with sum = total - x
        target_sum = sum(nums) - x

        # Dictionary to store prefix sum and its earliest index
        # Initialize with 0 sum at index -1 (before array starts)
        prefix_sum_index = {0: -1}

        # Track maximum length of valid subarray and current prefix sum
        max_length = -1
        current_sum = 0

        # Iterate through array to find longest subarray with target_sum
        for index, value in enumerate(nums):
            # Update current prefix sum
            current_sum += value

            # Store first occurrence of this prefix sum
            if current_sum not in prefix_sum_index:
                prefix_sum_index[current_sum] = index

            # Check if we can form a subarray with target_sum
            # We need prefix_sum where: current_sum - prefix_sum = target_sum
            required_prefix = current_sum - target_sum
            if required_prefix in prefix_sum_index:
                # Calculate length of valid subarray
                subarray_length = index - prefix_sum_index[required_prefix]
                max_length = max(max_length, subarray_length)

        # If no valid subarray found, return -1
        # Otherwise, return number of elements to remove from both ends
        return -1 if max_length == -1 else len(nums) - max_length
