class Solution:
    def maxDepth(self, s: str) -> int:
        """
        Calculate the maximum depth of nested parentheses in a string.
      
        Args:
            s: Input string containing parentheses and other characters
          
        Returns:
            Maximum nesting depth of valid parentheses
        """
        max_depth = 0  # Track the maximum depth encountered
        current_depth = 0  # Track the current nesting level
      
        # Iterate through each character in the string
        for char in s:
            if char == '(':
                # Opening parenthesis increases depth
                current_depth += 1
                # Update maximum depth if current is greater
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                # Closing parenthesis decreases depth
                current_depth -= 1
            # Other characters are ignored
      
        return max_depth
