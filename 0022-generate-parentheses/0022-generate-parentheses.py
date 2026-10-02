class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate all combinations of well-formed parentheses.
      
        Args:
            n: Number of pairs of parentheses
          
        Returns:
            List of all valid parentheses combinations
        """
        def backtrack(left_count: int, right_count: int, current_string: str) -> None:
            """
            Recursively build valid parentheses combinations using backtracking.
          
            Args:
                left_count: Number of opening parentheses used so far
                right_count: Number of closing parentheses used so far
                current_string: Current parentheses string being built
            """
            # Pruning: invalid states
            # - Used more than n opening or closing parentheses
            # - More closing than opening parentheses (invalid sequence)
            if left_count > n or right_count > n or left_count < right_count:
                return
          
            # Base case: found a valid combination with n pairs
            if left_count == n and right_count == n:
                result.append(current_string)
                return
          
            # Try adding an opening parenthesis
            backtrack(left_count + 1, right_count, current_string + '(')
          
            # Try adding a closing parenthesis
            backtrack(left_count, right_count + 1, current_string + ')')
      
        # Initialize result list to store all valid combinations
        result = []
      
        # Start the backtracking process with empty string
        backtrack(0, 0, '')
      
        return result
