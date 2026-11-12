class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        Find the length of the longest monotonic subarray.
        A monotonic subarray is either strictly increasing or strictly decreasing.
      
        Args:
            nums: List of integers
          
        Returns:
            Length of the longest monotonic subarray
        """
        # Initialize result and current length counter
        max_length = 1
        current_length = 1
      
        # Check for longest strictly increasing subarray
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                # Extend current increasing sequence
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                # Reset counter when sequence breaks
                current_length = 1
      
        # Reset counter for checking decreasing subarray
        current_length = 1
      
        # Check for longest strictly decreasing subarray
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                # Extend current decreasing sequence
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                # Reset counter when sequence breaks
                current_length = 1
      
        return max_length
