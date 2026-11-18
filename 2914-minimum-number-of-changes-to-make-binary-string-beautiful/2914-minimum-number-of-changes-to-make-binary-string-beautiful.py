class Solution:
    def minChanges(self, s: str) -> int:
        """
        Calculate the minimum number of changes needed to make the string
        consist of identical pairs of consecutive characters.
      
        The string is divided into pairs: (s[0], s[1]), (s[2], s[3]), etc.
        For each pair, if the two characters are different, one change is needed.
      
        Args:
            s: Input string to be processed
          
        Returns:
            Minimum number of character changes required
        """
        # Count mismatches within each pair by checking odd-indexed positions
        # against their preceding even-indexed positions
        # range(1, len(s), 2) generates indices: 1, 3, 5, ...
        return sum(s[i] != s[i - 1] for i in range(1, len(s), 2))
