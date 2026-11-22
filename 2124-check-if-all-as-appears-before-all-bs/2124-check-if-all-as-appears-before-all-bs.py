class Solution:
    def checkString(self, s: str) -> bool:
        """
        Check if string s has all 'a's appearing before all 'b's.
      
        Args:
            s: Input string containing only 'a' and 'b' characters
          
        Returns:
            True if all 'a's appear before all 'b's, False otherwise
        """
        # If "ba" substring exists, it means there's a 'b' followed by an 'a'
        # This violates the condition that all 'a's must come before all 'b's
        return "ba" not in s
