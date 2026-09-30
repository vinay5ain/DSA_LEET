class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        # Initialize result array to store group assignments (0 or 1)
        result = [0] * len(seq)
      
        # Track current depth/nesting level of parentheses
        depth = 0
      
        # Iterate through each character in the sequence
        for index, char in enumerate(seq):
            if char == "(":
                # For opening parenthesis:
                # Assign to group 0 if depth is even, group 1 if odd
                result[index] = depth & 1
                # Increase depth after opening parenthesis
                depth += 1
            else:  # char == ")"
                # For closing parenthesis:
                # Decrease depth first (matching the corresponding opening)
                depth -= 1
                # Assign to same group as its matching opening parenthesis
                result[index] = depth & 1
      
        return result
