class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
      
        # min_changes[i][j] stores the minimum changes needed to make substring s[i-1:j] 
        # into a semi-palindrome (a string that becomes palindrome after grouping by some divisor)
        min_changes = [[float('inf')] * (n + 1) for _ in range(n + 1)]
      
        # Calculate minimum changes for each substring
        for start in range(1, n + 1):
            for end in range(start, n + 1):
                substring_length = end - start + 1
              
                # Try each possible divisor of the substring length
                for divisor in range(1, substring_length):
                    if substring_length % divisor == 0:
                        changes_needed = 0
                      
                        # Check pairs of characters that should match in the semi-palindrome
                        for left_idx in range(substring_length):
                            # Calculate the corresponding right index for semi-palindrome check
                            # This pairs characters based on the divisor pattern
                            groups_count = substring_length // divisor
                            group_pos = left_idx // divisor
                            offset = left_idx % divisor
                            right_idx = (groups_count - 1 - group_pos) * divisor + offset
                          
                            # Only check each pair once (avoid double counting)
                            if left_idx >= right_idx:
                                break
                          
                            # Count mismatches that need to be changed
                            if s[start - 1 + left_idx] != s[start - 1 + right_idx]:
                                changes_needed += 1
                      
                        # Update minimum changes for this substring
                        min_changes[start][end] = min(min_changes[start][end], changes_needed)
      
        # dp[i][j] stores the minimum changes to partition s[0:i] into j parts
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # Base case: empty string with 0 partitions needs 0 changes
      
        # Fill the DP table
        for length in range(1, n + 1):
            for partitions in range(1, k + 1):
                # Try all possible positions for the last partition
                for prev_length in range(length - 1):
                    # Cost = previous partitions cost + cost of current partition
                    dp[length][partitions] = min(
                        dp[length][partitions], 
                        dp[prev_length][partitions - 1] + min_changes[prev_length + 1][length]
                    )
      
        return dp[n][k]
