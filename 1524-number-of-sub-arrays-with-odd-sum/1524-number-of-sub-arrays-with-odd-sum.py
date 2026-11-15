class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
      
        # Count of prefix sums by parity: [even_count, odd_count]
        # Initialize with [1, 0] since empty prefix has sum 0 (even)
        parity_count = [1, 0]
      
        # Total count of subarrays with odd sum
        result = 0
      
        # Running prefix sum
        prefix_sum = 0
      
        for num in arr:
            # Update prefix sum
            prefix_sum += num
          
            # Get current parity (0 for even, 1 for odd)
            current_parity = prefix_sum & 1
          
            # To get odd sum subarray, we need opposite parity
            # If current is even (0), we need odd (1): 0 ^ 1 = 1
            # If current is odd (1), we need even (0): 1 ^ 1 = 0
            opposite_parity = current_parity ^ 1
          
            # Add count of prefix sums with opposite parity
            result = (result + parity_count[opposite_parity]) % MOD
          
            # Update count for current parity
            parity_count[current_parity] += 1
      
        return result
