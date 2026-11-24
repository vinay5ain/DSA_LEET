class Solution:
    def maxLength(self, nums: List[int]) -> int:
        """
        Find the maximum length of a subarray where the product equals GCD * LCM.
      
        For any subarray, the mathematical property holds that:
        product of elements = GCD of elements * LCM of elements
        if and only if the subarray contains coprime elements in a specific pattern.
      
        Args:
            nums: List of positive integers
          
        Returns:
            Maximum length of valid subarray
        """
        n = len(nums)
        max_length = 0
      
        # Calculate upper bound for product to avoid unnecessary computation
        # If product exceeds LCM of all elements * max element, we can stop early
        from math import gcd, lcm
        max_product_bound = lcm(*nums) * max(nums)
      
        # Try all possible subarrays starting from index i
        for i in range(n):
            current_product = 1
            current_gcd = 0  # GCD with 0 returns the other number
            current_lcm = 1
          
            # Extend subarray from index i to j
            for j in range(i, n):
                # Update product, GCD, and LCM incrementally
                current_product *= nums[j]
                current_gcd = gcd(current_gcd, nums[j])
                current_lcm = lcm(current_lcm, nums[j])
              
                # Check if the mathematical property holds
                if current_product == current_gcd * current_lcm:
                    max_length = max(max_length, j - i + 1)
              
                # Early termination: if product is too large, no need to continue
                if current_product > max_product_bound:
                    break
      
        return max_length
