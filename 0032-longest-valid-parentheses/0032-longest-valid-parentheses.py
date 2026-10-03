class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Get the length of the input string
        n = len(s)
      
        # dp[i] represents the length of the longest valid parentheses substring
        # ending at position i-1 in the original string (1-indexed for easier calculation)
        dp = [0] * (n + 1)
      
        # Iterate through each character with 1-based indexing
        for i, char in enumerate(s, 1):
            # Only closing parentheses can form valid pairs
            if char == ")":
                # Case 1: Current ')' matches with previous '(' to form "()"
                if i > 1 and s[i - 2] == "(":
                    # Add 2 for the new pair and include any valid substring before it
                    dp[i] = dp[i - 2] + 2
              
                # Case 2: Current ')' might match with a '(' before a valid substring
                else:
                    # Find the position before the valid substring ending at i-1
                    j = i - dp[i - 1] - 1
                  
                    # Check if there's a matching '(' at position j-1
                    if j > 0 and s[j - 1] == "(":
                        # Length = previous valid substring + 2 for new pair + 
                        # any valid substring before the matching '('
                        dp[i] = dp[i - 1] + 2 + dp[j - 1]
      
        # Return the maximum length found
        return max(dp)
