class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def dfs(current_expression):
            # Find the first closing brace
            closing_brace_index = current_expression.find('}')
          
            # Base case: no more braces to expand
            if closing_brace_index == -1:
                result_set.add(current_expression)
                return
          
            # Find the matching opening brace for the first closing brace
            # Search backwards from just before the closing brace
            opening_brace_index = current_expression.rfind('{', 0, closing_brace_index - 1)
          
            # Extract parts: before the brace, inside the brace, and after the brace
            prefix = current_expression[:opening_brace_index]
            suffix = current_expression[closing_brace_index + 1:]
            brace_content = current_expression[opening_brace_index + 1:closing_brace_index]
          
            # Expand each option within the braces
            for option in brace_content.split(','):
                # Recursively process the expression with this option substituted
                dfs(prefix + option + suffix)
      
        # Initialize result set to store unique expanded strings
        result_set = set()
      
        # Start the depth-first search expansion
        dfs(expression)
      
        # Return sorted list of all unique expanded strings
        return sorted(result_set)
