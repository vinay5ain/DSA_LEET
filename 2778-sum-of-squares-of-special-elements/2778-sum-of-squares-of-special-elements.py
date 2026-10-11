class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        """
        Calculate the sum of squares of elements at positions that are divisors of the array length.
      
        Args:
            nums: List of integers
          
        Returns:
            Sum of squares of elements at special indices
        """
        # Get the total length of the input array
        n = len(nums)
      
        # Iterate through the array with 1-based indexing
        # Sum the squares of elements where the index divides the array length evenly
        result = sum(
            num * num  # Square the current element
            for index, num in enumerate(nums, 1)  # Start enumeration from 1 (1-based indexing)
            if n % index == 0  # Check if current index is a divisor of array length
        )
      
        return result
