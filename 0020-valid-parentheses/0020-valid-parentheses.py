class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []

        # Set of valid bracket pairs
        valid_pairs = {'()', '[]', '{}'}

        # Iterate through each character in the string
        for char in s:
            # If it's an opening bracket, push it onto the stack
            if char in '({[':
                stack.append(char)
          
            else:
     
                if not stack or stack[-1] + char not in valid_pairs:
                    return False

   
                stack.pop()

        return not stack
