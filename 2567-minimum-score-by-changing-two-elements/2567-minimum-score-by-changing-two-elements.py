class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # Sort the array in ascending order
        nums.sort()
      
        # After changing exactly 2 elements to any value, we want to minimize the sum
        # The sum is defined as the difference between max and min elements
      
        # We have 3 strategies to minimize the difference:
        # 1. Change the 2 smallest elements (use nums[2] as new min, nums[-1] as max)
        # 2. Change the 2 largest elements (use nums[0] as min, nums[-3] as new max)
        # 3. Change 1 smallest and 1 largest element (use nums[1] as new min, nums[-2] as new max)
      
        option1 = nums[-1] - nums[2]  # Change 2 smallest elements
        option2 = nums[-3] - nums[0]  # Change 2 largest elements
        option3 = nums[-2] - nums[1]  # Change 1 smallest and 1 largest
      
        # Return the minimum difference among all three strategies
        return min(option1, option3, option2)
