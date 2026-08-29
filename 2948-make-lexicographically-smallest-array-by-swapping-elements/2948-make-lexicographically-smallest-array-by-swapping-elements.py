class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
      
        # Create pairs of (value, original_index) and sort by value
        sorted_with_indices = sorted(zip(nums, range(n)))
      
        # Initialize result array
        result = [0] * n
      
        i = 0
        while i < n:
            # Find the end of current group where consecutive differences <= limit
            j = i + 1
            while j < n and sorted_with_indices[j][0] - sorted_with_indices[j - 1][0] <= limit:
                j += 1
          
            # Extract and sort the original indices for current group
            original_indices = sorted(index for _, index in sorted_with_indices[i:j])
          
            # Assign smallest available values to smallest available positions
            # This ensures lexicographically smallest arrangement within the group
            for position, (value, _) in zip(original_indices, sorted_with_indices[i:j]):
                result[position] = value
          
            # Move to next group
            i = j
      
        return result